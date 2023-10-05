import random

counter = 0
right_counter = 0

while counter != 10:
    random_number = random.randint(0, 6)
    user_input = input('\nУгадайте число: ')
    if int(user_input) == random_number:
        right_counter += 1
        counter += 1
        print('Вы угадали!')
    else:
        counter += 1
        print('Вы не угадали :( ')

if right_counter in [2, 3, 4]:
    print(f'\nКонец игры, вы угадали {right_counter} раза')
else:
    print(f'\nКонец игры, вы угадали {right_counter} раз')
