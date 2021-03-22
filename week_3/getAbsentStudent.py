# finds absent student using hash table

# O(n) time and space


all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
present_students = ["정연", "모모", "채영", "쯔위", "사나", "나연", "미나", "다현"]


def get_absent_student(all_array, present_array):
    s = {}
    for i in all_array:
        s[i] = False

    for i in present_array:
        del s[i]

    for i in s:
        return i


print(get_absent_student(all_students, present_students))