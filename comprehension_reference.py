import os

db_pass = os.environ.get('PASS')

nums = [1,2,3,4,5,6,7,8,9,10]

my_list = [n*n for n in nums]
my_list = map(lambda n: n*n, nums)


my_list = [n for n in nums if n%2==0]
my_list = filter(lambda n: n%2==0, nums)

letters = ['a', 'b', 'c', 'd']; numbers = range(4)
my_list = [[letter, number] for letter in letters for number in numbers ]
my_dict = {name: letter for name, letter in zip(letters, numbers) if letter%2==0}
for i in enumerate(letters):
    print(i)

nums = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9]
my_set = {n for n in nums if n%2==0}


my_gen = (n*n for n in nums)
for i in my_gen:
    print(i)

nums = [3,1,6,2,7,8,4,9,9]
nums_tuple = (3,1,6,2,7,8,4,9,9)
s_li = sorted(nums, reverse=True)
s_tuple = sorted(nums_tuple, reverse=True)


print(nums[1:7:2])


url = 'http://mohamedkassem.com'
url[-4:]
url[7:-4]

person = {'name': 'Mohamed', 'age': 23}
person_list = ['Mohamed',23]
sent = 'My name is {0[name]} and my age is {0[age]}'.format(person)
sent = 'My name is {0[0]} and my age is {0[1]}'.format(person_list)
sent = f'My name is {person_list[0]} and my age is {person_list[1]}'

class Person():

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age


p1 = Person('Mohamed', 23)
print(f'My name is {p1.name} and my age is {p1.age}')

[f'The value is {i:02}' for i in range(1, 11)]


my_dict = {"item": "football", "price": 10.00}
my_dict.get('count')
my_dict.setdefault('count', 10)
my_dict

from collections import Counter
Counter(nums)
Counter(nums).most_common(5)[0]


",".join(letters)

colors = ["red", "blue", "green"]
c = "red"

if c in colors:
     print(c)


