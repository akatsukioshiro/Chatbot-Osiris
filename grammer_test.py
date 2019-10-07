#!"python.exe"

state="0"

def type1(sen):
	global state
	#print(state)
	if(sen[0]=="shall" or sen[0]=="should" or sen[0]=="does" or sen[0]=="must" or sen[0]=="will" or sen[0]=="can" or sen[0]=="do" or sen[0]=="may" or sen[0]=="can" or sen[0]=="could" or sen[0]=="would" or sen[0]=="might"):
		if(sen[1]=="i" or sen[1]=="you" or sen[1]=="he" or sen[1]=="she" or sen[1]=="they" or sen[1]=="we" or sen[1]=="it"):
			if(sen[1]=="i" or sen[1]=="we" and state=="0"):
				sen[1]="you"
				state="1"
			elif(sen[1]=="you" and state=="0"):
				sen[1]="i"
				state="1"
			if(sen[len(sen)-1]=="you" and state=="1"):
				sen[len(sen)-1]="me"
				state="2"
			elif(sen[len(sen)-1]=="me" and state=="1"):
				sen[len(sen)-1]="you"
				state="2"
			elif(sen[len(sen)-1]=="something" and state=="1"):
				sen[len(sen)-1]="anything"
				state="2"
			x=""
			x=x+sen[1]+" "+sen[0]
			#print(x)
			for index in range(2,len(sen),1):
				if(index<(len(sen)-2)):
					if(sen[index]!="i" and sen[index]!="you" and sen[index]!="he" and sen[index]!="she" and sen[index]!="they" and sen[index]!="we" and sen[index]!="it" and sen[index]!="shall" and sen[index]!="will" and sen[index]!="can" and sen[index]!="do" and sen[index]!="may" and sen[index]!="can" and sen[index]!="could" and sen[index]!="would" and sen[index]!="might"):
						#print(sen[index])
						#print(sen[index+1])
						#print(sen[index+2])
						
						if(sen[index+1]=="your"):
							sen[index+1]="my"
						elif(sen[index+1]=="my" or sen[index+1]=="our"):
							sen[index+1]="your"
						elif(sen[index+1]=="myself"):
							sen[index+1]="yourself"
						elif(sen[index+1]=="yourself"):
							sen[index+1]="myself"
						if(sen[index+2]!="can" and sen[index+2]!="could" and sen[index+2]!="may" and sen[index+2]!="might"):
							if(sen[index+1]=="you"):
								sen[index+1]="me"
							elif(sen[index+1]=="me" or sen[index+1]=="us"):
								sen[index+1]="you"
							elif(sen[index+1]=="i" or sen[index+1]=="we"):
								sen[index+1]="you"
						elif(sen[index+2]=="can" or sen[index+2]=="could" or sen[index+2]=="may" or sen[index+2]=="might"):
							if(sen[index+1]=="you"):
								sen[index+1]="i"
							elif(sen[index+1]=="i" or sen[index+1]=="we"):
								sen[index+1]="you"
								
				x=x+" "+sen[index]
				#print(x)
				
			return x.capitalize()

def type2(sen):
	global state
	if(sen[0]=="am" or sen[0]=="are" or sen[0]=="is" or sen[0]=="has" or sen[0]=="have" or sen[0]=="will" or sen[0]=="would" or sen[0]=="shall" or sen[0]=="should"):
		if(sen[1]=="i" or sen[1]=="it" or sen[1]=="we" or sen[1]=="he" or sen[1]=="she" or sen[1]=="they" or sen[1]=="you" ):
			if(sen[1]=="i" and sen[0]=="am" and state=="0"):
				sen[1]="you"
				sen[0]="are"
				#print("1")
				state="1"
			elif(sen[1]=="we" and sen[0]=="are" and state=="0"):
				sen[1]="you"
				sen[0]="are"
				#print("2")
				state="1"
			elif(sen[1]=="you" and sen[0]=="are" and state=="0"):
				sen[1]="i"
				sen[0]="am"
				#print("3")
				state="1"
			if(sen[len(sen)-1]=="you" and state=="1"):
				sen[len(sen)-1]="me"
				state="2"
			elif(sen[len(sen)-1]=="me" and state=="1"):
				sen[len(sen)-1]="you"
				state="2"
			elif(sen[len(sen)-1]=="something" and state=="1"):
				sen[len(sen)-1]="anything"
				state="2"
			x=""
			x=x+sen[1]+" "+sen[0]
			for index in range(2,len(sen),1):
				if(index<(len(sen)-2)):
					if(sen[index]!="i" and sen[index]!="you" and sen[index]!="he" and sen[index]!="she" and sen[index]!="they" and sen[index]!="we" and sen[index]!="it" and sen[index]!="shall" and sen[index]!="will" and sen[index]!="can" and sen[index]!="do" and sen[index]!="may" and sen[index]!="can" and sen[index]!="could" and sen[index]!="would" and sen[index]!="might"):
						if(sen[index+1]=="me" or sen[index+1]=="us"):
							sen[index+1]="you"
						elif(sen[index+1]=="you"):
							sen[index+1]="me"
						elif(sen[index+1]=="your"):
							sen[index+1]="my"
						elif(sen[index+1]=="my" or sen[index+1]=="our"):
							sen[index+1]="your"
						
				x=x+" "+sen[index]
			return x.capitalize()

