Capital_city = {
    'Nepal': 'Kathmandu',
    'Ukraine': 'Kyiv',
    'France': 'Paris',
    'Denmark': 'Copenhagen',
    'China': 'Beijing',
    'Canada': 'Ottawa',
    'Italy': 'Rome',
    'Australia': 'Kanbera'
}

sorted_countries = sorted(Capital_city.items(), reverse=True)

for country, capital in sorted_countries:
    print(f"{country} - {capital}")
