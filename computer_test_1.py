# import wireless_charging  # 무선충전 모듈을 임포트합니다. (실제로 존재하는 모듈이 아님, 예시용)

# 자리 안내
seats = {
    "1조": 6,
    "2조": 7,
    "3조": 7,
    "4조": 8,
    "5조": 9,
    "6조": 8,
}

# 자리 선택 함수
def choose_seat():
    print("자리 배치 안내:")
    print('1조(6명) | 4조(8명) \n2조(7명) | 5조(9명) \n3조(7명) | 6조(8명)')
    print()

    # 컴퓨터 자리 안내
    print("4조 바로 앞에 컴퓨터 자리가 있습니다.\n")

    # 사용자 선택
    choice = input("모둠 자리(1조, 2조, 3조, 4조, 5조, 6조) 또는 컴퓨터 자리를 선택하세요: ").strip()

    # 선택에 따른 출력

    if choice == '1조':
        print("자리 TV전원이 켜집니다.")
    elif choice == '2조':
        print("자리 TV전원이 켜집니다.")
    elif choice == '3조':
        print("자리 TV전원이 켜집니다.")
    elif choice == '4조':
        print("자리 TV전원이 켜집니다.")
    elif choice == '5조':
        print("자리 TV전원이 켜집니다.")
    elif choice == '6조':
        print("자리 TV전원이 켜집니다.")

    elif choice == "컴퓨터자리":
        print("TV와 컴퓨터 전원이 켜집니다.")
        # # 무선 충전 코드 실행
        # wireless_charging.activate()  # 예시로 무선충전 활성화
    elif choice in seats:
        print(f"{choice}에 TV화면이 켜집니다.")
        # # 무선 충전 코드 실행
        # wireless_charging.activate()  # 예시로 무선충전 활성화
    else:
        print("잘못된 선택입니다. 다시 선택해 주세요.")

# 자리 선택 함수 호출
choose_seat()
