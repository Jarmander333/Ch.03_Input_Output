'''
Grading PROGRAM
---------------
Create a program that asks the user for their semester grade, final exam grade, 
and final exam worth and then calculates the overall final grade. 
Ask your instructor if you don't know how to calculate weighted averages.
You don't have to print out the letter grade. We will do that in the next chapter.

Test with the following:

Sem Grade: 86   Final Exam: 52   Exam worth: 15%    Overall: 80.9
Sem Grade: 95   Final Exam: 32   Exam worth: 10%    Overall: 88.7
Sem Grade: 72   Final Exam: 100   Exam worth: 20%    Overall: 77.6
'''

sem_grade = float(input("Please input your semester grade excluding the final exam: "))
exam_grade = float(input("Please input your overall exam grade: "))
exam_valu_deci = float(input("Please input your overall exam worth (0 - 100): "))
exam_valu = exam_valu_deci * 0.01
sem_valu = 1.00 - exam_valu
sem_average = sem_grade * sem_valu + exam_grade * exam_valu

print("Your semester average is " + str(sem_average))

'''
if sem_average >= 98:
    print("You got an A+!")
elif 97 >= sem_average >= 94:
    print("You got an A!")
elif 90 >= sem_average >= 93:
    print("You got an A-!")
elif 87 >= sem_average >= 89:
    print("You got a B+!")
elif 83 >= sem_average >= 86:
    print("You got a B!")
elif 80 >= sem_average >= 82:
    print("You got a B-!")
else:
    print("You got a F!")
'''
