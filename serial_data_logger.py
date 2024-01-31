import csv
import datetime
import serial
import time
import sys

def read_serial_data(serial_connection):
    """
    Reads data from the serial port.
    """
    if serial_connection.in_waiting > 0:
        line = serial_connection.readline().decode('utf-8').rstrip()
        try:
            return float(line)
        except ValueError:
            print(f"Invalid data: {line}")
            return None
          
          

def main(com_port):
    """
    Main function to read serial data and write to a CSV file.
    """
    # Use the provided COM port
    ser = serial.Serial(com_port, 9600, timeout=1)

    # Generate a unique file name with the current timestamp
    csv_filename = 'data_log_' + datetime.datetime.now().strftime('%Y-%m-%d-%I%M%S%p') + '.csv'
    value = ''

    # Write header to the CSV file
    with open(csv_filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Timestamp', 'Value'])
        
    data_buffer = []  # Buffer to store data points

    try:
        while True:
            value = read_serial_data(ser)
            x = (value - 0.1312)/1.2961

            if value is not None:
                timestamp = datetime.datetime.now().strftime('%Y-%m-%d %I:%M:%S %p')
                data_buffer.append([timestamp, value])  # Add data to buffer

                if len(data_buffer) >= 10:
                  # Open the file in append mode and write the data
                  with open(csv_filename, 'a', newline='') as file:
                      writer = csv.writer(file)
                      # write single rows instead of writerows to force CR/LF on each line
                      for data_point in data_buffer:
                          writer.writerow(data_point)            
                      file.flush() 
                  data_buffer.clear()

            time.sleep(0.1)  # Delay between readings in milliseconds (100 ms)

    except KeyboardInterrupt:
        # write whats left in the buffer
        with open(csv_filename, 'a', newline='') as file:
            writer = csv.writer(file)
            #writer.writerow([timestamp, value])
            for data_point in data_buffer:
                writer.writerow(data_point)            
            file.flush()      
        print("Data logging stopped")
    finally:
        ser.close()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 serial_data_logger.py COM_PORT")
    else:
        com_port = sys.argv[1]
        main(com_port)
