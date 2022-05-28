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

SHEET = GSPREAD_CLIENT.open('Survey_Data')
survey = SHEET.worksheet('survey')

def loading():
    print("Please wait while we are loading.. ")

def get_welcome_message():

    #welcome message
    print("\u001b[35mWelcome to Social media survey application")

#Print loading message
loading()

SurveyProcessor = SurveyProcessor(survey)

average_hour_per_day = SurveyProcessor.calculate_avg_hoursperday()

most_popular = SurveyProcessor.calculate_mostpoularsocialmedia()

no_mental_health = SurveyProcessor.calculate_mentalhealthaffect()

no_addicted = SurveyProcessor.calculate_consideraddicted()

no_harassed_online = SurveyProcessor.calculate_harasssedonline()

no_after_bed = SurveyProcessor.calculate_useafterbed()

no_before_bed = SurveyProcessor.calculate_beforebed()

average_visits_per_day = SurveyProcessor.calculate_visits_per_day()

# SurveyResult = SurveyResult()
# SurveyResult.add_avg_hours(averageHoursPerDay)
# SurveyResult.add_most_popular_socialmedia(mostPopular)
# SurveyResult.harass_online(harassonline)
# SurveyResult.mental_health_affect(mentalhealth)
# SurveyResult.use_after_bed(afterbed)
# SurveyResult.use_before_bed(beforebed)
# SurveyResult.visits_per_day(visitsperday)
# SurveyResult.consider_addicted(addicted)

get_welcome_message()
user_choice = input("1 - Average hours per day. \n2 - Most popular Social Media \nPlease make a selection. \n")

if(user_choice == "1"):
    print("Mot popular Social Media", most_popular)
elif(user_choice == "2"):
    print("Average number of hours spent by any person per day", average_hour_per_day)
elif(user_choice == "3"):
    print("Average number of visits made by any person per day", average_visits_per_day)
elif(user_choice == "4"):
    print("Number of people that use Social Media before bed", no_before_bed)
elif(user_choice == "5"):
    print("Number of people that use Social Media after bed", no_after_bed)
elif(user_choice == "6"):
    print("Number of people that consider addicted to Social Media", no_addicted)
elif(user_choice == "7"):
    print("Number of people that consider they were harassed online in Social Media", no_harassed_online)
elif(user_choice == "8"):
    print("Number of people that consider their mental health is affected because of Social Media", no_mental_health)
#print(SurveyResult.get_result())

#Use SurveyResult.get_result() and print output