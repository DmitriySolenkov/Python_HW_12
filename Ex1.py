import csv


class Subject:
    def __init__(self, subject, grades: list, tests: list):
        self.name = subject
        self.grades = grades
        self.tests = tests

    def __str__(self):
        return f'{self.name}. Grades: {self.grades}. Tests: {self.tests}'

    def print_average_test_score(self):
        count, sum = 0, 0
        for elem in self.tests:
            count += 1
            sum += elem
        print(f'Average test score in {self.name}: {sum//count}')


class Student:
    def __init__(self):
        self._surname = ''
        self._name = ''
        self._second_name = ''
        self.subjects = []

    @property
    def surname(self):
        return self._surname

    @property
    def name(self):
        return self._name

    @property
    def second_name(self):
        return self._second_name

    @surname.setter
    def surname(self, value):
        if value.isalpha() and value.istitle():
            self._surname = value

    @name.setter
    def name(self, value):
        if value.isalpha() and value.istitle():
            self._name = value

    @second_name.setter
    def second_name(self, value):
        if value.isalpha() and value.istitle():
            self._second_name = value

    @property
    def full_name(self):
        return f'{self._surname} {self._name} {self._second_name}'


def load_subjects(student):
    with open('subjects.csv', 'r', newline='') as f:
        csv_file = csv.reader(f)
        for line in csv_file:
            if line[0] == student.surname:
                new_subject = ''
                grades = []
                tests = []
                for elem in line:
                    if "." in elem:
                        elem = elem.split(".")
                        grade = int(elem[0])
                        grades.append(grade)
                    try:
                        test = int(elem)
                        tests.append(test)
                    except:
                        pass

                student.subjects.append(Subject(line[1], grades, tests))


def print_average_grade(student):
    count, sum = 0, 0
    for subject in student.subjects:
        for grade in subject.grades:
            count += 1
            sum += grade
    print(f'Average grade in all subjects: {sum/count}')


with open('subjects.csv', 'w', newline='') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(['Marston', 'English', 4.0, 3.0, 5.0, 2.0, 87, 73, 98, 91])
    filewriter.writerow(['Marston', 'Mathematics', 5.0, 5.0, 3.0, 2.0, 63, 9, 100, 54])
    filewriter.writerow(['Marston', 'Economics', 2.0, 2.0, 5.0, 5.0, 95, 87, 23, 2])
    filewriter.writerow(['Auditore', 'Russian', 5.0, 3.0, 3.0, 3.0, 84, 43, 65, 88])
    filewriter.writerow(['De_Santa', 'Robbing', 4.0, 5.0, 5.0, 2.0, 65, 99, 93, 84])
    filewriter.writerow(['Marston', 'Swiming', 2.0, 4.0, 2.0, 5.0, 34, 65, 67, 81])

student = Student()
while (student.surname == ''):
    # 'Marston' recommended
    surname = input("Enter student's surname:")
    student.surname = surname
while (student.name == ''):
    name = input("Enter student's name:")
    student.name = name
while (student.second_name == ''):
    second_name = input("Enter student's second_name:")
    student.second_name = second_name
print(student.full_name)

load_subjects(student)
for elem in student.subjects:
    print(elem)
for elem in student.subjects:
    elem.print_average_test_score()
print_average_grade(student)
