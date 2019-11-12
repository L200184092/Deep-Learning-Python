# -----------------------
# stdin
#
# Contoh penggunaan stdin
# -----------------------

import sys

while True:
    data = sys.stdin.readline()
    if not data:
        break

    print(data, end = "")
