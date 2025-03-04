import sys
from json_reader import read_json
from cheapest_flights import find_cheapest_flight

if len(sys.argv) < 2:
    print("Usage: python main.py <filename.json>")
    sys.exit(1)
    
json_file = sys.argv[1]

data = read_json(json_file)

cheapest_flights = find_cheapest_flight(data['flights'], data['origin'], data['dest'], data['k'])

if cheapest_flights:
    print(cheapest_flights)
