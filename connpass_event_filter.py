from connpass import Connpass
import pytz
from datetime import datetime
from dateutil import parser

def sort_by_started_at(events):
    return sorted(events, key=lambda event: event['started_at'])

def remove_past_events(events):
    utc = pytz.UTC
    date_now = utc.localize(datetime.utcnow())
    # date_now = parser.parse('2018-03-24T15:00:00+09:00')
    future_events = []
    for event in events:
        # print(json.dumps(event, ensure_ascii=False, indent=2))
        if 'started_at' in event and parser.parse(event['started_at']) > date_now:
            future_events.append(event)
        elif 'ended_at' in event and parser.parse(event['ended_at']) > date_now:
            future_events.append(event)
    return future_events

def get_events(series_id):
    events = []
    try:
        return Connpass().search(series_id=[series_id])['events']
    except ConnectionError as e:
        print("Cannot get events because of ConnectionError.")
        print(e)
    except JSONDecodeError as e:
        print("Cannot get events because of JSONDecodeError. (Maybe connpass is in maintenance)")
        print(e)

