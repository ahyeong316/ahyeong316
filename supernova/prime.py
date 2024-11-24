def is_prime(number):
    if number <= 1:  # 1 이하의 숫자는 소수가 아님
        return False
    for i in range(2, int(number**0.5) + 1):  # 2부터 √number까지 나눠보기
        if number % i == 0:
            return False
    return True

# 숫자 입력받기
num = int(input("소수인지 확인할 숫자를 입력하세요: "))

if is_prime(num):
    print(f"{num}은(는) 소수입니다!")
else:
    print(f"{num}은(는) 소수가 아닙니다.")
