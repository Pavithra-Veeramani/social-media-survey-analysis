class SurveyResult:
    """
    Using object oriented programming the class maintains a dictionary that
     holds the analysed data a key-value pair.
    """

    def __init__(self):
        self._result = dict()

    def add_avg_hours(self, avgHours):
        """
        sets the average hours per day data into dictionary.
        """
        self._result['AverageHoursPerDay'] = avgHours
    
    def add_most_popular_socialmedia(self, mostPopular):
        """
        sets the most popular socila media data into dictionary.
        """
        self._result['MostPopularSocialMedia'] = mostPopular

    def mental_health_affect(self, mentalhealth):
        """
        sets the mental health affect data into dictionary.
        """
        self._result['MentalHealth'] = mentalhealth

    def consider_addicted(self, addicted):
        """
        sets the consider addicted data into dictionary.
        """
        self._result['ConsiderAddicted'] = addicted

    def harass_online(self, online):
        """
        sets the harassed online data into dictionary.
        """
        self._result['HarassedOnline'] = online

    def use_after_bed(self, afterbed):
        """
        sets using social media after bed into dictionary.
        """
        self._result['UseAfterBed'] = afterbed

    def use_before_bed(self, beforebed):
        """
        sets using social media before data into dictionary.
        """
        self._result['UseBeforeBed'] = beforebed

    def get_result(self):
        return self._result

    def visits_per_day(self, visitsperday):
        """
        sets the average visits per day data into dictionary.
        """
        self._result['VisitsPerDay'] = visitsperday
