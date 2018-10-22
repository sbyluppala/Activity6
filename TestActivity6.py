# import statements

import unittest
import requests
import act6_2


class Current_Conditions_activity(unittest.TestCase):
	api_start = 'https://api.openweathermap.org/data/2.5/weather?q='

	api_key = '&appid=19e9a25146ef7516044eb1d272dc6ec4'

	city = 'omaha'

	country = 'us'

	url = api_start + city + ',' + country + api_key

	json_data = requests.get(url).json()

	def test_conditions_for_exceptions(self):
		result = act6_2.check_current_conditions(self.json_data)
		expected = 'Please enter valid input'
		self.assertMultiLineEqual(expected, result)

	def test_current_temperature_for_exceptions(self):
		result = act6_2.current_temperature(self.json_data)
		expected = 'Please enter valid input'
		self.assertMultiLineEqual(expected, result)

	def test_current_humidity_for_exceptions(self):
		result = act6_2.current_humidity(self.json_data)
		expected = 'Please enter valid input'
		self.assertMultiLineEqual(expected, result)

	def test_low_temperature_for_exceptions(self):
		result = act6_2.low_temperature(self.json_data)
		expected = 'Please enter valid input'
		self.assertMultiLineEqual(expected, result)

	def test_high_temperature_for_exceptions(self):
		result = act6_2.high_temperature(self.json_data)
		expected = 'Please enter valid input'
		self.assertMultiLineEqual(expected, result)


if __name__ == '__main__':
	unittest.main()
