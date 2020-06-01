### Features
DDT (Data-driven Testing) with Python Selenium Webdriver and CSV files. Very useful if you have test cases that contains the same test steps.
In this exemple we are going to test website: https://www.zara.com/pl/

### Prepering environment:

Python, Selenium, ddt library, Chromedriver

You can easly install it on Ubuntu:

### Python 3.x

`pip install -r requirements.txt`

You also need to install ChromeDriver

`sudo ln -s /your_project_folder/DDT-with-Python-Selenium/chromedriver /usr/bin`

The folder structure for exemple looks like:

    
    ├── data
    │   ├── bad_adres.cvc
    │   ├── bad_city.cvc
    │   ├── bad_emails.cvc
    │   └── ...
    ├── library
    │   └── GetData.py
    ├── pages
    │   ├── base_page.py
    │   ├── home_page.py
    │   ├── login_page.py
    │   └── register_page.py
    ├── tests
    │   ├── base_test.py
    │   └── register_private_page_test.py
    │── locators.py
    └── run.py
    └── readme.md
    └── requirements.txt


In directory "data" we store the csv files. 

Directory  "library" include a file where is a function to read the specific csv files.

Directory "pages" contain Clases for specific pages and directory tests contains tests.

Finally in file locators.py we store selectors. File run.py create test suite.

readme.md - this file 

requirements.txt (pip freeze > requirements.txt)
