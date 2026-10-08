names = []
numbers = []

for i in range(5):
    name = input("Enter name: ")
    number = int(input("Enter number: "))

    names.append(name)
    numbers.append(number)

print("Maximum number:", max(numbers))

names.sort(reverse=True)

print("Names in descending order:")
print(names)