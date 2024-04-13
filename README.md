In order to make this work you need to:
1. Install python (https://realpython.com/installing-python/#how-to-install-python-on-windows). This project was created with Python 3.9.13
2. Follow the Allure Report installation (https://allurereport.org/docs/gettingstarted-installation/)
3. (Optional) If you want to set up a virtual python enviroment, please follow the next link for Windows: https://mothergeo-py.readthedocs.io/en/latest/development/how-to/venv-win.html
4. Run 'pip install -r /path/to/requirements.txt'
5. Have installed Google Chrome in your system. This project was created with Chrome 123.0.6312.123, if you have other Chrome version you need to repalce the /Global/chromedriver.exe with the correct version: https://chromedriver.chromium.org/downloads

To execute it you need to:
1. Make sure you are in the Global folder
2. Run the next commands in your terminal: python -m pytest --alluredir allure-results
3. Run the next commands in your terminal: allure serve allure-results
