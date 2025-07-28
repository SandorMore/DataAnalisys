x = 1;
y = 1;

print(x- - - - -y)
for i in "Sigma":
    print(i, end="\t")

print(*range(1,100), sep=" ", end="\t")

print('\"negate\"')

class Sigma:
    def __init__(self, kor : int):
        self.kor = kor
    
    def Print(msg : str):
        print(msg)
#no double printing
Sigma1 = Sigma(12)

print(Sigma1.Print())
for i, j in enumerate([7,21,323,421,123,55,7534,1]):
    print(f"Index is: {i}, and value is: {j}")