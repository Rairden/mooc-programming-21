from datetime import datetime


def PICtoISO8601(pic: str):
    """returns a date tuple in ISO8601 format - yyyymmdd"""
    year = pic[4:6]
    month = pic[2:4]
    day = pic[:2]

    century = pic[6]
    if century == "+":
        year = f"18{year}"
    elif century == "-":
        year = f"19{year}"
    elif century == "A":
        year = f"20{year}"

    return int(year), int(month), int(day)


def controlChar(pic: str):
    """returns a control character which is a checksum or check digit"""
    checksum = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    date = pic[:6]
    pid = pic[7:10]

    num = int(date + pid)  # concatenate date + pid, divide by 31, then use remainder to select checksum index
    idx = num % 31
    return checksum[idx]


def is_it_valid(pic: str):
    """
    Finnish Personal Identity Codes (PIC)
    X is century marker: + (1800s), - (1900s) or A (2000s); yyy is personal identifier; z is control char
    ddmmyyXyyyz
    230827-906F has birthday of 08-23-1927
    """

    centuryMarkers = "-+A"
    century = pic[6]
    if len(pic) != 11 or century not in centuryMarkers:
        return False

    iso8601 = PICtoISO8601(pic)  # yyyymmdd
    try:
        datetime(iso8601[0], iso8601[1], iso8601[2])
    except:
        return False

    control = pic[-1]
    if control != controlChar(pic):
        return False

    return True


if __name__ == '__main__':
    valid = "230827-906F"
    valid2 = "310823A9877"
    invalid = "320823A9877"

    print(is_it_valid(valid))
    print(is_it_valid(invalid))
