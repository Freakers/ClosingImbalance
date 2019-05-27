import statistics

class calculatemedian:

    def __init__(self, min=0, max=1, value=0.5):
        self.min = int(min)
        self.max = int(max)
        self.spread = max - min
        self.minmedian = self.spread * 0.25 + self.min
        self.maxmedian = self.spread * 0.75 + self.max
        self.value = value
        print("Min   : " + str(self.min))
        print("Max   : " + str(self.max))
        print("Spread: " + str(self.spread))
        print("Value : " + str(self.value))
        print("MinMedian: " +str(self.minmedian))
        print("MaxMedian: " +str(self.maxmedian))

    def getminmedian(self):
        return self.minmedian

    def getmaxmedian(self):
        return self.maxmedian

med = calculatemedian(10, 11, 10.1)
print("mmin = " + str(med.getminmedian()))
print("mmax = " + str(med.getmaxmedian()))

