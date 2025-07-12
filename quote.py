import requests

def generate_quote():
    response = requests.get("https://zenquotes.io/api/random")
    if response.status_code != 200:    
        return 'Failed to fetch a quote'
    
    data = response.json()
    quote = data[0]['q']
    author = data[0]['a']

    return f'{quote} - {author}'


if __name__ == "__main__":
    quote = generate_quote()
    print(quote)


