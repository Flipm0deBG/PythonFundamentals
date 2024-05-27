# Define the letter patterns
letters = {
    'S': [" **** ", "*    *", "*     ", " **** ", "     *", "*    *", " **** "],
    'O': [" **** ", "*    *", "*    *", "*    *", "*    *", "*    *", " **** "],
    'F': ["******", "*     ", "*     ", "***** ", "*     ", "*     ", "*     "],
    'T': ["******", "  **  ", "  **  ", "  **  ", "  **  ", "  **  ", "  **  "],
    'U': ["*    *", "*    *", "*    *", "*    *", "*    *", "*    *", " **** "],
    'N': ["*    *", "**   *", "* *  *", "*  * *", "*   **", "*    *", "*    *"],
    'I': [" ***** ", "   *  ", "   *  ", "   *  ", "   *  ", "   *  ", " ***** "]
}

# Number of lines for each letter representation
num_lines = len(letters['S'])

# Print the word SOFTUNI line by line
for i in range(num_lines):
    for letter in "SOFTUNI":
        print(letters[letter][i], end="  ")
    print()
