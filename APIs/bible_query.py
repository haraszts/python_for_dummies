import requests
def get_bible_verse(reference):
    url = f"http://bible_api.com/{reference.replace(' ', '%20')}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(f"\n{data['reference']}\n")
        print(data['text'])
    else:
        print("verse not found or invalid reference")

ref = input()
get_bible_verse(ref)
#nincs tesztelve még