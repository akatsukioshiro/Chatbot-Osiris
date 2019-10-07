#!"python.exe"

oslibli="Osiris Library List\\"

emo=open(oslibli+"emotionalizer.libs","r+")
const=emo.readlines()
emo.close()

emo_dict=dict()

while(1):
	constants=[]
	pos=[]
	neg=[]
	for em in const:
		cats=em.split(":")
		emo_dict.update({cats[0]:cats[1]})
	for x in emo_dict:
		#print(x)
		for y in emo_dict[x]:
			emo_dict[x]=emo_dict[x].replace("\n","")
			if(x=="constants"):
				constants=emo_dict[x].split(",")
			elif(x=="pos"):
				pos=emo_dict[x].split(",")
			elif(x=="neg"):
				neg=emo_dict[x].split(",")
	#print(constants)
			
			
	
	line=input("ques: ")
	cage=line.lower().split(" ")
	word=set(cage).difference(set(constants))
	if(word.intersection(set(pos))):
		print("pos")
	elif(word.intersection(set(neg))):
		print("neg")