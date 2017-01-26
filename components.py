from interfaces import IAccountingEntry, IDocument, IStorage
from zope.interface import implementer
import datetime

# Implementation.

@implementer(IAccountingEntry)
class Entry(object):
    def __init__(self, cr, dr, amount):
        self.cr=cr
        self.dr=dr
        self.amount=amount

@implementer(IDocument)
class Document(object):
    def __init__(self, number, date):
        self.number=number
        self.date=date

@implementer(ICreditSlip)
class CreditSlip(Document):
    def __init__(self, number, date):
        super(CreditSlip, self).__init__(number, date)
        self.entries=[]

    def addentry(self, entry):
        self.entries.append(entry)
