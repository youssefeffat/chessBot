class ChessboardController:
    def __init__(self, stockfish_path, camera_id=0, hardware_port="/dev/ttyUSB0"):
        self.camera = CameraModule(camera_id)
        self.vision = VisionModule()
        self.chess_logic = ChessLogicModule(stockfish_path)
        self.move_processor = MoveProcessor()
        self.hardware_comm = HardwareCommModule(hardware_port)

    def start_game(self):
        # Step 1: Initialize board and capture the initial state
        initial_image = self.camera.capture_image()
        self.vision.calibrate_board(initial_image)
        
        while not self.chess_logic.board.is_game_over():
            # Step 2: Capture the player's move
            current_image = self.camera.capture_image()
            player_move = self.vision.detect_move(current_image)

            if player_move:
                print(f"Player move detected: {player_move}")
                self.chess_logic.apply_player_move(player_move)
                
                # Step 3: Get the bot's move
                bot_move = self.chess_logic.get_bot_move()
                print(f"Bot move: {bot_move}")
                
                # Step 4: Process and send the bot's move to the hardware
                move_dict = self.move_processor.process_move(bot_move)
                self.hardware_comm.send_move(move_dict)

    def shutdown(self):
        # Cleanup resources
        self.chess_logic.close_engine()
        self.camera.release()
        self.hardware_comm.close_connection()
