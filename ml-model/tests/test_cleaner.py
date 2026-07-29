from app.services.cleaner import clean_text


def test_clean_text_lowercases():
    assert clean_text("Hello World") == "hello world"


def test_clean_text_removes_special_characters():
    assert clean_text("Python3.11 & FastAPI!") == "python3 11 fastapi"


def test_clean_text_collapses_multiple_spaces():
    assert clean_text("too    many     spaces") == "too many spaces"


def test_clean_text_strips_leading_trailing_whitespace():
    assert clean_text("   padded text   ") == "padded text"


def test_clean_text_handles_empty_string():
    assert clean_text("") == ""
