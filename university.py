# write your code here

import collections
import operator


def take_input():
    file = open('applicants.txt', 'r')
    data = file.readlines()
    student_score = {}
    first_choice = {'Biotech':[], 'Chemistry':[], 'Engineering':[], 'Mathematics':[],
                      'Physics':[]}
    second_choice = {'Biotech':[], 'Chemistry':[], 'Engineering':[], 'Mathematics':[],
                      'Physics':[]}
    third_choice = {'Biotech':[], 'Chemistry':[], 'Engineering':[], 'Mathematics':[],
                      'Physics':[]}
    for line in data:
        name = line.split()[0]+' '+line.split()[1]
        gpa_one = float(line.split()[2]) # physics
        gpa_two = float(line.split()[3]) # chemistry
        gpa_three = float(line.split()[4]) # math
        gpa_four = float(line.split()[5]) # computer science / engineering
        special_exam = float(line.split()[6])
        first = line.split()[7]
        second = line.split()[8]
        third = line.split()[9]
        ## mean
        physics_math = (float(gpa_one) + float(gpa_three)) / 2   # for physics department
        computer_math = (float(gpa_three) + float(gpa_four)) / 2  # for engineeering department
        chemistry_physics = (float(gpa_one) + float(gpa_two)) / 2 # for biotech department
        ##mean

        if first == 'Biotech':
            if special_exam < chemistry_physics:
                first_choice[first].append([name, chemistry_physics])
            elif special_exam >= chemistry_physics:
                first_choice[first].append([name, special_exam])
        elif first == 'Chemistry':
            if special_exam < gpa_two:
                first_choice[first].append([name, gpa_two])
            elif special_exam >= gpa_two:
                first_choice[first].append([name, special_exam])
        elif first == 'Physics':
            if special_exam < physics_math:
                first_choice[first].append([name, physics_math])
            elif special_exam >= physics_math:
                first_choice[first].append([name, special_exam])
        elif first == 'Engineering':
            if special_exam < computer_math:
                first_choice[first].append([name, computer_math])
            elif special_exam >= computer_math:
                first_choice[first].append([name, special_exam])
        elif first == 'Mathematics':
            if special_exam < gpa_three:
                first_choice[first].append([name, gpa_three])
            elif special_exam >= gpa_three:
                first_choice[first].append([name, special_exam])

        if second == 'Biotech':
            if special_exam < chemistry_physics:
                second_choice[second].append([name, chemistry_physics])
            elif special_exam >= chemistry_physics:
                second_choice[second].append([name, special_exam])
        elif second == 'Chemistry':
            if special_exam < gpa_two:
                second_choice[second].append([name, gpa_two])
            elif special_exam >= gpa_two:
                second_choice[second].append([name, special_exam])
        elif second == 'Physics':
            if special_exam < physics_math:
                second_choice[second].append([name, physics_math])
            elif special_exam >= physics_math:
                second_choice[second].append([name, special_exam])
        elif second == 'Engineering':
            if special_exam < computer_math:
                second_choice[second].append([name, computer_math])
            elif special_exam >= computer_math:
                second_choice[second].append([name, special_exam])
        elif second == 'Mathematics':
            if special_exam < gpa_three:
                second_choice[second].append([name, gpa_three])
            elif special_exam >= gpa_three:
                second_choice[second].append([name, special_exam])

        if third == 'Biotech':
            if special_exam < chemistry_physics:
                third_choice[third].append([name, chemistry_physics])
            elif special_exam >= chemistry_physics:
                third_choice[third].append([name, special_exam])
        elif third == 'Chemistry':
            if special_exam < gpa_two:
                third_choice[third].append([name, gpa_two])
            elif special_exam >= gpa_two:
                third_choice[third].append([name, special_exam])
        elif third == 'Physics':
            if special_exam < physics_math:
                third_choice[third].append([name, physics_math])
            elif special_exam >= physics_math:
                third_choice[third].append([name, special_exam])
        elif third == 'Engineering':
            if special_exam < computer_math:
                third_choice[third].append([name, computer_math])
            elif special_exam >= computer_math:
                third_choice[third].append([name, special_exam])
        elif third == 'Mathematics':
            if special_exam < gpa_three:
                third_choice[third].append([name, gpa_three])
            elif special_exam >= gpa_three:
                third_choice[third].append([name, special_exam])
    file.close()

    return first_choice, second_choice, third_choice


def get_applicants(first_choice, second_choice, third_choice):
    n = int(input())
    successfull_applicants = []
    for a, v in first_choice.items():
        v.sort(key=lambda x: (-float(x[1]), x[0]))
    for a, v in second_choice.items():
        v.sort(key=lambda x: (-float(x[1]), x[0]))
    for a, v in third_choice.items():
        v.sort(key=lambda x: (-float(x[1]), x[0]))

    all_applicants = {'Biotech':[], 'Chemistry':[], 'Engineering':[], 'Mathematics':[],
                      'Physics':[]}
    for department, students in first_choice.items():
        for student in students:
            if len(all_applicants[department]) < n:
                all_applicants[department].append(student)
                successfull_applicants.append(student[0])


    second_choice_update = {'Biotech':[], 'Chemistry':[], 'Engineering':[], 'Mathematics':[],
                      'Physics':[]}
    for department, students in second_choice.items():
        for student in students:
            if student[0] not in successfull_applicants:
                second_choice_update[department].append(student)

    for department, students in second_choice_update.items():
        for student in students:
            if len(all_applicants[department]) < n:
                all_applicants[department].append(student)
                successfull_applicants.append(student[0])

    third_choice_updated = {'Biotech':[], 'Chemistry':[], 'Engineering':[], 'Mathematics':[],
                      'Physics':[]}
    for department, students in third_choice.items():
        for student in students:
            if student[0] not in successfull_applicants:
                third_choice_updated[department].append(student)

    for department, students in third_choice_updated.items():
        for student in students:
            if len(all_applicants[department]) < n:
                all_applicants[department].append(student)
                successfull_applicants.append(student[0])

    for a, v in all_applicants.items():
        v.sort(key=lambda x: (-float(x[1]), x[0]))
    return all_applicants


def output_successful_applicants(applicants):
    for department, students in applicants.items():
        print(department)
        for student in students:
            print((student[0] + ' ' +str(float(student[1]))))
        print('\n')
    biotech = open('biotech.txt', 'w')
    chemistry = open('chemistry.txt', 'w')
    engineering = open('engineering.txt', 'w')
    mathematics = open('mathematics.txt', 'w')
    physics = open('physics.txt', 'w')
    for students in applicants['Biotech']:
        biotech.write(students[0] +' '+str(float(students[1])))
        biotech.write('\n')
    biotech.close()
    for students in applicants['Chemistry']:
        chemistry.write(students[0] +' '+str(float(students[1])))
        chemistry.write('\n')
    chemistry.close()
    for students in applicants['Engineering']:
        engineering.write(students[0] +' '+str(float(students[1])))
        engineering.write('\n')
    engineering.close()
    for students in applicants['Mathematics']:
        mathematics.write(students[0] +' '+str(float(students[1])))
        mathematics.write('\n')
    mathematics.close()
    for students in applicants['Physics']:
        physics.write(students[0] +' '+str(float(students[1])))
        physics.write('\n')
    physics.close()



first_choice, second_choice, third_choice = take_input()
successful_applicants = get_applicants(first_choice, second_choice, third_choice)
output_successful_applicants(successful_applicants)
#print(get_applicants(first_choice, second_choice, third_choice))



