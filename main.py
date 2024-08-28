from turtle import Turtle, Screen
import random

screen = Screen()                                       

turtle = Turtle()                                       
turtle.hideturtle()                                     
turtle.speed("fastest")                                 

colors = ["red", "blue", "green", "orange", "purple", "black", "yellow", "pink", "teal", "plum"]

for i in range(100):                                    
    turtle.circle(100)                                  
    turtle.color(random.choice(colors))                 
    current_heading = turtle.heading()                  
    new_heading = current_heading + 10                  
    turtle.setheading(new_heading)                      
    turtle.circle(100)                                  

screen.exitonclick()    
