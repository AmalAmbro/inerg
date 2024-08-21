# Project setup
create virtual environment "env"

# python should be greater than 3.9
python3 -m venv env
source env/bin/activate

# install requirements
pip install -r requirements.txt

# migrate
python manage.py migrate

# create superuser
python manage.py createsuperuser

# load excel data
python manage.py load_well_data well_data.xls

# run server
# as per task running at port 8080 (default will be 8000)
python manage.py runserver 8080

# Goto
http://localhost:8080/data
