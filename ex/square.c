#include <stdio.h>

int main(void) {
    int x;
    printf("정수를 입력하세요: ");
    if (scanf("%d", &x) != 1) {
        printf("입력 오류\n");
        return 1;
    }
    printf("%d의 제곱은 %d입니다.\n", x, x * x);
    return 0;
}
