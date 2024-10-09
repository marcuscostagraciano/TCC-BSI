def arithmetic_mean(ndarray):
    ndarray_length = 0
    ndarray_sum = 0

    for number in ndarray:
        ndarray_sum += number
        ndarray_length += 1

    return ndarray_sum / ndarray_length


def geometric_mean(ndarray):
    ndarray_multiplication = 1
    ndarray_length = 0

    for number in ndarray:
        ndarray_multiplication *= number
        ndarray_length += 1

    return ndarray_multiplication ** (1 / ndarray_length)


def variance(ndarray):
    ndarray_mean = arithmetic_mean(ndarray)
    ndarray_length = 0
    ndarray_sum = 0

    for number in ndarray:
        ndarray_sum += (number - ndarray_mean) ** 2
        ndarray_length += 1

    return ndarray_sum / (ndarray_length - 1)


def standard_deviation(ndarray):
    ndarray_variance = variance(ndarray)

    return ndarray_variance ** (1 / 2)


def variation_coefficient(ndarray):
    ndarray_std = standard_deviation(ndarray)
    ndarray_arithmetic_mean = arithmetic_mean(ndarray)

    return ndarray_std / ndarray_arithmetic_mean


def amplitude(ndarray):
    max_value = ndarray[0]
    min_value = ndarray[0]

    for number in ndarray:
        if max_value < number:
            max_value = number
        if number < min_value:
            min_value = number

    return max_value - min_value


print(f"{arithmetic_mean([1, 2, 3]) = }")
print(f"{geometric_mean([3, 12, 16, 36]) = }")
print(f"{variance([5, 8, 10, 7]) = }")
print(f"{standard_deviation([5, 8, 10, 7]) = }")
print(f"{variation_coefficient([5, 8, 10, 7]) = }")
print(f"{amplitude([5, 8, 10, 7]) = }")
