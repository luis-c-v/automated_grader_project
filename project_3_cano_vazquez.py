"""   
Name: Luis Cano Vazquez
Course: CSCI 1101B
Assignment: Project 3, Grading Tests!
Date: April 12, 2020

Program excutes a grading policy that requests two files and returns a detailed class overview
"""


NUMS = "0123456789"


def get_students(filename):
    """Takes class roster and returns a dictionary of the class using student Ids"""
    class_copy = open(filename)
    list_of_students = class_copy.readlines()
    class_dict = {}
    for student in list_of_students:
        stud_details = student.strip().split(',')
        # clears whitespace of file and splits each string into small list of student information
        # id number, first name, last name
        stud_id = stud_details[0]
        if stud_id[0] in NUMS:
            # ensures that it pulls only digits (student_ID)
            # ****could have used str.isdigit() method but ran into handling error later on****
            class_dict[stud_id] = (stud_details[1], stud_details[2])
            # assigns the student id as the key and the first and last name as values
    return class_dict


def get_exam_data(filename):
    """Returns a list containing all non-commented and non-empty lines from the given file"""
    test_copy = open(filename)
    list_of_lines = test_copy.readlines()
    clean_list = []
    for line in list_of_lines:
        if line[0] != '#':
            # omits commented lines
            clean_line = line.strip()
            if clean_line != '':
                # ensures that we don't add any empty strs after we strip each line
                clean_list.append(clean_line)
    return clean_list


def get_student_responses(list_from_exam_data):
    """Returns a dictionary that has student IDs as keys and student answers as values"""
    response_dict = {}
    for line in list_from_exam_data:
        if line[0] in NUMS:
            stud_info = line.split(',')
            # divides line into IDs and responses, then uses indexes to assign to response_dict
            response_dict[stud_info[0]] = stud_info[1]
        elif "model" in line:
            # finds line with the real answers
            bb_list = line.split()
            for line in bb_list:
                if line[0] in NUMS:
                    response_dict['answers'] = line
    return response_dict


def grade_exams(responses, student_info):
    """Grades each exam and returns a dictionary with added mark to each student's value"""
    true_answers = responses.get('answers')
    del responses['answers']
    # pulls the correct answers and deletes key to avoid interference with future mapping
    class_scores = []
    for key in responses.keys():
        # grades students exams question by question
        student_score = 0
        i = 0
        for answer in responses.get(key):
            if answer == true_answers[i]:
                student_score += 1
            i += 1
        student_info[key] = list(student_info[key]) + [student_score]  
        # creates a dictionary key out of the student's [first and last names] and 
        # adds their mark to the assigned key
        class_scores.append(student_score)
        # adds each student's score to list to generate minor class stats
    student_info['max'] = "{0:.2f}".format(max(class_scores))
    student_info['min'] = "{0:.2f}".format(min(class_scores))
    student_info['question_count'] = len(true_answers)
    student_info['average'] = "{0:.2f}".format(sum(class_scores)/len(responses.keys()))
    return student_info


def outline_class(dictionary, class_file, test_file):
    """Returns a beautiful outline of the class details after grading"""
    print('Class file name = ' + class_file)
    print('Test file name = ' + test_file)
    print('Number of questions = ' + str(dictionary['question_count']))
    print("-" * 40)
    print('{:<8}{:<14}{:<14}{:>4}'.format('Stud_Id', 'Given_name', 'Family_name', 'Mark'))
    print("-" * 40)
    for key in sorted(dictionary.keys()):
        # organizes the display of students through their key (IDs) 
        if key[0] in NUMS:
            # ensures we are displaying student info and not class stats just yet
            vals = dictionary.get(key)
            print('{:<8}{:<14}{:<14}{:>4}'.format(key, vals[0], vals[1], vals[2]))
    print("=" * 40)
    print('Average mark = ' + str(dictionary['average']))
    print('Minimum mark = ' + str(dictionary['min']))
    print('Maximum mark = ' + str(dictionary['max']))


def main():
    """Function requests two files and returns a detailed outline of the class with scored test"""
    class_info = input('Enter class list file name: ')
    test_info = input('Enter test data file name: ')
    student_dict = get_students(class_info)
    # creates student dictionary
    useful_test_data = get_exam_data(test_info)
    # creates a list of useful test data
    response_dict = get_student_responses(useful_test_data)
    # creates dictionary with student responses keyed by id
    graded_dictionary = grade_exams(response_dict, student_dict)
    # grades each exam and includes mark into student dictionary
    return outline_class(graded_dictionary, class_info, test_info)
    # last line organizes all our data


main()