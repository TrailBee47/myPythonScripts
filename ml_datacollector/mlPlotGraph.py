import csv
import matplotlib.pyplot as plt

def plot_csv_data(file_name):
    data = []

    with open(file_name, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data.append([float(value) for value in row])

    num_sensors = len(data[0])  # Number of sensors

    # Generate x-values as indices of the data points
    x_values = list(range(1, len(data) + 1))

    # Plot each sensor's data
    for sensor_idx in range(num_sensors):
        y_values = [row[sensor_idx] for row in data]
        plt.plot(x_values, y_values, label=f"Sensor {sensor_idx+1}")

    plt.xlabel('Time')
    plt.ylabel('Sensor Value')
    plt.title('Sensor Data Plot')
    plt.legend()
    plt.show()

# Get the file name from user input
file_name = input("Enter the CSV file name: ")

# Plot the CSV data
plot_csv_data(file_name)

