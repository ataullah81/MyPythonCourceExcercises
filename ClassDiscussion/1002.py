words1 = list(map(str, input().split()))
words2 = list(map(str, input().split()))

word3 = ""
word4 = ""
for i in words1:
    word3 += str(i)
for j in words2:
    word4 += str(j)
if word3 == word4:
    print("true")
else:
    print("false")
#print("word1 represents string", words1[0], "+", words1[1], "->", word3)
print(word3)
print(word4)
