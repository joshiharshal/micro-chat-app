analytics = []

def record_event(event: dict):
    analytics.append(event)

def get_events():
    return analytics
