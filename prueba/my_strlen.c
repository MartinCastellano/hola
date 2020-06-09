/* Custom strlen implementation
 * May 16, 2019
 */
 
#include <stdlib.h>
#include <stdint.h>
 
/* https://jameshfisher.com/2017/01/24/bitwise-check-for-zero-byte */
#define zero(v) ((v - 0x0101010101010101) & ~v & 0x8080808080808080)
 
size_t my_strlen(const char * str) {
    uint64_t ans = zero(*(uint64_t *)str);
    size_t z = 0;
 
    /* ans = 0 means that the argument does not contain any zero byte */
    while (ans == 0) {
        /* Shift the string and find any zero in the next chunk */
        str += 8;
        z += 8;
        ans = zero(*(uint64_t *)str);
    }
 
    /* Find the first non-null byte, starting by the least significant one (little-endian) */
    while ((ans & 0xFF) == 0) {
        ans >>= 8;
        ++z;
    }
 
    return z;
}
 
/******************************************************************************/
 
#include <stdio.h>
#define strlen my_strlen
// #include <>
 
int main(int argc, char ** argv) {

    unsigned char Response[3]={0x00,0x01,0x10};
    // This initializes Response to a sequence of 269 identical values, each of which is zero. Note that 0x00, 0, and '\0' are all the same thing.

    if (argc > 1) {
        printf("%lu\n", strlen(Response));
        
    } else {
        fprintf(stderr, "Syntax: %s <string>\n", argv[0]);
    }
}