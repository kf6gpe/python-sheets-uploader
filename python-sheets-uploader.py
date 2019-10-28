from __future__ import print_function
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import csv
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


FLAGS = flags.FLAGS
flags.DEFINE_string('spreadsheet_key', None, 'Spreadsheet key')
flags.DEFINE_string('csv_file', None, 'csv file to import')
flags.DEFINE_string('credentials', None, 'sheets credentials')
flags.mark_flag_as_required('spreadsheet_key')
flags.mark_flag_as_required('csv_file')
flags.mark_flag_as_required('credentials')


def main(argv):

    SPREADSHEET_KEY = FLAGS.spreadsheet_key
    CSV_FILE = FLAGS.csv_file
    CREDENTIALS = FLAGS.credentials
    # Authorize and get a client
    creds = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS, SCOPES)

    print("authorize")

    client = gspread.authorize(creds)

    print("open")

    # Open the sheet
    sheet = client.open_by_key(SPREADSHEET_KEY)
    worksheet = sheet.worksheets()[0]

    # Read the CSV
    with open(CSV_FILE, newline='') as csvfile:
      data = csv.reader(csvfile, delimiter=',')
      for row in data:
        print(row)
        worksheet.append_row(row)
        # Don't run afoul of quota limitations.
        # time.sleep(1)

if __name__ == '__main__':
  app.run(main)
