'''
GRADING PROGRAM

Test with the following:

Sem Grade: 86   Final Exam: 52   Exam worth: 15%    Overall: 80.9
Sem Grade: 95   Final Exam: 32   Exam worth: 10%    Overall: 88.7
Sem Grade: 72   Final Exam: 100   Exam worth: 20%    Overall: 77.6
'''

'''
sem_grade: the overall semester grade
sem_value: how much the semester was worth
exam_grade: the overall exam grade
exam_value: how much the exam was worth
'''
sem_grade = float(input("Please input your semester grade excluding the final exam: ")) # Asks for the semester grade
exam_grade = float(input("Please input your overall exam grade: ")) # Asks for the exam grade
exam_value = float(input("Please input your overall exam worth: ")) # Asks how much the exam was worth

# Checks is the user's exam value is a decimal, or not.
if 1 <= exam_value <= 100: # Checks if 'exam_value' is > 1 and < 100
    exam_value = exam_value * 0.01 # If it is, change it to decimal form
# !!! If none of this applies, it just moves on !!!

sem_value = 1.00 - exam_value # Find how much the semester was worth based on the exam value
sem_average = sem_grade * sem_value + exam_grade * exam_value # Calculate the average

print("Your semester average is " + str(sem_average)) # Prints the average
