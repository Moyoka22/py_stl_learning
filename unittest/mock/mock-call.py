from unittest import mock
from unittest.mock import call  # * can be used to prepare assertations

if __name__ == "__main__":
    mock = mock.Mock()
    cursor = mock.connection.cursor.return_value
    cursor.execute.return_value = ["foo"]

    cur = mock.connection.cursor()
    cur.execute("select * from DUAL")
    expected = [call.connection.cursor(), call.cursor().execute("select * from DUAL")]
    mock.mock_calls == expected  # * True
