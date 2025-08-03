import os
import random
import time
from datetime import datetime
from dotenv import load_dotenv

import pywhatkit  # pip install pywhatkit python-dotenv

from quotes import QUOTES

def pick_quote() -> str:
    return random.choice(QUOTES)

def main():
    load_dotenv()
    group_id = os.getenv("GROUP_ID")
    if not group_id:
        raise SystemExit("Missing GROUP_ID in .env")

    quote = pick_quote()
    msg = f"Quote of The Day ({datetime.now().date()}):\n\"{quote}\" \n-Marcus Aurelius"

    # Send immediately; keep tab open briefly so pywhatkit can press 'Enter'
    # pywhatkit expects the *group ID* (from the group invite link), not the group name.
    # Example GROUP_ID format: "ABCD1234EFG...=="
    pywhatkit.sendwhatmsg_to_group_instantly(group_id, msg, wait_time=20, tab_close=True, close_time=5)

    # A small sleep helps ensure the tab close happens after send
    time.sleep(6)

if __name__ == "__main__":
    main()
