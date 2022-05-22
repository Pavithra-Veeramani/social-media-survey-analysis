import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
CREDS = Credentials.from_service_account_file('credentials.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Survey_Data')

survey = SHEET.worksheet('survey')
surveyData = survey.get_all_values()

pprint(surveyData)

def calculate_avg_hoursperday(data):
    """
    Get Average Number of hours spent per day across all social media sites.
    Run a while loop to collect a valid string of data from the user
    via the terminal, which must be a string of 6 numbers separated
    by commas. The loop will repeatedly request data, until it is valid.
    """
    hours = data.col_values(8)

    totalHours = 0
    for i, hour in enumerate(hours):
        if(i == 0):
            continue
        int_hour = int(hour)
        totalHours = totalHours + int_hour

    average = totalHours / (len(hours)-1)

    print("Average time spent in Social media:", average)
    return average


calculate_avg_hoursperday(survey)