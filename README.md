# Temperature Monitor and Alarm Checker

**Course/Level:** ND1 Mechatronics Engineering  
**Language:** Python 3  
**Project type:** Mini Project

## 1. Project Overview

The Temperature Monitor and Alarm Checker is a beginner-friendly Python
console application. It collects five temperature readings in degrees
Celsius, calculates the highest, lowest, and average readings, and reports
whether each reading is normal, elevated, or at the high-temperature alarm
level.

## 2. Objectives

- Accept five temperature readings from a user.
- Reject non-numeric input and ask the user to try again.
- Calculate the maximum, minimum, and average temperature.
- Classify each reading using the project's temperature thresholds.
- Count readings that trigger the high-temperature alarm.

## 3. Temperature Thresholds

The program uses these example thresholds:

| Reading | Program message |
|---|---|
| Below 35 °C | Normal temperature |
| 35 °C to below 50 °C | Temperature is elevated |
| 50 °C or above | High temperature alert |

**Important:** These are demonstration values for this programming project,
not certified safety limits. A real machine or process must use limits set
for its sensor, equipment, material, and operating conditions.

## 4. Requirements

- Python 3.8 or later
- A terminal/command prompt, or a Python editor such as IDLE or VS Code

No third-party Python packages are required.

## 5. How to Run

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run:

   ```bash
   python temperature_monitor.py
   ```

   On some systems, use:

   ```bash
   python3 temperature_monitor.py
   ```

4. Enter five numeric temperature readings when prompted.

## 6. Python Concepts Demonstrated

- **Functions:** `get_temperature_readings()`, `analyze_temperatures()`,
  and `main()` organize the program into reusable parts.
- **Loops:** `for` loops collect and inspect readings; a `while` loop repeats
  an input prompt until valid numeric input is entered.
- **Conditional statements:** `if`, `elif`, and `else` classify readings.
- **Data types and conversion:** `float()` converts keyboard input to a
  decimal number.
- **Lists:** readings are stored in a Python list.
- **Exception handling:** `try` and `except ValueError` handle invalid input.
- **Built-in functions:** `max()`, `min()`, `sum()`, and `len()` calculate
  the summary statistics.

## 7. Example

Input readings:

```text
25
32
40
55
45
```

Expected summary:

```text
Highest temperature: 55.0 °C
Lowest temperature:  25.0 °C
Average temperature: 39.40 °C
Total high-temperature alarms: 1
```

## 8. Possible Future Improvements

- Read live data from a temperature sensor.
- Save readings and timestamps to a CSV file.
- Display a temperature trend graph.
- Allow the operator to configure alarm thresholds.
- Add a graphical user interface.

## 9. Project Files

```text
temperature-monitor/
├── temperature_monitor.py
└── README.md
```

## 10. Disclaimer

This is an educational software demonstration. It does not connect to a
physical sensor and must not be used as the only protection or alarm system
for real equipment.
