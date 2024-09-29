import pytest
import json
from unittest.mock import patch, mock_open
from system.dns import Dns

dns_data = {
    "test-server.com": {"alias": "1.1.1.1"},
    "1.1.1.1": {
        "name": "test-server.com",
        "module_name": "test_server",
        "class_name": "TestServer",
        "port_mapping": {"80": "http", "22": "ssh", "21": "ftp"},
    },
}


@pytest.fixture
def dns_obj():
    with patch("builtins.open", mock_open(read_data=json.dumps(dns_data))):
        return Dns("fake_dns.json", "test_campaign")


def test_dns_init(dns_obj):
    assert dns_obj.world == dns_data


def test_find_with_alias(dns_obj):
    server = dns_obj.find("test-server.com")
    assert server == dns_data["1.1.1.1"]


def test_find_without_alias(dns_obj):
    server = dns_obj.find("1.1.1.1")
    assert server == dns_data["1.1.1.1"]


def test_find_with_error(dns_obj):
    server = dns_obj.find("2.2.2.2")
    assert server is None
