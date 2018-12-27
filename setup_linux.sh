echo 'Setup app'
virtualenv venv -p python3
source venv/bin/activate
git clone https://github.com/MarianMandziuk/simple-app.git
cd simple-app
pip install -r requirements.txt
cd simpleapp
python manage.py runserver