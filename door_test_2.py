def check_entry():
    # Step 1: 이름과 학번 입력
    name = input("이름을 입력하세요: ")
    student_id = input("학번을 입력하세요: ")
    
    # Step 2: 학번이 'AI'로 시작하는지 확인 (예: AI2024001)
    if student_id.startswith("AI"):  # 학번이 'AI'로 시작하면 인공지능학과로 간주
        print(f"{name}님, 인공지능학과 확인 완료! 문이 열립니다.")
        
        # Step 3: 출입 여부 질문
        entry = input("출입하시겠습니까? (YES/NO): ").strip().upper()
        
        # Step 4: 출입 여부 확인 및 메시지 출력
        if entry == "YES":
            print("출석이 인정되었습니다. 오늘도 좋은 하루 보내세요!")
        elif entry == "NO":
            print("출석이 인정되지 않았습니다. 다음에 다시 방문해주세요.")
        else:
            print("잘못된 입력입니다. YES 또는 NO로 입력해주세요.")
    else:
        print(f"{name}님, 학번 확인 실패! 문이 닫힙니다.")
        print("인공지능학과가 아닌 경우 출입할 수 없습니다.")

# 함수 실행
check_entry()
