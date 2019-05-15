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
    def __init__(self, name, father_name,  surname, class_room, father, mother, class_subj):
        Person.__init__(self, name, father_name,  surname)
        self.class_room = class_room
        self.father = father
        self.mother = mother
        self.subj = class_subj
 
    def get_class_room(self):
        return self.class_room
 
    def get_parents(self):
        return self.father, self.mother

    def get_class_kid_list(self):
        self.class_kid_list = [self.get_full_name(),self.class_room]
        return self.class_kid_list

    def get_class_subj_list(self):
        self.class_subj_list = self.subj
        return self.class_subj_list

class Teacher(Person):
    def __init__(self, name, father_name, surname, classes, subject):
        Person.__init__(self, name, father_name, surname)
        self.classes = classes
        self.subject = subject

    def get_teachers_list(self):
        self.teachers_list = [self.get_full_name(), self.subj]
        return self.subject
 
    def get_classes(self):
        return self.classes    
    
        
if __name__ == '__main__':  
    students = [Student('Виктория', 'Валерьевна', 'Чкалова', '4A', 'Чкалов Валерий Сергеевич', 'Чкалова Валерия Сергеевна',['Алгебра', 'Физика', 'Химия']),
                Student('Алина', 'Ивановна', 'Иванова', '4A', 'Иванов Иван Валерьевич', 'Иванова Арина Сергеевна',['Алгебра', 'Физика', 'Химия']),
                Student('Ален', 'Петрович', 'Иксанов', '7A', 'Иксанов Петр Валерьевич', 'Иксанова Роза Сергеевна',['Алгебра', 'Физика', 'Химия'])]
    teachers = [Teacher('Иван', 'Иванович', 'Иванов', '4A', 'Алгебра'),
                Teacher('Петр', 'Петрович', 'Петров',  '6A','Физика'),
                Teacher('Сидор', 'Сидорович', 'Сидоров', '7A', 'Химия')]

print('1. Получить полный список всех классов школы: ')
st = set([val.get_class_room() for val in students])
print(st)

print('2. Получить список всех учеников в указанном классе: ')
class_id ='4A'
st_list = []
for _ in students:
    if _.get_class_room() == class_id:
        st_list.append([_.get_short_name()])
print(st_list)
print('3. Получить список всех предметов указанного ученика')
st_name='Иванова А.И.'
st_subj = []
st_par = []
for _ in students:
    if _.get_short_name() == st_name:
        st_subj =_.get_class_subj_list()
        st_par=_.get_parents()
print(st_subj)
print('4. Узнать ФИО родителей указанного ученика')
print(st_par)
print('5. Получить список всех Учителей, преподающих в указанном классе')
class_id ='4A'
t_list = []
for _ in teachers:
     if _.get_classes() == class_id:
        t_list.append([_.get_short_name()])
print(t_list)
