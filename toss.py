import random as r
def tamp():
	lis=[]
	rang=int(input("   enter number of player"))
	i=1
	for i in range(rang):
		lis.append(i+1)

	while (rang!=0):
		sn=1
		name=input("   enter player name  ")
		rand=r.choices(lis)
		print(f"   {sn} {name} = {rand[0]}")
		lis.remove(rand[0])
		rang-=1
		sn+=1
	  
tamp()