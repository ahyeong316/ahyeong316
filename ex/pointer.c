// pointer.c
#include <stdio.h>

void add_ten(int *p) {
    *p += 10;
}

int main() {
    int num = 5;
    printf("원래 값: %d\n", num);

    add_ten(&num);
    printf("포인터 함수 후 값: %d\n", num);

    return 0;
}
