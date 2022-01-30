from typing import List

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    def rate_hw(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and course in lecturer.courses_attached 
            and course in self.courses_in_progress and str(grade).isnumeric() and 0 < int(grade) < 11):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _average_rating(self):
        sum_rating = 0
        number_of_ratings = 0
        for grade in self.grades.values():
            sum_rating += sum(grade)
            number_of_ratings += len(grade)
        if number_of_ratings:
            return sum_rating / number_of_ratings
        else:
            return 'Оценок нет'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Это не студент!')
            return
        return self._average_rating() < other._average_rating()

    def __str__(self) -> str:
        return (f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}\n'
            f'Средняя оценка за домашние задания: {self._average_rating()}\n'
            f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
            f'Завершенные курсы: {", ".join(self.finished_courses)}')

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _average_rating(self):
        sum_rating = 0
        number_of_ratings = 0
        for grade in self.grades.values():
            sum_rating += sum(grade)
            number_of_ratings += len(grade)
        if number_of_ratings:
            return sum_rating / number_of_ratings
        else:
            return 'Оценок нет'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Это не лектор!')
            return
        return self._average_rating() < other._average_rating()

    def __str__(self) -> str:
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self._average_rating()}'

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress
            and str(grade).isnumeric() and 0 < int(grade) < 11):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self) -> str:
        return f'Имя: {self.name}\nФамилия: {self.surname}'

def average_rating_student_course(students: List[Student], course):
    sum_rating = 0
    number_of_ratings = 0
    for student in students:
        if course in student.grades:
            sum_rating += sum(student.grades[course])
            number_of_ratings += len(student.grades[course])
    if number_of_ratings:
        print(f'Средняя оценка по курсу {course} у студентов: {sum_rating / number_of_ratings}.')
    else:
        print(f'Оценок по курсу {course} нет') 

def average_rating_lecturer_course(lecturers: List[Lecturer], course):
    sum_rating = 0
    number_of_ratings = 0
    for lecture in lecturers:
        if course in lecture.grades:
            sum_rating += sum(lecture.grades[course])
            number_of_ratings += len(lecture.grades[course])
    if number_of_ratings:
        print(f'Средняя оценка по курсу {course} у лекторов: {sum_rating / number_of_ratings}.')
    else:
        print(f'Оценок по курсу {course} нет') 


student_1 = Student('Василий', 'Пупло', 'муж.')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['VB']
student_1.finished_courses += ['C++']

student_2 = Student('Софья', 'Ковалевская', 'жен.')
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['C++']
student_2.finished_courses += ['VB']

reviewer_1 = Reviewer('Сергей', 'Петров')
reviewer_1.courses_attached += ['VB']
reviewer_1.courses_attached += ['Python']

reviewer_2 = Reviewer('Андрей', 'Сидиров')
reviewer_2.courses_attached += ['Python']
reviewer_2.courses_attached += ['C++']

lecturer_1 = Lecturer('Александр', 'Строгий')
lecturer_1.courses_attached += ['Python']
lecturer_1.courses_attached += ['VB']

lecturer_2 = Lecturer('Иван', 'Добрый')
lecturer_2.courses_attached += ['Python']
lecturer_2.courses_attached += ['C++']

reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_2, 'Python', 10)
reviewer_1.rate_hw(student_1, 'VB', 9)

reviewer_2.rate_hw(student_1, 'Python', 9)
reviewer_2.rate_hw(student_2, 'Python', 10)
reviewer_2.rate_hw(student_2, 'C++', 10)

student_1.rate_hw(lecturer_1, 'Python', 9)
student_1.rate_hw(lecturer_1, 'VB', 9)
student_1.rate_hw(lecturer_1, 'Python', 8)

student_2.rate_hw(lecturer_2, 'Python', 8)
student_2.rate_hw(lecturer_2, 'C++', 8)
student_2.rate_hw(lecturer_2, 'Python', 9)

print(student_1)

print(reviewer_1)

print(lecturer_1)

print(student_1 > student_2)

print(lecturer_1 > lecturer_2)

average_rating_student_course([student_1, student_2], 'Python')

average_rating_lecturer_course([lecturer_1, lecturer_2], 'Pyton')