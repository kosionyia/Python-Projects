from src.storage import load_parcels, save_parcels
from src.index import create_indexes, add_to_indexes, remove_from_indexes, update_indexes
from src.cache import get_cache, add_to_cache, clear_cache
from src.auth import login

def show_parcel(parcel):
    print(f" {parcel['tracking_code']} | {parcel['sender']} -> {parcel['receiver']}")
    print(f" {parcel['origin']} -> {parcel['destination']} | {parcel['status']} | {parcel['weight_kg']} kg | shipped {parcel['date_shipped']}")

def main():
    parcels = load_parcels()
    tracking_index, city_index = create_indexes(parcels)

    print("==============================================")
    print(" SWIFT ARROW COURIERS — TRACKING WINDOW")
    print("==============================================")

    user = login()
    if user is None:
        return

    print(f"\n200 — Welcome, {user['name']} ({user['position']}).")

    while True:
        print("\n--------- WINDOW MENU ---------")
        print("1. GET parcel <code>")
        print("2. GET parcels to <city>")
        print("3. POST parcel")
        print("4. PUT parcel <code>")
        print("5. DELETE parcel <code>")
        print("6. Close the window")
        print("-------------------------------")

        choice = input("\nEnter choice: ").strip()

        if choice == "1":
            code = input("Tracking code: ").strip()
            if code in get_cache(code):
                print("\n200 — Found (from the tray)")
                show_parcel(get_cache(code))
                continue

            if code not in tracking_index:
                print(f"\n404 — There is no parcel {code}.")
                continue

            parcel = parcels[tracking_index[code]]
            print("\n200 — Found")
            show_parcel(parcel)
            add_to_cache(code, parcel)

        elif choice == "2":
            city = input("Destination city: ").strip()

            if city in get_cache(city):
                results = get_cache(city)
                print(f"\n200 — {len(results)} parcels found (from the tray)")
                for parcel in results:
                    print(f" {parcel['tracking_code']} | {parcel['sender']} -> {parcel['receiver']} | {parcel['status']}")
                continue

            if city not in city_index:
                print(f"\n404 — No parcels found for {city}.")
                continue

            results = [parcels[i] for i in city_index[city]]
            print(f"\n200 — {len(results)} parcels found")
            for parcel in results:
                print(f" {parcel['tracking_code']} | {parcel['sender']} -> {parcel['receiver']} | {parcel['status']}")
            add_to_cache(city, results)

        elif choice == "3":
            print("Enter the new parcel details.")
            parcel = {
                "tracking_code": input("Tracking code: ").strip(),
                "sender": input("Sender: ").strip(),
                "receiver": input("Receiver: ").strip(),
                "origin": input("Origin: ").strip(),
                "destination": input("Destination: ").strip(),
                "status": input("Status: ").strip(),
                "weight_kg": float(input("Weight (kg): ")),
                "date_shipped": input("Date shipped: ").strip()
            }

            if parcel["tracking_code"] in tracking_index:
                print("400 — That tracking code already exists.")
                continue

            parcels.append(parcel)
            add_to_indexes(parcel, len(parcels) - 1, tracking_index, city_index)
            save_parcels(parcels)
            clear_cache()
            print(f"\n201 — Parcel {parcel['tracking_code']} registered.")

        elif choice == "4":
            code = input("Tracking code to update: ").strip()

            if code not in tracking_index:
                print(f"\n404 — There is no parcel {code}.")
                continue

            position = tracking_index[code]
            old_parcel = parcels[position]
            new_status = input("New status: ").strip()

            old_city = old_parcel["destination"]
            old_parcel["status"] = new_status

            update_indexes(old_parcel, position, old_city, city_index)
            save_parcels(parcels)
            clear_cache()
            print(f"\n200 — Parcel {code} updated.")

        elif choice == "5":
            code = input("Tracking code to delete: ").strip()

            if user["position"] != "Station Master":
                print("\n403 — Clerks may not delete parcels.")
                continue

            if code not in tracking_index:
                print(f"\n404 — There is no parcel {code}.")
                continue

            position = tracking_index[code]
            parcel = parcels[position]
            parcels.pop(position)

            tracking_index, city_index = create_indexes(parcels)
            save_parcels(parcels)
            clear_cache()
            print(f"\n200 — Parcel {code} deleted.")

        elif choice == "6":
            print("\n200 — Window closed.")
            break

        else:
            print("\n400 — I cannot read that choice.")

if __name__ == "__main__":
    main()
