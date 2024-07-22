import instaloader
import csv

L = instaloader.Instaloader()

username = 'xxxxxxxxx'
password = 'xxxxxxxxx'
L.login(username, password)

target_account = 'xxxxxxxx'

profile = instaloader.Profile.from_username(L.context, target_account)

followers_list = []

for follower in profile.get_followers():
    followers_list.append(follower.username)

chunk_size = 1000
for i in range(0, len(followers_list), chunk_size):
    chunk = followers_list[i:i + chunk_size]
    file_name = f"{target_account}_followers_part_{i//chunk_size + 1}.csv"
    with open(file_name, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Username'])
        for follower in chunk:
            writer.writerow([follower])
    print(f"Guardado {file_name}")

print(
    f"Todos los seguidores de {target_account} han sido guardados en archivos CSV.")
