import json
count = 0
students = {}  # (name, id)
addCourses = []  # course catalog
enrollCourses = {}  # enrollment record for students

class Course:
    def __init__(self, course, id, creditHours, courseType, addCourses):
        self.course = course
        self.id = id
        self.creditHours = creditHours
        self.courseType = courseType
        self.addCourses = addCourses

class Add(Course):#choice 1 
    def __init__(self, course, courseID, creditHours, courseType, addCourses):
       super().__init__(course, courseID, creditHours, courseType, addCourses)

    def addToCatalog(self):
        subAddCourses = [course,id,creditHours,courseType]
        self.addCourses.append(subAddCourses)
        return addCourses

class Enroll:#choice 2
    def __init__(self, course, name, countCourse, addCourses, enrollCourses):
       self.name = name
       self.course = course
       self.countCourse = countCourse
       self.addCourses = addCourses
       self.enrollCourses = enrollCourses

    def enrollCatalog(self):
        for i in self.addCourses:
            if i[0] == course:
                enrollCourses[f"course {name}({countCourse})"] = course
                print(f"You enrolled successfully in this course: {course}")
                return
        print("This course doesn't exist in the catalog.")

class Drop:#choice 3
    def __init__(self, course, enrollCourses):
       self.course = course
       self.enrollCourses = enrollCourses

    def drop(self):
        for key, value in list(enrollCourses.items()):
            if value == course:
                enrollCourses.pop(key,None)
                print("You dropped this course successfully.")
                return
        print("Invalid input. There is no course in the enrollment catalog called", self.course)

class Students:#for every student
    def __init__(self, name, id, count):
        self.name = name
        self.id = id
        self.count = count 

    def addToCatalog(self):
        students[f"Name{self.count}"] = name
        students[f"Id{self.count}"] = id
        return students

while True:
    EnrollCourses = {}  # reset each student's enrollments
    countCourse = 0
    count += 1
    print("Welcom to enrollment system for a university!!")
    name = input("Enter your name: ")
    id = int(input("Enter your id: "))

    studentInstance = Students(name, id, count)
    students = studentInstance.addToCatalog()

    while True:
        choice = int(input("""1. Add Course: Add a new course to the catalog.\n
2. Enroll Student in Course: Enroll a student in a specified course.\n
3. Drop Course for Student: Drop a specified course for a student.\n
4. List Student Courses: Display all courses a student is enrolled in.\n
5. Save Course Catalog: Save the current course catalog to a file.\n
6. Load Course Catalog: Load the course catalog from a file.\n
7. Exit: Exit the program.\n
-------------------------------------------------------------------\n
Enter a choice: """))

        if choice == 1:
            course = input("Enter course name: ")
            courseID = input("Enter course ID: ")
            creditHours = input("Enter credit hours: ")
            courseType = input("Enter course type (core/elective): ")
            cours = Add(course, courseID, creditHours, courseType, addCourses)
            addCourses = cours.addToCatalog()
            print(f"Course {course} added to catalog.")

        elif choice == 2:
            course = input("Enter your enrollment course: ")
            countCourse += 1
            cours = Enroll(course, name, countCourse, addCourses, EnrollCourses)
            cours.enrollCatalog()

        elif choice == 3:
            course = input("Enter a course to drop: ")
            drop = Drop(course,enrollCourses)
            drop.drop()

        elif choice == 4:
            print(f"Courses enrolled: {enrollCourses}")

        elif choice == 5:
            with open(f'data{id}.json', 'w') as json_file:
                json.dump(addCourses, json_file)
            print(f"Courses saved to data{id}.json")

        elif choice == 6:
            file_name = input("Enter the name of the JSON file: ")
            with open(file_name, 'r') as json_file:
                    loadCourseCatalog = json.load(json_file)
                    print("Loaded Courses:", loadCourseCatalog)
            
        elif choice == 7:
            break
        else:
            print("Invalid input. Please try again!")

    complete = input("Is there any student who wants to register also? (y/n): ")
    if complete.lower() == 'n':
        break

print("Have a nice day!!!")

