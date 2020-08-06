# grading_project_3



# Your program should ask the user for a class file name (like "class1.txt") and an exam data file name (like "test1.txt").  
# Then, your program should grade all the students' responses and print out the results (plus a few statistics) in a nicely-formatted output table.


# *** Task 1: Extract the Class List ***
# Define a function get_students()
# your function should return a dictionary that contains student names and IDs from the specified file


# *** Task 2: Extract the Exam Data ***
# Create a function get_exam_data()
# Your function should return a list containing all non-commented and non-empty lines from the given file. The list should contain the 
# string for each line, with any whitespace or newline characters removed from both ends of the string


# *** Task 3: Extract the Student Responses ***
# Define a function get_student_responses()
# This function should take a list of lines as a parameter (such as those returned by get_exam_data()). It should return a dictionary 
# that has student IDs as keys and student answers as values


# *** Task 4: Grade the Exams Automatically ***
# Implement the top level instructions in your program, they should be put into a main() function
# You can assume that only valid file names will be used.  Additionally, class and test files are generally paired.  For example, class1.txt 
# goes with test1.txt. Students from Class 1 will show up in the Test 1 file.
