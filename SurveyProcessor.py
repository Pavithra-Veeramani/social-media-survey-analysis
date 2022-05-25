class SurveyProcessor:

    # Instance attribute for the Data
    def __init__(self, data):
        self.data = data

    def calculate_avg_hoursperday(self):
        """
        Get Average Number of hours spent per day across all social media sites.
        Run a while loop to collect a valid string of data from the user
        via the terminal, which must be a string of 6 numbers separated
        by commas. The loop will repeatedly request data, until it is valid.
        """
        hours = self.data.col_values(8)

        totalHours = 0
        for i, hour in enumerate(hours):
            if i == 0:
                continue
            if hour == '':
                continue
            int_hour = int(hour)
            totalHours = totalHours + int_hour

        average = totalHours / (len(hours)-1)

        print("Average time spent in Social media:", average)
        return average


    def calculate_mostpoularsocialmedia(self):
        """
        Get Average Number of hours spent per day across all social media sites.
        Run a while loop to collect a valid string of data from the user
        via the terminal, which must be a string of 6 numbers separated
        by commas. The loop will repeatedly request data, until it is valid.
        """
        sites = self.data.col_values(5)

        noYoutube = 0
        noTtok = 0
        noInsta = 0
        noFb = 0
        noLinked = 0
        noTwtr = 0
        for i, site in enumerate(sites):
            if(i == 0):
                continue
            if(site == ''):
                continue
            if(site == 'TTOK'):
                noTtok += 1
            elif(site == 'FB'):
                noFb += 1
            elif(site == 'YTUBE'):
                noYoutube += 1
            elif(site == 'TWTR'):
                noTwtr += 1
            elif(site == 'LNKD'):
                noLinked += 1
            elif(site == 'INST'):
                noInsta += 1

        if noYoutube >= noFb and noYoutube >= noTtok and noYoutube >= noInsta and noYoutube >= noLinked and noYoutube >= noTwtr:
            print('Youtube has the most : ', noYoutube)
        elif noFb >= noYoutube and noFb >= noTtok and noFb >= noInsta and noFb >= noLinked and noFb >= noTwtr:
            print('FB has the most : ', noFb)
        elif noTtok >= noYoutube and noTtok >= noFb and noTtok >= noInsta and noTtok >= noLinked and noTtok >= noTwtr:
            print('Ttok has the most : ', noTtok)
        elif noLinked >= noInsta and noLinked >= noTtok and noLinked >= noInsta and noLinked >= noFb and noLinked >= noTwtr:
            print('Linked has the most : ', noLinked)
        elif noInsta >= noYoutube and noInsta >= noTtok and noInsta >= noFb and noInsta >= noLinked and noInsta >= noTwtr:
            print('Insta has the most : ', noInsta)
        elif noTwtr >= noYoutube and noTwtr >= noTtok and noTwtr >= noInsta and noTwtr >= noLinked and noTwtr >= noFb:
            print('Twtr has the most : ', noTwtr)


    def calculate_mentalhealthaffect(self):
        health = self.data.col_values(11)

        affects = 0
        for i in health:
            if i == 'Y':
                affects += 1

        print("Number of people who think they have mental issues:", affects)

    def calculate_consideraddicted(self):

        addict = self.data.col_values(13)

        consider = 0

        for x in addict:
            if x == 'Y':
                consider += 1

        print("Number of people who think they are addicted:", consider)

    def calculate_harasssedonline(self):

        harass = self.data.col_values(12)

        online = 0

        for j in harass:
            if j == 'Y':
                online += 1

        print("Number of people harassed online:", online) 

    def calculate_useafterbed(self):

        useafter = self.data.col_values(10)

        after = 0

        for a in useafter:
            if a == 'Y':
                after += 1
        print("Number of people who use after bed:", after)

    def calculate_beforebed(self):

        beforebed = self.data.col_values(9)

        before = 0

        for z in beforebed:
            if z == 'Y':
                before += 1
        print("Number of people who use before bed:", before)