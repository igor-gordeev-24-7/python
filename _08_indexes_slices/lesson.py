numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_number = numbers[::-1]
numbers.reverse()
reversed(numbers)
print(type(list(reversed(numbers))))