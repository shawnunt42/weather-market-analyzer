from weather_service import get_lat_lon, get_hourly_forecast, get_high_low_for_date, get_target_date
from pricing import choose_best_bet
from gemini_explainer import make_prediction

def main():
    print("=== Weather Prediction Tool ===\n")

    state = input("State: ").strip()
    city = input("City: ").strip()

    print("\nSelect day:")
    print("1. Today")
    print("2. Tomorrow")
    print("3. Custom")

    day_choice = input("Choice: ").strip()

    custom_date = None
    if day_choice == "3":
        custom_date = input("Enter custom date (YYYY-MM-DD): ").strip()

    target_date = get_target_date(day_choice, custom_date)

    if target_date is None:
        print("Invalid day choice.")
        return

    print("\nChecking weather forecast...\n")

    lat, lon = get_lat_lon(city, state)

    if lat is None or lon is None:
        print("Could not find that city/state.")
        return

    periods = get_hourly_forecast(lat, lon)
    high_temp, low_temp = get_high_low_for_date(periods, target_date)

    if high_temp is None or low_temp is None:
        print("No forecast data found for that day.")
        return

    bet_info = choose_best_bet(high_temp, low_temp)

    result = make_prediction(
        city,
        state,
        target_date,
        bet_info["high"],
        bet_info["low"],
        bet_info["threshold"]
    )

    print(result)

if __name__ == "__main__":
    main()