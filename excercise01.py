A = "hello"
C = ["hello", "goodbye", "hello", "hello goodbye", "goodbye", "hello", "goodhellow"]
exactCount = 0
count = 0
map1 = {}
currMax = 0
for word in C:
    map2 = {}
    if word == "hello":
        exactCount+= 1
    if "hello" in word:
        count += 1
    for letter in word:
        map2[letter] = map2.get(letter,0) + 1
    map1[word] = map2
print(f"the word hello was in the array exactly {exactCount} times")
print(f"the word hello occured in the array {count} times")
currentmax = ""
count = 0
map3 = {"g":1,"o":3, "d":1,"f":1,"l":2,"w":1}
for i,j in map1.items():
    letcount = 0
    for key,val in j.items():
        if map3.get(key):
            if map3[key] > j[key]:
                letcount += j[key]
            else:
                letcount += map3[key]
    if letcount > count:
        count = letcount
        currentmax = i
print(f"most similar string to goodfellow is {currentmax}")