def type3(sen):
	global state
	if(sen[0]=="when" or sen[0]=="where" or sen[0]=="what"):#which,whom,why
		if(sen[1]=="am" or sen[1]=="are" or sen[1]=="is" or sen[1]=="has" or sen[1]=="have" or sen[1]=="will" or sen[1]=="would" or sen[1]=="shall" or sen[1]=="should" or sen[1]=="do" or sen[1]=="must" or sen[1]=="might" or sen[1]=="could" or sen[1]=="will" or sen[1]=="may" or sen[1]=="does"):
			if(sen[2]=="i" or sen[2]=="it" or sen[2]=="we" or sen[2]=="he" or sen[2]=="she" or sen[2]=="they" or sen[2]=="you" or sen[2]=="your" or sen[2]=="their" ):
				if(sen[2]=="i" and sen[1]=="am" and state=="0"):
					sen[2]="you"
					sen[1]="are"
					#print("1")
					state="1"
				elif(sen[2]=="we" and sen[1]=="are" and state=="0"):
					sen[2]="you"
					sen[1]="are"
					#print("2")
					state="1"
				elif(sen[2]=="you" and sen[1]=="are" and state=="0"):
					sen[2]="i"
					sen[1]="am"
					#print("3")
					state="1"
				elif(sen[2]=="i" or sen[2]=="we" and state=="0"):
					sen[2]="you"
					state="1"
				elif(sen[2]=="you" and state=="0"):
					sen[2]="i"
					state="1"
			
				if(sen[len(sen)-1]=="you" and state=="1"):
					sen[len(sen)-1]="me"
					state="2"
				elif(sen[len(sen)-1]=="me" and state=="1"):
					sen[len(sen)-1]="you"
					state="2"
				elif(sen[len(sen)-1]=="something" and state=="1"):
					sen[len(sen)-1]="anything"
					state="2"
				x=""
				x=x+sen[2]+" "+sen[1]
				for index in range(3,len(sen),1):
					if(index<(len(sen)-2)):
						if(sen[index]!="i" and sen[index]!="you" and sen[index]!="he" and sen[index]!="she" and sen[index]!="they" and sen[index]!="we" and sen[index]!="it" and sen[index]!="shall" and sen[index]!="will" and sen[index]!="can" and sen[index]!="do" and sen[index]!="may" and sen[index]!="can" and sen[index]!="could" and sen[index]!="would" and sen[index]!="might"):
							#print(sen[index])
							#print(sen[index+1])
							#print(sen[index+2])
						
							if(sen[index+1]=="your"):
								sen[index+1]="my"
							elif(sen[index+1]=="my" or sen[index+1]=="our"):
								sen[index+1]="your"
							elif(sen[index+1]=="myself"):
								sen[index+1]="yourself"
							elif(sen[index+1]=="yourself"):
								sen[index+1]="myself"
							if(sen[index+2]!="can" and sen[index+2]!="could" and sen[index+2]!="may" and sen[index+2]!="might"):
								if(sen[index+1]=="you"):
									sen[index+1]="me"
								elif(sen[index+1]=="me" or sen[index+1]=="us"):
									sen[index+1]="you"
								elif(sen[index+1]=="i" or sen[index+1]=="we"):
									sen[index+1]="you"
							elif(sen[index+2]=="can" or sen[index+2]=="could" or sen[index+2]=="may" or sen[index+2]=="might"):
								if(sen[index+1]=="you"):
									sen[index+1]="i"
								elif(sen[index+1]=="i" or sen[index+1]=="we"):
									sen[index+1]="you"
								
					x=x+" "+sen[index]
					#print(x)
				
				return x.capitalize()
				
		

while(1):
	state="0"
	#print("hi")
	x=input("ques: ").lower()
	x=x.replace("?","")
	x=x.strip()	
	sen=x.split(" ")
	choice_arr=[]
	choice_arr.append(str(type1(sen)))
	choice_arr.append(str(type2(sen)))
	choice_arr.append(str(type3(sen)))
	for ch in choice_arr:
		if(ch!="None"):
			print(ch)
			break
	
	