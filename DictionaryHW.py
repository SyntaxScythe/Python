dictionary = {'Codingal': 3, 'is': 2, 'best': 2, 'for': 2, 'Coding': 1}
print(dictionary)

value = int(input("Enter the value: "))
print("Frequency:", list(dictionary.values()).count(value))