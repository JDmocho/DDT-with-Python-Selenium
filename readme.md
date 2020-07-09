### Features
DDT (Data-driven Testing) with Python Selenium Webdriver and CSV files. Very useful if you have test cases that contains the same test steps.
In this exemple we are going to test website: https://www.zara.com/pl/

### Environment

- chromedriver 2.24.1
- ddt 1.4.1
- pip 20.1.1
- selenium 3.141.0
- Chrome 83.0.4103.116

### Before you start:

Install selenium, ddt. You can use pip (packege manager)


`sudo apt install python3-pip`

`pip install -r requirements.txt`

You need also Chromedriver or Geckodriver.

- Chromedriver is located on website:

https://sites.google.com/a/chromium.org/chromedriver/downloads

- Geckodriver you can download from:

https://github.com/mozilla/geckodriver/releases

Or use drivers from projects (files: chromedriver and geckodrivers)

Our driver should be in the following location: `/usr/local/bin/`

You can create symbolic link

`sudo ln -s /your_project_folder/DDT-with-Python-Selenium/chromedriver /usr/local/bin`


### The folder structure for example looks like:

    
    ├── data
    │   ├── incorrect_city_registration.csv
    │   ├── incorrect_emails_account.csv
    │   ├── incorrect_emails_registration.csv
    │   └── ...
    ├── library
    │   └── GetData.py
    ├── tests
    │   ├── base_test.py
    │   ├── login_form.py
    │   ├── register_form.py
    │   ├── search_form.py
    │   └── shoping_cart.py
    │── locators.py
    └── run.py
    └── readme.md
    └── requirements.txt


In directory "data" we store the csv files. 

Directory  "library" include a file where is a function to read the specific csv files.

Finally in file locators.py we store selectors. 

File run.py create test suite.

readme.md - this file 

requirements.txt (pip freeze > requirements.txt)
