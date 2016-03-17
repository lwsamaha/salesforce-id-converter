__author__ = 'lsamaha'

from sfid import *
import unittest

class TestSfid(unittest.TestCase):

    def test_tolongid(self):
        short_sfid1 = '001A0000006Vm9r'
        short_sfid2 = '003A0000005QB3A'
        short_sfid3 = '003A0000008qb1s'
        self.assertEquals(short_sfid1 + 'IAC', to_long_id(short_id=short_sfid1))
        self.assertEquals(short_sfid2 + 'IAW', to_long_id(short_id=short_sfid2))
        self.assertEquals(short_sfid3 + 'IAA', to_long_id(short_id=short_sfid3))