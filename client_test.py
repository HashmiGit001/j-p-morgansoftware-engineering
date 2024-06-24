import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        """Test getDataPoint to return correct tuple"""
        quotes = [
            {'stock': 'ABC', 'top_bid': {'price': 120}, 'top_ask': {'price': 121}},
            {'stock': 'DEF', 'top_bid': {'price': 95}, 'top_ask': {'price': 96}},
        ]
        expected_results = [
            ('ABC', 120, 121, 120.5),
            ('DEF', 95, 96, 95.5)
        ]

        for quote, expected in zip(quotes, expected_results):
            self.assertEqual(getDataPoint(quote), expected)

    def test_getDataPoint_bidGreaterThanAsk(self):
        """Test getDataPoint when bid is greater than ask (though unrealistic in a real scenario)"""
        quotes = [
            {'stock': 'ABC', 'top_bid': {'price': 121}, 'top_ask': {'price': 120}},
            {'stock': 'DEF', 'top_bid': {'price': 96}, 'top_ask': {'price': 95}},
        ]
        expected_results = [
            ('ABC', 121, 120, 120.5),
            ('DEF', 96, 95, 95.5)
        ]

        for quote, expected in zip(quotes, expected_results):
            self.assertEqual(getDataPoint(quote), expected)
    def test_getRatio_normal(self):
        """Test getRatio to return correct ratio"""
        self.assertEqual(getRatio(120.5, 95.5), 120.5 / 95.5)
        self.assertEqual(getRatio(95.5, 120.5), 95.5 / 120.5)

    def test_getRatio_divisionByZero(self):
        """Test getRatio when dividing by zero"""
        self.assertIsNone(getRatio(120.5, 0))
        self.assertEqual(getRatio(0, 95.5), 0)

if __name__ == '__main__':
    unittest.main()
