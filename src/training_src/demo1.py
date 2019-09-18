class AClass(object):
    aField = "testField"
    def aMethod(self):
        print('testField')


# class Person(object):
#     name = ''
#     age = ''
#     sex = ''
#     def greeting(self, msg):
#         print(self.name, ':', msg)


class Person(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return '<Person: %s>' % self.name

    def greeting(self, msg):
        print(self.name, ':', msg)

zhansan = Person('zhansan')
zhansan.greeting('hello')
# Person.greeting(self, 'hello')
# Person.greeting(zhansan, 'hello')

print(zhansan)

