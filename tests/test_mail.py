import pytest
from unittest.mock import patch, mock_open, call
import json
from darker_signs.mail import Mail

mailbox_data = [
    {
        "from": "zrio",
        "subject": "unittest",
        "message": "let's test",
        "read": False,
    },
    {
        "from": "security",
        "subject": "another unittest",
        "message": "let's test again",
        "read": True,
    },
]


@pytest.fixture
def mail_obj():
    with patch("builtins.open", mock_open(read_data=json.dumps(mailbox_data))):
        return Mail("fake_mailbox.json")


def test_mail_init(mail_obj):
    assert mail_obj.mailbox == mailbox_data
    assert mail_obj.mailbox_path == "fake_mailbox.json"


@patch("builtins.open", new_callable=mock_open)
@patch("json.dump")
def test_add_message(mock_json_dump, mock_open_func, mail_obj):
    new_message = {
        "from": "Charlie",
        "subject": "Hello",
        "message": "How are you?",
        "read": False,
    }

    mail_obj.add_message(from_user="Charlie", subject="Hello", message="How are you?")

    assert mail_obj.mailbox[-1] == new_message
    mock_open_func.assert_called_once_with("fake_mailbox.json", "w")
    mock_json_dump.assert_called_once_with(
        mail_obj.mailbox, mock_open_func(), indent="\t"
    )


@patch("builtins.print")
def test_print_mailbox(mock_print, mail_obj):
    mail_obj._Mail__print_mailbox()
    expected_calls = [
        call("1 N> zrio:unittest"),
        call("2  > security:another unittest"),
    ]
    mock_print.assert_has_calls(expected_calls)


@patch("builtins.input", return_value="1")
@patch("builtins.print")
def test_print_message_valid(mock_print, mock_input, mail_obj):
    result = mail_obj._Mail__print_message("1")
    assert result is True
    expected_calls = [
        call("From: zrio"),
        call("Subject: unittest"),
        call(""),
        call("let's test"),
    ]
    mock_print.assert_has_calls(expected_calls)


@patch("builtins.input", return_value="1")
@patch("builtins.print")
def test_print_message_invalid(mock_print, mock_input, mail_obj):
    result = mail_obj._Mail__print_message("3")
    assert result is False
    mock_print.assert_called_once_with("Message not found")
