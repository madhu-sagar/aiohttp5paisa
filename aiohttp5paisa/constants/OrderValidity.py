"""
Order Validity
0 - Day ( for the present day)
4 - EOS 
2 - GTC ( good till cancelled )
1- GTD ( good till date)
3 - IOC ( immediate or cancel)
6 - FOK (fill or kill)

"""

from enum import Enum,unique

@unique
class OrderValidity(Enum):
	DAY = 0
	EOS = 4
	GTC = 2
	GTD = 1
	IOC = 3
	FOK = 6
