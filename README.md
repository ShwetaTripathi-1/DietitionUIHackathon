# DietitianUIHackathon
DietitianUIHackathon

1. Save Chromedriver at Python\Scripts folder\
~\Python\Scripts 
2. Launch virtual environment \
    virtualenv venv
3. Activate virtual environment\
    cd venv/scripts
    activate
4. Once inside virtual environment install dependencies\
    pip install -r requirements.txt

5. Run test cases using behave framework\
   cd Features\
   behave



5. Command to run allure report files\
    behave -f allure_behave.formatter:AllureFormatter -o reports/features

6. Command to generate allure report in HTML\
    allure serve reports/features  
7. 