# class Name(object):
#     def __init__(self, name):
#         self.name = name

#     def __len__(self):
#         return len(self.name)

#     def split(self):
#         return self.name.split()

#     def lower(self):
#         return self.name.lower()

#     def lastname(self):
#         return self.name.split()[-1]


class Name(str):
    def lastname(self):
        return self.split()[-1]


zhangsan = Name('Zhang San')
print(len(zhangsan))  # 9
print(zhangsan.split())  # ['Zhang', 'San']
print(zhangsan.lower())  # 'zhang san'
print(zhangsan.lastname())  # 'San'

print(zhangsan)
