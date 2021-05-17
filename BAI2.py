import re
file = open("paper.txt",encoding="utf8")
wordArr =[]
for line in file:
    res = re.findall(r'\w+', line)
    wordArr += res


print(wordArr)
#Tu xuat hien nhieu nhat trong file
print("Từ xuất hiện nhiều nhât trong file: ",end="")
print(max(set(wordArr),key = wordArr.count))

#Tạo bộ từ điển
wordSet = list(set(wordArr))
wordSet.sort()
print(wordSet)

#Dictionary
wordDict = dict()
for key in wordSet:
    wordDict[key] = wordArr.count(key)
print(wordDict)