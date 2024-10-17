# from __future__ import print_function
# import datetime
# import os.path
# from google.auth.transport.requests import Request
# from google.oauth2.credentials import Credentials
# from google_auth_oauthlib.flow import InstalledAppFlow
# from googleapiclient.discovery import build
#
# # Updated SCOPES to include full calendar access and event management
# SCOPES = [
#     'https://www.googleapis.com/auth/calendar',               # Full access to calendars
#     'https://www.googleapis.com/auth/calendar.events',         # View and edit events
#     'https://www.googleapis.com/auth/calendar.events.readonly' # View events only
# ]
#
# def main():
#     """Shows basic usage of the Google Calendar API.
#     Prints the start and name of the next 10 events on the user's calendar.
#     """
#     creds = None
#     # The file token.json stores the user's access and refresh tokens, and is
#     # created automatically when the authorization flow completes for the first time.
#     if os.path.exists('token.json'):
#         creds = Credentials.from_authorized_user_file('token.json', SCOPES)
#     # If there are no (valid) credentials available, let the user log in.
#     if not creds or not creds.valid:
#         if creds and creds.expired and creds.refresh_token:
#             creds.refresh(Request())
#         else:
#             flow = InstalledAppFlow.from_client_secrets_file(
#                 '/Users/abhinav/Desktop/ClientID_GoogleCalendar.json', SCOPES)
#             creds = flow.run_local_server(port=0)
#         # Save the credentials for the next run
#         with open('token.json', 'w') as token:
#             token.write(creds.to_json())
#
#     service = build('calendar', 'v3', credentials=creds)
#
#     # Call the Calendar API
#     now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
#     print('Getting the upcoming 10 events')
#     events_result = service.events().list(calendarId='primary', timeMin=now,
#                                           maxResults=10, singleEvents=True,
#                                           orderBy='startTime').execute()
#     events = events_result.get('items', [])
#
#     if not events:
#         print('No upcoming events found.')
#     for event in events:
#         start = event['start'].get('dateTime', event['start'].get('date'))
#         print(start, event['summary'])
#
#
# if __name__ == '__main__':
#     main()


# from __future__ import print_function
# import datetime
# import os.path
# from google.auth.transport.requests import Request
# from google.oauth2.credentials import Credentials
# from google_auth_oauthlib.flow import InstalledAppFlow
# from googleapiclient.discovery import build
# from whisper_transcribe import transcribe_audio
#
#
# # Updated SCOPES to include full calendar access and event management
# SCOPES = [
#     'https://www.googleapis.com/auth/calendar',               # Full access to calendars
#     'https://www.googleapis.com/auth/calendar.events',         # View and edit events
#     'https://www.googleapis.com/auth/calendar.events.readonly' # View events only
# ]
#
#
#
# # Function to interpret the transcription and return the command
# def interpret_command(transcription):
#     transcription = transcription.lower()
#
#     if 'add' in transcription or 'create' in transcription and 'event' in transcription:
#         return 'add'
#     elif 'edit' in transcription and 'event' in transcription:
#         return 'edit'
#     elif 'delete' in transcription and 'event' in transcription:
#         return 'delete'
#     else:
#         return None
#
#
# # Authenticate and authorize Google Calendar access
# def authenticate_google():
#     """Authenticate the user and return the service object for Google Calendar."""
#     creds = None
#     if os.path.exists('token.json'):
#         creds = Credentials.from_authorized_user_file('token.json', SCOPES)
#
#     if not creds or not creds.valid:
#         if creds and creds.expired and creds.refresh_token:
#             creds.refresh(Request())
#         else:
#             flow = InstalledAppFlow.from_client_secrets_file(
#                 '/Users/abhinav/Desktop/ClientID_GoogleCalendar.json', SCOPES)
#             creds = flow.run_local_server(port=0)
#         with open('token.json', 'w') as token:
#             token.write(creds.to_json())
#
#     return build('calendar', 'v3', credentials=creds)
#
#
# # Function to add a new event to the Google Calendar
# def add_event(service):
#     event = {
#         'summary': 'New Event',
#         'start': {
#             'dateTime': '2024-10-13T15:00:00+03:00',  # Example: 3 PM on October 13, 2024
#             'timeZone': 'Asia/Bahrain',
#         },
#         'end': {
#             'dateTime': '2024-10-13T16:00:00+03:00',
#             'timeZone': 'Asia/Bahrain',
#         }
#     }
#
#     event = service.events().insert(calendarId='primary', body=event).execute()
#     print(f'Event created: {event.get("htmlLink")}')
#
#
# # Function to edit an existing event
# def edit_event(service, event_id):
#     event = service.events().get(calendarId='primary', eventId=event_id).execute()
#
#     event['summary'] = 'Updated Event'
#     event['start']['dateTime'] = '2024-10-13T17:00:00+03:00'  # Example: new time
#     event['end']['dateTime'] = '2024-10-13T18:00:00+03:00'
#
#     updated_event = service.events().update(calendarId='primary', eventId=event_id, body=event).execute()
#     print(f'Event updated: {updated_event.get("htmlLink")}')
#
#
# # Function to delete an event
# def delete_event(service, event_id):
#     service.events().delete(calendarId='primary', eventId=event_id).execute()
#     print('Event deleted.')
#
#
# # Main function
# def main():
#     service = authenticate_google()
#
#     # Record audio and transcribe it (simplified flow)
#     transcription = transcribe_audio('output.wav')  # Get transcription from voice command
#
#     # Interpret the user's command
#     command = interpret_command(transcription)
#
#     if command == 'add':
#         add_event(service)
#     elif command == 'edit':
#         # You'll need to pass an event_id from your calendar to edit
#         edit_event(service, 'event_id_here')
#     elif command == 'delete':
#         # You'll need to pass an event_id from your calendar to delete
#         delete_event(service, 'event_id_here')
#     else:
#         print('Command not recognized')
#
#
# if __name__ == '__main__':
#     main()

