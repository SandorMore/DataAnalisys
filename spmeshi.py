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
def printf(msg):
    print(msg)
nums = [1,2,34,5,6,7,8,9]
for i in range(0, 21):
    printf("asd")
print(list(set(tuple(list(num for num in map(int, nums) if num >= 5)))))


    
printf("asd")


def sort(list):
    list = sorted(list)
    return list

a = [2,1,23,12,1012,3]
sort(a)