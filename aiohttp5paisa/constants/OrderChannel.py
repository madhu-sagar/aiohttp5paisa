"""
Type of Client

"""

from enum import Enum,unique

@unique
class OrderChannel(Enum):
	WEB = 'WEB'
	ANDROID = 'Android'
	IOS = 'iOS'