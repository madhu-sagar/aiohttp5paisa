"""
UUID
"""
import base64
import uuid

def uuid():

	
    r_uuid = base64.urlsafe_b64encode(uuid.uuid4().bytes).decode()
    return r_uuid.replace('=', '')