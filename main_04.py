day_in_week = input('Upisite naziv dana u tjednu (hr naziv): ')

#region IF nacin
# if day_in_week.lower() == 'ponedjeljak':
#     print(f'{day_in_week.capitalize()} je radni dan.')
# elif day_in_week.lower() == 'utorak':
#     print(f'{day_in_week.capitalize()} je radni dan.')
# elif day_in_week.lower() == 'srijeda':
#     print(f'{day_in_week.capitalize()} je radni dan.')
# elif day_in_week.lower() == 'četvrtak':
#     print(f'{day_in_week.capitalize()} je radni dan.')
# elif day_in_week.lower() == 'petak':
#     print(f'{day_in_week.capitalize()} je radni dan.')
# elif day_in_week.lower() == 'subota':
#     print(f'{day_in_week.capitalize()} je vikend.')
# elif day_in_week.lower() == 'nedjelja':
#     print(f'{day_in_week.capitalize()} je vikend.')
# else:
#     print(f'Upisali ste krivi naziv dana u tjednu.')
#endregion


# Drugi nacin za ovako dugacke IF uvjete je match / case
#   -> u drugim programskim jezicima koristi se naziv switch / case
#   match / case je ukljucen u Python tek od verzije 3.10,
#   ako koristite stariju verziju onda ovo NECE raditi!!!


#region MATCH

match day_in_week.lower():
    case 'ponedjeljak':
        print(f'{day_in_week.capitalize()} je radni dan.')
    case 'utorak':
        print(f'{day_in_week.capitalize()} je radni dan.')
    case 'srijeda':
        print(f'{day_in_week.capitalize()} je radni dan.')
    case 'četvrtak':
        print(f'{day_in_week.capitalize()} je radni dan.')
    case 'petak':
        print(f'{day_in_week.capitalize()} je radni dan.')
    case 'subota':
        print(f'{day_in_week.capitalize()} je vikend.')
    case 'nedjelja':
        print(f'{day_in_week.capitalize()} je vikend.')
    case _:
        print(f'Upisali ste krivi naziv dana u tjednu.')

#endregion