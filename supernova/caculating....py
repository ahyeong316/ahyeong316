def calculator():
    print("간단한 계산기입니다.")
    print("사용법: 숫자와 연산자를 입력하세요. (예: 5 + 3)")
    expression = input("계산식 입력: ")
    try:
        result = eval(expression)
        print(f"결과: {result}")
    except:
        print("잘못된 입력입니다.")

calculator()
