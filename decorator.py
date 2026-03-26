from datetime import datetime, timedelta
from functools import wraps
 
def filter_last_5_minutes(func):#decorator
    @wraps(func)
    def wrapper(logs):
        result = func(logs)
        # Current time
        now = datetime.now() #3:30 PM current time
        threshold = now - timedelta(minutes=5) #3:25pm
        # Filter logs based on timestamp
        filtered_logs = []
        for log in result:
            timestamp = log.get("timestamp")
            # Handle missing or invalid timestamp
            if isinstance(timestamp, datetime) and timestamp >= threshold:
                filtered_logs.append(log)
        return filtered_logs
    return wrapper
 
 
@filter_last_5_minutes
def get_logs(logs):
    return logs
 
 
# Example usage
logs = [
    {"message": "log1", "timestamp": datetime.now() - timedelta(minutes=2)},
    {"message": "log2", "timestamp": datetime.now() - timedelta(minutes=10)},
    {"message": "log3", "timestamp": datetime.now() - timedelta(minutes=14)},
    {"message": "log4", "timestamp": datetime.now() - timedelta(minutes=12)},
    {"message": "log5", "timestamp": datetime.now() - timedelta(minutes=3)}]
 
print(get_logs(logs))
 