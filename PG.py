import string
import random

if __name__ == "__main__":
    s1 = string.ascii_lowercase
     # lowercase letter
    s2 = string.ascii_uppercase
     #Uppercase letter
    s3 = string.digits
    # All Digits
    s4 = string.punctuation
    # All Punctuation
    Passwordlength = int(input("Enter Password length\n")) #Todo1: Handle Gibberish
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    print("Your Password is: ")
    print("".join(random.sample(s, Passwordlength)))

