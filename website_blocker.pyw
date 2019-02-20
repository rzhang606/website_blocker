'''Blocks websites during certain times'''
import time
from datetime import datetime as dt

hosts_temp="hosts"
hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
website_list["www.facebook.com", "facebook.com"]

while True:
	if dt(dt.now().year, dt.now().month. dt.now().day,16) < dt.now() < 
	dt(dt.now().year, dt.now().month. dt.now().day,17):
		print("Working Hours...")
		with open(hosts.path, 'r+') as file:
			content=file.read()
			for website in website_list:
				if website in content:
					pass
				else:
					file.write(redirect + " " + webstie + "\n")
	else:
		with open(hosts_path, 'r+') as file:
			content = file.readlines()
			file.seek(0)  #goes to the top of the file
			for line in content:
				if not any(website in line for website in website_list):
					file.write(line)
			file.truncate() # deletes everything below 
		print("Fun Hours")
	time.sleep(5) # how often the program iterates runs in seconds
