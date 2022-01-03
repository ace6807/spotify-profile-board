# Spotify Profile Board


## Configuration
1. Create and activate python virtual environment
1. Install dependencies

```bash
> pip install -r requirements.txt
```

2. Create a `.env` using `sample.env` as a template
3. Configure application at https://developer.spotify.com/dashboard  and populate `.env`: 
4. Init db

```bash
> export FLASK_APP=run.py
> flask shell

>>> db.create_all()
```

5. Run app
```bash
> export FLASK_ENVIRONMENT=development
> export FLASK_APP=run.py
> flask run
```