**creating a virtual environment**
mkvirtualenv django3 --python=/usr/bin/python3.6
**installing django**
pip install django 
workon django3
python -m django --version 
cd ~
git clone https://github.com/Mukullight/django.git
cd dj4e-samples (master)
virtualenv .venv
source .venv/bin/activate
python --version
pip install -r requirements.txt 
python manage.py check 
python manage.py makemigrations
python manage.py migrate 
python manage.py createsuperuser --username dj4e-samples
python manage.py changepassword dj4e-samples
dj4e__nn_!
#### 
**Building your application**
