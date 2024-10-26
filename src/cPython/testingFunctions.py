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


def max_value(ndarray):
    max_value = ndarray[0]

    for number in ndarray:
        if max_value < number:
            max_value = number

    return max_value


def min_value(ndarray):
    min_value = ndarray[0]

    for number in ndarray:
        if number < min_value:
            min_value = number

    return min_value


def amplitude(ndarray):
    max_v = max_value(ndarray)
    min_v = min_value(ndarray)
    return max_v - min_v


def arithmetic_mean_w_python_functions(ndarray):
    return sum(ndarray) / len(ndarray)


def variance_w_python_functions(ndarray):
    ndarray_mean = arithmetic_mean_w_python_functions(ndarray)
    ndarray_sum = sum([(number - ndarray_mean) ** 2 for number in ndarray])
    ndarray_length = len(ndarray)

    return ndarray_sum / (ndarray_length - 1)


def standard_deviation_w_python_functions(ndarray):
    ndarray_variance = variance_w_python_functions(ndarray)

    return ndarray_variance ** (1 / 2)


def max_value_w_python_functions(ndarray):
    return max(ndarray)


def min_value_w_python_functions(ndarray):
    return min(ndarray)


def amplitude_w_python_functions(ndarray):
    return max(ndarray) - min(ndarray)
