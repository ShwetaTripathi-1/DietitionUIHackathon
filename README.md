# DietitianUIHackathon
DietitianUIHackathon

1. Launch virtual environment \
    virtualenv venv
2. Activate virtual environment\
    cd venv/scripts
    activate
3. Once inside virtual environment install dependencies\
    pip install -r requirements.txt

4.  Command to run allure report files\
    behave -f allure_behave.formatter:AllureFormatter -o reports/features

5. Command to generate allure report in HTML\
    allure serve reports/features  