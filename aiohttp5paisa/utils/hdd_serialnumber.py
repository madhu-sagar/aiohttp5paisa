"""
Get the hard disk serial number 
"""
import os

def hdd_serialnumber():
	
	cmd = 'udevadm info --query=all --name=/dev/sda | grep ID_SERIAL'
	serial_num = os.system(cmd)

	import subprocess
	out1 = subprocess.Popen(['udevadm', 'info','query=all','--name=/dev/sda'],stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
	out2 = subprocess.Popen(["grep", "ID_SERIAL"],stdin = out1.stdout,stdout = subprocess.PIPE)
	output, err = out2.communicate()
	out1.stdout.close()
	out2.stdout.close()

	ser_num = str(output).split("\\n")[0].split("=")[1]

	return ser_num