from __future__ import print_function
import datetime
import os.path
import re
import dateparser
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import whisper

# If modifying these SCOPES, delete the file token.json.
SCOPES = [
    'https://www.googleapis.com/auth/calendar',
    'https://www.googleapis.com/auth/calendar.events',
    'https://www.googleapis.com/auth/calendar.events.readonly'
]


# Function to transcribe audio using Whisper
def transcribe_audio(audio_file):
    model = whisper.load_model("base")
    result = model.transcribe(audio_file)
    transcription = result['text']
    print(f"Transcription received: {transcription.strip()}")
    return transcription.strip()


# Updated parse_event_details function
def parse_event_details(transcription):
    # Use regex to match a date format like "October 21, 2024"
    date_match = re.search(
        r'\b(?:january|february|march|april|may|june|july|august|september|october|november|december)\b \d{1,2},? \d{4}',
        transcription, re.IGNORECASE)
    if date_match:
        date_str = date_match.group(0)
        event_date = dateparser.parse(date_str)
        print(f"Parsed date (from regex): {event_date}")
    else:
        event_date = None  # Default to None if no valid date is found
        print(f"No date found in transcription")

    # Adjusted time regex to capture formats like "10:00am", "10 am", "10 a.m."
    time_match = re.search(r'\b(\d{1,2}(:\d{2})?\s?(a\.m\.|p\.m\.|am|pm))\b', transcription, re.IGNORECASE)
    if time_match:
        time_str = time_match.group(0)
        print(f"Parsed time: {time_str}")
    else:
        time_str = "10:00am"  # Default time if no time is found
        print("No time found, defaulting to 10:00am")

    # Extract the event title by looking for phrases like "called" or "named"
    title_match = re.search(r'(called|named)\s(.+)', transcription)
    if title_match:
        title = title_match.group(2)
        print(f"Parsed title: {title}")
    else:
        title = "Untitled Event"  # Default title if not provided
        print("No title found, defaulting to 'Untitled Event'")

    return title, event_date, time_str


# Function to add an event to Google Calendar
def add_event(service, title, event_date, event_time):
    if event_date is None:
        print("Couldn't determine the event date. Please specify a valid date.")
        return

    # Format the event time properly
    if 'am' in event_time.lower() or 'pm' in event_time.lower():
        event_time_obj = datetime.datetime.strptime(event_time, '%I:%M%p').time()
    else:
        event_time_obj = datetime.datetime.strptime(event_time, '%H:%M').time()

    event_datetime = datetime.datetime.combine(event_date, event_time_obj).isoformat()

    event = {
        'summary': title,
        'start': {
            'dateTime': event_datetime,
            'timeZone': 'UTC',
        },
        'end': {
            'dateTime': (datetime.datetime.combine(event_date, event_time_obj) + datetime.timedelta(hours=1)).isoformat(),
            'timeZone': 'UTC',
        },
    }

    event = service.events().insert(calendarId='primary', body=event).execute()
    print(f'Event created: {event.get("htmlLink")}')


def main():
    """Main function to run the Google Calendar voice assistant."""
    creds = None
    if os.path.exists('.venv/token.json'):
        creds = Credentials.from_authorized_user_file('.venv/token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                '/Users/abhinav/Desktop/ClientID_GoogleCalendar.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('.venv/token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('calendar', 'v3', credentials=creds)

    transcription = transcribe_audio('.venv/output.wav')  # Get transcription from voice command
    title, event_date, event_time = parse_event_details(transcription)

    if event_date is not None:
        add_event(service, title, event_date, event_time)


if __name__ == '__main__':
    main()

