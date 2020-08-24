"""
Status of the order

"""

from enum import Enum,unique
@unique
class OrderStatus(Enum):
	INVALID = -1,
	PENDING = 0,
	PARTIALLY_FILLED = 1,
	FILLED = 2