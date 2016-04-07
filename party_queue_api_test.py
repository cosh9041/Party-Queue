""" Unit testing file for party queue api """

import unittest
import models
import party_queue_api
import sys
sys.path.insert(1, '/home/user/Downloads/google_appengine')
sys.path.insert(1, '/home/user/Downloads/google_appengine/lib/yaml/lib')
sys.path.insert(1, '/home/user/workspaces/Party-Queue/lib')
from google.appengine.ext import testbed
from google.appengine.ext import ndb
from google.appengine.ext import testbed
import unittest

class TestPartyQueueApiTestCase(unittest.TestCase):
    def Setup(self):
        # Setting up testbed with the method stubs uses an in memory datastore
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_datastore_v3_stub()
        self.testbed.init_memcache_stub()
        # Clear ndb's in-context cache between tests.
        # This prevents data from leaking between tests.
        # Alternatively, you could disable caching by
        # using ndb.get_context().set_cache_policy(False)
        ndb.get_context().clear_cache()

    def tearDown(self):
        self.testbed.deactivate()

    def test_build_playlist_response(self):
        self.AssertEqual(1,1)

# Main: Run Test Cases
if __name__ == '__main__':
    unittest.main()

