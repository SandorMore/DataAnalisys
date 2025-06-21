import numpy as np
import pandas as pd

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