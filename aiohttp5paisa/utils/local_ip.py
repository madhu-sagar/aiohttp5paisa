"""
Local IP
"""

import socket
def local_ip():

	    
	hostname = socket.gethostname()    
	ip_address = socket.gethostbyname(hostname)    
	
	return ip_address