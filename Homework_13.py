class Person:
    name: str
    surname: str
    age: int

    def __init__(self, name, surname, age):
        self.set_name(name)
        self.set_surname(surname)
        self.set_age(age)

    def set_name(self, name):
        if 2 < len(name) < 20:
            self.name = name
        else:
            print("Incorrect name length!")

    def get_name(self):
        return self.name

    def set_surname(self, surname):
        if 2 < len(surname) < 50:
            self.surname = surname
        else:
            print("Incorrect surname length!")

    def get_surname(self):
        return self.surname

    def set_age(self, age):
        if 18 < age < 100:
            self.age = age
        else:
            print("Incorrect age!")

    def get_age(self):
        return self.age

    def show_info(self):
        return f"Name: {self.name} surname: {self.surname}, age: {self.age}"


class Student(Person):
    subject: str
    university: str

    def __init__(self, name, surname, age, subject, university):
        super().__init__(name, surname, age)
        self.set_subject(subject)
        self.set_university(university)

    def set_subject(self, subject):
        if 2 < len(subject):
            self.subject = subject
        else:
            print("Incorrect subject!")

    def get_subject(self):
        return self.subject

    def set_university(self, university):
        if 5 < len(university) < 150:
            self.university = university
        else:
            print("Incorrect university")

    def get_university(self):
        return self.university


class Teacher(Person):
    subject: str
    faculty: str
    university: str

    def __init__(self, name, surname, age, subject, faculty, university):
        super().__init__(name, surname, age)
        self.set_subject(subject)
        self.set_faculty(faculty)
        self.set_university(university)

    def set_subject(self, subject):
        if 2 < len(subject):
            self.subject = subject
        else:
            print("Incorrect subject!")

    def get_subject(self):
        return self.subject

    def set_faculty(self, faculty):
        if 5 < len(faculty) < 150:
            self.faculty = faculty
        else:
            print("Incorrect faculty")

    def get_faculty(self):
        return self.faculty

    def set_university(self, university):
        if 5 < len(university) < 150:
            self.university = university
        else:
            print("Incorrect university")

    def get_university(self):
        return self.university


class University:
    def __init__(self, name_university):
        self.name_university = name_university


class Faculty(University):
    def __init__(self, name_faculty, name_university):
        super().__init__(name_university)
        self.name_faculty = name_faculty


class Subject(Faculty):
    def __init__(self, name_subject, name_faculty, name_university):
        Faculty.__init__(self, name_faculty, name_university)
        self.name_subject = name_subject


math_teacher = Teacher("Hanna", "Shevchenko", 45, "High math", "Engineering", "Polytechnic institute")
language_teacher = Teacher("Ivan", "Kovalchuk", 57, "English language", "Pedagogical", "Shevchenko university")

student1 = Student("Anton", "Smituh", 20, "High math", "Polytechnic institute")
student2 = Student("Alina", "Semenec", 23, "Engineering", "Polytechnic institute")
student3 = Student("Valentin", "Petrenko", 21, "English language", "Shevchenko university")

university1 = University("Polytechnic institute")
university2 = University("Shevchenko university")

faculty1 = Faculty("Engineering", "Polytechnic institute")
faculty2 = Faculty("Pedagogical", "Shevchenko university")

subject1 = Subject("High math", "Engineering", "Polytechnic institute")
subject2 = Subject("English language", "Pedagogical", "Shevchenko university")

print("Age:", math_teacher.age)
print(Teacher.mro())
print(student1.surname)
print(Subject.mro())
print(faculty1.name_faculty, faculty2.name_faculty)