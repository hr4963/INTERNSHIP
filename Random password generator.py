import random
import string
print("HEY USER WELCOME TO RANDOM PASSWORD GENERATOR")
def main():
        
        length=int(input("ENTER THE LENGTH YOU WANT"))
        lowerD=string.ascii_lowercase
        upperD=string.ascii_uppercase
        digitD=string.digits
        symbolD=string.punctuation
        combine=lowerD+upperD+digitD+symbolD
        x=random.sample(combine,length)
        password="".join(x)
        print(password)
        main()

main()