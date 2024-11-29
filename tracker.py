import pandas as pd
from value_class import Values

def main():
    print("Running tracker")
    file_path = "tracker.csv"
    
    value = get_user_input()
    
    save_user_input(value, file_path)
    
    summarise_hours(file_path)

def get_user_input():
    print("Input values")
    value_date = input("Enter date:")
    value_start = input("Enter start time (24hr clock):")
    value_breaks = input("Enter length of breaks (mins):")
    value_end = input("Enter end time (24hr clock):")
    
    new_hours = Values(date = value_date, 
                       start = value_start, 
                       breaks = value_breaks, 
                       end = value_end)
    
    return new_hours

def save_user_input(value: Values, file_path):
    print("Saving user input to {file_path}")
    with open(file_path, "a") as f:
        f.write(f"{value.date},{value.start},{value.breaks},{value.end}\n")
        
def summarise_hours(file_path):
    print("Summarising hours")
    with open(file_path, "r") as f:
        df = pd.read_csv(f)
        df['date'] = pd.to_datetime(df['date'], dayfirst = True)
        df['hrs_worked'] = df['end'] - df['breaks'] - df['start']
        df['weekday'] = df['date'].dt.day_name()
        expected_hrs = pd.read_csv('expected.csv')
        df_joined = df.merge(expected_hrs, how = 'left', on = 'weekday')
        df_joined['difference'] = df_joined['hrs_worked'] - df_joined['expected_hours']
        total_over_under = df_joined['difference'].sum()
        return print(total_over_under)
    
if __name__ == "__main__":
    main()