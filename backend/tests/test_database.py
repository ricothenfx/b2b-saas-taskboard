from app.core.database import engine


def test_database_connection():

    conn = engine.connect()

    assert conn is not None

    conn.close()