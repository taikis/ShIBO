from __future__ import print_function
import datetime
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar']
CAL_NAME = 'work by ShIBO'


def cred():
    '''認証のための関数

    Returns
    -------
    Credential
        認証トークン
    '''
    creds = None
    if os.path.exists('cred/token.json'):
        creds = Credentials.from_authorized_user_file(
            'cred/token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'cred/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('cred/token.json', 'w') as token:
            token.write(creds.to_json())
    return creds


service = build('calendar', 'v3', credentials=cred())


def readEvent10():

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
    print('Getting the upcoming 10 events')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                          maxResults=10, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])


def searchCalendar(calName):
    page_token = None
    calendar_items = []
    while True:
        calendar_list = service.calendarList().list(pageToken=page_token).execute()
        for calendar_list_entry in calendar_list['items']:
            calendar_items.append(calendar_list_entry)
        page_token = calendar_list.get('nextPageToken')
        if not page_token:
            break
    for calendar_list_entry in calendar_items:
        if calendar_list_entry['summary'] == calName:
            return calendar_list_entry['id']
    return None


def getCalenderId():
    calendar_id = searchCalendar(CAL_NAME)
    # ない場合は作る
    if calendar_id is None:
        calendar = {
            'summary': CAL_NAME,
            'timeZone': 'Asia/Tokyo'
        }
        
        calendar_id = service.calendars().insert(body=calendar).execute()['id']
    print(calendar_id)
    return calendar_id


def createEvent(dicts, calendar_id):
    for event_dict in dicts:
        event = {
            'summary': event_dict["subject"],
            'start': {
                'dateTime': event_dict["startDate"].isoformat(),
                'timeZone': 'Asia/Tokyo',
            },
            'end': {
                'dateTime': event_dict["endDate"].isoformat(),
                'timeZone': 'Asia/Tokyo',
            },
        }
        event = service.events().insert(calendarId=calendar_id, body=event).execute()


if __name__ == '__main__':
    # readEvent10(creds)
    createEvent(getCalenderId())
