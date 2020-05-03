import random

print("how many times do u wanna play this game...?????")

k=0

k=int(input())

for l in range(k):
 
	x=0
   
	x=random.randrange(0,10)
   
	print("enter ur choice but it should be in 0 to 10")
  
	y=0
   
 	y=int(input())
  
  	if(y==x):
     
   		print("congratulations u won!")
  
  	elif(y>x):
  
      		print("choice is greater than magic number ;(")
   
 	elif(y<x):
      
  		print("choice is smaller than magic number oopsie!!!")
  
  	else:
      
  		print("something went wrong!!!!")
   
 
   	print("Btw magic number was")
    
	print (x)

print("thank you:)")