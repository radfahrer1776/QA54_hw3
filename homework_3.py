def print_list_reverse(lst):
    if lst is None or not isinstance(lst, list) or len(lst) == 0:
        print("Wrong list")
        return

    print(lst[::-1])


def is_valid_point(point):
    if point is None or point == ():
        return None

    if not isinstance(point, tuple):
        return False

    if len(point) != 2:
        return False

    if not isinstance(point[0], (int, float)):
        return False

    if not isinstance(point[1], (int, float)):
        return False

    return True


def print_sublist_reverse(lst, start, finish):
    if (lst is None or
            not isinstance(lst, list) or
            len(lst) == 0 or
            not isinstance(start, int) or
            not isinstance(finish, int) or
            start < 0 or
            finish >= len(lst) or
            start > finish):
        print("Wrong args")
        return

    result = lst[:]
    result[start:finish + 1] = result[start:finish + 1][::-1]

    print(result)


def get_students_by_grade(students):
    if students is None or not isinstance(students, dict) or len(students) == 0:
        return {}

    result = {}

    for name, grade in students.items():
        if grade not in result:
            result[grade] = []

        result[grade].append(name)

    return result

print("--- Task 1: Print list reverse ---\n")

print_list_reverse([1,2,3,4,5])
print_list_reverse([])
print_list_reverse(None)
print_list_reverse("12345")


print("\n--- Task 2: Check valid point ---\n")

print(is_valid_point((3, 5)))
print(is_valid_point((3, "5")))
print(is_valid_point([3, 5]))
print(is_valid_point((1, 2, 3)))
print(is_valid_point(()))
print(is_valid_point(None))


print("\n--- Task 3: Print sublist reverse ---\n")

print_sublist_reverse([10, 20, 30, 40, 50, 60], 1, 3)
print_sublist_reverse([1, 2, 3, 4, 5], 0, 2)
print_sublist_reverse([1, 2, 3], 0, 2)

print_sublist_reverse([], 0, 2)
print_sublist_reverse(None, 0, 2)
print_sublist_reverse([1, 2, 3], "0", 2)
print_sublist_reverse([1, 2, 3], 0, 5)
print_sublist_reverse([1, 2, 3], 2, 1)


print("\n--- Task 4: Students by grade ---\n")

print(get_students_by_grade({
    "Alice": 90,
    "Bob": 85,
    "Diana": 90,
    "Charlie": 85
}))

print(get_students_by_grade({
    "John": 100,
    "Mike": 100,
    "Anna": 95
}))

print(get_students_by_grade({}))
print(get_students_by_grade(None))
print(get_students_by_grade([]))