#!/bin/bash
cd ../
python3 -m venv myvenv1
source myvenv1/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py runserver

