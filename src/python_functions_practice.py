def return_10():
    return 10

def add (first_number, second_number):
    return first_number + second_number

def subtract(first_number, second_number):
    return first_number - second_number

def multiply(first_number, second_number):
    return first_number * second_number

def divide(first_number, second_number):
    return first_number / second_number

def length_of_string(string):
    return len(string)

def join_string(string_1, string_2):
    return string_1 + string_2

def add_string_as_number(first_number, second_number):
    return int(first_number) + int(second_number)

def number_to_full_month_name(month_number):
    months = {1 : "January",
              2 : "February",
              3 : "March",
              4 : "April",
              5 : "May",
              6 : "June",
              7 : "July",
              8 : "August",
              9 : "September",
              10 : "October",
              11 : "November",
              12 : "December"}
    return months[month_number]

def number_to_short_month_name(month_number):
    months = {1 : "Jan",
              2 : "Feb",
              3 : "Mar",
              4 : "Apr",
              5 : "May",
              6 : "Jun",
              7 : "Jul",
              8 : "Aug",
              9 : "Sep",
              10 : "Oct",
              11 : "Nov",
              12 : "Dec"}
    return months[month_number]

def calculate_volume_cube(side):
    return side ** 3

def get_string_reversed(string):
    new_string = ""
    for i in range(1,len(string)+1):
        new_string += string[-i]
    return new_string

def get_degrees_celsius(fahrenheit):
    return round((fahrenheit - 32)/1.8)