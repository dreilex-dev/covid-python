#here we open the file with the data
f = open("covid.in", "r")

#we read the first line where we have the new cases
new_cases = f.readline().split()

#we read the second line where we have the covid tests done in that day
tests = f.readline().split()

#we are converting the input to integer values
for i in range(0, len(new_cases)):
    new_cases[i] = int(new_cases[i])
    tests[i] = int(tests[i])

#we are importing the turtle module and set the initial parameters
import turtle
t = turtle.Turtle()
t.color("Gray")
t.speed(40)
t.penup()
t.setpos(10, 0)
t.pendown()

#calculating the avg values for the new cases and tests done
avg_new_cases = round(sum(new_cases)/len(new_cases))
avg_tests = round(sum(tests)/len(tests))


#define the xoy lines
def draw_axes(t, length):
    
    #draw the x-axis
    t.penup()
    t.color("black")
    t.goto(0, 0)
    t.pendown()
    t.forward(len(tests)*30)

    # Draw the y-axis
    t.penup()
    t.color("black")
    t.goto(0, 0)
    t.pendown()
    t.left(90)
    t.forward(max(tests)/300 + 50)
    t.right(90)

#define the function to draw the tests/day. The window height is 300 px, we divide with 300 in order to have the graph within
    
def tests_graph():
    for y in tests:
        t.left(90)
        t.forward(y/300)
        t.color("red")
        t.circle(2)
        t.color("blue")
        t.back(y/300)
        t.right(90)
        t.penup()
        t.forward(10)
        t.pendown()

#define the function to get the average line of the daily tests
def tests_average_line() :
    t.color("red")
    t.penup()
    t.left(90)
    t.forward(avg_tests/300)
    t.left(90)
    t.forward(10)
    t.pendown()
    t.forward(len(tests)*10-10)
    t.left(90)
    t.penup()
    t.forward(avg_tests/300)
    t.left(90)
    t.forward(len(tests)*10)
    t.pendown()

#define the function to draw the cases/day. Scaling the values ti have the graph within the window
def cases_graph():
    for x in new_cases:
        t.left(90)
        t.forward(x/10)
        t.color("red")
        t.circle(2)
        t.color("gray")
        t.back(x/10)
        t.right(90)
        t.penup()
        t.forward(10)
        t.pendown()

#define the function to get the average line of the cases
def cases_average_line():
    t.color("red")
    t.penup()
    t.left(90)
    t.forward(avg_new_cases/10)
    t.left(90)
    t.forward(10)
    t.pendown()
    t.forward(len(new_cases)*10-10)
    t.left(90)
    t.penup()
    t.forward(avg_new_cases/10)
    t.left(90)
    t.forward(len(new_cases)*10)
    t.pendown()

#define the function to get the percentage of cases vs the number of tests per day
procent = [0] * len(new_cases)
def percentage_graph():
    for i in range(0,len(new_cases)):
            procent[i] = new_cases[i]/tests[i]*1000
            t.color("purple")
            t.left(90)
            t.pendown()
            t.forward(procent[i])
            t.color("red")
            t.circle(2)
            t.penup()
            t.backward(procent[i])
            t.right(90)
            t.forward(10)   

#calling the functions
tests_graph()
tests_average_line()
cases_graph()
cases_average_line()
percentage_graph()
draw_axes(t, 500)

print("Daily average (new cases) = " , avg_new_cases)
print("Daily average tests =", avg_tests)

#percentage of the infected people
print("Percentage of the infected people = " , round((avg_new_cases/avg_tests)*100,2), "%")

print("22 iulie - 08 august, 2020")

#lista of the new cases
#print(new_cases)

#lista of the tests
#print(tests)

