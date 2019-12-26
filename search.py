import urllib.request
from bs4 import BeautifulSoup
import xml.dom.minidom
import re



try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found") 

while(1): 
	# to search 
	#query = "internet meanings"
	query=input("Search Something: ")
	query=query+" dictionary meanings"
	try:
		k=""  
		for j in search(query, tld="com", num=10, stop=1, pause=2): 
			#print(j)
			if(j.strip()!=""):
				k=j
		page = urllib.request.urlopen(k).read()
		soup = BeautifulSoup(page,features="html.parser")
		soup.prettify()
		bloop=str(soup).replace('<html lang="en">',"").strip()#.replace("<!DOCTYPE doctype html>\n\n","<xml>").replace("</html>","</xml>").strip()
		#print(bloop)

		m=re.compile('(?<=(<div class="def ddef_d">))((.|\n)*?)(?=(</div>))').search(bloop)
		#print(m.group(2));
		sentences='<xml><div class="def ddef_d">'+m.group(2)+"</div></xml>"
		document=xml.dom.minidom.parseString(sentences);
		output=""
		for x in range(0,len(document.getElementsByTagName("div")[0].childNodes),1):
			if(document.getElementsByTagName("div")[0].childNodes[x].nodeValue!=" " and str(document.getElementsByTagName("div")[0].childNodes[x].nodeValue)!="None"):
				#print(document.getElementsByTagName("div")[0].childNodes[x].nodeValue);
				if(str(document.getElementsByTagName("div")[0].childNodes[x].nodeValue)!="None"):
					output=output+" "+str(document.getElementsByTagName("div")[0].childNodes[x].nodeValue).strip()
			elif(str(document.getElementsByTagName("div")[0].childNodes[x].nodeValue)=="None"):
				#print(document.getElementsByTagName("div")[0].childNodes[x].childNodes[0].nodeValue);
				output=output+" "+str(document.getElementsByTagName("div")[0].childNodes[x].childNodes[0].nodeValue).strip()
				if(str(document.getElementsByTagName("div")[0].childNodes[x].childNodes[0].nodeValue)=="None"):
					#print(document.getElementsByTagName("div")[0].childNodes[x].childNodes[0].firstChild.nodeValue)
					output=output+" "+str(document.getElementsByTagName("div")[0].childNodes[x].childNodes[0].firstChild.nodeValue).strip()
		
		output=output.replace("None ","").strip().split("(")[0]
		print(output)
		#for anchor in soup.findAll('div class="def ddef_d"'):
		#    print(anchor)
	except AttributeError as e:
		try:
			page = urllib.request.urlopen("https://dictionary.cambridge.org/dictionary/english/"+query).read()
			soup = BeautifulSoup(page,features="html.parser")
			soup.prettify()
			bloop=str(soup).replace('<html lang="en">',"").strip()#.replace("<!DOCTYPE doctype html>\n\n","<xml>").replace("</html>","</xml>").strip()
			#print(bloop)
		
			m=re.compile('(?<=(<div class="def ddef_d">))((.|\n)*?)(?=(</div>))').search(bloop)
			#print(m.group(2));
			sentences='<xml><div class="def ddef_d">'+m.group(2)+"</div></xml>"
			document=xml.dom.minidom.parseString(sentences);
			output=""
			for x in range(0,len(document.getElementsByTagName("div")[0].childNodes),1):
				if(document.getElementsByTagName("div")[0].childNodes[x].nodeValue!=" " and str(document.getElementsByTagName("div")[0].childNodes[x].nodeValue)!="None"):
					#print(document.getElementsByTagName("div")[0].childNodes[x].nodeValue);
					if(str(document.getElementsByTagName("div")[0].childNodes[x].nodeValue)!="None"):
						output=output+" "+str(document.getElementsByTagName("div")[0].childNodes[x].nodeValue).strip()
				elif(str(document.getElementsByTagName("div")[0].childNodes[x].nodeValue)=="None"):
					#print(document.getElementsByTagName("div")[0].childNodes[x].childNodes[0].nodeValue);
					output=output+" "+str(document.getElementsByTagName("div")[0].childNodes[x].childNodes[0].nodeValue).strip()
					if(str(document.getElementsByTagName("div")[0].childNodes[x].childNodes[0].nodeValue)=="None"):
						#print(document.getElementsByTagName("div")[0].childNodes[x].childNodes[0].firstChild.nodeValue)
						output=output+" "+str(document.getElementsByTagName("div")[0].childNodes[x].childNodes[0].firstChild.nodeValue).strip()
		
			output=output.replace("None ","").strip().split("(")[0]
			print(output)
			#for anchor in soup.findAll('div class="def ddef_d"'):
			#    print(anchor)
		except Exception:
			pass