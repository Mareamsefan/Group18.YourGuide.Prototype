import json
from Gruppe_18_src.Tour import Tour

# shows all avilable tours


def read_tours_from_file_add_to_list(file_name, tour_list):
    with open(file_name, "r") as file:
        items = json.load(file)
        for item in items:
            tour = Tour(item['destination'], item['cost'], item['duration'], item['pictureURL'],
                        item['language'], item['max_travelers'])
            tour_list.append(tour)



def filter_tour_by_location(tour_list, destination):
    return 0


def filter_tour_by_price(tour_list, max_price, min_price):
    return 0
