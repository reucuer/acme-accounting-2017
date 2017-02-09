from interfaces import IAccountingEntry, IDocument, IStorage, ICreditSlip
from zope.interface import implementer
import datetime

# Implementation.
RUB = 643
EUR = 810


@implementer(IAccountingEntry)
class Entry(object):
    def __init__(self, cr, dr, amount, currency=None, moment=None):
        self.cr=cr
        self.dr=dr
        self.amount=amount
        if currency is None:
            currency=RUB
        self.currency=currency
        if moment is None:
            self.moment=datetime.datetime.utcnow()

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
