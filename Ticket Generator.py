#Name: Lam Manning & Sadie Huberman
#Date: Nov.7th
#Initialize
import turtle
t = turtle.Turtle()

#Functions

#Draws a text box with a label. This function uses a turtle to draw a text box with a label next to it.
#Parameters:
#(string: label) label is the word that appears next to the text box
#(integer: y_location) y_location represents the vertical loction of the text box
#(string: value) value is the word that appears inside the text box. It is taken from parameters (name, dayofweek, age, coupon)
def draw_textbox(label,value, y_location):
    t.up()
    t.goto(-50, y_location)
    t.pd()
    t.write(label, font=("Arial", 15, "bold"), align="right")
    t.pendown()
    for i in range(2):
        t.forward(200)
        t.left(90)
        t.forward(25)
        t.left(90)
    t.goto(50, y_location)
    t.write(value, font=("Arial", 15, "bold"), align="center")
    t.penup()
    t.goto(-40, y_location + 5)


#Draws a text box with a label. This function uses a turtle to draw a small text box with a label. The size of the text box is perfect for Y or N questions.
#Parameters:
#(string: label) label is the word that appears next to the text box
#(integer: y_location) y_location represents the vertical loction of the text box  
def draw_small_textbox(label, y_location):
    t.goto(60, y_location)
    t.write(label, font=("Arial", 15), align="right")
    t.pendown()
    for i in range(2):
        t.forward(50)
        t.left(90)
        t.forward(25)
        t.left(90)
    t.penup()
    t.goto(80, y_location + 5)
    
#Draws an admission ticket with a label and customer information inside. This function uses a turtle to draw a ticket with the name of the customer and the price paid for the ticket.
#(string: name) represents the customers name that appears inside the ticket
#(string: price) represents the price the customer paid that appears inside the ticket
#(string: dayofweek) represents the day of the week that the ticket was purchased
#(integer: y_location) y_location represents the vertical loction of the ticket  
def draw_ticket(name, price, dayofweek, y_location):
    t.goto(-50, y_location)
    t.pendown()
    for i in range(2):
        t.forward(250)
        t.left(90)
        t.forward(100)
        t.left(90)
    t.penup()
    t.goto(50, y_location +75)
    t.write("Admit One", font=("Arial", 15), align="right")
    t.goto(200, y_location +75)
    t.write(dayofweek, font=("Arial", 15), align="right")
    t.goto(100, y_location +35)
    t.write(name, font=("Arial", 15), align="right")
    t.goto(100, y_location)
    t.write(price, font=("Arial", 15), align="right")

#Draws the final form and imputs all the information inside along with the ticket
#(string: name) represents the customers name that appears i nside the ticket and on the form
#(string: price) represents the price the customer paid that appears inside the ticket and on the form
#(string: dayofweek) represents the day of the week that the ticket was purchased and on the form
def final_form(name, dayofweek, age, coupon):
    if(int(age)<=3):
            price= 0
    elif(int(age)<=18) and (dayofweek=="Monday"or dayofweek=="Tuesday"or dayofweek=="Wednesday"or dayofweek=="Thursday"or dayofweek=="Friday"):
            price=7.50
    elif(int(age)<=18)and(coupon=="FREEFRIDAY") and (dayofweek=="Friday"):
            price=0
    elif(int(age)<=18)and(coupon=="SUNDAY10") and (dayofweek=="Sunday"):
            price=5
    elif(int(age)<=18) and (dayofweek=="Saturday" or dayofweek=="Sunday"):
            price=15
    elif(int(age)>18):
            price=15
    t.up()
    t.goto(0,300)
    t.pd()
    t.write("AMC", align='left', font=('Ariel', 32, 'bold'))
    draw_textbox("Name: ",name, 250)
    draw_textbox("Day of the Week: ",dayofweek, 200)
    draw_textbox("Age: ",age, 150)
    draw_textbox("Coupon Code: ",coupon, 100)
    draw_small_textbox("AMC",-100)
    draw_ticket(name, price, dayofweek,-100)
    
#Main

final_form("Sadie", "Tuesday", 30, "N/A")
turtle.done()