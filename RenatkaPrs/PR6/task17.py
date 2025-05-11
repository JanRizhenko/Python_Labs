champions = {
    'Brazil': [1958, 2002, 1962, 1970, 1994],
    'England': [1966],
    'Italy': [2006, 1934, 1938, 1982],
    'Spain': [2010],
    'Germany': [2014, 1954, 1974, 1990],
    'France': [2018, 1998],
    'Uruguay': [1930, 1950],
    'Argentina': [1978, 1986, 2022]
}

for country in champions:
    champions[country].sort()

for country, years in champions.items():
    print(f"{country}: {years}")
