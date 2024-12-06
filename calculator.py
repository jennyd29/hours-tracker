import pandas as pd
from value_class import CalculatorValues

def main():
    file_path = "test_input.csv"
    
    value = get_user_input()
    
    save_user_input(value, file_path)
    
    #create_output()
    
def get_user_input():
    print("Input information")
    value_location = input("Enter location:")
    value_n_sessions = input("Enter number of sessions:")
    
    new_sessions = CalculatorValues(location = value_location, 
                                    n_sessions = value_n_sessions)
    
    return new_sessions

def save_user_input(value: CalculatorValues, file_path):
    print(f"Saving user input to {file_path}")
    with open(file_path, "a") as f:
        f.write(f"{value.location},{value.n_sessions}\n")
        


if __name__ == "__main__":
    main()