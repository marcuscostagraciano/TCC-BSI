#include <stddef.h>  // for size_t

unsigned long get_min_value_using_C(const unsigned long *array, const size_t size) {
    if (size == 0)
        return 0;

    unsigned long min_value = array[0];

    for (size_t i = 1; i < size; i++)
        if (array[i] < min_value)
            min_value = array[i];

    return min_value;
}
