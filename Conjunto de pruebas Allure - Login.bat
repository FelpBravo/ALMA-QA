echo. #################### PRUEBAS ##################
O:

cd O:\physharm\selenium-test\src

del /f /q .\allure-results

cd ..

python -m pytest .\src\tests\test_login\test_signin.py --alluredir .\src\allure-results

python -m pytest .\src\tests\test_panel\test_panel_001.py --alluredir .\src\allure-results

python -m pytest .\src\tests\test_directory\test_directory_001.py --alluredir .\src\allure-results

python -m pytest .\src\tests\test_directory\test_directory_002.py --alluredir .\src\allure-results

python -m pytest .\src\tests\test_directory\test_directory_003.py --alluredir .\src\allure-results

python -m pytest .\src\tests\test_directory\test_directory_004.py --alluredir .\src\allure-results

python -m pytest .\src\tests\test_directory\test_directory_005.py --alluredir .\src\allure-results

python -m pytest .\src\tests\test_directory\test_directory_006.py --alluredir .\src\allure-results

python -m pytest .\src\tests\test_directory\test_directory_007.py --alluredir .\src\allure-results

python -m pytest .\src\tests\test_directory\test_directory_008.py --alluredir .\src\allure-results

python -m pytest .\src\tests\test_directory\test_directory_009.py --alluredir .\src\allure-results

python -m pytest .\src\tests\test_directory\test_directory_remove.py --alluredir .\src\allure-results

python -m pytest .\src\tests\test_directory\test_directory_010.py --alluredir .\src\allure-results

python -m pytest .\src\tests\test_users_groups\test_users\test_users_001.py --alluredir .\src\allure-results

python -m pytest .\src\tests\test_users_groups\test_users\test_users_002.py --alluredir .\src\allure-results

python -m pytest .\src\tests\test_users_groups\test_users\test_users_003.py --alluredir .\src\allure-results

python -m pytest .\src\tests\test_users_groups\test_groups\test_groups_001.py --alluredir .\src\allure-results

python -m pytest .\src\tests\test_users_groups\test_groups\test_groups_002.py --alluredir .\src\allure-results

python -m pytest .\src\tests\test_search\test_simple\test_search_001.py --alluredir .\src\allure-results

python -m pytest .\src\tests\test_search\test_simple\test_search_002.py --alluredir .\src\allure-results

python -m pytest .\src\tests\test_search\test_simple\test_search_003.py --alluredir .\src\allure-results

python -m pytest .\src\tests\test_grid\test_tree\test_tree_001.py --alluredir .\src\allure-results

python -m pytest .\src\tests\test_grid\test_visualize\test_visualize_001.py --alluredir .\src\allure-results

python -m pytest .\src\tests\test_grid\test_delete\TestDelete001.py --alluredir .\src\allure-results

python -m pytest .\src\tests\test_grid\test_delete\TestDelete002.py --alluredir .\src\allure-results

python -m pytest .\src\tests\test_grid\test_delete\TestDelete003.py --alluredir .\src\allure-results

python -m pytest .\src\tests\test_grid\test_download\test_download_001.py --alluredir .\src\allure-results

python -m pytest .\src\tests\test_grid\test_download\test_download_002.py --alluredir .\src\allure-results

python -m pytest .\src\tests\test_grid\test_edit\test_edit_001.py --alluredir .\src\allure-results

python -m pytest .\src\tests\test_grid\test_edit\test_edit_002.py --alluredir .\src\allure-results

python -m pytest .\src\tests\test_grid\test_attach\test_attach_001.py --alluredir .\src\allure-results

python -m pytest .\src\tests\test_grid\test_attach\test_attach_002.py --alluredir .\src\allure-results

python -m pytest .\src\tests\test_grid\test_commentary\test_commentary_001.py --alluredir .\src\allure-results

python -m pytest .\src\tests\test_grid\test_commentary\test_commentary_002.py --alluredir .\src\allure-results

python -m pytest .\src\tests\test_grid\test_share\test_share_001.py --alluredir .\src\allure-results

python -m pytest .\src\tests\test_grid\test_share\test_share_002.py --alluredir .\src\allure-results

python -m pytest .\src\tests\test_search\test_advanced\test_advanced_001.py --alluredir .\src\allure-results

python -m pytest .\src\tests\test_search\test_advanced\test_advanced_002.py --alluredir .\src\allure-results

python -m pytest .\src\tests\test_search\test_advanced\test_advanced_003.py --alluredir .\src\allure-results

python -m pytest .\src\tests\test_search\test_advanced\test_advanced_004.py --alluredir .\src\allure-results

python -m pytest .\src\tests\test_document_upload\test_upload\test_upload_001.py --alluredir .\src\allure-results

python -m pytest .\src\tests\test_document_upload\test_upload\test_upload_002.py --alluredir .\src\allure-results

python -m pytest .\src\tests\test_document_upload\test_upload\test_upload_003.py --alluredir .\src\allure-results

python -m pytest .\src\tests\test_document_upload\test_upload\test_upload_004.py --alluredir .\src\allure-results

python -m pytest .\src\tests\test_document_upload\test_upload\test_upload_005.py --alluredir .\src\allure-results

python -m pytest .\src\tests\test_document_upload\test_upload\test_upload_006.py --alluredir .\src\allure-results

python -m pytest .\src\tests\test_document_upload\test_upload\test_upload_007.py --alluredir .\src\allure-results

python -m pytest .\src\tests\test_document_upload\test_upload\test_upload_008.py --alluredir .\src\allure-results

python -m pytest .\src\tests\test_document_upload\test_upload\test_upload_009.py --alluredir .\src\allure-results

python -m pytest .\src\tests\test_document_upload\test_upload\test_upload_010.py --alluredir .\src\allure-results

python -m pytest .\src\tests\test_document_upload\test_upload_flow\test_flow_001.py --alluredir .\src\allure-results

python -m pytest .\src\tests\test_document_upload\test_upload_flow\test_flow_002.py --alluredir .\src\allure-results

python -m pytest .\src\tests\test_document_upload\test_upload_flow\test_flow_003.py --alluredir .\src\allure-results

python -m pytest .\src\tests\test_document_upload\test_upload_flow\test_flow_004.py --alluredir .\src\allure-results

python -m pytest .\src\tests\test_document_upload\test_upload_flow\test_flow_005.py --alluredir .\src\allure-results

python -m pytest .\src\tests\test_document_upload\test_upload_flow\test_flow_006.py --alluredir .\src\allure-results

python -m pytest .\src\tests\test_document_upload\test_upload_flow\test_flow_007.py --alluredir .\src\allure-results

python -m pytest .\src\tests\test_document_upload\test_upload_flow\test_flow_008.py --alluredir .\src\allure-results

python -m pytest .\src\tests\test_document_upload\test_upload_flow\test_flow_009.py --alluredir .\src\allure-results