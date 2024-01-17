import random
import string

print("                     Password Generator\n")
l=int(input("Enter the length of the password to be generated: "))
print("\nGenerating strong password......")
pas=""
for i in range(l-1):
    pas=pas+random.choice(string.ascii_letters+string.digits)
pas+=random.choice('@'+'#'+'$'+'!'+'&')
print("\nGenerated Password is: ",pas)
