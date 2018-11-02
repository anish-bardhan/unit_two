#prints statements listing the possible options
print("styles: astro, evolve, spongebob, littlered, or face")
print("sizes: extra small, small, medium, large, or extra large")
print("colors: black, white, green, red, yellow, blue, orange, or purple")
print("order days: one, two, three, four, or five")

#gives questions to recieve user input
style = input("what is the custom style?")
size = input("what is the custom size?")
color = input("what is the custom color?")
days = input("how many days does the customer need the order by?")
#puts input into an array
order = (style, size, color, days)
#prints array
print(order)

#defines a method
def style_method(style):
    #sets starting price to zero
    style_price = 0
    #if else statement to determine which option was selected
    if style == "astro":
        #adds price to the total so final price can be found at the end
        style_price += 2
    elif style == "evolve":
        style_price += 4
    elif style == "spongebob":
        style_price += 2
    elif style == "littlered":
        style_price += 1
    elif style == "face":
        style_price += 3
    else:
        #tells user that their input was incorrect
        print("incorrect information was inputted\nplease restart")
    #returns price to be used later on
    return style_price

def size_method(size):
    size_price = 0
    if size == "extra small":
        size_price += 2
    elif size == "small":
        size_price += 1
    elif size == "medium":
        size_price += 1
    elif size == "large":
        size_price += 1
    elif size == "extra large":
        size_price += 2
    else:
        print("incorrect information was inputted\nplease restart")
    return size_price

def color_method(color):
    color_price = 0
    if color == "black":
        color_price += 1
    elif color == "white":
        color_price += 0
    elif color == "green":
        color_price += 2
    elif color == "red":
        color_price += 2
    elif color == "yellow":
        color_price += 2
    elif color == "blue":
        color_price += 2
    elif color == "orange":
        color_price += 3
    elif color == "purple":
        color_price += 3
    else:
        print("incorrect information was inputted\nplease restart")
    return color_price

def days_method(days):
    days_price = 0
    if days == "one":
        days_price += 5
    elif days == "two":
        days_price += 3
    elif days == "three":
        days_price += 2
    elif days == "four":
        days_price += 1
    elif days == "five":
        days_price += 0
    else:
        print("incorrect information was inputted\nplease restart")
    return days_price

#calls method using user input
style_method(style)
#saves output of method into a variable
style_ans = style_method(style)

size_method(size)
size_ans = size_method(size)

color_method(color)
color_ans = color_method(color)

days_method(days)
days_ans = days_method(days)

#adds all prices together for subtotal
price = (style_ans + size_ans + color_ans + days_ans)

#defines a method
def price_method(price):
    #sets total to zero
    total = 0
    #adds price to total
    total += price
    #adds five to the total
    total += 5
    #prints the final total
    print(total)

#calls method
price_method(price)
