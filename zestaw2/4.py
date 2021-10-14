def funkcja(temp: int, temperature_type):
    acc_values = ['farenheit', 'rankine', 'kelvin']
    if temperature_type not in acc_values:
        return 'bledna wartosc'
    else:
        if temperature_type in acc_values[0]:
            return temp*1.8 + 32
        elif temperature_type in acc_values[1]:
            return (temp + 273.15) * 9/5
        elif temperature_type in acc_values[2]:
            return temp + 273.15

print(funkcja(233, 'kelvin'))