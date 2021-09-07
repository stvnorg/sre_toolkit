from datetime import datetime

def epoch_to_utc(epoch_time):
    return str(datetime.utcfromtimestamp(epoch_time))
