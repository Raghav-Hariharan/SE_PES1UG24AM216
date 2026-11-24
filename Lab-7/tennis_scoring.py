
def _validate_string(value, function_name):
    """Ensure that the input is a string."""
    if not isinstance(value, str):
        raise TypeError(f"{function_name} requires a string input")


def parse_score(text):
    """Parse a score in A-B format into two non-negative integers."""
    _validate_string(text, "parse_score")

    parts = text.strip().split("-")

    if len(parts) != 2:
        raise ValueError("Score must contain exactly one hyphen")

    try:
        a, b = (int(part.strip()) for part in parts)
    except ValueError:
        raise ValueError("Both scores must be valid integers") from None

    if a < 0 or b < 0:
        raise ValueError("Scores cannot be negative")

    return a, b


def game_lead(text):
    """Calculate the difference between two tennis point scores."""
    _validate_string(text, "game_lead")

    points = {"0": 0, "15": 1, "30": 2, "40": 3}

    parts = text.strip().split("-")

    if len(parts) != 2:
        raise ValueError("Score must contain exactly one hyphen")

    first, second = (part.strip() for part in parts)

    if first not in points or second not in points:
        raise ValueError("Points must be 0, 15, 30 or 40")

    return points[first] - points[second]


def set_spread(games_csv):
    """Calculate the difference between maximum and minimum game scores."""
    _validate_string(games_csv, "set_spread")

    parts = games_csv.strip().split(",")

    if not parts or any(not part.strip() for part in parts):
        raise ValueError("At least one valid game score is required")

    try:
        games = [int(part.strip()) for part in parts]
    except ValueError:
        raise ValueError("All game scores must be valid integers") from None

    if any(game < 0 for game in games):
        raise ValueError("Game scores cannot be negative")

    return max(games) - min(games)


def main():
    print("==== Running parse_score ====")
    user_input = input("Enter points won as A-B (e.g. 3-2): ")
    try:
        result = parse_score(user_input)
        print("Points A and B:", result)
    except (ValueError, TypeError) as error:
        print("Invalid input:", error)

    print("\n==== Running game_lead ====")
    user_input = input("Enter a game score (e.g. 40-30): ")
    try:
        result = game_lead(user_input)
        print("Lead in Points:", result)
    except (ValueError, TypeError) as error:
        print("Invalid input:", error)

    print("\n==== Running set_spread ====")
    user_input = input("Enter games won per set as CSV (e.g. 6,4,7): ")
    try:
        result = set_spread(user_input)
        print("Spread:", result)
    except (ValueError, TypeError) as error:
        print("Invalid input:", error)


if __name__ == "__main__":
    main()
