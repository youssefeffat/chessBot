from ChessboardController import ChessboardController
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class main:
    def __init__(self):
        self.stockfish_path = os.getenv("STOCKFISH_PATH")
        self.camera_id = int(os.getenv("CAMERA_ID"))
        self.hardware_port = os.getenv("HARDWARE_PORT")
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

    # Create the main game object
    game = main()
    # Initialize and run the game
    game.initialize()
    game.run()
