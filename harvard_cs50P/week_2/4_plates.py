# Ashton Hollick 11/2024

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    numbers = 0
    valid = False
    
    while not valid:
        # must be a minimum of 2 and maxium of 6 length
        if 2 <= len(s) <= 6 and s.isalnum():
            # if only 2 chars, only letters allowed
            if len(s) == 2 and not s.isalpha():
                valid = False
                break
            else:
                for i in s:
                    #adding the digits, the value of digits variable gets updated accordingly
                    if i.isdigit():
                        numbers += 1

                 # checking conditions of all possible plate lengths using stored numbers
                if numbers == 0 and len(s) >= 2:
                    valid = True
                    break
                
                if numbers == 1 and s[-1].isdigit() and s[-1] != '0':
                    valid = True
                    break

                if numbers == 2 and s[-2:].isdigit() and s[-2] != '0':
                    valid = True
                    break

                if numbers == 3 and s[-3:].isdigit() and s[-3] != '0':
                    valid = True
                    break

                if numbers == 4 and s[-4:] and s[-4] != '0':
                    valid = True
                    break

                else:
                    valid = False
                    break
                    
        else:
            valid = False
            break

    return valid


main()