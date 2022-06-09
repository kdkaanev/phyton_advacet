import re

email = input()
regex = r'"(?P<user>^[a-zA-z]{4,})(?P<symbol>[@])\w+(?P<domain>[.a-z]+)'
username = []
symbol = []
domain = []


email_elements = re.finditer(regex, email)
for element in email_elements:
    username.append(element.group('user'))
    symbol += element.group('symbol')
    domain += element.group('domain')
print(username)

    