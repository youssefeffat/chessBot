import chess
import chess.engine as chess_engine
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class ChessLogicModule:
    def __init__(self, stockfish_path):
        self.board = chess.Board()
        self.engine = chess.engine.SimpleEngine.popen_uci(stockfish_path)
    
    def apply_player_move(self, player_move):

        """
        Push player move into the board 
        player move type :, ex:"e2e4"
        """
        try:
            self.board.push_uci(player_move)
        except ValueError:
            self.close_engine()
            raise Exception(f"Illegal move: {player_move}")

    def get_bot_move(self):
        result = self.engine.play(self.board, chess_engine.Limit(time=2.0))
        bot_move = result.move
        self.board.push(bot_move)
        return bot_move.uci()

    def close_engine(self):
        self.engine.quit()

stockfish_path = os.getenv("STOCKFISH_PATH")
print("stockfish path : ", stockfish_path)
chess = ChessLogicModule(stockfish_path)
chess.apply_player_move("e2e4")
botMove = chess.get_bot_move()
print(botMove)
chess.apply_player_move("e4e5")
botMove = chess.get_bot_move()
print(botMove)
chess.close_engine()

