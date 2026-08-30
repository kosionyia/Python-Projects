def create_indexes(parcels):
    tracking_index = {}
    city_index = {}

    for position, parcel in enumerate(parcels):
        tracking_index[parcel["tracking_code"]] = position

        city = parcel["destination"]
        if city not in city_index:
            city_index[city] = []

        city_index[city].append(position)

    return tracking_index, city_index

def add_to_indexes(parcel, position, tracking_index, city_index):
    tracking_index[parcel["tracking_code"]] = position

    city = parcel["destination"]
    if city not in city_index:
        city_index[city] = []

    city_index[city].append(position)

def remove_from_indexes(parcel, position, tracking_index, city_index):
    tracking_index.pop(parcel["tracking_code"], None)

    city = parcel["destination"]
    if city in city_index and position in city_index[city]:
        city_index[city].remove(position)

def update_indexes(parcel, position, old_city, city_index):
    if old_city != parcel["destination"]:
        if old_city in city_index and position in city_index[old_city]:
            city_index[old_city].remove(position)

        new_city = parcel["destination"]
        if new_city not in city_index:
            city_index[new_city] = []

        city_index[new_city].append(position)
