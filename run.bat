call D:\Selenium_Hydrid_Framework\venv\Scripts\activate
timeout /t 5
pytest -s -v -m "regression" --html=./Reports/report.html testCases/ --browser chrome
call D:\Selenium_Hydrid_Framework\venv\Scripts\deactivate
