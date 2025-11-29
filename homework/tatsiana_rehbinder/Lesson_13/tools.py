from datetime import datetime, timedelta


def add_week(dt):
    return dt + timedelta(weeks=1)


def get_weekday(dt):
    return dt.strftime("%A")


def days_ago(dt):
    return (datetime.now() - dt).days


actions = {
    "1": add_week,
    "2": get_weekday,
    "3": days_ago,
}

file_path = "C:/Users/USER/svetlika/homework/eugene_okulik/hw_13/data.txt"

with open(file_path, encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        if not line:
            continue

        number, rest = line.split(".", 1)
        dt_str, _ = rest.split(" - ", 1)

        dt = datetime.fromisoformat(dt_str.strip())

        result = actions[number](dt)

        print(result)
