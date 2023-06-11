list_student = input('Введіть призвищя учнів ').title()

list_student_split = list_student.split()
list_student_split = [name for name in list_student_split if
                      name.isalpha()]  # виключеня числових значеннь чесно взяв у гпт:)
list_student_split.sort()

for list_final in list_student_split:
    print(list_final)
