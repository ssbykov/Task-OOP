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
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self._average_rating()} {self.courses_attached}'

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


best_student = Student('Василий', 'Пупло', 'муж.')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['VB']
best_student.finished_courses += ['C++']

student = Student('Софья', 'Ковалевская', 'жен.')
student.courses_in_progress += ['Python']
student.courses_in_progress += ['VB']


cool_Reviewer = Reviewer('Sergei', 'Bykov')
cool_Reviewer.courses_attached += ['VB']
cool_Reviewer.courses_attached += ['Python']
# print(cool_Reviewer.name, cool_Reviewer.surname,cool_Reviewer.courses_attached)

cool_lecturer = Lecturer('Some', 'Buddy')
cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['VB']

cool_lecturer_2 = Lecturer('Some_1', 'Buddy_1')
cool_lecturer_2.courses_attached += ['VB']

cool_Reviewer.rate_hw(student, 'Python', 8)
cool_Reviewer.rate_hw(student, 'Python', 9)
cool_Reviewer.rate_hw(student, 'Python', 7)
# cool_Reviewer.rate_hw(best_student, 'VB', 8)
# cool_Reviewer.rate_hw(best_student, 'Python', 9)

# print(cool_lecturer.grades)
# print(cool_lecturer.courses_attached)
# print(cool_lecturer_2.courses_attached)

cool_Reviewer.rate_hw(best_student, 'Python', 7)
cool_Reviewer.rate_hw(best_student, 'VB', 8)
cool_Reviewer.rate_hw(best_student, 'Python', 9)
 
# print(cool_Reviewer)
print(cool_lecturer)
print(cool_lecturer_2)
# print(best_student)
# print(student)
# # print(best_student < student)
# if best_student < cool_lecturer:
#     print('Софья круче!')
# elif best_student > student:
#     print('Василий круче!')
# else:
#     print('Все хороши!')