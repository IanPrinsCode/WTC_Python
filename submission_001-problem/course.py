from typing import Counter


class Course_Topics:
    def get_data_set():
        course_topics = [
        "Functions",
        "How to make decisions",
        "How to repeat code",
        "How to structure data",
        "Introduction to Python",
        "Modules",
        "Tools of the Trade"
        ]
        return course_topics
    def get_data_list():
        students = [
        ("Matthew", "How to structure data", "Problem 2", "[GRADED]"),
        ("Daniel", "How to repeat code", "Problem 3", "[STARTED]"),
        ("Ian", "How to structure data", "Problem 3", "[COMPLETED]"),
        ("Zaid", "How to make decisions", "Problem 1", "[STARTED]"),
        ("Taylan", "Introduction to Python", "Problem 1", "[STARTED]")
        ]
        return students

def get_topics(course_topics):
    print("Course Topics:")
    for topic in course_topics:
        print("* " + topic)

def get_problems(course_topics):
    problem_dict = dict()
    print("Problems:")
    for topic in course_topics:
        problem_dict.update({topic : ["Problem 1", "Problem 2", "Problem 3"]})
        print("* " + topic + " : ", end = "")
        print(*problem_dict[topic], sep=", ")
    
def get_tracking():
    students = Course_Topics.get_data_list()
    # print("Student Progress:")
    # count = 1
    # for name, mod, prob, prog in students:
    #     print(str(count) + ". ", end="")
    #     print(f"{name} - {mod} - {prob} {prog}")
    #     count += 1

def sort_by_progress(students):
    sorted_list = []
    for item in students:
        if item[3] == "[STARTED]":
            sorted_list.append(item)
    for item in students:
        if item[3] == "[GRADED]":
            sorted_list.append(item)
    for item in students:
        if item[3] == "[COMPLETED]":
            sorted_list.append(item)
    count = 1
    print("Student Progress:")
    for name, mod, prob, prog in sorted_list:
        print(str(count) + ". ", end="")
        print(f"{name} - {mod} - {prob} {prog}")
        count += 1

def create_outline():
    """
    TODO: implement your code here
    """
    get_topics(Course_Topics.get_data_set())
    get_problems(Course_Topics.get_data_set()) 
    
    get_tracking()
    sort_by_progress(Course_Topics.get_data_list())

if __name__ == "__main__":
    create_outline()
