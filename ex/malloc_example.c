// malloc_example.c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int n;
    printf("입력 개수: ");
    scanf("%d", &n);

    int *arr = (int *)malloc(sizeof(int) * n);

    if (arr == NULL) {
        printf("메모리 할당 실패\n");
        return 1;
    }

    printf("%d개의 정수를 입력하세요:\n", n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    int sum = 0;
    for (int i = 0; i < n; i++)
        sum += arr[i];

    printf("평균: %.2f\n", (float)sum / n);

    free(arr);
    return 0;
}
