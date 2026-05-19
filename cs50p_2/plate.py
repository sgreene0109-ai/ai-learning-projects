def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if s[0].isalpha() == False:
        return False
    if s[1].isalpha() == False:
        return False
    for x in s:
        if not x.isdigit() and not x.isalpha():
            return False
    found_digit = False
    for x in s:
        if x.isdigit():
            found_digit = True
            if x == "0":
                return False
        if found_digit and x.isalpha():
            return False
        return True
main ()
          


