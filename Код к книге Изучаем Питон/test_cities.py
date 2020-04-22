import unittest
from city_functions import city_country


class NamesTestCase(unittest.TestCase):
    # Тесты для "city_country"

    def test_city_country(self):
        # Имена вида 'Santiago Chile Earth' работают правильно?
        city_and_country = city_country('santiago', 'chile')
        self.assertEqual(city_and_country, 'Santiago, Chile')

    def test_city_country_population(self):
        city_and_country = city_country('santiago', 'chile', 'population=5000000')
        self.assertEqual(city_and_country, 'Santiago, Chile, Population=5000000')


if __name__ == '__main__':
    unittest.main()
