"""
Temperature Monitor and Alarm Checker
ND1 Mechatronics Engineering Mini Project

Collects five temperature readings in Celsius, calculates summary
statistics, and reports readings against configurable warning levels.
"""

WARNING_LIMIT = 50.0
ELEVATED_LIMIT = 35.0
NUMBER_OF_READINGS = 5


def get_temperature_readings():
    """Collect five valid numeric temperature readings."""
    temperatures = []

    print("TEMPERATURE MONITORING SYSTEM")
    print("-----------------------------")

    for index in range(NUMBER_OF_READINGS):
        while True:
            try:
                temperature = float(
                    input(f"Enter temperature {index + 1} in Celsius: ")
                )
                temperatures.append(temperature)
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

    return temperatures


def analyze_temperatures(temperatures):
    """Display statistics and check each reading against alarm levels."""
    highest = max(temperatures)
    lowest = min(temperatures)
    average = sum(temperatures) / len(temperatures)

    print("\nTEMPERATURE REPORT")
    print("------------------")
    print(f"Highest temperature: {highest:.1f} °C")
    print(f"Lowest temperature:  {lowest:.1f} °C")
    print(f"Average temperature: {average:.2f} °C")

    print("\nALARM STATUS")
    print("------------")

    alarm_count = 0

    for temperature in temperatures:
        if temperature >= WARNING_LIMIT:
            print(f"{temperature:.1f} °C - HIGH TEMPERATURE ALERT!")
            alarm_count += 1
        elif temperature >= ELEVATED_LIMIT:
            print(f"{temperature:.1f} °C - Temperature is elevated.")
        else:
            print(f"{temperature:.1f} °C - Normal temperature.")

    print(f"\nTotal high-temperature alarms: {alarm_count}")


def main():
    """Run the temperature monitoring application."""
    readings = get_temperature_readings()
    analyze_temperatures(readings)
    print("\nTemperature monitoring completed.")


if __name__ == "__main__":
    main()
