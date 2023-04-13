import numpy as np
import matplotlib.pyplot as plt
import random

def create_one_sprite():
    chance_of_one = 0.5
    left = np.random.choice([0, 1], size=(5, 3), p=[1 - chance_of_one, chance_of_one])
    right = np.fliplr(left)
    right = right[:, 1:]
    sprite = np.concatenate((left, right), axis=1)
    return sprite


def create_sprites(n):
    row_size = 12 # 8 sprites per row
    row_count = n // row_size + 1
    sprites = np.zeros((row_count * 5 + 2 * (row_count - 1), row_size * 5 + 2 * (row_size - 1)))
    for i in range(n):
        sprite = create_one_sprite()
        x = (i % row_size) * 7
        y = (i // row_size) * 7
        sprites[y:y + 5, x:x + 5] = sprite
    return sprites


def create_one_colorful_sprite(layers):
    sprite = [[[0, 0, 0] for i in range(5)] for j in range(5)]
    for i in range(layers):
        chance_of_one = 0.25
        color = np.random.randint(0, 255, size=3)
        for i in range(5):
            for j in range(3):
                if np.random.random() < chance_of_one:
                    sprite[i][j] = color
        for i in range(5):
            for j in range(3):
                sprite[i][4 - j] = sprite[i][j]   
    return sprite


def create_colorful_sprites(n):
    sprite_size = 5
    blank_size = 5
    row_size = 12 # 8 sprites per row
    row_count = n // row_size + 1
    sprites = np.zeros((row_count * sprite_size + blank_size * (row_count - 1), row_size * sprite_size + blank_size * (row_size - 1), 3))
    for i in range(n):
        sprite = create_one_colorful_sprite(3)
        x = (i % row_size) * (sprite_size + blank_size)
        y = (i // row_size) * (sprite_size + blank_size)
        sprites[y:y + sprite_size, x:x + sprite_size] = sprite
    sprites = sprites.astype(int)
    return sprites


# sprites = create_one_sprite()
# sprites = create_sprites(80)
# sprites = create_one_colorful_sprite(3)
sprites = create_colorful_sprites(80)

plt.imshow(sprites, cmap='gray')
plt.show()
