# Contacts Manager web app

## Requirements:
- see requirements.txt file

## Run the app
- clone the repo
- run `flask run` at the root level
- open `http://127.0.0.1:5000/contacts` in a browser

## Run the tests on backend
- set the driver path to your chromedriver in the test_frontend file:

driver = webdriver.Chrome("/usr/local/bin/chromedriver")`

- go to `server/tests`
- run `pytest`

## Run the tests on frontend

- go to `static`
- run `jest -u`

## Design

![app design](https://image.ibb.co/fv2qGp/Zrzut_ekranu_2018_09_25_o_15_49_43.png)
