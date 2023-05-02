class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grade = {}

    def _round_rate(self):
        sum_ = 0
        counter = 0
        for i in self.grade.values():
            for j in i:
                sum_ += j
                counter += 1
        res = sum_ / counter
        return res

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grade:
                lecturer.grade[course] += [grade]
            else:
                lecturer.grade[course] = [grade]
        else:
            print('на курсе нет такого лектора!')

    def __str__(self):
        co = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя за домашние задания: {self._round_rate()}\nКурсы в процессе: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}'
        return co

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Это не студент')
            return
        return self._round_rate() < other._round_rate()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grade = {}

    def _round_rate(self):
        sum_ = 0
        counter = 0
        for i in self.grade.values():
            for j in i:
                sum_ += j
                counter += 1
        res = sum_ / counter
        return res

    def __str__(self):
        comm = f'Имя:{self.name} \nФамилия:{self.surname} \nСредняя оценка за лекции:{self._round_rate()}'
        return comm

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Это не лектор!')
            return
        return self._round_rate() < other._round_rate()


class Reviewer(Mentor):
    grade = {}

    def __str__(self):
        comm = f'Имя:{self.name} \nФамилия:{self.surname}'
        return comm

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in student.courses_in_progress:
            if course in student.grade:
                student.grade[course] += [grade]
            else:
                student.grade[course] = [grade]
        return 'Ошибка'


some_reviever1 = Reviewer("Гена", "Чёткий")
some_reviever2 = Reviewer("Саша", "Белый")
some_lecturer1 = Lecturer("Михаил", "Сусойкин")
some_lecturer2 = Lecturer("Владимир", "Путилин")
some_student1 = Student("Илья", "Пупкин", "муж")
some_student2 = Student("Василий", "Тёркин", "муж")

some_student1.courses_in_progress += ["SQL"]
some_student1.courses_in_progress += ["Python"]
some_student2.courses_in_progress += ["SQL"]
some_student2.courses_in_progress += ["Python"]
some_lecturer1.courses_attached += ["Python"]
some_lecturer2.courses_attached += ["SQL"]

some_student1.finished_courses += ["Ландшафтный дизайн"]
some_student2.finished_courses += ["Exsel"]
some_student1.finished_courses += ["Minecraft"]
some_student2.finished_courses += ["Gamer"]

some_student1.rate_lecturer(some_lecturer1, "Python", 5)
some_student2.rate_lecturer(some_lecturer2, "SQL", 7)

some_reviever1.rate_hw(some_student1, "Python", 9)
some_reviever1.rate_hw(some_student1, "SQL", 4)
some_reviever2.rate_hw(some_student2, "SQL", 9)
some_reviever2.rate_hw(some_student2, "Python", 7)
some_student1.rate_lecturer(some_lecturer1, "Python", 7)
some_student2.rate_lecturer(some_lecturer2, "SQL", 9)
some_student1.rate_lecturer(some_lecturer1, "Python", 2)
some_student2.rate_lecturer(some_lecturer2, "SQL", 10)
some_reviever1.rate_hw(some_student1, "Python", 5)
some_reviever2.rate_hw(some_student2, "SQL", 4)
some_reviever1.rate_hw(some_student2, "SQL", 6)
some_reviever2.rate_hw(some_student1, "Python", 8)
some_reviever1.rate_hw(some_student2, "SQL", 1)

some_student_list = [some_student1, some_student2]
some_lecturer_list = [some_lecturer1, some_lecturer2]


def rating_for_all(course, some_student_list):
    sum_rating_stud = 0
    total_rating = 0
    for student in some_student_list:
        for course in student.grade:
            student_sum_rating = student._round_rate()
            sum_rating_stud += student_sum_rating
            total_rating += 1
    circle_rating = round(sum_rating_stud / total_rating, 2)
    print(f'Средняя оценка на курсе {course} :{circle_rating}')


rating_for_all("SQL", some_student_list)
rating_for_all("Python", some_lecturer_list)
print(some_lecturer1)
print(some_lecturer2)
print(some_student1)
print(some_student2)
print(some_reviever1)
print(some_reviever2)
print(some_lecturer1.__lt__(some_lecturer2))

