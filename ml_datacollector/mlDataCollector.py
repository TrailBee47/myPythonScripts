import serial
import time
import os
import csv

# Function to list all available serial ports
def list_serial_ports():
    import serial.tools.list_ports
    ports = serial.tools.list_ports.comports()
    return [port.device for port in ports]

# Function to record data to a file
def record_data(file_path, tag):
    with open(file_path, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        while True:
            data = ser.readline().decode().strip()
            print(data)  # Echo received serial data
            
            # Exclude start and stop statements from the file
            if "Starting sample collection in" not in data and "Done... will start again in 60 seconds" not in data:
                if ',' in data:  # Check if data is comma-separated
                    if not any(c.isalpha() for c in data):  # Check if data contains alphabetic characters
                        csv_writer.writerow(data.split(','))  # Write data without quotes

            
            if "Done... will start again in 60 seconds" in data:
                break
    
    # Prompt for renaming the file
    new_file_name = input("Enter a new name for the recorded data file (without extension): ")
    new_file_name = f"{new_file_name}.csv"
    os.rename(file_path, new_file_name)
    print(f"Data recorded and saved as {new_file_name}")

# Get the user's selection for the serial port
serial_ports = list_serial_ports()
print("Available serial ports:")
for i, port in enumerate(serial_ports):
    print(f"{i + 1}. {port}")

selection = input("Select a serial port (enter number): ")
selected_port = serial_ports[int(selection) - 1]

# Establish the serial connection
ser = serial.Serial(selected_port, 9600, timeout=1)

# Enable or disable the echo of received serial data
enable_echo = True  # Change to False to disable echo
if enable_echo:
    ser.flushInput()  # Clear the input buffer

# Send the "training enable" command after establishing the connection
ser.write("training enable\n\r".encode())

# Get user input and send commands to the device
command = ""
while command.lower() != "exit":
    if command:  # Only ask for command after the first iteration
        command = input("Enter a command to send (or 'exit' to quit): ")

        # Convert '\n' and '\r' to their corresponding characters
        command = command.replace('\\n', '\n').replace('\\r', '\r')

        # Send the modified command with a newline character
        ser.write((command + '\n').encode())

    # Rest of the code...
    if ser.in_waiting:
        record_data("data.txt", "tag")

# Close the serial connection
ser.close()
