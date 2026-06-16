import random
n = random.randint(1,100)
a= -1
guesses = 0
while(a !=n):
   
    a = int(input("Entert the number : "))
    if a>n:
        print("Enter a LOWER number:")
        guesses +=1
    elif a<n:
        print("Enter a HIGHER number :")
        guesses +=1
print(f" You have guess  '{n}' this number correctly in : {guesses} attempt")         
     