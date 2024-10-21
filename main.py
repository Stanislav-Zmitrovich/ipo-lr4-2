def integer_parts(numbers):
    return [int(x) for x in numbers]

# Пример использования
float_numbers = [1.1, 2.5, 3.7, 4.2, 5.9]
integer_numbers = integer_parts(float_numbers)
print(integer_numbers)

