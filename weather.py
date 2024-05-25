import requests


def check_weather():
    weath = ['Шереметьево', 'Череповца', 'Лондона']
    url_create = {'n':'', 'q':'', 'MTqu&':'','lang': 'ru'}
    for i in weath:
        url = f'https://wttr.in/{i}'
        response = requests.get(url, params=url_create)
        print(response.url)
        response.raise_for_status()
        print(response.text)

def main():
    check_weather()


if __name__ == "__main__":
    main()