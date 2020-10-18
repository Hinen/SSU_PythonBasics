typeList = ['가위', '바위', '보']
resultList = []

for type1 in typeList:
    for type2 in typeList:
        resultList.append([type1, type2])

print(resultList)