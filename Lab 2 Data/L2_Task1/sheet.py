'''
This module hooks a google API 
Google sheet at [https://goo.gl/7G8WHH]
email oAuth2: [pylabrobot@python-labs-217214.iam.gserviceaccount.com]

'''
import const,gspread, json
from oauth2client.service_account import ServiceAccountCredentials

CREDENTIALS = const.CREDENTIALS_FILE

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS, scope)

try: client = gspread.authorize(creds)
except: 
	print("Error: You must be connected to the internet in order to fill the Sheet")
	exit()


sheet = client.open_by_url(const.SHEET_LINK).sheet1


def UpdateSheetElement(value,cord):
	'''
	Downloads each element to Google Sheet at certain position

	Happened to be slow, may be useful 
	'''
	
	if cord.lower() == 'x': 
		row = len(sheet.col_values(1))
		sheet.update_cell(row+1, 1, value)

	elif cord.lower() == 'y':
		row = len(sheet.col_values(2))
		sheet.update_cell(row+1, 2, value)

	else: return False

	return True


def UpdateSheetByArray(array):
	'''
	Download xy array to Sheets
	'''
	
	column = 1 

	for col in array:
		for row in col:
			CurrentRow = len(sheet.col_values(column)) + 1
			sheet.update_cell(CurrentRow,column,row)

		column +=1


def PurgeSheet():
	'''
	Clears the Sheet
	'''
	sheet.clear()
	sheet.update_cell(1,1,"X")
	sheet.update_cell(1,2,"Y")


def ReadSheet():
	'''
	Returns data from the Sheet, assuming it is XY table
	'''
	x = sheet.col_values(1)
	y = sheet.col_values(2)

	del x[0]
	del y[0]

	x = [int(i) for i in x]
	y = [int(i) for i in y]

	xx = [x]+[y]
	return xx

