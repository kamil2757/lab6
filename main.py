# import random
#
# n = int(input("Введите N: "))
# numbers = [random.randint(1, 100) for _ in range(n)]
#
# print(f"Исходный список: {numbers}")
# print(f"Сумма: {sum(numbers)}")
# print(f"Среднее: {sum(numbers) / len(numbers):.2f}")
# print(f"Минимум: {min(numbers)}")
# print(f"Максимум: {max(numbers)}")
#
# numbers.sort()
# print(f"Отсортированный: {numbers}")
#
# unique = list(dict.fromkeys(numbers))
# print(f"Без дубликатов: {unique}\n")

# Задание 2
# from collections import Counter
# numbers2 = [1, 2, 3, 2, 4, 5, 1, 6, 3, 7]
#
# counts = Counter(numbers2)
# duplicates = [num for num, count in counts.items() if count > 1]
# print(f"Дубликаты: {duplicates}")
#
# seen = set()
# duplicates2 = set()
# for num in numbers2:
#     if num in seen:
#         duplicates2.add(num)
#     seen.add(num)
#
# print(f"Дубликаты: {list(duplicates2)}\n")

# Задание 3
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# transposed = [list(row) for row in zip(*matrix)]
#
# print("Исходная матрица:")
# for row in matrix:
#     print(row)
#
# print("\nТранспонированная матрица:")
# for row in transposed:
#     print(row)
# print()

# students = [
#     ("Иван", 25, 4.5),
#     ("Мария", 22, 4.8),
#     ("Пётр", 30, 4.2),
#     ("Анна", 20, 4.9)
# ]
#
# oldest = max(students, key=lambda s: s[1])
# print(f"Самый старший: {oldest[0]}, {oldest[1]} лет")
#
# best = max(students, key=lambda s: s[2])
# print(f"Лучший студент: {best[0]}, балл {best[2]}")
#
# avg_age = sum(s[1] for s in students) / len(students)
# print(f"Средний возраст: {avg_age:.1f}")
#
# sorted_students = sorted(students, key=lambda s: s[2], reverse=True)
# print("\nПо баллу:")
# for name, age, gpa in sorted_students:
#     print(f"{name}: {gpa}")
# print()


#
# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]
#
# set1 = set(list1)
# set2 = set(list2)
#
# union = set1 | set2
# intersection = set1 & set2
# difference = set1 - set2
#
# print(f"Объединение: {sorted(union)}")
# print(f"Пересечение: {sorted(intersection)}")
# print(f"Разность: {sorted(difference)}")
#
# union_ordered = list1 + [x for x in list2 if x not in list1]
# intersection_ordered = [x for x in list1 if x in list2]

# user_lst = list(map(int,input('Введите числа через пробел: ').split(' ')))
# lst = user_lst[::]
#
# for _ in range(len(lst)):
#     for i in range(len(lst) - 1):
#         if lst[i] > lst[i+1]:
#             lst[i + 1], lst[i] = lst[i], lst[i + 1]
# print(lst)
#
# if lst == user_lst:
#     print('Список отсортирован')
# else:
#     print('Списоск НЕ отсортирован')


# lst = [1,4,77,1,3,5,63]
#
# def merge(left, right):
#     result = []
#     i = 0
#     j = 0
#
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#
#     result.extend(left[i:])
#     result.extend(right[j:])
#
#     return result
#
# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
#
#     mid = len(arr) // 2
#     left_half = merge_sort(arr[:mid])
#     right_half = merge_sort(arr[mid:])
#
#     return merge(left_half, right_half)
#
# print(merge_sort(lst))


# def quick_sort(arr, low, high):
#     if low < high:
#         pivot_index = partition(arr, low, high)
#
#         quick_sort(arr, low, pivot_index - 1)
#         quick_sort(arr, pivot_index + 1, high)
#
#
# def partition(arr, low, high):
#     pivot = arr[high]
#     i = low - 1
#
#     for j in range(low, high):
#         if arr[j] <= pivot:
#             i += 1
#             arr[i], arr[j] = arr[j], arr[i]
#
#     arr[i + 1], arr[high] = arr[high], arr[i + 1]
#     return i + 1
#
#
# lst = [3, 1, 4, 1, 5, 9, 2, 6]
# quick_sort(lst, 0, len(lst) - 1)
# print(f"Отсортированный: {lst}")

