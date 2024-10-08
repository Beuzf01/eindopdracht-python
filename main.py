from inlog import *
from weather import *
from suntimes import *


def main():
    while True:
        account_choice = input("Welcome! Do you:\n"
                           "1. Want to log in?\n"
                           "2. Want to sign up?\n"
                            "3. Want to continue as guest?\n"
                           "your choice: ")

        if account_choice == "1" or "log in" in account_choice:
            login_success = login()
            if login_success:
                break
            else:
                continue

        elif account_choice == "2" or "sign up" in account_choice:
            signup()
            break
        elif account_choice == "3" or "guest" in account_choice:
            guest_signin()
            break
        else:
            print("Sorry, we didnt understand that")
            continue

    while True:
        weather_menu = input("How can we help you today?\n"
                             "1. Display weather forecast in a selected place for up to 5 days\n"
                             "2. Display sunrise and sunset times of the current day in a selected place\n"
                             "3. Close the application\n"
                             "choice: ")
        if weather_menu == "1":
            city, cnt = usrinput()
            loc_status, location_data = locationfetch(city)
            lat, lon = locationprocessing(loc_status, location_data)
            if lat and lon:
                weather_status, location_weather = weatherfetch(lat, lon)
                weather_data = weatherprocessing(weather_status, location_weather, cnt, city)


        elif weather_menu == "2":
            print("_" * 40)
            sun_city = input("which city would you like to know the sunrise and sunset of? ")
            sun_lat, sun_lon = sun_locationfetch(sun_city)
            if sun_lat and sun_lon:
                sun_data = suntimes_fetch(sun_lat, sun_lon)
            if sun_data:
                print("_" * 40)
                sunprocessing(sun_data)
            print("_" * 40)
        elif weather_menu == "3":
            print("_" * 40)
            print("have a great day!")
            break
        else:
            print("We didnt quite understand, try again")
            continue
        again = input("would you like to do something else? (y/n) ").strip()
        if again.upper() == "Y":
            print("_" * 40)
            continue
        if again.upper() == "N":
            print("_" * 40)
            print("have a nice day!")
            print("_" * 40)
            break
        else:
            print("_" * 40)
            print("invalid input")
            print("_" * 40)


if __name__ == '__main__':
    main()