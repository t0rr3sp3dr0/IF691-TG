#include <stdio.h>

#define ABC (('9' - '0' + 1) + ('Z' - 'A' + 1) + ('z' - 'a' + 1))
#define LEN (ABC + 1 + 1)

int fwd[LEN];
int bwd[128];

void init_idx() {
    int i = 0;
    for (char c = '0'; c <= '9'; ++c) {
        fwd[i] = c;
        bwd[c] = i;
        ++i;
    }
    for (char c = 'A'; c <= 'Z'; ++c) {
        fwd[i] = c;
        bwd[c] = i;
        ++i;
    }
    for (char c = 'a'; c <= 'z'; ++c) {
        fwd[i] = c;
        bwd[c] = i;
        ++i;
    }
    fwd[i] = '\0';
    bwd['\0'] = i;
}

char pwd[16 + 1];
void next_pwd() {
    for (int i = 7; i >= 0; --i) {
        pwd[i] = fwd[bwd[pwd[i]] + 1];
        if (pwd[i] != '\0')
            break;
        pwd[i] = fwd[0];
    }
    for (int i = 7; i >= 0; --i) {
        char c = pwd[i + 8] = pwd[i];
        if (c >= 'A' && c <= 'Z')
            pwd[i + 8] += 'a' - 'A';
        if (c >= 'a' && c <= 'z')
            pwd[i + 8] += 'A' - 'a';
    }
}

int main() {
    init_idx();
    for (int i = 0; i < ABC * ABC * ABC * ABC; ++i) {
        for (int j = 0; j < ABC * ABC * ABC * ABC; ++j) {
            next_pwd();
            printf("%s\n", pwd);
        }
    }
    return 0;
}
