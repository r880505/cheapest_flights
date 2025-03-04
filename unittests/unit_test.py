import unittest
from cheapest_flights import find_cheapest_flight

class TestFindCheapestFlight(unittest.TestCase):
    def setUp(self):
        """Setup sample flight data for testing"""
        self.flights = [
            {"from": 0, "to": 1, "price": 100},
            {"from": 1, "to": 2, "price": 150},
            {"from": 0, "to": 2, "price": 300}
        ]

    def test_direct_flight(self):
        """Test when a direct flight exists"""
        cost, route = find_cheapest_flight(self.flights, 0, 2, 1)
        self.assertEqual(cost, 250)
        self.assertEqual(route, "0 - 100 -> 1 - 150 -> 2")

    def test_no_flight_available(self):
        """Test when no flights exist"""
        empty_flights = []
        cost, route = find_cheapest_flight(empty_flights, 0, 2, 1)
        self.assertEqual(cost, -1)
        self.assertEqual(route, "No valid route found")

    def test_no_valid_path_due_to_stop_limit(self):
        """Test when a path exists but exceeds stop limit"""
        cost, route = find_cheapest_flight(self.flights, 0, 2, 0)  # No stops allowed
        self.assertEqual(cost, 300)  # Direct flight is the only option
        self.assertEqual(route, "0 - 300 -> 2")

    def test_single_city_trivial_case(self):
        """Test when source and destination are the same"""
        cost, route = find_cheapest_flight(self.flights, 1, 1, 1)
        self.assertEqual(cost, 0)
        self.assertEqual(route, "1")

    def test_cheapest_path_with_multiple_stops(self):
        """Test when multiple routes exist, ensuring the cheapest is chosen"""
        flights = [
            {"from": 0, "to": 1, "price": 100},
            {"from": 1, "to": 2, "price": 200},
            {"from": 0, "to": 2, "price": 500},
            {"from": 1, "to": 3, "price": 50},
            {"from": 3, "to": 2, "price": 50}
        ]
        cost, route = find_cheapest_flight(flights, 0, 2, 2)
        self.assertEqual(cost, 200)
        self.assertEqual(route, "0 - 100 -> 1 - 50 -> 3 - 50 -> 2")

if __name__ == "__main__":
    unittest.main()
