# Initialize the variable to hold the mathematical equation:

equation = ""

# Function to update the equation and display the result:
def show(value, label_result):
    global equation
    equation += value
    label_result.config(text=equation)

def clear(label_result):
    global equation
    equation = ""
    label_result.config(text=equation)
    
# Function to evaluate and calculate the equation:
def calculate(label_result):
    global equation
    try:
        result = eval(equation)
        equation = str(result)
        label_result.config(text=equation)
    except SyntaxError:
         equation = "Syntax Error"
         print("Syntax Error occurred")
         label_result.config(text=equation)

    except:
# Handle any other error that may occur during calculation:
        equation = "Error"
        label_result.config(text=equation)