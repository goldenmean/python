'''
Data structure for Timeseries storage
'''

import matplotlib.pyplot as plt
from datetime import datetime

class TimeSeriesData:
    def __init__(self):
        self.data = {}

    def add_data(self, timestamp, value):
        """Add a new data point"""
        self.data[timestamp] = value

    def get_value(self, timestamp):
        """Retrieve value for a given timestamp"""
        return self.data.get(timestamp)

    def calculate_mean(self):
        """Calculate mean of all values"""
        return sum(self.data.values()) / len(self.data)

    def calculate_median(self):
        """Calculate median of all values"""
        sorted_values = sorted(self.data.values())
        n = len(sorted_values)
        if n % 2 == 0:
            return (sorted_values[n//2 - 1] + sorted_values[n//2]) / 2
        else:
            return sorted_values[n//2]

    def visualize(self):
        """Visualize the time series data"""
        timestamps = list(self.data.keys())
        values = list(self.data.values())

        plt.figure(figsize=(12, 6))
        plt.plot(timestamps, values)
        plt.xlabel('Timestamp')
        plt.ylabel('Value')
        plt.title('Time Series Data')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

# Example usage
ts_data = TimeSeriesData()

# Add sample data
ts_data.add_data(datetime(2023, 1, 1), 10)
ts_data.add_data(datetime(2023, 1, 2), 15)
ts_data.add_data(datetime(2023, 1, 3), 12)
ts_data.add_data(datetime(2023, 1, 4), 18)
ts_data.add_data(datetime(2023, 1, 5), 20)

print("Mean:", ts_data.calculate_mean())
print("Median:", ts_data.calculate_median())

ts_data.visualize()