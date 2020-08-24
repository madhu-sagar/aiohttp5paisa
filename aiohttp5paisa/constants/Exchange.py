"""
Exchanges available
"""

from enum import Enum,unique

@unique
class Exchange(Enum):
	NSE = 'N'
	BSE = 'B'
	MCX = 'M'

