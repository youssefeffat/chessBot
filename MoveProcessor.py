import json

class MoveProcessor:
    def __init__(self):
        pass

    def process_move(self, move):
        source_square = move[:2]
        destination_square = move[2:]
        return {
            "source_square": source_square,
            "destination_square": destination_square
        }

    def format_move_for_hardware(self, move_dict):
        return json.dumps(move_dict)

    def save_move_as_json(self, move_dict, filename="bot_move.json"):
        with open(filename, 'w') as f:
            json.dump(move_dict, f, indent=4)
