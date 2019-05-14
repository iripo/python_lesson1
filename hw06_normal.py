class Classroom:
    def __init__(self, class_room):
        self.class_room = {
            'class_num': int(class_room.split()[0]),
            'class_letter': class_room.split()[1]
        }
 
    def get_name(self):
        return str(self.class_room['class_num']) + ' ' + self.class_room['class_letter']

class Person:
    def __init__(self, name, father_name, surname):
        self.name = name
        self.surname = surname
        self.father_name = father_name

 
    def get_full_name(self):
        return self.surname + ' ' + self.name + ' '+ self.father_name

    def get_short_name(self):
        return '{} {}.{}.'.format(self.surname.title(), self.name[0].upper(), self.father_name[0].upper())

class Student(Person):
    def __init__(self, name, father_name,  surname, class_room, father, mother):
        Person.__init__(self, name, father_name,  surname)
        self.class_room = class_room
        self.father = father
        self.mother = mother
 
    def get_class_room(self):
        return self.class_room
 
    def get_parents(self):
        return self.father.get_full_name(), self.mother.get_full_name()

class Teacher(Person):
    def __init__(self, name, father_name, surname, classes, subject):
        Person.__init__(self, name, father_name, surname)
        self.classes = classes
        self.subject = subject
 
    def get_subject(self):
        return self.subject
 
    def get_classes(self):
        return self.classes    
    
        
if __name__ == '__main__':  
    class_room = ['5 А', '6 Б', '7 В']
    parents = [Person('Валерий', 'Павлович', 'Чкалов'),
               Person('Василиса', 'Петровна', 'Чкалова'),
               Person('Николай', 'Францевич', 'Гастелло'),
               Person('Нина', 'Федоровна', 'Гастелло'),
               Person('Юрий', 'Алексеевич', 'Гагарин'),
               Person('Юлия', 'Андреевна', 'Гагарина')]
    students = [Student('Виктория', 'Валерьевна', 'Чкалова', class_room[0], parents[0], parents[1]),
                Student('Никита', 'Николаевич', 'Гастелло',  class_room[1], parents[2], parents[3]),
                Student('Юлий', 'Юрьевич', 'Гагарин',  class_room[2], parents[4], parents[5])]
    teachers = [Teacher('Иван', 'Иванович', 'Иванов', [class_room[0], class_room[1]], 'Алгебра'),
                Teacher('Петр', 'Петрович', 'Петров', [class_room[2], class_room[1]],'Физика'),
                Teacher('Сидор', 'Сидорович', 'Сидоров', [class_room[0], class_room[2]], 'Химия')]

st = set([val.get_class_room() for val in students])
print(st)

for cl_room in class_room:
    st_list = [val.get_short_name() for val in students if val.get_class_room() == cl_room]
    print(cl_room)
    print(st_list)

student = students[0]
parents = student.get_parents()
print(parents)