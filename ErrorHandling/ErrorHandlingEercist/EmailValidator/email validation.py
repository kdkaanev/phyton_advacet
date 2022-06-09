from custom_exception import InvalidDomainError, NameTooShortError,MustContainAtSymbolError

valid_domain ={'.com', '.bg', '.net', '.org'}

while True:
    text = input()
    if text == 'End':
        break
    email_parts = text.split('@')
    if len(email_parts) > 2:
        continue
    elif len(email_parts) < 2:
        raise MustContainAtSymbolError("Email must contain @")
    else:
        username = email_parts[0]
        if len(username) < 5:
            raise NameTooShortError("Name must be more than 4 characters")

        domain = f".{email_parts[1].split('.')[-1]}"
        if domain not in valid_domain:
            raise InvalidDomainError(f"Domain must be one of the following: {', '.join(valid_domain)}")

    print('Email is valid')

