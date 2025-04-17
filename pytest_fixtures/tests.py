import pytest

@pytest.fixture
def db_connection():
    conn = create_db_connection()
    yield conn
    conn.close()

def test_db_query(db_connection):
    assert db_connection.query('SELECT 1').fetchone() == (1,) is not None

