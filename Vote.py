from Check import *

first = 0
second = 0
third = 0

def re_check():
    passed = check()
    if passed == True: pass
    else: print("Wrong ID or Password")
    
def vote():
    re_check()
    v = input("Which candidate(1 or 2 or 3): ")
    return v

vote()