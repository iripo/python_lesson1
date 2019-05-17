import random 

class Card:
    def __init__(self, name):
        line = [['' for x in range(9)] for y in range(3)]
        alist=list(range(1, 91))
        ilist = list(range(0,9))
        self.card = []
        bn = []
        il = []
        for j in range(3):
            while len(il)<5:
                b=random.choice(alist)
                im=random.choice(ilist)
                line[j][im] = b
                bn.append(b)
                il.append(im)
                alist=list(set(alist) - set(bn))
                ilist=list(set(ilist) - set(il))
            self.card.append(line[j])
            ilist = list(range(0,9))
            il = []
        self.name = name
        self.count_barrel = 15

    def __str__(self):
        rez = '{:-^26}\n'.format(self.name)
        for x in range(3):
            rez += '{:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2}'\
                    .format(*self.card[x]) + '\n'
        return rez + '--------------------------'

computer = Card(' Карточка компьютера ')
player = Card(' Карточка игрока ')
bag = list(range(1, 91))
while True:
    barrel = bag.pop(random.randint(0, len(bag) - 1))
    print('\nНовый бочонок: {} (осталось {})'.format(barrel, len(bag)))
    print(computer)
    print(player)
    reply = input('Зачеркнуть цифру? (y/n/q)')
    reply = reply.lower()
    while len(reply) == 0 or reply not in 'ynq':
        print('\n\n!!! Ответ не распознан!\n')
        print('Новый бочонок: {} (осталось {})'.format(barrel, len(bag)))
        print(computer)
        print(player)
        reply = input('Зачеркнуть цифру? (y/n/q)')
        reply = reply.lower()

    if reply == 'q':
        print('Вы вышли из игры.')
        break
    elif reply == 'y':
        test = False  # Есть ли такая цифра на карточке игрока?
        for x in range(3):
            if barrel in player.card[x]:
                test = True
                player.card[x][player.card[x].index(barrel)] = '-'
                player.count_barrel -= 1
            if barrel in computer.card[x]:
                computer.card[x][computer.card[x].index(barrel)] = '-'
                computer.count_barrel -= 1
        if test:
            if player.count_barrel < 1:
                print('Вы Выиграли!')
                break
            elif computer.count_barrel < 1:
                print('Компьютер Выиграл!')
                break
        else:
            print('Вы проиграли! Такого числа нет на Вашей карточке!')
            break
    elif reply == 'n':
        test = False  # Есть ли такая цифра на карточке игрока?
        for x in range(3):
            if barrel in player.card[x]:
                print('Вы проиграли! Такое число есть на Вашей карточке!')
                test = True
                break
            if barrel in computer.card[x]:
                computer.card[x][computer.card[x].index(barrel)] = '-'
                computer.count_barrel -= 1
        if test:
            break
        if player.count_barrel < 1:
            print('Вы Выиграли!')
            break
        elif computer.count_barrel < 1:
            print('Компьютер Выиграл!')
            break