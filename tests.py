from components import *

class TestEntryImplementation:
    def setUp(self):
        self.e=Entry("50","71",1000)

    def tearDown(self):
        pass

    def test_implementation(self):
        assert IAccountingEntry.implementedBy(Entry)

    def test_provision(self):
        assert IAccountingEntry.providedBy(self.e)

    def test_construction(self):
        assert self.e.cr=="50", "wrong credit account"
