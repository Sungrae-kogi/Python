class Person(object):
    def __init__(self, year, month, day, sec):
        self.year=year
        self.month=month
        self.day=day
        self.sec=sec

    def __str__(self):
        return '{}년 {}월 {}일생 {}입니다.'.format(self.year, self.month, self.day, self.sec)

    @classmethod
    def ssn_constructor(cls,ssn):
        front,back =ssn.split('-')
        sec=back[0]

        if sec=='1' or sec=='2':
            year ='19'+front[:2]
        else:
            year = '20' + front[:2]

        if (int(sec)%2)==0:
            sec='여성'
        else:
            sec='남성'

        month = front[2:4]
        day= front[4:6]

        return cls(year, month, day, sec)

ssn_1 = '900829-1034356'
ssn_2 = '051224-4061569'

person_1 = Person.ssn_constructor(ssn_1)
print(person_1)
person_2 = Person.ssn_constructor(ssn_2)
print(person_2)
