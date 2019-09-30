# albert_api
##### BY JAVIER AVITIA

## Setup
1. Download or Clone the repository from **[GitHub][gh]**.
2. Once copied onto your Desktop, open up a terminal and navigate into the folder *albert_api* > *albertapp*.
3. Execute the follow command in the terminal:
	pip install -r requirements.txt
4. Confirm the following packages are installed by running pip freeze:
- Django==2.2.5
- pytz==2019.2
- sqlparse==0.3.0
5. Execute the following to start the app:
	python manage.py runserver 8080
6. The app is now running on **[Port 8080][8080]**

## Endpoints
1. Validate Credit Card Number [cc_api/validate_cc][val]
2. Get Major Industry Identifier (MII) [cc_api/get_mii][mii]
3. Get Issuer Identification Number (IIN) [cc_api/get_iin][iin]
4. Get Account Number [cc_api/get_acc_num][acc]
5. Get Check Digit [cc_api/get_check_digit][check]

[gh]: https://github.com/JavierAvitia/albert_api "Click here!"
[8080]: http://127.0.0.1:8080/ "Albert API (click to open)"
[val]: http://127.0.0.1:8080/cc_api/validate_cc "Validate Credit Card"
[mii]: http://127.0.0.1:8080/cc_api/get_mii "Get MII"
[iin]: http://127.0.0.1:8080/cc_api/get_iin "Get IIN"
[acc]: http://127.0.0.1:8080/cc_api/get_acc_num "Get Account Number"
[check]: http://127.0.0.1:8080/cc_api/get_check_digit "Get Check Digit"