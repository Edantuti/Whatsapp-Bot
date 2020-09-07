from datetime import datetime
from pytz import timezone
def checkTime():
  IST = datetime.now(timezone('UTC')).astimezone(timezone('Asia/Kolkata')).strftime('%d')
  return IST