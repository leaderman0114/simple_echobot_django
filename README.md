### simple echo bot in django

```
need telegram bot token in tgbot/management/commands/botpy at line 9
```

### create virtual environment
```bash
python -m venv env
```

### activate virtual environment
linux 
```bash
source env/bin/activate
```

windows
```bash
env\Scripts\activate
```


### install packages
```bash
pip install -r requirements.txt
```

### execute models
```bash
python manage.py makemigrations
python manage.py migrate

or

python manage.py makemigrations <appname>
python manage.py migrate <appname>
```

### run django project for admin panel
```bash
python manage.py runserver
```

### run telegram bot project
```bash
python manage.py bot
```
