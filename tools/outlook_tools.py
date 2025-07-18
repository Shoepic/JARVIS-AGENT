
import os
from O365 import Account
from langchain.tools import Tool

# Load credentials from environment
credentials = (
    os.getenv("MICROSOFT_CLIENT_ID"),
    os.getenv("MICROSOFT_CLIENT_SECRET")
)

account = Account(credentials)

# Authenticate on first run (will prompt browser login)
if not account.is_authenticated:
    account.authenticate(scopes=[
        'basic', 'calendar_all', 'mailbox_all'
    ])

schedule = account.schedule()
calendar = schedule.get_default_calendar()

def list_events():
    events = calendar.get_events(limit=5)
    return "\n".join([f"{e.subject} at {e.start}" for e in events])

tools = [
    Tool(
        name="list_calendar_events",
        func=lambda x: list_events(),
        description="Use this to see the next few calendar events."
    )
]
