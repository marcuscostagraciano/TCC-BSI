#include <stddef.h>  // for size_t

unsigned long get_max_value(const unsigned long *array, size_t size) {
    if (size == 0)
        return 0;

    unsigned long max_value = array[0];

    for (size_t i = 1; i < size; i++) {
        if (array[i] > max_value) {
            max_value = array[i];
        }
    }

    return max_value;
}
