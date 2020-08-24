"""
Exchange Segment

C-Cash, D-Derivative, U-Currency
"""

fron enum import Enum,unique

@unique
class ExchangeSegment(Enum):
	CASH = 'C'
	DERIVATIVE = 'D'
	CURRENCY = 'U'
