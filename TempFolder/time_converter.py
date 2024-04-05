import datetime

def time_converter(timestamp):
    dt_object = datetime.datetime.fromtimestamp(timestamp)
    formatted_date = dt_object.strftime('%Y-%m-%d %H:%M:%S')
    return formatted_date