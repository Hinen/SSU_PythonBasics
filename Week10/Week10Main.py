def incTypeCount(char):
    global digitCount
    global spaceCount
    global alphaCount

    if char.isdigit():
        digitCount += 1
    elif char.isspace():
        spaceCount += 1
    if char.isalpha():
        alphaCount += 1

digitCount = 0
spaceCount = 0
alphaCount = 0

str = input("문자열을 입력하세요.")
for c in str:
    incTypeCount(c)

print("digits : %d spaces : %d alphas : %d" % (digitCount, spaceCount, alphaCount))