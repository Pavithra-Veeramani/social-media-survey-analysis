import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint
import xlsxwriter
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

print("Please wait while we are loading.. ")
SHEET = GSPREAD_CLIENT.open('Survey_Data')
survey = SHEET.worksheet('survey')

def get_welcome_message():
    #welcome message
    print("\u001b[35mWelcome to Social media survey application")

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

    print("1 - Most popular Social Media")
    print("2 - Average hours per day")
    print("3 - Average visits per day")
    print("4 - Most popular Social Media")
    print("5 - Most popular Social Media")
    print("6 - Most popular Social Media")
    print("7 - Most popular Social Media")
    print("8 - Most popular Social Media")
    print("Any other key to exit")
    
    while True:
        user_choice = input("Please make a selection. \n")

        if(user_choice == "1"):
            print("Mot popular Social Media", SurveyResult.get_result()['MostPopularSocialMedia'])
        elif(user_choice == "2"):
            print("Average number of hours spent by any person per day", SurveyResult.get_result()['AverageHoursPerDay'])
        elif(user_choice == "3"):
            print("Average number of visits made by any person per day", SurveyResult.get_result()['VisitsPerDay'])
        elif(user_choice == "4"):
            print("Number of people that use Social Media before bed", SurveyResult.get_result()['UseBeforeBed'])
        elif(user_choice == "5"):
            print("Number of people that use Social Media after bed", SurveyResult.get_result()['UseAfterBed'])
        elif(user_choice == "6"):
            print("Number of people that consider addicted to Social Media", SurveyResult.get_result()['ConsiderAddicted'])
        elif(user_choice == "7"):
            print("Number of people that consider they were harassed online in Social Media", SurveyResult.get_result()['HarassedOnline'])
        elif(user_choice == "8"):
            print("Number of people that consider their mental health is affected because of Social Media", SurveyResult.get_result()['MentalHealth'])
        else:
            print("Thank you for using our Social Media Analysis.")
            break

process_survey_data()
get_welcome_message()
get_user_input()