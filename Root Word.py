import urllib.request
from bs4 import BeautifulSoup
import xml.dom.minidom
import re

searchRoot = []
state=0

def rem(word):
	regex = re.compile('[^a-zA-Z]')
	return regex.sub('', word.strip())

def root(query):
	global searchRoot, state
	file=open("Osiris Library List\OPTED v0.03 Letter "+list(query)[0].upper()+".html","r")
	dictn=file.read()
	file.close()
	dictn=dictn.replace('<!-- saved from url=(0057)http://www.mso.anu.edu.au/~ralph/OPTED/v003/wb1913_a.html --><html class="gr__mso_anu_edu_au">',"").replace("</html>","")
	m=re.compile('(?<=(<body data-gr-c-s-loaded="true">))((.|\n)*?)(?=(</body>))').search(dictn)
	sentences='<xml>'+m.group(2)+"</xml>"
	document=xml.dom.minidom.parseString(sentences);
	try:
		for x in document.getElementsByTagName("p"):
			if(x.childNodes[0].firstChild.nodeValue.lower().strip()==query.lower().strip()):
				#print(x.childNodes[0].firstChild.nodeValue)
				#print("\n"+x.childNodes[3].nodeValue.replace(")","",1).strip())
				if(x.childNodes[2].nodeName == "i"):
					#print(x.childNodes[3].nodeValue.replace(")","",1).strip())
					#print("\'"+x.childNodes[2].firstChild.nodeValue.strip()+"\'")
					if(x.childNodes[2].firstChild.nodeValue.strip() != "n." and x.childNodes[2].firstChild.nodeValue.strip() != "v. t." and x.childNodes[2].firstChild.nodeValue.strip() != "v." and x.childNodes[2].firstChild.nodeValue.strip() != "prep."):# and x.childNodes[2].firstChild.nodeValue.strip() != "v. i."):
						searchRoot.append(x.childNodes[3].nodeValue.replace(")","",1).strip())
						#print(x.childNodes[3].nodeValue.replace(")","",1).strip())
				state=1
	except (IndexError,AttributeError):
		try:
			if(len(x.childNodes[2].childNodes) == 0 and query!="i"):
				searchRoot.append(x.childNodes[3].nodeValue.replace(")","",1).strip())
		except IndexError:
			pass
		pass
	#print(state)
	for x in searchRoot:
		if(x.strip().split(" ")[0].lower() != "the"):
			for y in range(0,len(x.strip().split(" ")),1):
				if(x.strip().split(" ")[y].lower() == "of"):
					print(rem(x.strip().split(" ")[y+1].lower()))
					state=2
					break
			break
		elif(x.strip().split(" ")[0].lower() == "the"):
			for y in range(0,len(x.strip().split(" ")),1):
				if(x.strip().split(" ")[y].lower() == "verb"):
					print(rem(x.strip().split(" ")[y+1].lower()[:(len(list(x.strip().split(" ")[y+1].lower()))-1)]))
					state=2
					break
				elif(x.strip().split(" ")[y].lower().capitalize() == "See"):
					print(rem(x.strip().split(" ")[y+1].lower()[:(len(list(x.strip().split(" ")[y+1].lower()))-1)]))
					state=2
					break
			break
	searchRoot=[]
	#print(state)

def rootword(query): 
	global state
	state=0
	query=rem(query.lower())
	root(query)
	
	if(state == 0):
		if(list(query)[len(list(query))-1]=="s"):
			query="".join(list(query)[:(len(list(query))-1)])
			root(query)
	
	if(state == 0):
		print(query)
	elif(state == 1):
		print(query)
		
					
while(1):
	query=input("\nSearch Something: ")
	for x in query.split(" "):
		rootword(x.strip())