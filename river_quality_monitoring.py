from datetime import datetime


# ============================================================
# BTPR3203 Python for Data Science Assignment
# River Quality Monitoring System
# ============================================================


# ============================================================
# PART 1: RIVER STATION MANAGEMENT
# ============================================================

river_stations = {
    "Sungai Klang KL": {
        "state": "Selangor",
        "wqi": 68.3,
        "status": ""
    },

    "Sungai Muar": {
        "state": "Johor",
        "wqi": 54.1,
        "status": ""
    },

    "Sungai Perak": {
        "state": "Perak",
        "wqi": 84.6,
        "status": ""
    },

    "Sungai Pahang": {
        "state": "Pahang",
        "wqi": 45.8,
        "status": ""
    }
}


# ============================================================
# PART 2: READING LOG
# ============================================================
reading_log = []


def classify_wqi(wqi):
    """
    Convert a WQI value into its class and pollution status.
    """

    if wqi > 92.7:
        return "Class I - Clean"

    elif wqi > 76.5:
        return "Class II - Slightly Polluted"

    elif wqi > 51.9:
        return "Class III - Moderately Polluted"

    elif wqi > 31.0:
        return "Class IV - Polluted"

    else:
        return "Class V - Heavily Polluted"


def get_class_label(wqi):

    if wqi > 92.7:
        return "Class I"

    elif wqi > 76.5:
        return "Class II"

    elif wqi > 51.9:
        return "Class III"

    elif wqi > 31.0:
        return "Class IV"

    else:
        return "Class V"


def classify_all_stations(show_message=True):

    for station_data in river_stations.values():
        station_data["status"] = classify_wqi(
            station_data["wqi"]
        )

    if show_message:
        print("\nAll river stations have been classified.")


def get_valid_station_name(prompt="Enter station name: "):
    """
    Get a non-empty station name.
    """

    while True:
        station_name = input(prompt).strip()

        if station_name == "":
            print("Error: Station name cannot be empty.")
        else:
            return station_name


def get_valid_state():
  

    while True:
        state = input("Enter state: ").strip()

        if state == "":
            print("Error: State cannot be empty.")
        else:
            return state


def get_valid_wqi(prompt="Enter WQI value (0-100): "):
    

    while True:
        try:
            wqi = float(input(prompt))

            if wqi < 0 or wqi > 100:
                print(
                    "Error: WQI value must be between 0 and 100."
                )
            else:
                return wqi

        except ValueError:
            print(
                "Error: Please enter a valid numeric WQI value."
            )


# ============================================================
# PART 1 FUNCTIONS
# ============================================================

def display_stations():
    """
    Display all monitoring stations in a formatted table.
    """

    if not river_stations:
        print("\nNo river stations are available.")
        return

    print("\n" + "=" * 100)

    print(
        f"{'Station Name':<25}"
        f"{'State':<18}"
        f"{'WQI':<12}"
        f"{'Status':<40}"
    )

    print("=" * 100)

    for station_name, station_data in river_stations.items():
        print(
            f"{station_name:<25}"
            f"{station_data['state']:<18}"
            f"{station_data['wqi']:<12.2f}"
            f"{station_data['status']:<40}"
        )

    print("=" * 100)


def add_or_update_station():
    """
    Add a new station or update an existing station.
    """

    print("\n===== Add / Update River Station =====")

    station_name = get_valid_station_name()
    state = get_valid_state()
    wqi = get_valid_wqi()

    if station_name in river_stations:
        river_stations[station_name]["state"] = state
        river_stations[station_name]["wqi"] = wqi

        print(
            f"Station {station_name} updated with "
            f"new WQI: {wqi:.2f}."
        )

    else:
        river_stations[station_name] = {
            "state": state,
            "wqi": wqi,
            "status": ""
        }

        print(f"New station {station_name} added.")

    # Refresh all station classifications
    classify_all_stations(show_message=False)

    display_stations()


# ============================================================
# PART 2 FUNCTIONS
# ============================================================

def log_monitoring_reading():
    """
    Log a monitoring reading for an existing station.
    """

    print("\n===== Log Monitoring Reading =====")

    station_name = input("Enter station name: ").strip()

    if station_name == "":
        print("Error: Station name cannot be empty.")
        return

    if station_name not in river_stations:
        print(f"Error: Station {station_name} not found.")
        return

    try:
        wqi = float(
            input("Enter WQI reading (0-100): ")
        )

    except ValueError:
        print(
            "Error: Please enter a valid numeric WQI value."
        )
        return

    if wqi < 0 or wqi > 100:
        print(
            "Error: WQI value must be between 0 and 100."
        )
        return

    # Store the reading as a tuple
    reading = (
        datetime.now(),
        station_name,
        wqi
    )

    reading_log.append(reading)

    # Update the latest WQI and status
    river_stations[station_name]["wqi"] = wqi
    river_stations[station_name]["status"] = classify_wqi(wqi)

    print(
        f"Reading logged successfully for {station_name}."
    )

    print(f"New WQI: {wqi:.2f}")

    print(
        f"Current status: "
        f"{river_stations[station_name]['status']}"
    )


