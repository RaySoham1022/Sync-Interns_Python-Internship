
URL SHORTENER
------------------------------

- Install Python
- Install Django
- 
- Make a .env file from .env.sample
- Fill the Appropriate Details in the .env file

## Run Locally

- Fork the Project

Clone the project

```bash
  git clone <https link>
```

Go to the project directory

```bash
  cd ShoteningURL
```

Create a new python virtual environment

```bash
  pip install virtualenv
```

```bash
  python -m venv venv
```

Activate the virtual environment

For Mac:

```bash
  source venv/bin/activate
```

For Windows:

```bash
  .\venv\Scripts\activate.bat
```

Install PyShorteners

```bash
  pip install pyshorteners
```

Make migrations

```bash
  python manage.py makemigrations
```

```bash
  python manage.py migrate
```

Start the server

```bash
  python manage.py runserver
```
