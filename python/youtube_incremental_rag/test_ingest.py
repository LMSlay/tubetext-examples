import copy, sqlite3, tempfile, unittest
from pathlib import Path
from ingest import ingest

def row(vid='SYNTHETIC01'):
    return {'status':'ok','videoId':vid,'source':'captions','language':'en','transcript':'Alpha Beta','segments':[{'start':0.2,'duration':1,'text':'Alpha'},{'start':2,'duration':0.5,'text':'Beta'}]}

class Tests(unittest.TestCase):
    def setUp(self): self.db=sqlite3.connect(':memory:')
    def tearDown(self): self.db.close()
    def count(self): return self.db.execute('SELECT count(*) FROM documents').fetchone()[0]
    def test_success_timestamp(self):
        self.assertEqual(ingest([row()],self.db)['inserted'],['SYNTHETIC01'])
        self.assertEqual(self.db.execute('SELECT start,end FROM documents ORDER BY id').fetchall(),[(0.2,1.2),(2.,2.5)])
    def test_replay(self):
        ingest([row()],self.db); self.assertEqual(ingest([row()],self.db)['duplicates'],['SYNTHETIC01']); self.assertEqual(self.count(),2)
    def test_mixed_failure(self):
        out=ingest([row(),{'status':'error','videoId':'SYNTHETIC02'},row('SYNTHETIC03')],self.db)
        self.assertEqual(len(out['inserted']),2); self.assertEqual(len(out['review']),1)
    def test_unknown_status(self):
        x=row();x['status']='future_status';self.assertTrue(ingest([x],self.db)['review'])
    def test_empty_transcript(self):
        x=row();x['transcript']=' ';self.assertTrue(ingest([x],self.db)['review'])
    def test_missing_segments(self):
        x=row();del x['segments'];self.assertTrue(ingest([x],self.db)['review'])
    def test_invalid_time(self):
        for value in [-1,float('inf'),float('nan'),True,'1']:
            x=row();x['segments'][0]['start']=value;self.assertTrue(ingest([x],self.db)['review'])
    def test_out_of_order(self):
        x=row();x['segments'].reverse();self.assertTrue(ingest([x],self.db)['review'])
    def test_changed_content(self):
        ingest([row()],self.db);x=row();x['transcript']='changed';self.assertEqual(ingest([x],self.db)['review'][0]['reason'],'changed_content_requires_explicit_refresh');self.assertEqual(self.count(),2)
    def test_metadata_change(self):
        ingest([row()],self.db);x=row();x['viewCount']=999;self.assertTrue(ingest([x],self.db)['duplicates'])
    def test_ai_excluded(self):
        x=row();x['source']='ai';self.assertTrue(ingest([x],self.db)['review'])
    def test_unicode_preserved(self):
        x=row();x['segments'][0]['text']='你好\n世界';ingest([x],self.db);self.assertEqual(self.db.execute('SELECT text FROM documents ORDER BY id').fetchone()[0],'你好\n世界')
    def test_restart(self):
        with tempfile.TemporaryDirectory() as d:
            path=str(Path(d)/'data.db')
            with sqlite3.connect(path) as db: ingest([row()],db)
            with sqlite3.connect(path) as db: self.assertTrue(ingest([row()],db)['duplicates'])
    def test_invalid_array(self):
        with self.assertRaises(ValueError):ingest({},self.db)
    def test_duplicate_segments_not_deleted(self):
        x=row();x['segments'].insert(1,copy.deepcopy(x['segments'][0]));ingest([x],self.db);self.assertEqual(self.count(),3)
    def test_huge_timestamp_then_valid(self):
        x=row();x['segments'][0]['start']=10**400
        out=ingest([x,row('SYNTHETIC03')],self.db)
        self.assertEqual(len(out['review']),1);self.assertEqual(out['inserted'],['SYNTHETIC03'])
    def test_nonfinite_metadata_then_valid(self):
        x=row();x['viewCount']=float('inf')
        out=ingest([x,row('SYNTHETIC03')],self.db)
        self.assertEqual(len(out['review']),1);self.assertEqual(out['inserted'],['SYNTHETIC03'])
    def test_rollback(self):
        ingest([],self.db)
        self.db.execute("CREATE TRIGGER reject_doc BEFORE INSERT ON documents BEGIN SELECT RAISE(ABORT,'synthetic storage failure'); END")
        with self.assertRaises(sqlite3.IntegrityError): ingest([row()],self.db)
        self.assertEqual(self.db.execute('SELECT count(*) FROM videos').fetchone()[0],0)
        self.assertEqual(self.count(),0)
if __name__=='__main__':unittest.main()
