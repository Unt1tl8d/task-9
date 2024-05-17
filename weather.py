import requests



def weather():
    weath = ['Шереметьево', 'Череповца', 'Лондона']
    for i in weath:    
        url = f'https://wttr.in/{i}?n?q?MTqu&lang=ru'
        response = requests.get(url)
        response.raise_for_status()
        print(response.text)

def main():
    weather()


if __name__ == "__main__":
    main()