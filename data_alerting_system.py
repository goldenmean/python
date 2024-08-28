'''
Designing an alert system for Samsara’s internal sensor data acquisition system.
Here’s a basic example of how you might implement an alert when the state of the
system changes
'''


import time

# Sample thresholds for different parameters
THRESHOLDS = {
    'temperature': 5.0,  # degrees Celsius
    'pressure': 10.0,    # psi
    'status': 1          # status change
}

# Sample previous sensor data
previous_data = {
    'temperature': 25.0,
    'pressure': 100.0,
    'status': 0
}

def get_current_sensor_data():
    # This function should interface with the actual sensors to get current data
    # For this example, we'll use dummy data
    return {
        'temperature': 30.0,
        'pressure': 112.0,
        'status': 1
    }

def check_for_alerts(previous_data, current_data):
    alerts = []
    for key in current_data:
        if abs(current_data[key] - previous_data[key]) > THRESHOLDS[key]:
            alerts.append(f"Alert: {key} changed from {previous_data[key]} to {current_data[key]}")
    return alerts

while True:
    current_data = get_current_sensor_data()
    alerts = check_for_alerts(previous_data, current_data)
    if alerts:
        for alert in alerts:
            print(alert)
    previous_data = current_data
    time.sleep(5)  # Check every 5 seconds