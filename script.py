import numpy as np
import pandas as pd
print(len("fueled sexmachine"))
a = [123,123,1313213,43]
a.__reduce__

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

print(Kutya("Bodri", 4).faj)