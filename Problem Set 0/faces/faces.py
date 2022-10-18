def convert(input: str):
   input = input.replace(':)', '🙂')
   input = input.replace(':(', '🙁')
   return input

def main():
    print(convert(input()))

main()