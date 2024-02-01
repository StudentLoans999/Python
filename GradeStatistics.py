In this exercise you will write a program for printing out grade statistics for a university course.

The program asks the user for results from different students on the course. These include exam points and numbers of exercises completed. The program then prints out statistics based on the results.

Exam points are integers between 0 and 20. The number of exercises completed is an integer between 0 and 100.

The program kees asking for input until the user types in an empty line. You may assume all lines contain valid input, which means that there are two integers on each line, or the line is empty.

And example of how the data is typed in:

Sample output
Exam points and exercises completed: 15 87
Exam points and exercises completed: 10 55
Exam points and exercises completed: 11 40
Exam points and exercises completed: 4 17
Exam points and exercises completed:
Statistics:

When the user types in an empty line, the program prints out statistics. They are formulated as follows:

The exercises completed are converted into exercise points, so that completing at least 10% of the exercises grants one point, 20% grants two points, and so forth. Completing all 100 exercises grants 10 exercise points. The number of exercise points granted is an integer value, rounded down.

The grade for the course is determined based on the following table:

exam points + exercise points	grade
0–14	0 (i.e. fail)
15–17	1
18–20	2
21–23	3
24–27	4
28–30	5
There is also an exam cutoff threshold. If a student received less than 10 points from the exam, they automatically fail the course, regardless of their total number of points.

With the example input from above the program would print out the following statistics:

Sample output
Statistics:
Points average: 14.5
Pass percentage: 75.0
Grade distribution:
  5:
  4:
  3: *
  2:
  1: **
  0: *
Floating point numbers should be printed out with one decimal precision.

NB: this exercise doesn't ask you to write any specific functions, so you should not place any code within an if __name__ == "__main__" block. If any functionality in your program is e.g. in the main function, you should include the code calling this function normally, and not contain it in an if block like in the exercises which specify certain functions.

Hint:

The user input in this program consists of lines with two integer values:

Sample output
Exam points and exercises completed: 15 87

grade_distribution = [] # create a list to store all the grade values
total_students = 0 # a counter to keep track of the number of students
total_points = 0 # a variable to accumulate the total points for all students

while True: # loop until break
    user_input = input("Exam points and exercises completed: ") # user input two numbers separated by a space (first number: 0-20 second number 0-100)

    if user_input == "": # check if the user input nothing (enter key) and break the While loop if so
        break

    points_and_exercises = user_input.split() # split users input of two numbers separated by a space into two separate numbers
    exam_points = points_and_exercises[0] # assign the first number to exam_points variable
    exercises = points_and_exercises[-1] # assign the second number to exercises variable
    
    exam_points = int(exam_points) # convert str variable to int
    exercises = int(exercises) # convert str variable to int

    completed_exercises = max(0, min(100, exercises)) # ensure that the completed exercises value is within the valid range (0-100)

    completion_percentage = completed_exercises / 100 # convert the completed exercises integer variable into a percentage variable
    exercise_points = int(completion_percentage * 10) # calculate exercise points (an integer value, rounded down) based on the completion percentage variable    

    total_student_points = exam_points + exercise_points # create a new variable that will be used to determine the grade, by summing up exam points and exercise points
    total_students += 1 # increment the student counter each iteration

    if exam_points < 10: # user input less than 10 for exam points, so gets automatic grade of 0 and adds that to the grade distribution list
        grade_distribution.append("0")

     # Determine grade based on user's input (the total student points) and adds the grade to the grade distribution list
    elif 0 <= total_student_points <= 14:
        grade_distribution.append("0")
    elif 15 <= total_student_points <= 17:
        grade_distribution.append("1")
    elif 18 <= total_student_points <= 20:
        grade_distribution.append("2")
    elif 21 <= total_student_points <= 23:
        grade_distribution.append("3")
    elif 24 <= total_student_points <= 27:
        grade_distribution.append("4")
    else:
        grade_distribution.append("5")

    total_points += total_student_points # accumulate total points for all students

points_average = total_points / total_students if total_students > 0 else 0 # calculate points average by dividing total points variable over the total students counter (number of inputs done), if at least one input was entered 

# Count of all the grades in the grade list
grade_5s = grade_distribution.count("5")
grade_4s = grade_distribution.count("4")
grade_3s = grade_distribution.count("3")
grade_2s = grade_distribution.count("2")
grade_1s = grade_distribution.count("1")
grade_0s = grade_distribution.count("0")

# Calculate pass percentage
pass_count = grade_1s + grade_2s + grade_3s + grade_4s + grade_5s # Count up all the grades in the grade list (doesn't include 'grade_0s' because that is not a passing grade)
pass_percentage = (pass_count / total_students) * 100 if total_students > 0 else 0 # divide all the grades earned by the total students counter (number of inputs done) and then multiply the result by 100 to make it into a percentage

print("Statistics:")
print(f"Points average: {points_average:.1f}") # rounded to 1 decimal place afterwards
print(f"Pass percentage: {pass_percentage:.1f}") # rounded to 1 decimal place afterwards
print(f"Grade distribution:")

grade_marker = "*" # used to mark what grades were earned and the amount of each

# Output how many of each grade was earned
print(f"    5: {grade_5s*grade_marker}") 
print(f"    4: {grade_4s*grade_marker}")
print(f"    3: {grade_3s*grade_marker}")
print(f"    2: {grade_2s*grade_marker}")
print(f"    1: {grade_1s*grade_marker}")
print(f"    0: {grade_0s*grade_marker}")
