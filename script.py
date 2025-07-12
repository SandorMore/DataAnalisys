import numpy as np
import pandas as pd
import random


print("jabud", *range(10), sep="\t")
print(len("fueled sexmachine"))
a = [123,123,1313213,43]
a.__reduce__
def playGame():
    counter = 0
    thought = random.randint(1,100)
    while True:
        x = int(input("Gondoltam egy szamra"))
        if x == thought:
            print("Nyertél")
            print( f"{counter} tippből találtad ki")
            break
        
        elif x > thought:
            print("Az számom kisebb mint amire te gondoltál")
        elif x < thought:
            print("A számom nagyobb mint amire te gondoltál")

        counter += 1    
    return

print("jabud")
print("sigma")

playGame()
s = ""

letters = ['a','b','z', 'r', 'z', 'm', 'z']
s = s.join(letters)
c = 3
print(s)
print(c + (b := 4))

name = str(input("Name here: "))
list_of_banned_names = ["nigga", "ass", "nigger", "hell", "fuck", "reggin", "aggin", "fasz", "geci"]

for banned in list_of_banned_names:
    if banned in name:
        name = name.replace(banned, "*" * len(banned))

print(name)
name = name.replace(" ", "")
print(f"A nec hossza whitespace nelkul: {len(name.strip())}")
class Kutya:
    def __init__(self, name, faj):
        self.name = name
        self.faj = faj

        if type(self.faj) != type("a"):
            print("sigma")
    
    tries = ["ye","no"]
    num = random.randint(1,len(tries))

    def ugat(self):
        return "Vau"

class Goon:
    def __init__(self, load : int, daysOfCharge : int, fertile : bool):
        self.load = load
        self.daysOfCharge = daysOfCharge
        self.fertile = fertile

    def Bust(self):
        self.daysOfCharge = 0
        print("Busted a nut") 
    
        if self.fertile:
            return "Chance for a child"

    def Edge(self):
        return "Nincs bust kishaver!"
    
    def Baszas(spermStrength : int):
        gyerekszületés : int = random.randint(1,10) * spermStrength
        if gyerekszületés > 35:
            return "Gyereked lesz"
        return "Nincs gyerek"
    
    def SilentGoon(hangerő : int):
        if (hangerő > 5):
            return "Lebuktál"
        return "Shussh"

print(Kutya("Bodri", 4).ugat())
print(Goon(5, 11, True).Bust())