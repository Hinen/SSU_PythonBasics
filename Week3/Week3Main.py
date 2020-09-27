print("## 안나와 신후의 가위, 바위, 보 게임 ##")
anna = input("안나를 위한 가위, 바위, 보를 입력하세요 : ")
sinHoo = input("신후를 위한 가위, 바위, 보를 입력하세요 : ")

error = False
if anna != "가위" and anna != "바위" and anna != "보":
    print("안나 값 입력 오류 -> " + anna)
    error = True

if sinHoo != "가위" and sinHoo != "바위" and sinHoo != "보":
    print("신후 값 입력 오류 -> " + sinHoo)
    error = True

if not error:
    if anna == sinHoo:
        print("무승부")
    elif (anna == "가위" and sinHoo == "보") or (anna == "바위" and sinHoo == "가위") or (anna == "보" and sinHoo == "바위"):
        print("안나 승리")
    else:
        print("신후 승리")