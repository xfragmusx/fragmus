def age_checker():
    age = (input('Enter your age:'))
    name = input("enter your name:")

    if age < 18 or name == 'alice':
        print('not allow to drink')
    elif age <= 21 and name == 'Bob':
        print('not allow to drink (USA CITIZEN)')
    else:
        print('allow to drink')


print('abc')
def greet():
    print('Hello')


def call_greet():
    greet()

call_greet()