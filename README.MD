Build your Todo List software by using Python Flask, Tailwindcss, Nodejs, Firebase

# To install virtualenv package in mac

```
pip3 install virtualenv
```

# To install virtualenv package in win

```
pip install virtualenv
```

# To create virtualenv in mac

```
python3 -m venv env
```

# To create virtualenv in win

```
python -m venv env
```

# To start the the app in mac

```
python3 app.py
```

# To start the the app in windows

```
python app.py
```

# To export the GUI into exe in mac

```
pyinstaller --name="ToDo" --paths=env/lib/python3.10/site-packages  --onefile --add-data="templates:templates" --add-data="static:static" --add-data="config:config"  app.py --noconsole --noconfirm
```

# To export the GUI into exe in win

```
pyinstaller --name="ToDo" --paths=env/Lib/site-packages  --onefile --add-data "templates;templates" --add-data "static;static" --add-data "config;config"  app.py --noconsole --noconfirm
```