from app import greet


def test_greet():
    assert greet("Shayan") == "bye, Shayan!"  # nosec B101
