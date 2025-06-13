#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void) {
    int answer, guess, tries = 0;
    const int max_tries = 7;

    srand(time(NULL));
    answer = rand() % 100 + 1;  // 1~100

    printf("🎮 업다운 게임 시작! (1~100 사이 숫자 맞히기)\n");

    while (tries < max_tries) {
        printf("숫자를 입력하세요 (%d/%d): ", tries + 1, max_tries);
        scanf("%d", &guess);
        tries++;

        if (guess < answer)
            printf("👉 UP!\n");
        else if (guess > answer)
            printf("👈 DOWN!\n");
        else {
            printf("🎉 정답입니다! %d번 만에 맞혔어요!\n", tries);
            break;
        }
    }

    if (tries == max_tries && guess != answer)
        printf("😢 실패! 정답은 %d였습니다.\n", answer);

    return 0;
}
