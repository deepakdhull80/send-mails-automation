@echo OFF
echo         %DATE%
echo Installing packages ...


python /setup/get-pip.py

pip install secure-smtplib
pip install ssl
pip install email