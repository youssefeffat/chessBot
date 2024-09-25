class main:
    def __init__(self, stockfish_path, camera_id=0, hardware_port="/dev/ttyUSB0"):
        self.stockfish_path = stockfish_path
        self.camera_id = camera_id
        self.hardware_port = hardware_port
        self.controller = None

    def initialize(self):
        """Initialize the controller and game components."""
        print("Initializing game...")
        # Initialize the ChessboardController with necessary components
        self.controller = ChessboardController(self.stockfish_path, self.camera_id, self.hardware_port)
        print("Game initialized successfully.")

    def run(self):
        """Run the main game loop."""
        try:
            print("Starting game...")
            # Start the game and handle moves
            self.controller.start_game()
        except Exception as e:
            print(f"An error occurred during the game: {e}")
        finally:
            # Ensure resources are cleaned up properly at the end
            print("Shutting down game...")
            self.controller.shutdown()
            print("Game shutdown completed.")

    def shutdown(self):
        """Gracefully shutdown the game."""
        if self.controller:
            self.controller.shutdown()

if __name__ == "__main__":
    # Define paths and configurations
    stockfish_path = "/path/to/stockfish"  # Update with actual Stockfish path
    camera_id = 0  # Default camera (change if needed)
    hardware_port = "/dev/ttyUSB0"  # Port for hardware communication

    # Create the main game object
    game = main(stockfish_path, camera_id, hardware_port)
    
    # Initialize and run the game
    game.initialize()
    game.run()
