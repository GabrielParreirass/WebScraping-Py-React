from flask import Flask, json
from flask_cors import CORS
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json
import time

app = Flask(__name__)
cors = CORS(app)


@app.route('/api', methods=['GET'])
async def hello():

    SITE_LINK = 'https://www.sofascore.com/team/football/cruzeiro/1954'
    SITE_MAP = {
        "fields": {
            "jogos": {
                'xpath_timeCasa': '/html/body/div[1]/main/div/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div[2]/a[$$NUMBER$$]/div/div/div[3]/div[1]',
                'xpath_timeFora': '/html/body/div[1]/main/div/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div[2]/a[$$NUMBER$$]/div/div/div[3]/div[2]',
                'xpath_golsCasa': '/html/body/div[1]/main/div/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div[2]/a[$$NUMBER$$]/div/div/div[5]/div[1]',
                'xpath_golsFora': '/html/body/div[1]/main/div/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div[2]/a[$$NUMBER$$]/div/div/div[5]/div[2]'
            }
        }
    }

    DIC_JOGOS = {
        "jogos": {

        }
    }

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(executable_path='C:\\chromeDriver', options=chrome_options)

    time.sleep(2)
    driver.get(SITE_LINK)
    time.sleep(5)

    time.sleep(1)

    elemento_atual = 1

    while elemento_atual < 9:
        time_casa = driver.find_element_by_xpath(
            SITE_MAP['fields']['jogos']['xpath_timeCasa'].replace("$$NUMBER$$", str(elemento_atual)))

        time_fora = driver.find_element_by_xpath(
            SITE_MAP['fields']['jogos']['xpath_timeFora'].replace("$$NUMBER$$", str(elemento_atual)))

        gols_casa = driver.find_element_by_xpath(
            SITE_MAP['fields']['jogos']['xpath_golsCasa'].replace("$$NUMBER$$", str(elemento_atual)))

        gols_fora = driver.find_element_by_xpath(
            SITE_MAP['fields']['jogos']['xpath_golsFora'].replace("$$NUMBER$$", str(elemento_atual)))

        DIC_JOGOS["jogos"].update({elemento_atual: {
            "time_casa": f"{time_casa.text}", "time_fora": f"{time_fora.text}", "gols_casa": gols_casa.text, "gols_fora": gols_fora.text}})

        elemento_atual += 1

    response = app.response_class(
        response=json.dumps(DIC_JOGOS),
        status=200,
        mimetype='application/json'
    )
    return response


app.run()
