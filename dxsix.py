from decimal import Decimal

import math

pi = math.pi

INPUT_RADIUS = float(input('Введіть радіус кулі>>>'))
radius = INPUT_RADIUS ** 3
ball_volume = 4 / 3 * pi * radius
ball_volume_final = Decimal(str(ball_volume)).quantize(Decimal('0.01'))

print(ball_volume_final)
