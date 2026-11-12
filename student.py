class Student:
    def __init__(self, name, studentId, grade):
        self.__name = name
        self.__studentId = studentId
        self.__grade = grade

        def get_name(self):
            return self.__name
        def get_studetId(self):
            return self.__studentId
        def get_grade(self):
            return self.__grade
        
    def set_grade(self, grade):
        self.__grade = grade

    def display_info(self):
        print(f"Name: {self.__name} | ID: {self.__studentId} | Grade {self.__grade}")

s1 = Student("Juan Dela Cruz", "2026-001", 89.3)
s2 = Student("Maria Santos", "2026-002", 88.5)

s1.set_grade(92.0)

s1.display_info()
s2.display_info()