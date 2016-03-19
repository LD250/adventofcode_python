#!/usr/bin/python

def main():
    row = 6
    col = 6
    value = 27995004
    max_row = 11
    # To continue, please consult the code grid in the manual.  Enter the code at row 3010, column 3019.
    def find_from(max_row, row, col, value, to_row, to_col):
        while not (col == to_col and row == to_row):
            if row > 1:
                col += 1
                row -= 1
            else:
                max_row += 1
                row = max_row
                col = 1
            value = value * 252533 % 33554393
        return value

    print find_from(11, 6, 6, value, 3010, 3019)

if __name__ == "__main__":
    main()
