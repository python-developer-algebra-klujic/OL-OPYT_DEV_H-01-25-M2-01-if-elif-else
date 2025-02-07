day_in_week = input('Upisite naziv dana u tjednu (hr naziv): ')

if day_in_week.lower() == 'ponedjeljak':
    print(f'{day_in_week.capitalize()} je radni dan.')
elif day_in_week.lower() == 'utorak':
    print(f'{day_in_week.capitalize()} je radni dan.')
elif day_in_week.lower() == 'srijeda':
    print(f'{day_in_week.capitalize()} je radni dan.')
elif day_in_week.lower() == 'četvrtak':
    print(f'{day_in_week.capitalize()} je radni dan.')
elif day_in_week.lower() == 'petak':
    print(f'{day_in_week.capitalize()} je radni dan.')
elif day_in_week.lower() == 'subota':
    print(f'{day_in_week.capitalize()} je vikend.')
elif day_in_week.lower() == 'nedjelja':
    print(f'{day_in_week.capitalize()} je vikend.')
else:
    print(f'Upisali ste krivi naziv dana u tjednu.')
