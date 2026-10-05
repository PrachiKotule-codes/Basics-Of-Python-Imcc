# Accept S and N. Print square of first N numbers starting from S

S = int(input("Enter starting number: "))
N = int(input("Enter N: "))

for i in range(S, S + N):
    print(i * i)



