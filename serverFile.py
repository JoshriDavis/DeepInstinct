import clientFile
import baseFile

# Initial variables
firstNumber = 0
secondNumber = 0
operation = ""
result = 0
clientServer = "server"

# Receives the numbers from Client
def getClientData(firstNum, secondNum, op):
    baseFile.log(getClientData.__name__, baseFile.enter, clientServer)
    global firstNumber, secondNumber, operation
    firstNumber = firstNum
    secondNumber = secondNum
    operation = op
    baseFile.log(getClientData.__name__, baseFile.exit, clientServer)

# Perform the operation of the given numbers
def performOperation(firstNum, secondNum, op):
    baseFile.log(performOperation.__name__, baseFile.enter, clientServer)
    global result
    match op:
        case "add":
            result = Addition(firstNum, secondNum)
        case "subtract":
            result = Subtract(firstNum, secondNum)
        case "multiply":
            result = Multiply(firstNum, secondNum)
        case "divide":
            result = Divide(firstNum, secondNum)
    baseFile.log(performOperation.__name__, baseFile.exit, clientServer)

# Return the result to the client
def sendResultToClient():
    baseFile.log(sendResultToClient.__name__, baseFile.enter, clientServer)
    clientFile.getDataFromServer(result)
    baseFile.log(sendResultToClient.__name__, baseFile.exit, clientServer)

# Addition function
def Addition(firstNum, secondNum):
    return firstNum + secondNum

# Subtract function
def Subtract(firstNum, secondNum):
    return firstNum - secondNum

# Multiply function
def Multiply(firstNum, secondNum):
    return firstNum * secondNum

# Divide function
def Divide(firstNum, secondNum):
    return firstNum / secondNum

# Run the server
def run():
    performOperation(firstNumber, secondNumber, operation)
    sendResultToClient()