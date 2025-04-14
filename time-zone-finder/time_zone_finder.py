from datetime import datetime, timezone

# Dictionary mapping GMT offsets to their corresponding time zone names
time_zones = {
    "GMT-12:00": "AoE (Anywhere on Earth)",
    "GMT-11:00": "SST (Samoa Standard Time)",
    "GMT-10:00": "HST (Hawaii Standard Time)",
    "GMT-9:30": "MART (Marquesas Islands Time)",
    "GMT-9:00": "AKST (Alaska Standard Time)",
    "GMT-8:00": "PST (Pacific Standard Time)",
    "GMT-7:00": "MST (Mountain Standard Time)",
    "GMT-6:00": "CST (Central Standard Time)",
    "GMT-5:00": "EST (Eastern Standard Time)",
    "GMT-4:00": "AST (Atlantic Standard Time)",
    "GMT-3:30": "NST (Newfoundland Standard Time)",
    "GMT-3:00": "BRT (Brasilia Time)",
    "GMT-2:00": "GST (South Georgia Time)",
    "GMT-1:00": "CVT (Cape Verde Time)",
    "GMT+0:00": "UTC (Coordinated Universal Time)",
    "GMT+1:00": "CET (Central European Time)",
    "GMT+2:00": "EET (Eastern European Time)",
    "GMT+3:00": "MSK (Moscow Time)",
    "GMT+3:30": "IST (Iran Standard Time)",
    "GMT+4:00": "GST (Gulf Standard Time)",
    "GMT+4:30": "AFT (Afghanistan Time)",
    "GMT+5:00": "PKT (Pakistan Standard Time)",
    "GMT+5:30": "IST (Indian Standard Time)",
    "GMT+5:45": "NPT (Nepal Time)",
    "GMT+6:00": "BST (Bangladesh Standard Time)",
    "GMT+6:30": "CCT (Cocos Islands Time)",
    "GMT+7:00": "ICT (Indochina Time)",
    "GMT+8:00": "CST (China Standard Time)",
    "GMT+8:45": "CWST (Central Western Standard Time)",
    "GMT+9:00": "JST (Japan Standard Time)",
    "GMT+9:30": "ACST (Australian Central Standard Time)",
    "GMT+10:00": "AEST (Australian Eastern Standard Time)",
    "GMT+10:30": "LHST (Lord Howe Standard Time)",
    "GMT+11:00": "SBT (Solomon Islands Time)",
    "GMT+12:00": "NZST (New Zealand Standard Time)",
    "GMT+12:45": "CHAST (Chatham Standard Time)",
    "GMT+13:00": "TOT (Tonga Time)",
    "GMT+14:00": "LINT (Line Islands Time)"
    }

def get_gmt_time():

    # Get current time in GMT.
    # Returns: Tuple of current GMT hour and minute as integers.
    
    gmt_time = datetime.now(timezone.utc).strftime('%H:%M')
    L = gmt_time.split(':')
    gmth, gmtm = int(L[0]), int(L[1])
    return gmth, gmtm

def get_time():

    # Inputs the current time in local time zone.
    # Returns: Tuple of current local hour and minute as integers.

    intime = input("Enter the current time in 24 hrs format (HH:MM): ")
    parts = intime.strip().split(':')
    if len(parts) != 2:
        print("Invalid time format. Please use HH:MM.")
        return get_time()
    
    try:
        h, m = map(int, parts)
    except ValueError:
        print("Please enter numbers only for hours and minutes.")
        return get_time()

    return h, m


def calculate_offset(h,m,gmth,gmtm):

    # Calculates the offset from GMT in hours and minutes.
    # h- Local time hours, m- Local time minutes, gmth- GMT time hours and gmtm- GMT time minutes.
    # Returns: Tuple of offset hours and minutes as integers.

    th = h - gmth
    tm = m-gmtm
    
    # Adjust minutes and hours accordingly
    if tm < 0:
        tm += 60
        th -= 1
    elif tm >= 60:
        tm -= 60
        th += 1

    # Normalize hour difference to range -12 to +14 (based on time zones)
    if th > 14:
        th -= 24
    elif th < -12:
        th += 24

    return th, tm

def get_time_zone(th, tm, sign):

    # th- offset hours, tm- offset minutes, sign- sign string for GMT format
    # Returns: String of time zone.

    # Format time zone string
    T = f"GMT{sign}{th}:{tm:02}"
    try:
        loc = time_zones[T]
    except KeyError:
        return "Unknown Time Zone"
    return loc

 #-----main-----

gmth, gmtm = get_gmt_time()         # Get current GMT time
h, m = get_time()                   # Get user input time
th, tm = calculate_offset(h,m,gmth,gmtm)            # Calculate offset from GMT

sign = "+" if th > 0 else ""        # Determine sign
loc = get_time_zone(th, tm, sign)   # Get time zone name

if loc == "Unknown Time Zone":      # Print Result
    print("No Valid Time Zone")
else:
    print(f"Your Time Zone is GMT{sign}{th}:{tm} ({loc})")
input("Press Enter to exit...")