def check_alerts():
    """
    Print alerts for rivers with WQI below 51.9.
    """

    print("\n===== River Quality Alerts =====")

    alert_found = False

    for station_name, station_data in river_stations.items():

        if station_data["wqi"] < 51.9:
            alert_found = True

            print(
                f"[!] ALERT: {station_name} in "
                f"{station_data['state']} is "
                f"{station_data['status']} "
                f"(WQI: {station_data['wqi']:.2f})."
            )

    if not alert_found:
        print(
            "All monitored rivers are within "
            "acceptable quality levels."
        )


def display_reading_log():

    print("\n===== Monitoring Reading History =====")

    if not reading_log:
        print("No readings have been logged yet.")
        return

    print("\n" + "=" * 75)

    print(
        f"{'Timestamp':<25}"
        f"{'Station Name':<35}"
        f"{'WQI':<10}"
    )

    print("=" * 75)

    for timestamp, station_name, wqi in reading_log:
        formatted_time = timestamp.strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        print(
            f"{formatted_time:<25}"
            f"{station_name:<35}"
            f"{wqi:<10.2f}"
        )

    print("=" * 75)


def part_2_menu():


    while True:
        print("\n======= Part 2: Reading Log =======")
        print("1. Log Monitoring Reading")
        print("2. Check River Alerts")
        print("3. Display Reading History")
        print("0. Return to Main Menu")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            log_monitoring_reading()

            # Automatically show alerts after a reading
            check_alerts()

        elif choice == "2":
            check_alerts()

        elif choice == "3":
            display_reading_log()

        elif choice == "0":
            break

        else:
            print(
                "Error: Invalid choice. Please enter 0 to 3."
            )


# ============================================================
# PART 3: RIVERSTATION CLASS
# ============================================================

class RiverStation:
  

    def __init__(self, name, state, wqi):
        self.name = name
        self.state = state
        self.wqi = wqi

    def determine_class(self):
        """
        Determine and return the correct WQI classification.
        """

        return classify_wqi(self.wqi)

    def display_summary(self):
        """
        Print a one-line summary of the station.
        """

        print(
            f"{self.name} | "
            f"{self.state} | "
            f"WQI: {self.wqi:.2f} | "
            f"{self.determine_class()}"
        )


def demonstrate_river_station_class():

    print("\n===== RiverStation Object Summaries =====")

    station_names = list(river_stations.keys())

    if len(station_names) < 2:
        print(
            "At least two river stations are required."
        )
        return

    first_station_name = station_names[0]
    second_station_name = station_names[1]

    first_station_data = river_stations[
        first_station_name
    ]

    second_station_data = river_stations[
        second_station_name
    ]

    station1 = RiverStation(
        first_station_name,
        first_station_data["state"],
        first_station_data["wqi"]
    )

    station2 = RiverStation(
        second_station_name,
        second_station_data["state"],
        second_station_data["wqi"]
    )

    station1.display_summary()
    station2.display_summary()


# ============================================================
# PART 3: AVERAGE WQI BY STATE
# ============================================================

def calculate_average_wqi_by_state():
    """
    Group stations by state and calculate average WQI.
    Results are sorted from highest to lowest.
    """

    print("\n===== Average WQI by State =====")

    if not river_stations:
        print("No river station data is available.")
        return

    state_data = {}

    for station_data in river_stations.values():
        state = station_data["state"]
        wqi = station_data["wqi"]

        if state not in state_data:
            state_data[state] = []

        state_data[state].append(wqi)

    state_averages = {}

    for state, wqi_values in state_data.items():
        average_wqi = (
            sum(wqi_values) / len(wqi_values)
        )

        state_averages[state] = average_wqi

    sorted_states = sorted(
        state_averages.items(),
        key=lambda item: item[1],
        reverse=True
    )

    print("\n" + "=" * 50)

    print(
        f"{'State':<30}"
        f"{'Average WQI':<20}"
    )

    print("=" * 50)

    for state, average_wqi in sorted_states:
        print(
            f"{state:<30}"
            f"{average_wqi:<20.2f}"
        )

    print("=" * 50)


