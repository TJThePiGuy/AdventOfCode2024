class AOCDSubmitter:

    def __init__(self, day:int, year:int, save:bool=True):
        self.aocd = __import__("aocd")
        self.day = day
        self.year = year
        self.save = save
        self.data = None
        self.get_data()

    def get_data(self):
        self.data = self.aocd.get_data(day = self.day, year = self.year, block = True)
        if(self.save):
            with open('helper/input', 'w+') as f:
                f.write(self.data)
    
    def submit(self, answer, part):
        self.aocd.submit(answer = answer, day = self.day, year = self.year, part = part)
    