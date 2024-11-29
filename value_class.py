class Values:
    def __init__(self, date, start, breaks, end) -> None:
        self.date = date
        self.start = start
        self.breaks = breaks
        self.end = end
        
        def __repr__(self):
            return f"<Value: {self.date}: start = {self.start}, breaks = {self.breaks} mins, end = {self.end}>"