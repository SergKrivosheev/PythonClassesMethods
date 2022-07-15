#Не реализовывал как отдельную программу, в которой надо вводить данные, а просто создал по два экземпляра классов
#Lecturer и Student, один экземпляр класса Reviewer. В 4 задании создал два списка с экземплярами класса и над ними
#проводил манипуляции в функциях вычисления средних оценок по курсу
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_rating(self):
        mean_grade = 0
        grade_counter = 0
        for course_name in self.grades:
            for grade in self.grades[course_name]:
                mean_grade += int(grade)
                grade_counter += 1
        return mean_grade/grade_counter

    def __courses_in_progress(self):
        return ', '.join(self.courses_in_progress)

    def __finished_courses(self):
        return ', '.join(self.finished_courses)

    def __lt__(self, other):
        if not isinstance(other, Student):
            return print('Не студент')
        else:
            return self.average_rating() < other.average_rating()

    def __gt__(self, other):
        if not isinstance(other, Student):
            return print('Не студент')
        else:
            return self.average_rating() > other.average_rating()

    def __str__(self):
        output = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_rating()}\nКурсы в процессе изучения: {self.__courses_in_progress()}\nЗавершенные курсы: {self.__finished_courses()}\n '
        return output

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in student.courses_in_progress: ##and course in self.courses_attached:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        output = f'Имя: {self.name}\nФамилия: {self.surname}\n'
        return output

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    def average_rating(self):
        mean_grade = 0
        grade_counter = 0
        if self.courses_attached:
            for course_name in self.grades:
                for grade in self.grades[course_name]:
                    mean_grade += int(grade)
                    grade_counter += 1
                    out_ = mean_grade/grade_counter
            return out_
        else:
            return 'Ошибка'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return print('Не лектор')
        else:
            return self.average_rating() < other.average_rating()

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            return print('Не лектор')
        else:
            return self.average_rating() > other.average_rating()


    def __str__(self):
        output = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка: {self.average_rating()}\n'
        return output

def average_students(st_list, course):
    i = 0
    mean = 0
    for element in st_list:
        if course in element.grades:
            for grade in element.grades[course]:
                mean += grade
                i += 1
    return print(f'Средняя оценка студентов по курсу {course} {mean / i}')

def average_lecturer(lec_list, course):
    i = 0
    mean = 0
    for element in lec_list:
        if course in element.grades:
            for grade in element.grades[course]:
                mean += grade
                i += 1
    return print(f'Средняя оценка преподавателя по курсу {course} {mean / i}')

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']
other_student = Student('Rude', 'Boy', 'Reptiloid')
other_student.courses_in_progress += ['Python']
other_student.courses_in_progress += ['Git']
other_student.finished_courses += ['Введение в программирование']

cool_mentor = Lecturer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
cool_reviewer = Reviewer('Adolf', 'Stein')
other_lecturer = Lecturer('Erik', 'Cartman')
other_lecturer.courses_attached += ['Python']

best_student.rate_lecturer(cool_mentor, 'Python', 10)
best_student.rate_lecturer(cool_mentor, 'Python', 8)
best_student.rate_lecturer(cool_mentor, 'Python', 5)
best_student.rate_lecturer(cool_mentor, 'Python', 10)
best_student.rate_lecturer(other_lecturer, 'Python', 6)
best_student.rate_lecturer(other_lecturer, 'Python', 7)
best_student.rate_lecturer(other_lecturer, 'Python', 5)
best_student.rate_lecturer(other_lecturer, 'Python', 9)
#средняя оценка по курсу Python 7.5

cool_reviewer.rate_hw(best_student, 'Python', 8)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Git', 8)
cool_reviewer.rate_hw(best_student, 'Python', 8)
cool_reviewer.rate_hw(other_student, 'Python', 6)
cool_reviewer.rate_hw(other_student, 'Python', 4)
cool_reviewer.rate_hw(best_student, 'Git', 4)
cool_reviewer.rate_hw(best_student, 'Git', 9)
#средняя оценка по курсу Python 7.2

students_list = [best_student, other_student]
lecturers_list = [cool_mentor, other_lecturer]

print(cool_reviewer)
print(cool_mentor)
print(best_student)
print(other_lecturer)
print(other_student)

print(cool_mentor < other_lecturer)
print(cool_mentor > other_lecturer)
print(best_student < other_student)
print(best_student > other_student)

print(average_students(students_list, 'Python'))
print(average_lecturer(lecturers_list, 'Python'))