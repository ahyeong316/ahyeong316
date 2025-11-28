// struct.c
#include <stdio.h>

typedef struct {
    int id;
    char name[20];
    float grade;
} Student;

void print_student(Student s) {
    printf("학번: %d\n", s.id);
    printf("이름: %s\n", s.name);
    printf("평점: %.2f\n", s.grade);
}

int main() {
    Student s1 = {20250001, "Kim", 3.92};
    print_student(s1);
    return 0;
}
