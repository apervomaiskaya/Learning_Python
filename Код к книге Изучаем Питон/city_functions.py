def city_country(city, country, population=''):
    # Печатает город и страну
    if population:
        city_and_country = city + ', ' + country + ', ' + population
    else:
        city_and_country = city + ', ' + country
    return city_and_country.title()




