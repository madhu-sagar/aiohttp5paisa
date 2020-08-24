"""
Type of Order

"""

from enum import Enum,unique

@unique
class OrderType(Enum):
	NEW = 'P'
	MODIFY = 'M'
	CANCEL = 'C'