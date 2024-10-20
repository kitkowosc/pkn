import pytest
from io import StringIO
import sys
import random

# Mocking input and output
def mock_input_output(inputs):
    input_iter = iter(inputs)
    sys.stdin = StringIO('\n'.join(inputs))
    sys.stdout = StringIO()
    return sys.stdin, sys.stdout

def test_initial_state():
    from PapierKamienNozyce import wins, losses, draws
    assert wins == 0
    assert losses == 0
    assert draws == 0

def test_player_input():
    from PapierKamienNozyce import playerMove
    inputs = ["k", "p", "n", "w"]
    for move in inputs:
        sys.stdin, sys.stdout = mock_input_output([move])
        assert playerMove() == move

def test_computer_move():
    from PapierKamienNozyce import computerMove
    random.seed(1)  # Seed the random number generator for reproducibility
    assert computerMove() in ["k", "p", "n"]

def test_game_result():
    from PapierKamienNozyce import game_result
    assert game_result("k", "n") == "Wygrana!"
    assert game_result("p", "k") == "Wygrana!"
    assert game_result("n", "p") == "Wygrana!"
    assert game_result("k", "k") == "To remis!"
    assert game_result("p", "p") == "To remis!"
    assert game_result("n", "n") == "To remis!"

if __name__ == "__main__":
    pytest.main()