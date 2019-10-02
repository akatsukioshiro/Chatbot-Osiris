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
	
###################################### DON'T EDIT THESE EVER #########################################

state="1"
	
def main(imports,ask):
	global state
	commands=imports.strip().split("\n")
	for index in range(0,len(commands),1):
		if(commands[index].strip()==""):
			continue
		#print(">>> "+commands[index])
		if(commands[index].split(":")[0].strip()=="dialogue" and ask.strip("?").strip().lower()==commands[index].split(":")[1].strip("?").strip().lower()):
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
					
		if(ask.strip()=="exit"):
			state="0"
			break


while state=="1":
	ask = input("Say Something: ")
	main(imports,ask)