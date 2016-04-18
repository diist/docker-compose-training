import app
import unittest

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()
    
    def tearDown(self):
        pass

    def test_get_root(self):
        print "\n*** Testing that '/' returns HTTP/200 ***"
        rv = self.app.get('/')
        assert rv.status_code == 200
    
    def test_vote_a(self):
        self._test_vote('a')
    
    def test_vote_b(self):
        self._test_vote('b')
    
    def _test_vote(self, option):
        print "\n*** Testing that voting for option {0} works ***".format(option)
        votes = self._vote_count(option)
        self.app.post('/', data={'vote': option})
        votes_post = self._vote_count(option)
        assert votes_post == votes + 2
    
    def _vote_count(self, option):
        rv = self.app.get('/')
        # Extract vote count from HTML
        votes = int(rv.data
                     .split("value=\"{0}\">".format(option))[1]
                     .split("</button>")[0]
                     .split(":")[1]
                    )
        return votes

if __name__ == '__main__':
    unittest.main()
