import os
#import pandas as pd
import pygsheets

#import os.path
#from googleapiclient.discovery import build
#from google_auth_oauthlib.flow import InstalledAppFlow
#from google.auth.transport.requests import Request

oauth_file = '/Users/gs/PycharmProjects/venv/lib/loadgsheets/credentials.json'
sheet_url = 'https://docs.google.com/spreadsheets/d/12DKljljljljljmtrct/edit#gid=0'
tab_name = 'Data_sheet'
save_path = '/Users/GS/PycharmProjects/wisdom/venv/lib/loadgsheets/'
auth_code ='4/authorizationcode '
 ##     Authorizataio code is capturing while setting up google account"

# Load from google sheets
gc = pygsheets.authorize(outh_file=oauth_file)
sh = gc.open_by_url(sheet_url)
wks = sh.worksheet_by_title(title=tab_name)

wks.export(filename='test_sample_download', path=save_path)


# Convert to dataframe
#df = wks.get_as_df()
#df = df[config.select_col]

# Save as csv
#df.to_csv(save_path, header=False, index=False, sep='\t')
