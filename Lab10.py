from Name import *
import csv
from gfxhat import touch, lcd, backlight, fonts
from PIL import Image, ImageFont, ImageDraw


def read_file(file_names):
    names = []

    for file_name in file_names:
        in_file = open(file_name, "r")
        lines = in_file.readlines()
        for line in lines:
            new_name = line.split(",")
            names.append(Name(new_name[0], int(new_name[1])))

    return names


def write_file(names):
    with open('names.csv', 'wb') as csvfile:
        fieldnames = ['First Name', 'Count']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for name in names:
            writer.writerow({'First Name': name.name, 'Count': str(name.count)})


def read_csv(file_name):
    names = []
    with open(file_name, 'rb')as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader, None)
        for row in csv_reader:
            names.append(Name(row[0], row[1]))

    return names


def print_names(names):
    print '{:<11} {:<}'.format("First Name", "Count")
    for name in names:
        print '{:<11} {:<}'.format(name.name, name.count)


def generateDictionary():
    font_dictionary = {}
    with open('font3.txt', 'rb')as font_file:
        font_reader = csv.reader(font_file, delimiter=',', quotechar=None)
        for row in font_reader:
            font_dictionary[row[1]] = convertBinary(row[0])

    return font_dictionary


def convertBinary(to_convert):
    to_convert = to_convert[2:len(to_convert)]
    bin_list = []
    for i in range(0, len(to_convert)):
        bin_list.append(bin(int(to_convert[i], 16))[2:].zfill(8))
    return bin_list


def displayObject(obj):
    x = 64
    y = 32

    backlight.set_all(120, 120, 120)
    backlight.show()

    for i in range(len(obj)):
        current_x = x
        for j in range(len(obj[i])):
            lcd.set_pixel(current_x, y, int(obj[i][j]))
            current_x += 1
        y += 1

    lcd.show()
    raw_input('< Hit a key >')
    lcd.clear()
    lcd.show()
    backlight.set_all(0, 0, 0)
    backlight.show()


def Task1():
    print("Completing Task 1")
    filenames = ['2000_GirlsNames.txt', '2000_BoysNames.txt']
    namelist = read_file(filenames)
    write_file(namelist)


def Task2():
    print("Completing Task 2")
    while True:
        try:
            file_name = raw_input("Please Enter the Name of the CSV file your wish to load: ")
            task2_names = read_csv(file_name)
            print_names(task2_names)
            break
        except IOError:
            print "That was not a valid file name"


def Task3():
    print("")
    print("Completing Task 3")
    csv_fonts = generateDictionary()
    while True:
        try:
            user_char = raw_input("Enter a character to display: ")
            displayObject(csv_fonts[user_char])
            break
        except KeyError:
            print "That was not a valid character"


Task1()
Task2()
Task3()
