"""
Type of Order
"""

from enum import Enum,unique

@unique
class BUYSELL(Enum)
	BUY = 'B'
	SELL = 'S'