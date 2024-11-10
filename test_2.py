
class Person_t:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def introduce(self):
        return f"姓名：{self.name}, 年龄：{self.age}"
class Teacher_t(Person_t):
    def __init__(self, name, age,subject):
        super().__init__(name, age)
        self.subject=subject
    def introduce(self):
        return f"{super().introduce()}, 教授科目：{self.subject}"
class Student_t(Person_t):
    def __init__(self, name, age,grade):
        super().__init__(name, age)
        self.grade=grade
    def introduce(self):
        return f"{super().introduce()}, 年级: {self.grade}"
    

class Course_t:
    def __init__(self,course_name,teacher):
        self.course_name=course_name
        self.teacher=teacher
        self.students = []
         

    def add_students(self,student):
      self.students.append(student)

    def remove_students(self,student):
      self.students.remove(student)
    def show_course_info(self):
       student_info = ', '.join([student.name for student in self.students])
       return (f"课程名称：{self.course_name}, "
                f"授课教师：{self.teacher.name}, "
                f"选修学生：{student_info if self.students else '无'}")
#实例
teacherMath=Teacher_t("Mr.zhang",20,"math")
teacherChinese=Teacher_t("Mr.li",21,"chinese")
courseMath=Course_t("math",teacherMath)
courseChinese=Course_t("chinese",teacherChinese)
student1=Student_t("一",16,"高一")
student2=Student_t("二",17,"高二")
student3=Student_t("三",18,"高三")

courseChinese.add_students(student1)
courseMath.add_students(student2)
courseMath.add_students(student3)

print(courseChinese.show_course_info())
print(courseMath.show_course_info())

courseMath.remove_students(student2)