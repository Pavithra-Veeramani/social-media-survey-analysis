class SurveyResult:
    """
    Using object oriented programming the class maintains a dictionary that
     holds the analysed data a key-value pair.
    """

    def __init__(self):
        self._result = dict()

    def add_avg_hours(self, avgHours):
        self._result['AverageHoursPerDay'] = avgHours

    def add_most_popular_socialmedia(self, mostPopular):
        self._result['MostPopularSocialMedia'] = mostPopular

    def mental_health_affect(self, mentalhealth):
        self._result['MentalHealth'] = mentalhealth

    def consider_addicted(self, addicted):
        self._result['ConsiderAddicted'] = addicted

    def harass_online(self, online):
        self._result['HarassedOnline'] = online

    def use_after_bed(self, afterbed):
        self._result['UseAfterBed'] = afterbed

    def use_before_bed(self, beforebed):
        self._result['UseBeforeBed'] = beforebed

    def get_result(self):
        return self._result

    def visits_per_day(self, visitsperday):
        self._result['VisitsPerDay'] = visitsperday