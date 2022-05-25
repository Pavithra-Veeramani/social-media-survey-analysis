class SurveyResult:

    def __init__(self):
        self.result = dict()

    def add_avg_hours(self, avgHours):
        self.result['AverageHoursPerDay'] = avgHours
        print(self.result)

    # @property
    # def x(self):
    #     """I'm the 'x' property."""
    #     print("getter of x called")
    #     return self._x

    # @x.setter
    # def x(self, value):
    #     print("setter of x called")
    #     self._x = value