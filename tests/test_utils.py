from unittest.mock import patch, mock_open, call
from darker_signs.utils import progress_bar, upload_file, download_file


@patch("darker_signs.utils.sleep", return_value=None)
@patch("darker_signs.utils.print")
def test_progress_bar(mock_print, mock_sleep):
    progress_bar(max=5, step=0.01)
    expected_calls = [
        call("\r0% |", end=""),
        call("\r1% /", end=""),
        call("\r2% -", end=""),
        call("\r3% \\", end=""),
        call("\r4% |", end=""),
        call("\r5% done"),
    ]
    mock_print.assert_has_calls(expected_calls)
    assert mock_print.call_count == 6


@patch("os.path.isfile", return_value=True)
@patch("darker_signs.utils.progress_bar")
def test_upload_file_success(mock_progress_bar, mock_isfile):
    result = upload_file("/fake/path/to/file.txt")
    mock_isfile.assert_called_once_with("/fake/path/to/file.txt")
    mock_progress_bar.assert_called_once_with(max=100, step=0.02)
    assert result is True


@patch("os.path.isfile", return_value=False)
@patch("darker_signs.utils.progress_bar")
def test_upload_file_failure(mock_progress_bar, mock_isfile):
    result = upload_file("/fake/path/to/nonexistent.txt")
    mock_isfile.assert_called_once_with("/fake/path/to/nonexistent.txt")
    mock_progress_bar.assert_not_called()
    assert result is False


@patch("darker_signs.utils.progress_bar")
@patch("builtins.open", new_callable=mock_open)
def test_download_file(mock_open, mock_progress_bar):
    result = download_file("/fake/path/to/file.txt", contents="Test content")
    mock_open.assert_called_once_with("/fake/path/to/file.txt", "w")
    mock_open().write.assert_called_once_with("Test content")
    mock_progress_bar.assert_called_once_with(max=100, step=0.02)
    assert result is True
