#include <stdio.h>
#include <ctype.h>
#include <stdint.h>



void hexdump(void *data, int size) {
    unsigned char *ptr = (unsigned char *)data;
    int64_t i, j;

    int64_t base = (int64_t) data;

    int bytes_per_line = 16;
    // printf("%08zx\n", base);
    for (i = 0; i < size; i += bytes_per_line) {
        // Exibe o offset
        printf("%08zx  ", i+base);

        // Exibe a parte hexadecimal
        for (j = 0; j < bytes_per_line; j++) {
            if (i + j < size) {
                printf("%02x ", ptr[i + j]);
            } else {
                // Preenche com espaços se a última linha for menor
                printf("   ");
            }

            if ( j == 7 ) {
                printf(" ");
            }
        }
        printf(" |");

        // Exibe a parte ASCII
        for (j = 0; j < bytes_per_line; j++) {
            if (i + j < size) {
                char ch = (char)ptr[i + j];
                printf("%c", isprint(ch) ? ch : '.');
            }
        }
        printf("|\n");
    }
}

/*
int main() {
    // Exemplo com uma string de texto
    const char *text_data = "Hello, world! This is a test string.\nWith some special chars: ~!@#$%^&*()_+";
    hexdump((void *)text_data, strlen(text_data), 16);

    printf("\n");

    // Exemplo com dados binários
    unsigned char binary_data[] = {
        0x48, 0x65, 0x6c, 0x6c, 0x6f, 0x2c, 0x20, 0x77,
        0x6f, 0x72, 0x6c, 0x64, 0x21, 0x0a, 0x01, 0x02,
        0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0a,
        0x0b, 0x0c, 0x0d, 0x0e, 0x0f, 0x10, 0x11, 0x12
    };
    hexdump((void *)binary_data, sizeof(binary_data), 16);

    return 0;
}
*/
