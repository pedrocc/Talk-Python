import requests
import bs4
import collections

weather_result = collections.namedtuple('WeatherResult', 'conditions, temperature, scale, local')


def main():
    print_header()
    code = input('Que zip code americano você deseja consultar? ')
    html = get_html_web(code)
    condicoes_cidade = get_weather_from_html(html)

    print("As condições da cidade {} são de {}{} no {}".format(condicoes_cidade.local, condicoes_cidade.temperature, condicoes_cidade.scale, condicoes_cidade.conditions) )

def print_header():
    print('======================================')
    print('    WELCOME TO THE FORECAST APP')
    print('====================================== \n')

def get_html_web(code):
    url = 'https://www.wunderground.com/weather-forecast/{}'.format(code)
    response_url = requests.get(url)
    return response_url.text

def get_weather_from_html(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    local = soup.find(id='location').find('h1').get_text()
    condition = soup.find(id='curCond').find(class_='wx-value').get_text()
    temperature = soup.find(id='curTemp').find(class_='wx-data').find(class_='wx-value').get_text()
    scale = soup.find(id='curTemp').find(class_='wx-data').find(class_='wx-unit').get_text()
    local = clean_local(local)
    retorno = weather_result(conditions=condition, temperature=temperature, scale=scale, local=local)
    return (retorno)

def clean_local(local):
    x = local.split()
    local = x[0]
    return local

if __name__ == '__main__':
    main()
