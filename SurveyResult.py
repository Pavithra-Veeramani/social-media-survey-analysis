class SurveyResult:

    def __init__(self):
        self._result = dict()

    def add_avg_hours(self, avgHours):
        self._result['AverageHoursPerDay'] = avgHours

    def add_most_popular_socialmedia(self, mostPopular):
        self._result['MostPopularSocialMedia'] = mostPopular

    def get_result(self):
        return self._result
    # @property
    # def x(self):
    #     """I'm the 'x' property."""
    #     print("getter of x called")
    #     return self._x

    # @x.setter
    # def x(self, value):
    #     print("setter of x called")
    #     self._x = value