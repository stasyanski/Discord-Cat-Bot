import requests

cat_dict = ['cat', 'cats', 'kitten', 'kittens', 'kitty', 'kitties', 'feline', 'felines', 'meow', 'purr', 'paws', 'whiskers', 'claws', 'tail', 'fur', 'purr', 'pussy',
            'puss', 'pussycat', 'pussycats', 'kittycat', 'kittycats', 'kitty-cat', 'kitty-cats']

def response(user_input: str) -> str:
    lowered: str = user_input.lower()
    if lowered in cat_dict:
        url = "https://api.thecatapi.com/v1/images/search"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()[0]['url'] 
        else:
            return "Cats are sleeping... Try again later!"
