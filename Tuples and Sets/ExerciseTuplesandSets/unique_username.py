usernames_number = int(input())
unique_username = set()
for _ in range(usernames_number):
    username = input()
    unique_username.add(username)
[print(user) for user in unique_username]
