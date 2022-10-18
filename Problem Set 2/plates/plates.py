def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    return IsLegalLength(s) and \
        StartsWithTwoLetters(s) and \
            s.isalnum() and \
                HasLegalDigitPlacement(s)

def IsLegalLength(plate):
    return len(plate) >= 2 and len(plate) <= 6

def StartsWithTwoLetters(plate):
    return plate[0].isalpha() and plate[1].isalpha()

def HasLegalDigitPlacement(plate):
    if (plate.isalpha()):
        return True

    for i in range(len(plate)):
        if (plate[i].isdigit()):
            digitSection = plate[i:len(plate)]
            return digitSection[0] != '0' and digitSection.isdigit() == True

main()