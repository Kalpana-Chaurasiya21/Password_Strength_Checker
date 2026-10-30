# password strength checker 
import re

#password strength check conditions:
#min 8 chars, digit, upperccase, lowercase, special char


def check_password_strength(password):
       if len(password)<8: #length of password
              return "Weak: password must be at least 8 chars"
       
       if not any(char.isdigit() for char in password):
              return "Weak:password must contain a digit"

       if not any(char.islower() for char in password):
              return "Weak: password must contain an lower chars"


       if not re.search(r'[!@#$%^&*(){}<>>?]',password):
              return "Medium: password must contain a special char"

       return "Strong: Your password is secured!"


def password_checker():
       print("Welcome to the password strength checker")

       while True:
            password=input("Enter your password(or type 'exit' to quite): ")
            if password.lower()=='exit':
                   print("Thank you for using this tool")
                   break


            result=check_password_strength(password)
            print(result)


#Run the password_checker tool

if __name__=="__main__":
       password_checker()
       

       