# ============================================================
# PART 3: TREND ANALYSIS
# ============================================================

def analyse_reading_trends():

    print("\n===== WQI Trend Analysis =====")

    station_readings = {}

    # Group reading log entries by station
    for timestamp, station_name, wqi in reading_log:

        if station_name not in station_readings:
            station_readings[station_name] = []

        station_readings[station_name].append(
            (timestamp, wqi)
        )

    valid_trends = {}

    for station_name, readings in station_readings.items():

        # At least two readings are required
        if len(readings) >= 2:
            readings.sort(
                key=lambda reading: reading[0]
            )

            first_wqi = readings[0][1]
            latest_wqi = readings[-1][1]

            highest_wqi = max(
                reading[1] for reading in readings
            )

            lowest_wqi = min(
                reading[1] for reading in readings
            )

            # Actual change between first and latest reading
            change = latest_wqi - first_wqi

            # Requirement: highest WQI minus lowest WQI
            improvement_range = (
                highest_wqi - lowest_wqi
            )

            valid_trends[station_name] = {
                "first": first_wqi,
                "latest": latest_wqi,
                "highest": highest_wqi,
                "lowest": lowest_wqi,
                "change": change,
                "range": improvement_range
            }

    if not valid_trends:
        print(
            "Insufficient data for trend analysis. "
            "Please log more readings."
        )
        return

    print("\n" + "=" * 100)

    print(
        f"{'Station':<25}"
        f"{'First':<12}"
        f"{'Latest':<12}"
        f"{'Lowest':<12}"
        f"{'Highest':<12}"
        f"{'Change':<12}"
        f"{'Range':<12}"
    )

    print("=" * 100)

    for station_name, trend in valid_trends.items():
        print(
            f"{station_name:<25}"
            f"{trend['first']:<12.2f}"
            f"{trend['latest']:<12.2f}"
            f"{trend['lowest']:<12.2f}"
            f"{trend['highest']:<12.2f}"
            f"{trend['change']:<+12.2f}"
            f"{trend['range']:<12.2f}"
        )

    print("=" * 100)

    greatest_improvement_station = max(
        valid_trends,
        key=lambda station: (
            valid_trends[station]["change"]
        )
    )

    least_improvement_station = min(
        valid_trends,
        key=lambda station: (
            valid_trends[station]["change"]
        )
    )

    greatest_change = valid_trends[
        greatest_improvement_station
    ]["change"]

    least_change = valid_trends[
        least_improvement_station
    ]["change"]

    print(
        f"\nGreatest WQI improvement: "
        f"{greatest_improvement_station} "
        f"({greatest_change:+.2f})"
    )

    if least_change < 0:
        print(
            f"Greatest WQI decline: "
            f"{least_improvement_station} "
            f"({least_change:+.2f})"
        )
    else:
        print(
            f"Least WQI improvement: "
            f"{least_improvement_station} "
            f"({least_change:+.2f})"
        )


# ============================================================
# PART 3: WQI CLASS SUMMARY
# ============================================================

def display_class_summary():

    print("\n===== WQI Class Summary =====")

    class_counts = {
        "Class I": 0,
        "Class II": 0,
        "Class III": 0,
        "Class IV": 0,
        "Class V": 0
    }

    for station_data in river_stations.values():
        class_label = get_class_label(
            station_data["wqi"]
        )

        class_counts[class_label] += 1

    print("\n" + "=" * 45)

    print(
        f"{'WQI Class':<20}"
        f"{'Number of Stations':<25}"
    )

    print("=" * 45)

    for class_label, number_of_stations in class_counts.items():
        print(
            f"{class_label:<20}"
            f"{number_of_stations:<25}"
        )

    print("=" * 45)


def run_all_trend_analysis():
    demonstrate_river_station_class()
    calculate_average_wqi_by_state()
    analyse_reading_trends()
    display_class_summary()


def part_3_menu():

    while True:
        print("\n======= Part 3: Trend Analysis =======")
        print("1. Display RiverStation Objects")
        print("2. Display Average WQI by State")
        print("3. Analyse Reading Trends")
        print("4. Display WQI Class Summary")
        print("5. Run All Part 3 Functions")
        print("0. Return to Main Menu")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            demonstrate_river_station_class()

        elif choice == "2":
            calculate_average_wqi_by_state()

        elif choice == "3":
            analyse_reading_trends()

        elif choice == "4":
            display_class_summary()

        elif choice == "5":
            run_all_trend_analysis()

        elif choice == "0":
            break

        else:
            print(
                "Error: Invalid choice. Please enter 0 to 5."
            )


