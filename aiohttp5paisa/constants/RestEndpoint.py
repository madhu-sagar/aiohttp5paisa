"""
REST Endpoints

"""

from enum import Enum

class RestEndpoint(Enum):
	LOGIN_URL = 'https://openapi.5paisa.com/VendorsAPI/Service1.svc/V2/LoginRequestMobileNewbyEmail'
	LOGIN_REQUESTCODE = '5PLoginV2'
	
	ORDERREQUEST_URL = 'https://openapi.5paisa.com/VendorsAPI/Service1.svc/V1/OrderRequest'
	ORDERREQUEST_REQUESTCODE = '5POrdReq'

	ORDERSTATUS_URL = 'https://openapi.5paisa.com/VendorsAPI/Service1.svc/OrderStatus'
	ORDERSTATUS_REQUESTCODE = '5POrdReq'

	TRADEINFORMATION_URL = 'https://openapi.5paisa.com/VendorsAPI/Service1.svc/TradeInformation'
	TRADEINFORMATION_REQUESTCODE = '5PTrdInfo' 

	MARGIN_URL = 'https://Openapi.5paisa.com/VendorsAPI/Service1.svc/V3/Margin'
	MARGIN_REQUESTCODE = '5PMarginV3'

	ORDERBOOK_URL = 'https://openapi.5paisa.com/VendorsAPI/Service1.svc/V2/OrderBook'
	ORDERBOOK_REQUESTCODE = '5PMarginV3'

	HOLDINGS_URL = 'https://openapi.5paisa.com/VendorsAPI/Service1.svc/V2/Holding'
	HOLDINGS_REQUESTCODE = '5PMarginV3'

	POSITIONS_URL = 'https://openapi.5paisa.com/VendorsAPI/Service1.svc/V1/NetPositionNetWise'
	POSITIONS_REQUESTCODE = '5PNPNWV1'