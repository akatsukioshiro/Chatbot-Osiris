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

state="1"
prev_ask=""
	
def main(sub_imports,ask):
	global state,imports
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
			state="0"
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
	if(exists=="0" and ask.strip()!="exit" and ask.strip().lower()!="no"):
		reask = input("And what must be the answer ?: ")
		if(reask.strip()!="exit"):
			content="\ndialogue: "+ask+"\nresponse: "+reask
			rem=open(omllibs+"User_Custom.oml","a+")
			rem.write(content)
			rem.close()
			imports=""
			reset()


while state=="1":
	ask = input("Say Something: ")
	if(ask.strip().lower()!="no"):
		prev_ask=ask
	main(imports,ask)