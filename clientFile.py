import serverFile
import baseFile

result = 0
clientServer = "client"

# Get user data
def getUserData():
    baseFile.log(getUserData.__name__, baseFile.enter, clientServer)
    #region first number validation flow
    while(1):
        try:
            firstNumber = float(input("Please enter the first number:\n"))
            break
        except:
            print("Wrong input!")
    #endregion

    #region second number validation flow
    while(1):
        try:
            secondNumber = float(input("Please enter the second number:\n"))
            break
        except:
            print("Wrong input!")
    #endregion
    
    #region operation validation flow
    exit = "no"
    while(exit == "no"):
        operation = input("Please add the operation (add / subtract / multiply / divide / quit):\n")
        match operation:
            case "add":
                exit == "yes"
                break
            case "subtract":
                exit == "yes"
                break
            case "multiply":
                exit == "yes"
                break
            case "divide":
                if(secondNumber == 0.0):
                    print("Cannot divide by zero! try another operation")
                    exit == "no"
                else:
                    exit == "yes"
                    break
            case "quit":
                print("Goodbye!")
                quit()
            case _:
                print("Wrong input!")
    #endregion

    baseFile.log(getUserData.__name__, baseFile.exit, clientServer)
    return firstNumber, secondNumber, operation

# Send data to server
def sendDataToServer(firstNumber, secondNumber, operation):
    baseFile.log(sendDataToServer.__name__, baseFile.enter, clientServer)
    serverFile.getClientData(firstNumber, secondNumber, operation)
    baseFile.log(sendDataToServer.__name__, baseFile.exit, clientServer)

# Get result
def getDataFromServer(res):
    baseFile.log(getDataFromServer.__name__, baseFile.enter, clientServer)
    global result
    result = res
    baseFile.log(getDataFromServer.__name__, baseFile.exit, clientServer)

# Print the result
def printResult():
    baseFile.log(printResult.__name__, baseFile.enter, clientServer)
    global result
    print(result)
    baseFile.log(printResult.__name__, baseFile.exit, clientServer)

# Main function
def main():
    firstNumber, secondNumber, operation = getUserData()
    sendDataToServer(firstNumber, secondNumber, operation)
    serverFile.run()
    printResult()

main()