import time

def countdown_timer(seconds):
    print("타이머를 시작합니다!")
    while seconds > 0:
        minutes, sec = divmod(seconds, 60)
        timer = f"{minutes:02}:{sec:02}"
        print(timer, end="\r")  # 현재 시간 표시
        time.sleep(1)
        seconds -= 1
    print("타이머 종료! 🔔")

time_input = int(input("초 단위로 시간을 입력하세요: "))
countdown_timer(time_input)
