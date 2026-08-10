from data import MORSE_CODE_DICT
import sys

string_to_translate = input()
morse_code = ""


for char in " ".join(string_to_translate.split()):
    if char == " ":
        morse_code += "    "
    elif char.upper() not in MORSE_CODE_DICT:
        print("One or more of the characters given is not in the ITU Morse Code. Please try again!")
        sys.exit(1)
    elif char.isalpha():
        morse_code += MORSE_CODE_DICT[char.upper()] + "   "
    else:
        morse_code += MORSE_CODE_DICT[char] + "   "


print(morse_code.strip())