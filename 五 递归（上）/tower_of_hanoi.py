"""汉诺塔"""


def move_disk(disk, from_pole, to_pole):
    print(f'Moving disk[{disk}] from {from_pole} to {to_pole}')


def move_tower(height, from_pole, with_pole, to_pole):
    if height >= 1:
        move_tower(height-1, from_pole, to_pole, with_pole)
        move_disk(height, from_pole, to_pole)
        move_tower(height-1, with_pole, from_pole, to_pole)


move_tower(3, '#1', '#2', '#3')
