class SurveyResult:

    def __init__(self):
        self._result = dict()

    def add_avg_hours(self, avgHours):
        self._result['AverageHoursPerDay'] = avgHours

    def add_most_popular_socialmedia(self, mostPopular):
        self._result['MostPopularSocialMedia'] = mostPopular

    def mental_health_affect(self, mentalhealth):
        self._result['Mentalhealth'] = mentalhealth

    def consider_addicted(self, addicted):
        self._result['Consideraddicted'] = addicted

    def harass_online(self, online):
        self._result['Harassedonline'] = online

    def use_after_bed(self, afterbed):
        self._result['useafterbed'] = afterbed

    def use_before_bed(self, beforebed):
        self._result['usebeforebed'] = beforebed

    def get_result(self):
        return self._result

    def visits_per_day(self, visitsperday):
        self._result['visitsperday'] = visitsperday

    # @property
    # def x(self):
    #     """I'm the 'x' property."""
    #     print("getter of x called")
    #     return self._x

    # @x.setter
    # def x(self, value):
    #     print("setter of x called")
    #     self._x = value