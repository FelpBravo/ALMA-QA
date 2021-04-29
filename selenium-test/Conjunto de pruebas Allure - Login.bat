echo. #################### PRUEBAS ##################
O:
cd O:\physharm\selenium-test
python -m pytest .\src\tests\test_directory\test_directory_001.py --alluredir .\src\allure-results

python -m pytest .\src\tests\test_directory_grid\test_carpetas_001.py --alluredir .\src\allure-results

python -m pytest .\src\tests\test_directory_grid\test_visualizar_001.py --alluredir .\src\allure-results

python -m pytest .\src\tests\test_documents\test_documents_001.py --alluredir .\src\allure-results

python -m pytest .\src\tests\test_login\test_signin.py --alluredir .\src\allure-results