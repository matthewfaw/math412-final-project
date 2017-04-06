class Entry:
    def __init__(self, year, category, nominee_work, credits):
        self.year = year
        self.category = category
        self.nominee_work = nominee_work
        self.credits = credits
    def __str__(self):
        s = 'Year: %s\nCategory: %s\nNominee Work: %s\nCredits: %s' % (self.year,self.category,self.nominee_work,self.credits)
        return s.encode('utf-8')
    def __repr__(self):
        return str(self)
    def toArray(self):
        return [
                self.year,
                self.category,
                self.nominee_work,
                self.credits
                ]