# lst = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# n = 20
#
#
# def getMidl(lst, target):
#     if not lst:
#         return -1
#
#     midl = len(lst) // 2
#
#     if lst[midl] == target:
#         return target
#     elif target < lst[midl]:
#         return getMidl(lst[:midl], target)
#     else:
#         return getMidl(lst[midl + 1:], target)



# def showMatrix(matrix, r=2):
#     verifyMatrix(matrix)
#
#     if not isinstance(matrix[0], (list, tuple)):
#         for item in matrix:
#             print(round(item, r), end=" ")
#         print()
#     else:
#         for i in range(len(matrix)):
#             for j in range(len(matrix[i])):
#                 print(round(matrix[i][j], r), end=" ")
#             print()
#
# def verifyMatrix(matrix):
#     if len(matrix) == 0:
#         raise ValueError('матрица пустая')
#
#     ln = len(matrix[0])
#     for a in matrix:
#         if len(a) != ln:
#             raise ValueError('матрица имеет строки разной длины')
#
#
# def transposition(m1):
#     verifyMatrix(m1)
#
#     res = []
#     for i in range(len(m1[0])):
#         a = []
#         for arr in m1:
#             a.append(arr[i])
#
#         res.append(a)
#     return res
#
#
# def summation(m1, m2):
#     verifyMatrix(m1)
#     verifyMatrix(m2)
#
#     if len(m1) != len(m2):
#         raise ValueError('Матрицы нельзя суммировать: разные длины')
#
#     if not isinstance(m1[0], (list, tuple)):
#         return [m1[i] + m2[i] for i in range(len(m1))]
#
#     if len(m1[0]) != len(m2[0]):
#         raise ValueError('Матрицы нельзя суммировать: разная длина строк')
#
#     res = []
#     for i in range(len(m1)):
#         arr = []
#         for j in range(len(m1[0])):
#             arr.append(m1[i][j] + m2[i][j])
#         res.append(arr)
#     return res
#
#
# def subtraction(m1, m2):
#     verifyMatrix(m1)
#     verifyMatrix(m2)
#
#     if len(m1) != len(m2):
#         raise ValueError('Матрицы нельзя вычитать: разные длины')
#
#     if not isinstance(m1[0], (list, tuple)):
#         return [m1[i] - m2[i] for i in range(len(m1))]
#
#     if len(m1[0]) != len(m2[0]):
#         raise ValueError('Матрицы нельзя вычитать: разная длина строк')
#
#     res = []
#     for i in range(len(m1)):
#         arr = []
#         for j in range(len(m1[0])):
#             arr.append(m1[i][j] - m2[i][j])
#         res.append(arr)
#     return res
#
#
# def multiplicationMatrix(m1, m2):
#     verifyMatrix(m1)
#     verifyMatrix(m2)
#
#     if len(m1[0]) != len(m2):
#         raise ValueError('Матрицы нельзя перемножать: внутренние размеры не совпадают')
#
#     res = []
#     m2_t = transposition(m2)
#
#     #перебор столбцов m1
#     for ln in m1:
#         arr = []
#         #перебор колонок m2
#         for cn in m2_t:
#             sm = 0
#             #суммируем элементы столбцов и колонок для получения нужного элемента
#             for i in range(len(ln)):
#                 sm += ln[i] * cn[i]
#             #добавляем элемент в строку
#             arr.append(sm)
#         #добавляем строку в массив
#         res.append(arr)
#     return res
#
#
#
# showMatrix(multiplicationMatrix([[1, 2, 3], [4, 8, 6]], [[1, 2], [2, 3], [4, 5]]))
# showMatrix(summation([1, 2],[3, 4]))
