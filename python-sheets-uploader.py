from __future__ import print_function
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import pickle
import os.path
import gspread
from absl import app
from absl import flags
from oauth2client.service_account import ServiceAccountCredentials



# Lint as: python3
"""TODO(rischpater): DO NOT SUBMIT without one-line documentation for python-sheets-uploader.

TODO(rischpater): DO NOT SUBMIT without a detailed description of python-sheets-uploader.
"""

SCOPES = 'https://www.googleapis.com/auth/spreadsheets'


# FLAGS = flags.FLAGS

SPREADSHEET_KEY = '1kbl4iBLutedEhsJ6MjeVjTdr8mnP_MDVXqYvVBoTRgI'


def main(argv):
    if len(argv) > 1:
        raise app.UsageError('Too many command-line arguments.')

    # Authorize and get a client
    creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', SCOPES)

    print("authorize")

    client = gspread.authorize(creds)

    print("open")

    # Open the sheet
    sheet = client.open_by_key(SPREADSHEET_KEY)
    worksheet = sheet.worksheets()[0]

    # Test --- append a record to the 
    worksheet.insert_row(['foo', 'bar'])

if __name__ == '__main__':
  app.run(main)