# ============================================================
# PART 4: FILE HANDLING AND EXCEPTION HANDLING
# ============================================================

DEFAULT_FILE_NAME = "river_stations.txt"


def get_file_name():

    file_name = input(
        f"Enter file name [{DEFAULT_FILE_NAME}]: "
    ).strip()

    if file_name == "":
        return DEFAULT_FILE_NAME

    return file_name


def export_river_stations():

    print("\n===== Export River Station Report =====")

    file_name = get_file_name()

    try:
        # Refresh statuses before exporting
        classify_all_stations(show_message=False)

        with open(
            file_name,
            "w",
            encoding="utf-8"
        ) as file:

            for station_name, station_data in river_stations.items():
                file.write(
                    f"{station_name}, "
                    f"{station_data['state']}, "
                    f"{station_data['wqi']}, "
                    f"{station_data['status']}\n"
                )

        print(
            f"River station report saved successfully "
            f"to '{file_name}'."
        )

    except PermissionError:
        print(
            f"Error: Permission denied. "
            f"Unable to write to '{file_name}'."
        )

    except OSError as error:
        print(
            f"Error: The file could not be saved. "
            f"Details: {error}"
        )


def load_river_stations():
    """
    Load river station data from a plain text file.
    """

    print("\n===== Load River Station Data =====")

    file_name = get_file_name()

    loaded_stations = {}

    try:
        with open(
            file_name,
            "r",
            encoding="utf-8"
        ) as file:

            line_number = 0

            for line in file:
                line_number += 1
                line = line.strip()

                # Skip empty lines
                if line == "":
                    continue

                parts = line.split(",")

                if len(parts) != 4:
                    print(
                        f"Error: Invalid file format "
                        f"on line {line_number}."
                    )
                    return

                station_name = parts[0].strip()
                state = parts[1].strip()
                wqi_text = parts[2].strip()

                if station_name == "":
                    print(
                        f"Error: Station name cannot be empty "
                        f"on line {line_number}."
                    )
                    return

                if state == "":
                    print(
                        f"Error: State cannot be empty "
                        f"on line {line_number}."
                    )
                    return

                # This may raise ValueError
                wqi = float(wqi_text)

                if wqi < 0 or wqi > 100:
                    print(
                        f"Error: WQI value on line "
                        f"{line_number} must be between "
                        f"0 and 100."
                    )
                    return

                loaded_stations[station_name] = {
                    "state": state,
                    "wqi": wqi,
                    "status": ""
                }

        if not loaded_stations:
            print(
                "Error: No valid river station data "
                "was found in the file."
            )
            return

        
        river_stations.clear()
        river_stations.update(loaded_stations)

        # Reclassify all loaded stations
        classify_all_stations(show_message=False)

        print(
            f"River station data loaded successfully "
            f"from '{file_name}'."
        )

        display_stations()

    except FileNotFoundError:
        print(
            f"Error: File '{file_name}' was not found."
        )

    except ValueError:
        print(
            "Error: The file contains a "
            "non-numeric WQI value."
        )

    except PermissionError:
        print(
            f"Error: Permission denied. "
            f"Unable to read '{file_name}'."
        )

    except OSError as error:
        print(
            f"Error: The file could not be read. "
            f"Details: {error}"
        )


def part_4_menu():

    while True:
        print("\n======= Part 4: File Handling =======")
        print("1. Export River Station Report")
        print("2. Load River Station Data")
        print("0. Return to Main Menu")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            export_river_stations()

        elif choice == "2":
            load_river_stations()

        elif choice == "0":
            break

        else:
            print(
                "Error: Invalid choice. "
                "Please enter 0, 1, or 2."
            )


# ============================================================
# MAIN MENU
# ============================================================

def main_menu():

    # Classify stations when the program starts
    classify_all_stations(show_message=False)

    while True:
        print("\n======= Main Menu =======")
        print("1. Classify All Stations")
        print("2. Add / Update Station")
        print("3. Log Monitoring Reading (Part 2)")
        print("4. Trend Analysis (Part 3)")
        print("5. Export Report (Part 4)")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            classify_all_stations()
            display_stations()

        elif choice == "2":
            add_or_update_station()

        elif choice == "3":
            part_2_menu()

        elif choice == "4":
            part_3_menu()

        elif choice == "5":
            part_4_menu()

        elif choice == "0":
            print(
                "\nThank you for using the "
                "River Quality Monitoring System."
            )
            break

        else:
            print(
                "Error: Invalid choice. "
                "Please enter a number from 0 to 5."
            )

if __name__ == "__main__":
    main_menu()
