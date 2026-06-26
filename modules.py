def ets_time():
    units = ["seconds", "minutes", "hours", "days"]

    mode = input("Mode: ETS2 -> Real Time (1) or Real Time -> ETS2 (2): ")
    value = float(input("Value: "))
    unit = input(f"Unit ({', '.join(units)}): ")

    if mode == "1":
        if unit == "minutes":
            real_time = value * 3
            new_unit = "seconds"
        elif unit == "hours":
            real_time = value * 3
            new_unit = "minutes"
        elif unit == "days":
            real_time = value * 24 * 3
            new_unit = "minutes"
        else:
            print("Invalid unit.")
            return

        if new_unit == "seconds" and real_time >= 60:
            rest = real_time % 60
            rest = int(rest)
            real_time /= 60
            real_time = int(real_time)
            additional = f" and {rest} seconds"
            new_unit = "minutes"
        elif new_unit == "minutes" and real_time >= 60:
            rest = real_time % 60
            rest = int(rest)
            real_time /= 60
            real_time = int(real_time)
            additional = f" and {rest} minutes"
            new_unit = "hours"
            
        print(f"Real Time: {real_time} {new_unit}{additional}")