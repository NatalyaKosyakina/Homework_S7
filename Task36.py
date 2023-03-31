# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.

def print_operation_table(operation, num_rows=6, num_columns=6):
    table = []
    for i in range(1, num_rows + 1):
        table.append([operation(i, j) for j in range(1, num_columns + 1)])
        print(*table[i-1], sep=" ")


operation_1 = lambda a, b: a * b
print_operation_table(operation_1)