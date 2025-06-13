#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void)
{
    int set_num;
    int lotto[100][6];  // 최대 100세트
    srand(time(NULL));

    printf("Enter lotto set number: ");
    scanf("%d", &set_num);

    for (int i = 0; i < set_num; i++) {
        int count = 0;
        while (count < 6) {
            int num = rand() % 45 + 1;
            int duplicate = 0;

            for (int j = 0; j < count; j++) {
                if (lotto[i][j] == num) {
                    duplicate = 1;
                    break;
                }
            }

            if (!duplicate) {
                lotto[i][count] = num;
                count++;
            }
        }
    }

    for (int i = 0; i < set_num; i++) {
        printf("set %d : ", i + 1);
        for (int j = 0; j < 6; j++)
            printf("%d ", lotto[i][j]);
        printf("\n");
    }

    return 0;
}
