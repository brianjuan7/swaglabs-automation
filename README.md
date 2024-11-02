# swaglabs-automation

This project automates a test ecommerce website, https://www.saucedemo.com/ using Python with pytest framework.

### Features

* POM pattern
* Full Python implementation
* Test reporting using pytest-html
* Screenshots on fail
* Logging capabilities
* Credentials encryption using cryptography library
* Supported browsers: Chrome, Firefox and Edge

### Built With

* Python 3.13
* pytest
* pytest-html
* Selenium
* cryptography

### Running the Project

1. Make sure that Python, pip and Java are installed in your machine

2. Install the libraries: pytest, pytest-html, Selenium and cryptography using pip, e.g.:
  ```sh
  pip install -U selenium
  ```
3. Running the test cases on the default browser, chrome
  ```sh
  pytest -v -s
  ```
4. Running the test cases on a specific browser
  ```sh
  pytest --browser "firefox" -v -s
  ```
5. Running specific test cases
  ```sh
  pytest -k "cart" -v -s
  ```
6. Pytest HTML report is located in **swaglabs-automation/resources/reports/report.html**, sample report:

   ![image](https://github.com/user-attachments/assets/57e750b3-41f9-4559-8c33-589bfe7af608)
