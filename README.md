# BEST IMPRESSIONS / PITCH app
## By `devjamesnjoroge`

<img src='https://github.com/devjamesnjoroge/best-impressions/blob/master/app/static/images/banner.jpg'>


## ABOUT

### A Flask app implementing user authentication and uses postgresql database to store pitches uploaded by users

## USER STORIES

A user can:
- See the pitches other people have posted.
- Vote on the pitch they liked and give it a downvote or upvote.
- Leave a comment when signed in.
- Receive a welcoming email once I sign up.
- View the pitches I have created in my profile page.
- Submit a pitch in any category.
- View the different categories.

## TECHNOLOGIES USED

- HTML
- CSS
- PYTHON
- POSTGRESQL

## REQUIREMENTS

- Local machine
- A code editor e.g. VSCODE
- Installed postgresql

## INSTALLATION

```
git clone https://github.com/devjamesnjoroge/best-impressions
cd best-impressions
```

**Launch virtual environment**
```
python -m venv virtual

source virtual/bin/activate
```

**Install all the app dependencies**
```
pip install -r requirements.txt 
```

**Database Setup**
edit the sqlalchemy url in config.py
replace with your database in the format:
```
SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://{User Name}:{password}@localhost/{database name}

```
change the production string in manage.py to development

**Environmental variables**

Create a start.sh file in root folder 
Edit file
```
export SECRET_KEY=<YOURS>
export MAIL_USERNAME=<your email>
export MAIL_PASSWORD=<mail password>
python3 manage.py server
```

## AUTHORS INFO

* [Linkedin](https://www.linkedin.com/in/devjamesnjoroge)
* [Email](njorogehjames20@gmail.com)

## LICENSE

[MIT LICENSE](LICENSE)

[Go back to the top](#)

