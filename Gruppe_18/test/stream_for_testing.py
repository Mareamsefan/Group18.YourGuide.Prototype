import io
import json
# Create a list of dictionaries
data_list = [
    {
        "destination": "Paris",
        "duration": 3,
        "cost": 150,
        "pictureURL": "https://example.com/paris.jpg",
        "language": "French",
        "max_travelers": 20,
        "booked": 5,
        "tour_Id": 0
    },
    {
        "destination": "New York City",
        "duration": 2,
        "cost": 120,
        "pictureURL": "https://example.com/nyc.jpg",
        "language": "English",
        "max_travelers": 15,
        "booked": 8,
        "tour_Id": 1
    },
    {
        "destination": "Tokyo",
        "duration": 4,
        "cost": 200,
        "pictureURL": "https://example.com/tokyo.jpg",
        "language": "Japanese",
        "max_travelers": 25,
        "booked": 10,
        "tour_Id": 2
    },
    {
        "destination": "Rome",
        "duration": 2,
        "cost": 100,
        "pictureURL": "https://example.com/rome.jpg",
        "language": "Italian",
        "max_travelers": 15,
        "booked": 3,
        "tour_Id": 3
    },
    {
        "destination": "London",
        "duration": 3,
        "cost": 180,
        "pictureURL": "https://example.com/london.jpg",
        "language": "English",
        "max_travelers": 18,
        "booked": 6,
        "tour_Id": 4
    },
    {
        "destination": "London",
        "duration": 3,
        "cost": 130,
        "pictureURL": "https://example.com/london.jpg",
        "language": "English",
        "max_travelers": 19,
        "booked": 4,
        "tour_Id": 5
    }
]

# Convert the list to a JSON-formatted string
json_data = json.dumps(data_list)

# Create a StringIO object with the JSON data
stream = io.StringIO(json_data)
