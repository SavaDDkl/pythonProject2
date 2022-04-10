import random

class Fighter:
    def __init__(self, name ='Неизвестно' ,health = 20 , armour = 10,damage = 5):
        self.name = name
        self.health = health
        self.armour = armour
        self.damage = damage


    def __str__(self):
        return f'👨Имя:{self.name}\n ♡Здоровье:{self.health}\n ⛨Броня:{self.armour}\n🗡Урон:{self.damage}'

    def take_damage(self, damage):
        final_damage = max(0 , damage - random.randint(0 , self.armour))
        self.health-=min(self.health, final_damage)
        return final_damage

    def attack(self, enemy):
        final_damage = enemy.take_damage(self.damage)
        print(f'{self.name} атаковал {enemy.name} и нанес {self.damage} урона . У {enemy.name} осталось {enemy.health} здоровья.')
        pass


player1 = Fighter()
print('- Игрок 1:')
print(player1)


player2 = Fighter(name ='Дима' ,health = 20 , armour = 5,damage = 8)
print('\n - Игрок 2:')
print(player2)


player3 = Fighter(name ='Бари' ,health = 10 , armour = 15,damage = 10)
print('\n - Игрок 3:')
print(player3)


player4 = Fighter(name ='Лада' ,health = 30 , armour = 0,damage = 12)
print('\n - Игрок 4:')
print(player4)


rounds = 1
players_alive = [player1 ,player2 ,player3 ,player4]
while len(players_alive) > 1:
    print(f'===РАУНД{rounds}===')
    for player in players_alive:
        enemy = player
        while enemy == player:
            enemy = random.choice(players_alive)
        player.attack(enemy)

    for player in players_alive:
        if player.health <= 0:
            players_alive.remove(player)

    rounds += 1
    if rounds > 40:
        break
