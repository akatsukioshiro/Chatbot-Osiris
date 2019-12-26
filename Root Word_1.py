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
	#try:
	options=[]
	for x in document.getElementsByTagName("p"):
		try:
			if(x.childNodes[0].firstChild.nodeValue.lower().strip()==query.lower().strip()):
				#print("\n"+x.childNodes[3].nodeValue.replace(")","",1).strip())
				#if(len(x.childNodes[2].childNodes) != 0):
				#	print("\n"+x.childNodes[2].firstChild.nodeValue.strip())
				if(x.childNodes[2].nodeName == "i"):
					if(len(x.childNodes[2].childNodes) != 0):
						options=x.childNodes[2].firstChild.nodeValue.strip().split("&")
			
					#print(options)
					for opt in options:
						#print(opt)
						if(opt.strip()=="p. pr."):
							searchRoot.append(x.childNodes[3].nodeValue.replace(")","",1).strip())
						elif(opt.strip()=="p. p."):
							searchRoot.append(x.childNodes[3].nodeValue.replace(")","",1).strip())
						elif(opt.strip()=="imp."):
							searchRoot.append(x.childNodes[3].nodeValue.replace(")","",1).strip())
						elif(opt.strip()=="v."):
							searchRoot.append(x.childNodes[3].nodeValue.replace(")","",1).strip())
						elif(len(x.childNodes[2].childNodes) == 0 and query!="i"):
							searchRoot.append(x.childNodes[3].nodeValue.replace(")","",1).strip())
						else: 
							continue
			elif(x.childNodes[0].firstChild.nodeValue.lower().strip()!=query.lower().strip()):
				continue
			state=1
		except IndexError:
			continue
	for x in searchRoot:
		if(x.strip().split(" ")[0].lower() != "the"):
			for y in range(0,len(x.strip().split(" ")),1):
				if(x.strip().split(" ")[y].lower() == "of"):
					print(rem(x.strip().split(" ")[y+1].lower()))
					state=2
					break
			break
		else:
			for y in range(0,len(x.strip().split(" ")),1):
				if(x.strip().split(" ")[y].lower() == "of"):
					if(x.strip().split(" ")[y+1].lower() == "the"):
						if(x.strip().split(" ")[y+2].lower() == "verb"):
							print(rem(x.strip().split(" ")[y+3].lower()))
							state=2
							break
			if(state!=2):
				for y in range(0,len(x.strip().split(" ")),1):
					if(x.strip().split(" ")[y] == "See"):
						if(list(x.strip().split(" ")[y-1])[len(list(x.strip().split(" ")[y-1]))-1] == "."):
							if(list(x.strip().split(" ")[y+1])[len(list(x.strip().split(" ")[y+1]))-1] == "."):
								print(rem(x.strip().split(" ")[y+1].lower()))
								state=2
								break
			break
		
	searchRoot=[]
	options=[]
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