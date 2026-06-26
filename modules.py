def _repr(n):
    return str(int(n)) if n == int(n) else str(n)


def _to_seconds(value, unit):
    return value * {"seconds": 1, "minutes": 60, "hours": 3600, "days": 86400}[unit]


def _fmt(seconds):
    seconds = round(seconds, 10)
    days = int(seconds // 86400)
    seconds -= days * 86400
    hours = int(seconds // 3600)
    seconds -= hours * 3600
    minutes = int(seconds // 60)
    secs = seconds - minutes * 60

    if secs and round(secs) == secs:
        secs = int(round(secs))

    parts = []
    if days:
        parts.append(f"{_repr(days)} {'day' if days == 1 else 'days'}")
    if hours:
        parts.append(f"{_repr(hours)} {'hour' if hours == 1 else 'hours'}")
    if minutes:
        parts.append(f"{_repr(minutes)} {'minute' if minutes == 1 else 'minutes'}")
    if secs:
        parts.append(f"{_repr(secs)} {'second' if secs == 1 else 'seconds'}")
    if not parts:
        return "0 seconds"
    if len(parts) == 1:
        return parts[0]
    return ", ".join(parts[:-1]) + " and " + parts[-1]


def ets_time():
    units = ["seconds", "minutes", "hours", "days"]

    mode = input("Mode: ETS2 → Real (1) or Real → ETS2 (2): ")
    value = float(input("Value: "))
    unit = input(f"Unit ({', '.join(units)}): ")

    if unit not in units:
        print("Invalid unit.")
        return

    seconds = _to_seconds(value, unit)

    if mode == "1":
        # ETS2 → Real: divide by 20
        print(f"Real Time: {_fmt(seconds / 20)}")
    elif mode == "2":
        # Real → ETS2: multiply by 20
        print(f"ETS2 Time: {_fmt(seconds * 20)}")
    else:
        print("Invalid mode.")
