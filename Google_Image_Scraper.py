#email:		king.ali.1331@gmail.com

#! /usr/bin/env python
try:
	import json
	import time
	import requests
	import urllib
	import os
	import sys
except:
	print '(!) Error...! \r\n Modules Importing Failed. Please check it manually.'
	sys.exit()
	
	
def banner():
	print'======================================'
	print'	Google Image Scrapper'
	print'======================================'
		
def go(query, path, BASE_PATH):
	BASE_URL = 'https://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=' + query + '&start=%d'
	start = 0
	while start < 60:
		print '[-] Starting from Page No. : '+str(start)
		try:
			r = requests.get(BASE_URL % start)
		except:
			print '(!) Error in Your Internet Connectivity. \r\n'
			time.sleep(2)
			pass
		for image_info in json.loads(r.text)['responseData']['results']:
			url = image_info['unescapedUrl']
			print url
			f1.write(''.join(url+'\r\n'))
		start += 4
		time.sleep(1.5)

def savePic(url, parameter, BASE_PATH):
	uri = BASE_PATH+'/'+parameter+'.jpg'
	if url != "":
		print '[+] Downloading Image Please Wait....!\r\n'
		try:
			urllib.urlretrieve(url,uri)
			print '[+] Downloaded: '+parameter+'.jpg'+'\r\n\r\n'
		except:
			print '(!) Image Downloading Failed. URL Connection Problem. \r\n'
			pass
			
######################################################
if __name__ == '__main__':
	banner()
	time.sleep(1)
	f1 = open('Image_links.txt', 'w+')
	search = raw_input("Enter Search Query e.g. Pak Army : ")
	directory = raw_input("Enter Directory Name : ")
	BASE_PATH = os.path.join(str(directory), search)
	if not os.path.exists(BASE_PATH):
		os.makedirs(BASE_PATH)
	go(search, str(directory), BASE_PATH)
	f1.close()
	print '\r\n'
	print '[-] All url saved in Image_links.txt file.\r\n'
	print '[+] Now Start Downloading Images....\r\n'
	a = []
	file = open('Image_links.txt').readlines()
	lenght = int(len(file))
	for ttt in file:
		ttt = ttt.strip('\r\n')
		if ttt in a:
			pass
		else:
			savePic(ttt, str(lenght), BASE_PATH)
		a.append(ttt)
		lenght -= 1	
	print '\r\n All Images Has Been Save. Please Check into the Directory. \r\n'
	print './ done'
	
