def main():
    time = convert(input('What time is it? ').strip().lower())
    if time >= 7 and time <= 8:
        print('breakfast time')
    elif time >= 12 and time <= 13:
        print('lunch time')
    elif time >= 18 and time <= 19:
        print('dinner time')


def convert(time):
    # Project instructions make no mention of handling errors
    # so perfect input will be assumed.
    tokens = time.split(' ')
    hours, minutes = tokens[0].split(':')

    if len(tokens) == 2 and tokens[1] == 'p.m.' and hours != '12':
        hours = int(hours) + 12

    return float(hours) + (float(minutes) / 60)


if __name__ == "__main__":
    main()