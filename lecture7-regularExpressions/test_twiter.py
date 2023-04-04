import pytest
from twiter import get_twitter_username

# url = "www.twitter.com/cibanez"
# url = "twitter.com/cibanez"

EXPECTED = "cibanez"


def test_invalid_url():
    assert get_twitter_username(input_url="https://www.google.com") == ""


def test_url_with_http_and_with_www():
    assert get_twitter_username(input_url="http://twitter.com/cibanez") == EXPECTED


def test_url_without_https_and_with_www():
    assert get_twitter_username(input_url="www.twitter.com/cibanez") == EXPECTED


def test_url_with_https_and_without_www():
    assert get_twitter_username(input_url="https://twitter.com/cibanez") == EXPECTED


def test_url_without_https_and_without_www():
    assert get_twitter_username(input_url="twitter.com/cibanez") == EXPECTED


def test_url_with_https_and_with_www():
    assert get_twitter_username(input_url="https://www.twitter.com/cibanez") == EXPECTED

