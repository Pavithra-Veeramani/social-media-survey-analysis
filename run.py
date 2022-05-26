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

#surveyData = survey.get_all_values()
#pprint(surveyData)

def write_output():
    workbook = xlsxwriter.Workbook('Result.xlsx')
 
    # The workbook object is then used to add new
    # worksheet via the add_worksheet() method.
    worksheet = workbook.add_worksheet()
    
    # Use the worksheet object to write
    # data via the write() method.
    worksheet.write('A1', 'Hello..')
    
    # Finally, close the Excel file
    # via the close() method.
    workbook.close()

SurveyProcessor = SurveyProcessor(survey)

averageHoursPerDay = SurveyProcessor.calculate_avg_hoursperday()

mostPopular = SurveyProcessor.calculate_mostpoularsocialmedia()

mentalhealth = SurveyProcessor.calculate_mentalhealthaffect()

addicted = SurveyProcessor.calculate_consideraddicted()

harassonline = SurveyProcessor.calculate_harasssedonline()

afterbed = SurveyProcessor.calculate_useafterbed()

beforebed = SurveyProcessor.calculate_beforebed()

visitsperday = SurveyProcessor.calculate_visits_per_day()

SurveyResult = SurveyResult()
SurveyResult.add_avg_hours(averageHoursPerDay)
SurveyResult.add_most_popular_socialmedia(mostPopular)
SurveyResult.harass_online(harassonline)
SurveyResult.mental_health_affect(mentalhealth)
SurveyResult.use_after_bed(afterbed)
SurveyResult.use_before_bed(beforebed)
SurveyResult.visits_per_day(visitsperday)
SurveyResult.consider_addicted(addicted)


print(SurveyResult.get_result())

#Use SurveyResult.get_result() and write in to another sheet in google