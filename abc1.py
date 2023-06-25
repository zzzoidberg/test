import getpass
from hashlib import sha512
from unittest.mock import patch
from urllib.parse import urlparse

import pyperclip


def main():
    if netloc := urlparse(pyperclip.paste()).netloc:
        pwd = getpass.getpass("")
        domain = ".".join(netloc.lower().split(".")[-2:])
        digest = int(sha512(f"{domain}{pwd}".encode("utf8")).hexdigest(), 16)
        pyperclip.copy("".join(_func(digest))[:32])


def _func(n):
    while n > 0:
        n, r = divmod(n, 96)
        if (c := chr(r + 32)) not in r" \"'(),./:;<>?[\]`{|}~":
            yield c


@patch("getpass.getpass", return_value="12345")
@patch("pyperclip.paste", return_value="https://docs.python.org/library/")
@patch("pyperclip.copy")
def test(mock_copy, _, __):
    main()
    mock_copy.assert_called_with("h9uKafsNm_grvM0y&3#x2i$hFSphEf26")


if __name__ == "__main__":
    main()
