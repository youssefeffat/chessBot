import chess
import chess.engine

class ChessLogicModule:
    def __init__(self, stockfish_path):
        self.board = chess.Board()
        self.engine = chess.engine.SimpleEngine.popen_uci(stockfish_path)
    
    def apply_player_move(self, player_move):
        try:
            self.board.push_uci(player_move)
        except ValueError:
            raise Exception(f"Illegal move: {player_move}")

    def get_bot_move(self):
        result = self.engine.play(self.board, chess.engine.Limit(time=2.0))
        bot_move = result.move
        self.board.push(bot_move)
        return bot_move.uci()

    def close_engine(self):
        self.engine.quit()
