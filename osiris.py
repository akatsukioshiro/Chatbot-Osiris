#!"python.exe"
import random

#------------------------------- Set Library List and OML File Paths --------------------------------#
oslibli="Osiris Library List\\" # ( import List of OML Libraries Path )
omllibs="OML Speech Libraries\\" # ( OML Libraries file path )

#################################<<<<< FORBIDDEN SECTION 001 >>>>>####################################
###################################### DON'T EDIT THESE EVER #########################################

#----------------------------------- import List of OML Libraries -----------------------------------#
oml=open(oslibli+"osiris.libs","r")
script=oml.readlines()
oml.close()

#----------------------------- global variable to concat all lib contents ---------------------------#
imports=""

#-------------------------------- function to concat all lib contents -------------------------------#
def reset():
	def import_oml(oml_file):
		global imports
		try:
			oml=open(omllibs+oml_file,"r")
			imports=imports+"\n"+oml.read()
			oml.close()
		except Exception as e:
			print(">>> Error[01]: Import File << "+oml_file+" >> Not Found")

#------------------------------------------- keywords list ------------------------------------------#
	command_list=["import"]

#----------------------------------------- Libraries Concat -----------------------------------------#
	for code in script:
		feeds=code.strip().split(" ")
		if(feeds[0]==command_list[0]):
			import_oml(feeds[1])

reset()	
###################################### DON'T EDIT THESE EVER #########################################

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
	if(sen[0]=="am" or sen[0]=="are" or sen[0]=="is" or sen[0]=="has" or sen[0]=="has" or sen[0]=="have" or sen[0]=="will" or sen[0]=="would" or sen[0]=="shall" or sen[0]=="should"):
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

stateX="1"
prev_ask=""
	
def main(sub_imports,ask):
	global stateX,imports
	exists="0"
	commands=sub_imports.strip().split("\n")
	for index in range(0,len(commands),1):
		if(commands[index].strip()==""):
			continue
		#print(">>> "+commands[index])
		if(commands[index].split(":")[0].strip()=="dialogue" and ask.strip("?").strip().lower()==commands[index].split(":")[1].strip("?").strip().lower()):
			exists="1"
			if(commands[index+1].split(":")[0].strip()=="response"):
				print(commands[index+1].split(":")[1].strip())
				break
			elif(commands[index+1].split(":")[0].strip()=="random" and commands[index+1].split(":")[1].strip()=="start"):
				randvalues=[]
				for subindex in range((index+1),len(commands),1):
					if(commands[subindex].strip().split(":")[0].strip()=="response"):
						randvalues.append(commands[subindex].strip())
					elif(commands[subindex].strip().split(":")[0].strip()=="random" and commands[subindex].strip().split(":")[1].strip()=="stop"):
						break
				print(randvalues[random.randrange(0, len(randvalues), 1)].split(":")[1].strip())
		
		if(ask.strip().lower()=="exit"):
			stateX="0"
			break
		elif(ask.strip().lower()=="no"):
			reask = input("And what must be the answer ?: ")
			if(reask.strip()!="exit"):
				rem=open(omllibs+"User_Custom.oml","r+")
				dats=rem.readlines()
				rem.close()
				for line in range(0,len(dats),1):
					if(dats[line].strip()==""):
						continue
					#print(">>>dialogue: "+prev_ask.strip("?").strip())
					temp=dats[line]
					temp=temp.replace("?","")
					#print("<<<"+temp.strip())
					if("dialogue: "+prev_ask.strip("?").strip()==temp.strip()):
						dats[line+1]="response: "+reask+"\n"
						#print(dats[line+1])
				rem=open(omllibs+"User_Custom.oml","w+")
				rem.write("")
				rem.close()
				rem=open(omllibs+"User_Custom.oml","a+")
				for line in range(0,len(dats),1):
					#print(dats[line])
					rem.write(dats[line])
				rem.close()
				imports=""
				reset()
			break
	
	gram_escape="0"
	
	if(exists=="0" and ask.strip()!="exit" and ask.strip().lower()!="no"):
		state="0"
		x=ask.lower()
		x=x.replace("?","")
		x=x.strip()	
		sen=x.split(" ")
		choice_arr=[]
		choice_arr.append(str(type1(sen)))
		choice_arr.append(str(type2(sen)))
		#choice_arr.append(str(type3(sen)))
		for ch in choice_arr:
			if(ch!="None"):
				print(ch)
				gram_escape="1"
				break
				
	if(exists=="0" and ask.strip()!="exit" and ask.strip().lower()!="no" and gram_escape=="0"):
		reask = input("And what must be the answer ?: ")
		if(reask.strip()!="exit"):
			content="\ndialogue: "+ask+"\nresponse: "+reask
			rem=open(omllibs+"User_Custom.oml","a+")
			rem.write(content)
			rem.close()
			imports=""
			reset()


while stateX=="1":
	ask = input("Say Something: ")
	if(ask.strip().lower()!="no"):
		prev_ask=ask
	main(imports,ask)