from datetime import datetime

def solution_station_2(date_string):
    days = {
        0: "月曜日",  # Monday
        1: "火曜日",  # Tuesday
        2: "水曜日",  # Wednesday
        3: "木曜日",  # Thursday
        4: "金曜日",  # Friday
        5: "土曜日",  # Saturday
        6: "日曜日",  # Sunday
    }
    date = datetime.strptime(date_string, "%Y-%m-%d")

    day_of_week = date.weekday()

    return days[day_of_week]
