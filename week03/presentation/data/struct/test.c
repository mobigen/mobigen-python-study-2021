#include <stdio.h>
typedef struct { 
    double v; // 8byte
    int t;  // 4byte
    char c; // 1byte
} save_type;

int main() {
    // 8 + 4 + 1 = 13 이지만 c에서 __attribute__((packed))등을 사용하지 않으면 구조체는 4byte씩 공간을 확보하므로 13 -> 16byte로 저장된다.
    save_type s = {7.5f, 9, 'A'};

    FILE *f = fopen("output", "w");
    fwrite(&s, sizeof(save_type), 1, f);
    fclose(f);
    return 0;
}