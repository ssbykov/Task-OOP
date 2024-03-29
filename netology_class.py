# https://github.com/netology-code/py-homeworks-basic/tree/master/6.classes


from typing import List


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    # При реализации данной функциии в проверку включены только студенты, которые проходят курс
    # Соответственно реализована проверка только по списку courses_in_progress.
    # Студенты, которые закончили курс, оценки лекторам по даннму предмету ставить уже не могут.
    # Так же добавил проверку на ввод данных по оценке.
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
        grades_lst = sum(self.grades.values(), [])
        if grades_lst:
            return sum(grades_lst) / len(grades_lst)
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
                f'Средняя оценка за домашние задания: {round(self._average_rating(), 1)}\n'
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
        grades_lst = sum(self.grades.values(), [])
        if grades_lst:
            return sum(grades_lst) / len(grades_lst)
        else:
            return 'Оценок нет'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Это не лектор!')
            return
        return self._average_rating() < other._average_rating()

    def __str__(self) -> str:
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {round(self._average_rating(), 1)}'


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

    grades_lst = sum([student.grades.get(course, []) for student in students], [])

    if grades_lst:
        print(f'Средняя оценка по курсу {course} у студентов: {round(sum(grades_lst) / len(grades_lst), 1)}.')
    else:
        print(f'Оценок по курсу {course} нет')


def average_rating_lecturer_course(lecturers: List[Lecturer], course):

    grades_lst = sum([lecturer.grades.get(course, []) for lecturer in lecturers], [])

    if grades_lst:
        print(f'Средняя оценка по курсу {course} у лекторов: {round(sum(grades_lst) / len(grades_lst), 1)}.')
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
reviewer_1.rate_hw(student_2, 'Python', 5)
reviewer_1.rate_hw(student_1, 'VB', 9)

reviewer_2.rate_hw(student_1, 'Python', 9)
reviewer_2.rate_hw(student_2, 'Python', 3)
reviewer_2.rate_hw(student_2, 'C++', 10)

student_1.rate_hw(lecturer_1, 'Python', 9)
student_1.rate_hw(lecturer_1, 'VB', 9)
student_1.rate_hw(lecturer_1, 'Python', 8)

student_2.rate_hw(lecturer_2, 'Python', 8)
student_2.rate_hw(lecturer_2, 'VB', 8)
student_2.rate_hw(lecturer_2, 'Python', 9)

print(student_1)

print(reviewer_1)

print(lecturer_1)

print(student_1 > student_2)

print(lecturer_1 > lecturer_2)

average_rating_student_course([student_1, student_2], 'Python')

average_rating_lecturer_course([lecturer_1, lecturer_2], 'Python')
