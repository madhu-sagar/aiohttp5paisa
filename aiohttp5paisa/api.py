"""
Client
"""


import aiohttp
from constants.BuySell import BuySell
from constants.Exchange import Exchange
from constants.ExchangeSegment import ExchangeSegment
from constants.OrderChannel import OrderChannel
from constants.OrderStatus import OrderStatus
from constants.OrderType import OrderType
from constants.OrderValidity import OrderValidity
from constants.RestEndpoint import RestEndpoint
from utils.encrpyt_decrypt import encrypt, decrpyt
from utils.hdd_serialnumber import hdd_serialnumber
from utils.local_ip import local_ip
from utils.public_ip import public_ip
from utils.uuid import uuid
import typing
from enum import Enum 
import os


class Api():
	"""docstring for Client"""

	def __init__(self, session = None ):
		
		if (session) :
			self.session = session 
		else :
			self.session = aiohttp.ClientSession()
		
		
		#TODO
		#CHECK IF .env exists
		#ELSE execute it and then load settings

		settings = dict()
		settings['appName'] = os.environ.get('FIVEPAISAAPPNAME')
		settings['appSource'] = os.environ.get('FIVEPAISAAPPSOURCE')
		settings['userId'] = os.environ.get('FIVEPAISAAPPUSERID')
		settings['appPassword'] =os.environ.get('FIVEPAISAAPPPASSWORD')
		settings['key'] = os.environ.get('FIVEPAISAUSERKEY')
		settings['encrpytionKey'] = os.environ.get('FIVEPAISAENCRYPTIONKEY')
		settings['osName'] = os.environ.get('FIVEPAISAOSNAME')
		settings['clientCode'] = os.environ.get('FIVEPAISACLIENTCODE')
		settings['appVer'] = os.environ.get('FIVEPAISAAPPVERSION')
		settings['VersionNo'] = os.environ.get('FIVEPAISAVERSIONNO')

		#TODO
		if(os.environ.get('FIVEPAISALOCALIP')) :
			settings['LocalIP'] = os.environ.get('FIVEPAISALOCALIP')
		else :
			settings['LocalIP'] = local_ip()

		if(os.environ.get('FIVEPAISAPUBLICIP')):
			settings['PublicIP'] = os.environ.get('FIVEPAISAPUBLICIP')
		else :
			settings['PublicIP'] = public_ip()

		if(os.environ.get('FIVEPAISAHDSERIALNUMBER')):
			settings['HDSerailNumber'] = os.environ.get('FIVEPAISAHDSERIALNUMBER')
		else :
			settings['HDSerailNumber'] = hdd_serialnumber()

		if((os.environ.get('FIVEPAISAMACADDRESS')) :
			settings['MACAddress'] = os.environ.get('FIVEPAISAMACADDRESS')
		else
			settings['MACAddress'] = mac_address()

		if(os.environ.get('FIVEPAISAMACHINEID')): 
			settings['MachineID'] = os.environ.get('FIVEPAISAMACHINEID')
		else
			settings['MachineID'] = machine_id()

		settings['ConnectionType'] = os.environ.get("FIVEPAISACONNECTIONTYPE")

		settings['Raw_Email_id'] = os.environ.get('FIVEPAISAEMAILID')
		settings['Raw_Password'] = os.environ.get('FIVEPAISALOGINPASSWORD')
		settings['Raw_My2PIN'] = os.environ.get('FIVEPAISAMY2PIN')


		settings['Email_id'] = encrypt(settings['Raw_Email_id'],settings['encrpytionKey'])
		settings['Password'] = encrypt(settings['Raw_Password'],settings['encrpytionKey'])
		settings['My2PIN'] = encrypt(settings['Raw_My2PIN'],settings['encrpytionKey'])


		self.settings = settings

	
	async def closesession(self):

		await self.session.close()


	async def positions(self):

		requestheader = { 'Content-Type' : 'application/json'}

		head = { 
			'appName' : settings['appName'], 
			'appVer' : settings['appVer'],
			'key' : settings['key'],
			'osName' : settings['osName'],
			'requestCode' : RestEndpoint.POSITIONS_REQUESTCODE.value,
			'userId' : settings['userId'],
			'password' : settings['appPassword']

		}

		body = { 
			'head' : head,
			'body' : {
					'ClientCode' : settings['clientCode']
				}
			}

		try :

			async with self.session.post(RestEndpoint.POSITIONS_URL.value,headers = requestheader,data = body) as resp :
				return await resp.json()

		except aiohttp.ClientError as e:
			print(f"Exception occured \n {str(e)}")
			return { 'error' : str(e)}


	async def margin(self):

		requestheader = { 'Content-Type' : 'application/json'}

		

		head = { 
			'appName' : settings['appName'], 
			'appVer' : settings['appVer'],
			'key' : settings['key'],
			'osName' : settings['osName'],
			'requestCode' : RestEndpoint.MARGIN_REQUESTCODE.value,
			'userId' : settings['userId'],
			'password' : settings['appPassword']
		}

		body = { 
			'head' : head,
			'body' : {
					'ClientCode' : settings['clientCode']
				}
			}

		try :

			async with self.session.post(RestEndpoint.MARGIN_URL.value,headers = requestheader,data = body) as resp :
				return await resp.json()

		except aiohttp.ClientError as e :
			print(f"Exception occured \n {str(e)}")
			return { 'error' : str(e)}

		


	async def orderbook(self):

		requestheader = { 'Content-Type' : 'application/json'}

		

		head = { 
			'appName' : settings['appName'], 
			'appVer' : settings['appVer'],
			'key' : settings['key'],
			'osName' : settings['osName'],
			'requestCode' : RestEndpoint.ORDERBOOK_REQUESTCODE.value,
			'userId' : settings['userId'],
			'password' : settings['appPassword']
		}

		body = { 
			'head' : head,
			'body' : {
					'ClientCode' : settings['clientCode']
				}
			}


		try :

			async with self.session.post(RestEndpoint.ORDERBOOK_URL.value,headers = requestheader,data = body) as resp :
				return await resp.json()

		except aiohttp.ClientError as e:
			print(f"Exception occured \n {str(e)}")
			return { 'error' : str(e)}




	async def holdings(self):

		requestheader = { 'Content-Type' : 'application/json'}

	
		head = { 
			'appName' : settings['appName'], 
			'appVer' : settings['appVer'],
			'key' : settings['key'],
			'osName' : settings['osName'],
			'requestCode' : RestEndpoint.HOLDINGS_REQUESTCODE.value,
			'userId' : settings['userId'],
			'password' : settings['appPassword']
		}

		body = { 
			'head' : head,
			'body' : {
					'ClientCode' : settings['clientCode']
				}
			}

		try :

			async with self.session.post(RestEndpoint.HOLDINGS_URL.value,headers = requestheader,data = body) as resp :
				return await resp.json()

		except aiohttp.ClientError as e:
			print(f"Exception occured \n {str(e)}")
			return { 'error' : str(e)}






	async def orderrequest(self):

		requestheader = { 'Content-Type' : 'application/json'}

		head = { 
			'appName' : settings['appName'], 
			'appVer' : settings['appVer'],
			'key' : settings['key'],
			'osName' : settings['osName'],
			'requestCode' : RestEndpoint.ORDERREQUEST_REQUESTCODE.value,
			'userId' : settings['userId'],
			'password' : settings['appPassword']
		}

		body = { 
			'head' : head,
			'body' : { 
					'ClientCode' : settings['clientCode'],
					'OrderFor' : XXX ,
					'Exchange' : XXX,
					'ExchangeType' : XXX,
					'Price' :  XXX,
					'OrderId' : XXX,
					'OrderType' : XXX,
					'Qty' : ,
					'OrderDateTime' : XXX,
					'ScripCode' : XXX,
					'AtMarket' : XXX,
					'RemoteOrderID' : XXX,
					'ExchOrderID' : XXX,
					'DisQty' : XXX,
					'StopLossPrice' : XXX,
					'IsStopLossOrder' : XXX,
					'IOCOrder' : XXX,
					'IsIntraday' : XXX,
					'ValidTillDate' : XXX,
					'AHPlaced' : XXX,
					'PublicIP' : XXX,
					'iOrderValidity' : XXX,
					'TradedQty' : XXX,
					'OrderRequestCode' : settings['clientCode'],
					'AppSource' : settings['appSource']
				}

			}


		try :

			async with self.session.post(RestEndpoint.ORDERREQUEST_URL.value,headers = requestheader,data = body) as resp :
				return await resp.json()

		except aiohttp.ClientError as e:

			print(f"Exception occured \n {str(e)}")
			return { 'error' : str(e)}


		

	async def orderstatus(self):


		requestheader = { 'Content-Type' : 'application/json'}

		head = { 
			'appName' : settings['appName'], 
			'appVer' : settings['appVer'],
			'key' : settings['key'],
			'osName' : settings['osName'],
			'requestCode' : RestEndpoint.ORDERSTATUS_REQUESTCODE.value,
			'userId' : settings['userId'],
			'password' : settings['appPassword']
		}

		#TODO Order list
		body = { 
			'head' : head,
			'body' : { 
					'ClientCode' : settings['clientCode'],
					'OrdStatusReqList' : XXX 
				}
			}

		try :

			async with self.session.post(RestEndpoint.ORDERSTATUS_URL.value,headers = requestheader,data = body) as resp :
				return await resp.json()

		except aiohttp.ClientError as e:

			print(f"Exception occured \n {str(e)}")
			return { 'error' : str(e)}



	async def tradeinformation(self):

		requestheader = { 'Content-Type' : 'application/json'}

		head = { 
			'appName' : settings['appName'], 
			'appVer' : settings['appVer'],
			'key' : settings['key'],
			'osName' : settings['osName'],
			'requestCode' : RestEndpoint.TRADEINFORMATION_REQUESTCODE.value,
			'userId' : settings['userId'],
			'password' : settings['appPassword']
		}

		#TODO Trade info list
		body = { 
			'head' : head,
			'body' : { 
				'ClientCode' : settings['clientCode'],
				'TradeInformationList' : XXX
				}
			}

		try :

			async with self.session.post(RestEndpoint.TRADEINFORMATION_URL.value,headers = requestheader,data = body) as resp :
				return await resp.json()

		except aiohttp.ClientError as e:

			print(f"Exception occured \n {str(e)}")
			return { 'error' : str(e)}

		 


	async def login(self):

		requestheader = { 'Content-Type' : 'application/json'}

		head = { 
			'appName' : settings['appName'], 
			'appVer' : settings['appVer'],
			'key' : settings['key'],
			'osName' : settings['osName'],
			'requestCode' : RestEndpoint.LOGIN_REQUESTCODE.value,
			'userId' : settings['userId'],
			'password' : settings['appPassword']
		}

		#TODO : RequestNo
		body = { 
			'head' : head,
			'body' : { 
				'Email_id' : settings['Email_id'],
				'Password' : settings['Password'],
				'LocalIP' : settings['LocalIP'],
				'PublicIP' : settings['PublicIP'],
				'HDSerialNumber' : settings['HDSerailNumber'],
				'MACAddress' : settings['MACAddress'],
				'MachineID' : settings['MachineID'],
				'VersionNo' : settings['VersionNo'],
				'RequestNo' : XXX,
				'My2PIN' : settings['My2PIN'],
				'ConnectionType' : settings['ConnectionType']
				}
			}

		try :

			async with self.session.post(RestEndpoint.LOGIN_URL.value,headers = requestheader,data = body) as resp :
				return await resp.json()

		except aiohttp.ClientError as e:

			print(f"Exception occured \n {str(e)}")
			return { 'error' : str(e)}











































	


		

