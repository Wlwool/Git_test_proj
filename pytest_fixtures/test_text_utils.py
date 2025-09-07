import pytest
from text_utils import normalize_text


@pytest.mark.parametrize("inp,expected", [
    ("  Hello  WORLD!!  ", "hello world"),
    ("NoTrailing?", "notrailing"),
    ("many   spaces", "many spaces"),
])
def test_normalize_success(inp, expected):
    assert normalize_text(inp) == expected

def test_normalize_none():
    with pytest.raises(ValueError):
        normalize_text(None)

