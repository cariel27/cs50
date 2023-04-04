import re


def get_twitter_username(input_url: str) -> str:
    if matches := re.search(pattern=r"^(?:https?://)?(?:www\.)?twitter\.com/([a-z0-9_]+)$", string=input_url, flags=re.IGNORECASE):
        return matches.group(1)
    else:
        return ""
