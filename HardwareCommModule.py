import serial

class HardwareCommModule:
    def __init__(self, port, baudrate=9600):
        self.serial_connection = serial.Serial(port, baudrate)

    def send_move(self, move_data):
        if isinstance(move_data, dict):
            move_data = json.dumps(move_data)
        self.serial_connection.write(move_data.encode())

    def close_connection(self):
        self.serial_connection.close()
