list1 = []
list2 = []
dict1 = {}
with open("test.txt", 'r') as file:
    for line in file:
        list1.append(line.strip())
for line in list1:
    for word in line.split():
        list2.append(word)
        dict1[word] = dict1.get(word,0) + 1
print(dict1)
