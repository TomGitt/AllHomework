from decimal import Decimal

import math

pi = math.pi

input_radius = float(input('Введіть радіус кулі>>>'))
radius_cubed = input_radius ** 3
ball_volume = 4 / 3 * pi * radius_cubed
ball_volume_final = Decimal(str(ball_volume)).quantize(Decimal('0.01'))

print(ball_volume_final)
