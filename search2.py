import urllib.request
from bs4 import BeautifulSoup
import xml.dom.minidom
import re

while(1): 
	query=input("\nSearch Something: ")
	#print(list(query)[0].upper())
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
				print("\n"+x.childNodes[3].nodeValue.replace(")","",1).strip())
	except IndexError:
		pass