def cost_to_fill(tank_size, fuel_level, price_per_gallon):
    needed = tank_size - fuel_level;
    price = price_per_gallon * needed;

    return f'${price:.2f}'

print(cost_to_fill(20.00, 0, 4.00))