# uwr25_remote/communicator.py

import serial
import time
from config import SerialConfig

class SerialCommunicator:
    def __init__(self):
        self.serial_port = None
        self.serial_config = SerialConfig()
        self.arduino_data = ""
        self.connected = False

    def open(self):
        while not self.connected:
            for i in range(13):
                port_name = f"COM{i}"
                if port_name in self.serial_config.skip_ports:
                    print(f"Skipping {port_name}")
                    continue
                try:
                    self.serial_port = serial.Serial(port_name, self.serial_config.speed, timeout=self.serial_config.timeout)
                    print(f"Connected to {port_name}")
                    self.connected = True
                    return
                except serial.SerialException as e:
                    print(f"Could not open {port_name}: {e}")
            print("No available COM port found, retrying in 3 seconds...")
            time.sleep(3)

    def communicate(self, cmd_vel):
        data_str = f"{cmd_vel['linear']['x']:.2f}," \
                   f"{cmd_vel['linear']['y']:.2f}," \
                   f"{cmd_vel['linear']['z']:.2f}," \
                   f"{cmd_vel['angular']['z']:.2f}\n"
        try:
            self.serial_port.write(data_str.encode())
        except Exception as e:
            print("Error sending data:", e)
        return data_str
    
    

    def read_from_arduino(self):
        if self.connected and self.serial_port and self.serial_port.is_open:
            try:
                if self.serial_port.in_waiting > 0:
                    self.arduino_data = self.serial_port.readline()
                    print("Received:", self.arduino_data)

            except Exception as e:
                print("Error reading data:", e)

    def close(self):
        if self.serial_port and self.serial_port.is_open:
            self.serial_port.close()
            print("Serial port closed")
        else:
            print("Serial port was not open")

    
