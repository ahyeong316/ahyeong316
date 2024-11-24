import random

number_to_guess = random.randint(1, 100)
print("1부터 100까지 숫자를 맞혀보세요!")

while True:
    guess = int(input("숫자를 입력하세요: "))
    if guess < number_to_guess:
        print("더 큰 숫자입니다!")
    elif guess > number_to_guess:
        print("더 작은 숫자입니다!")
    else:
        print("정답입니다!")
        break
