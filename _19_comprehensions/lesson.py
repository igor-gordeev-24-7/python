even_squares = []
# for i in range(10):
#     if i % 2 == 0:
#         even_squares.append(i ** 2)
# print(even_squares)

even_squares = [x ** 2 for x in range(10) if x % 2 == 0]
print(even_squares)