#!/usr/bin/env python
from urllib.parse import quote

board_name = "BOARD_NAME"
encoded_board_name = quote(board_name)
print(encoded_board_name) 