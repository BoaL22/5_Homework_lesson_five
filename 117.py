    
    #  1. Создайте программу для игры с конфетами человек против человека.
    #     Условие задачи: На столе лежит 117 конфета. Играют два игрока делая ход друг после друга. 
    #     Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
    #     Все конфеты оппонента достаются сделавшему последний ход.


from random import randint
import sys

all_candies = 117
player_one = 1
player_two = 2
bot = 'бот'

def toss():
    print()
    number_player = randint(1, 2)
    heads = 'орел'
    tails = 'решка'
    if number_player == 1:
        print(f'Первым ходит - {heads}')
    else:
        print(f'Первым ходит - {tails}')

def gameplay(player):
    
    global all_candies

    print(f'Ходит игрок {player}')
    number = int(input('Сколько конфет вы заберёте? '))

    if number > 0 and number < 29:
        all_candies = all_candies - number
        print(f'Осталось {all_candies} конфет! ')
    else:
        print('Введите число от 1 до 28! ')
        return gameplay(player)

    if all_candies == 0 or all_candies < 0:
        print(f'Победил игрок - {player}! ')
        sys.exit()

def Bot(bot):
    global all_candies

    print(f'Ходит игрок {bot}')
    number = randint(1, 28)
    print(f'Сколько конфет вы заберёте? {number}')
    all_candies = all_candies - number
    print(f'Осталось {all_candies} конфет! ')


    if all_candies == 0 or all_candies < 0:
        print(f'Победил игрок - {bot}! ')
        sys.exit()

def play():
    choice = input('Будете играть с ботом? да/нет: ')
    toss()

    if choice.lower().strip() == 'да':
        while True:
            gameplay(player_one)
            Bot(bot)

            if all_candies == 0 or all_candies < 0:
                break
        
    else:
        while True:
            gameplay(player_one)
            gameplay(player_two)

            if all_candies == 0 or all_candies < 0:
                break

play()

