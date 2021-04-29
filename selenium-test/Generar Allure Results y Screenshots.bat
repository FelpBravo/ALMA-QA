echo. ##########TESTS LOGIN ALLURE#############
O:
cd O:\physharm\selenium-test
.\environment\Scripts\activate.bat
cd .\src\tests
allure.bat generate ..\allure-results --output ..\allure-report --clean
cd..
allure open --port 5000
pause