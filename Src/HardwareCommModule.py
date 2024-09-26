import serial

class HardwareCommModule:
    def __init__(self, port, baudrate):
        self.serial_connection = serial.Serial(port, baudrate)

    def send_move(self, move_data):
        if isinstance(move_data, dict):
            move_data = transform_data(move_data)
        self.serial_connection.write(move_data.encode())
    
    # TODO: Implement the transform_data method
    def transform_data(self, data):
        """
        Transform data to a format that can be sent to the hardware
        """
        msg = data
        return msg    
    
    def close_connection(self):
        self.serial_connection.close()
