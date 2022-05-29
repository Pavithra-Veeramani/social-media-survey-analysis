"""
In order to use our Google Sheets API, we to need to install
additional dependencies into our project.
"""
import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint
from SurveyProcessor import SurveyProcessor
from SurveyResult import SurveyResult

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

print(" \u001b[33mWelcome to Social media survey application")
print(" Please wait while we are loading...")
SHEET = GSPREAD_CLIENT.open('Survey_Data')
survey = SHEET.worksheet('survey')

SurveyProcessor = SurveyProcessor(survey)
SurveyResult = SurveyResult()


def process_survey_data():

    average_hour_per_day = SurveyProcessor.calculate_avg_hoursperday()
    most_popular = SurveyProcessor.calculate_mostpoularsocialmedia()
    no_mental_health = SurveyProcessor.calculate_mentalhealthaffect()
    no_addicted = SurveyProcessor.calculate_consideraddicted()
    no_harassed_online = SurveyProcessor.calculate_harasssedonline()
    no_after_bed = SurveyProcessor.calculate_useafterbed()
    no_before_bed = SurveyProcessor.calculate_beforebed()
    average_visits_per_day = SurveyProcessor.calculate_visits_per_day()

    SurveyResult.add_avg_hours(average_hour_per_day)
    SurveyResult.add_most_popular_socialmedia(most_popular)
    SurveyResult.harass_online(no_harassed_online)
    SurveyResult.mental_health_affect(no_mental_health)
    SurveyResult.use_after_bed(no_after_bed)
    SurveyResult.use_before_bed(no_before_bed)
    SurveyResult.visits_per_day(average_visits_per_day)
    SurveyResult.consider_addicted(no_addicted)


def get_user_input():

    print(" \u001b[36m1 - Most popular Social Media")
    print(" \u001b[36m2 - Average hours per day")
    print(" \u001b[36m3 - Average visits per day")
    print(" \u001b[36m4 - People with mental health affect")
    print(" \u001b[36m5 - People who use social media before bed")
    print(" \u001b[36m6 - People who use social media after bed")
    print(" \u001b[36m7 - People who are addicted")
    print(" \u001b[36m8 - People who are harassed online")
    print(" \u001b[36mOthers - Exit")
    while True:
        user_choice = input(" Please make a selection to proceed\n")

        if(user_choice == "1"):
            print(
                " Most popular Social Media is ",
                SurveyResult.get_result()['MostPopularSocialMedia']['name'],
                SurveyResult.get_result()['MostPopularSocialMedia']['count'],
                "votes out of",
                SurveyResult.get_result()['MostPopularSocialMedia']['total']
            )
        elif(user_choice == "2"):
            print(
                " Average number of hours spent by any person per day",
                SurveyResult.get_result()['AverageHoursPerDay']
            )
        elif(user_choice == "3"):
            print(
                " Average number of visits made by any person per day",
                SurveyResult.get_result()['VisitsPerDay']
            )
        elif(user_choice == "4"):
            print(
                " Number of people that use Social Media before bed",
                SurveyResult.get_result()['UseBeforeBed']
            )
        elif(user_choice == "5"):
            print(
                " Number of people that use Social Media after bed",
                SurveyResult.get_result()['UseAfterBed']
            )
        elif(user_choice == "6"):
            print(
                " Number of people that consider addicted to Social Media",
                SurveyResult.get_result()['ConsiderAddicted']
            )
        elif(user_choice == "7"):
            print(
                " Number of people that consider they were harassed online",
                "in Social Media", SurveyResult.get_result()['HarassedOnline']
            )
        elif(user_choice == " 8"):
            print(
                " Number of people that consider their mental health is",
                "affected because of Social Media",
                SurveyResult.get_result()['MentalHealth']
            )
        else:
            print(" \u001b[33mApplication exited. To run the program again,",
            "press the button at the top.")
            print(" \u001b[33mThank you for using our Social Media Analysis.")
            break

process_survey_data()
get_user_input()
