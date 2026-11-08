import sys
from collections import Counter


def parse_log_line(line: str) -> dict:
    date, time, level, message = line.strip().split(maxsplit=3)
    return {"date": date, "time": time, "level": level.upper(), "message": message}


def load_logs(file_path: str) -> list[dict]:
    logs = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            if not line.strip():
                continue
            try:
                logs.append(parse_log_line(line))
            except ValueError:
                continue
    return logs


def filter_logs_by_level(logs: list[dict], level: str) -> list[dict]:
    return [log for log in logs if log["level"] == level.upper()]


def count_logs_by_level(logs: list[dict]) -> dict:
    return dict(Counter(log["level"] for log in logs))


def display_log_counts(counts: dict) -> None:
    print(f"{'Рівень логування':<17}| Кількість")
    print(f"{'-' * 17}|{'-' * 10}")
    for level, count in counts.items():
        print(f"{level:<17}| {count}")


def main() -> None:
    if len(sys.argv) < 2:
        print("Введіть запит в форматі: python hw5.3.py <шлях_до_лог_файлу> [рівень]")
        sys.exit(1)

    file_path = sys.argv[1]
    try:
        logs = load_logs(file_path)
    except FileNotFoundError:
        print(f"Помилка: файл '{file_path}' не знайдено.")
        sys.exit(1)
    except (OSError, UnicodeDecodeError) as error:
        print(f"Помилка читання файлу '{file_path}': {error}")
        sys.exit(1)

    display_log_counts(count_logs_by_level(logs))

    if len(sys.argv) > 2:
        level = sys.argv[2].upper()
        print(f"\nДеталі логів для рівня '{level}':")
        for log in filter_logs_by_level(logs, level):
            print(f"{log['date']} {log['time']} - {log['message']}")


if __name__ == "__main__":
    main()
