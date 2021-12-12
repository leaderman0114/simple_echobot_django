# -------------------------
# simple echo bot in django
# -------------------------


# need telegram bot token in tgbot/management/commands/botpy at line 9


# create virtual environment
python -m venv env
# -------------------------

# linux and macOS
source env/bin/activate
# ---------------------

# windows
env/Scripts/activate
# ------------------

# install packages
pip install -r requirements.txt
# -----------------------------

# execute models
python manage.py makemigrations
python manage.py migrate
# -----------------------------

# run django project for admin panel
python manage.py runserver
# ------------------------

# run telegram bot project
python manage.py bot
# ------------------
