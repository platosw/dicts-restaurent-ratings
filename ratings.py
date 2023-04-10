"""Restaurant rating lister."""


# put your code here
from random import choice

rest_rating = {}

RATE_FILE = open('scores.txt')
for line in RATE_FILE:
    line = line.replace('\n', '').split(':')
    rest_rating[line[0]] = int(line[1])
RATE_FILE.close()


def add_rating(rest_name, rating):
    rest_rating[rest_name] = rating
    rate_file = open('scores.txt', 'a')
    rate_file.write(f'{rest_name}:{rating}\n')
    rate_file.close()


def added():
    add_rest = input('\nWhat is the restaurent name to add to the datas? ')
    add_rate = input(
        'What is the restaurent\'s rating to add to the datas? ')
    add_rating(add_rest, add_rate)


def print_ratings():
    for restaurent in sorted(rest_rating.items()):
        print(f'{restaurent[0]} is rated at {restaurent[1]}.')


def random_rating():
    random = choice(sorted(rest_rating))
    print(f'\n{random} is rated at {rest_rating[random]}.')
    user_rating = input(f'What\'s your rating of {random}? ')
    rest_rating[random] = int(user_rating)


def chosen_rating():
    chosen = input('\nWhich restaurent\'s rating do you want to update? ')
    print(f'\n{chosen} is rated at {rest_rating[chosen]}.')
    user_rating = input(f'What\'s your rating of {chosen}? ')
    rest_rating[chosen] = int(user_rating)


while True:
    user_option = input(
        '1 = seeing all the ratings, 2 = Adding a new restaurent and rating it, 3 = Update a Random Restaurant’s Rating, 4 = Update a Chosen Restaurant’s Rating, q = exit ')

    if user_option == '1':
        print_ratings()
    elif user_option == '2':
        added()
    elif user_option == '3':
        random_rating()
    elif user_option == '4':
        chosen_rating()
    elif user_option == 'q':
        break
    else:
        print('Type Error!!')


RATE_FILE = open('scores.txt', 'w')
for key, value in rest_rating.items():
    RATE_FILE.write(f'{key}:{str(value)}\n')
RATE_FILE.close()
