class Values:
    def __init__(self, date, start, breaks, end) -> None:
        self.date = date
        self.start = start
        self.breaks = breaks
        self.end = end
        
        def __repr__(self):
            return f"<Value: {self.date}: start = {self.start}, breaks = {self.breaks} mins, end = {self.end}>"
        
class CalculatorValues:
    def __init__(self, location, n_sessions) -> None:
        self.location = location
        self.n_sessions = n_sessions
        
        def __repr__(self):
            return f"<Value: {self.location}, number of sessions = {self.n_sessions}>"
        
