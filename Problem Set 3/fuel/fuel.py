while True:
    try:
        numerator, denominator = input('Fraction: ').strip().split('/')
        numerator = int(numerator)
        denominator = int(denominator)

        if numerator > denominator:
            continue

        percentage = round(numerator / denominator * 100)

        if percentage <= 1:
            print('E')
        elif percentage >= 99:
            print('F')
        else:
            print(str(percentage) + '%')

        break

    except (ValueError, ZeroDivisionError):
        continue