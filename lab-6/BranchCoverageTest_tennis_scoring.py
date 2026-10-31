
import pytest

from tennis_scoring import game_score, set_winner, match_status


# Game score: negative point validation
def test_negative_player_a():
    with pytest.raises(ValueError):
        game_score(-1, 0)


def test_negative_player_b():
    with pytest.raises(ValueError):
        game_score(0, -1)


# Game score: normal scoring
def test_normal_score():
    assert game_score(1, 2) == "15-30"


def test_normal_score_reverse():
    assert game_score(2, 1) == "30-15"


# Game score: deuce and advantage
def test_deuce():
    assert game_score(3, 3) == "deuce"


def test_deuce_with_ahead_player():
    assert game_score(4, 4) == "deuce"


def test_game_a_from_deuce():
    assert game_score(5, 3) == "game A"


def test_game_b_from_deuce():
    assert game_score(3, 5) == "game B"


def test_advantage_a():
    assert game_score(4, 3) == "advantage A"


def test_advantage_b():
    assert game_score(3, 4) == "advantage B"


# Game score: outside deuce
def test_game_a_outside_deuce():
    assert game_score(4, 2) == "game A"


def test_game_b_outside_deuce():
    assert game_score(2, 4) == "game B"


# Set winner: normal set results
def test_set_winner_a():
    assert set_winner(6, 4) == "A"


def test_set_winner_b():
    assert set_winner(4, 6) == "B"


def test_set_a_not_enough_games():
    assert set_winner(5, 4) is None


def test_set_a_insufficient_lead():
    assert set_winner(6, 5) is None


def test_set_b_not_enough_games():
    assert set_winner(4, 5) is None


def test_set_b_insufficient_lead():
    assert set_winner(5, 6) is None


# Set winner: tiebreak conditions
def test_tiebreak_winner_a():
    assert set_winner(7, 6) == "A"


def test_tiebreak_winner_b():
    assert set_winner(6, 7) == "B"


def test_other_tiebreak_score():
    assert set_winner(6, 6) is None


# Match status
def test_match_a_wins():
    assert match_status(2, 0, 3) == "A wins"


def test_match_b_wins():
    assert match_status(0, 2, 3) == "B wins"


def test_match_decider():
    assert match_status(1, 1, 3) == "decider"


def test_match_in_progress():
    assert match_status(0, 0, 3) == "in progress"


def test_match_in_progress_with_one_set():
    assert match_status(1, 0, 3) == "in progress"
