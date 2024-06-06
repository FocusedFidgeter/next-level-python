from unittest.mock import patch
from solution import file_manager

def test_file_manager_write():
    with patch("solution.open") as mock_open:
        with file_manager("sample.txt", "w") as file:
            file.write("Hello, world!")

        mock_open.assert_called_once_with("sample.txt", "w", encoding="utf8")
        mock_open.return_value.close.assert_called_once()
