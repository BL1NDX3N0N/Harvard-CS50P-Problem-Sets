months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def ConvertVerboseDate(date: str):
    # This function only performs sanity checks on the date
    # and attempts to convert it to a format easier to work
    # with. Upon conversion failure, the argument passed to
    # this function will be returned to avoid
    # exception-generated overhead and it is up to the
    # caller to validate the returned data.
    if ' ' not in date:
        return date

    tokens = date.split(' ')

    if len(tokens) != 3:
        return date

    if tokens[0].title() in months:
        if tokens[1].endswith(','):
            tokens[1] = tokens[1][:-1]
        else:
            return date

        tokens[0] = months.index(tokens[0].title()) + 1
        return f'{tokens[0]}/{tokens[1]}/{tokens[2]}'

    return date

def IsMiddleEndianDate(date: str):
    if '/' not in date:
        return False

    tokens = date.split('/')

    if len(tokens) != 3:
        return False

    if tokens[0].isdigit() and tokens[1].isdigit() and tokens[2].isdigit():
        tokens[0] = int(tokens[0])
        tokens[1] = int(tokens[1])
        tokens[2] = int(tokens[2])
    else:
        return False

    if tokens[0] < 1 or tokens[0] > 12:
        return False
    if tokens[1] < 1 or tokens[1] > 31:
        return False
    if tokens[2] < 0 or tokens[2] > 9999:
        return False

    return True

def ConvertToBigEndianDate(date: str):
    month, day, year = date.split('/')
    return f'{year.zfill(4)}-{month.zfill(2)}-{day.zfill(2)}'

while True:
    date = ConvertVerboseDate(input('Date: ').strip())

    if IsMiddleEndianDate(date) == False:
        continue

    print(ConvertToBigEndianDate(date))
    break