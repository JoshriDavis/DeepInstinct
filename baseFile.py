from datetime import datetime

# Initial variables
enter = "Enter"
exit = "Exit"

# logging function
def log(functionName, state, clientServer):
    with open(clientServer + '.log', 'a') as log_file:
        log_file.write(f"{datetime.now()} ---- Function {functionName} {state} ----\n")