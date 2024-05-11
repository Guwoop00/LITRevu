# LITRevu

## Project Overview

LITRevu is a social networking platform designed for book enthusiasts to share their opinions, reviews, and recommendations on various literary works. Whether you're an avid reader, a literature enthusiast, or simply someone looking for your next great read, LITRevu provides a space to connect with like-minded individuals, discover new books, and engage in meaningful discussions about literature.

## Project Initialization

### MacOS and Linux:
In the terminal, navigate to the desired directory.
###### • Clone the project
```
git clone https://github.com/Guwoop00/LITRevu.git
cd LITRevu 
python3 -m venv env 
source env/bin/activate
```

### Windows:
In Windows PowerShell, navigate to the desired directory.
###### • Clone the project
```
git clone https://github.com/Guwoop00/LITRevu.git
cd LITRevu 
python -m venv env 
.\env\Scripts\activate
```

###### • Install required packages
Make sure all the packages are installed.
```
pip install -r requirements.txt
```

Then go to LITRevu\ and make migrations
```
python manage.py makemigrations
```
And
```
python manage.py migrate
```

## Usage

1. Launch the Django server:
```
python manage.py runserver
```

2. In your preferred web browser, go to http://127.0.0.1:8000/

### Features

- Sign up and log in;
- Browse a feed containing posts and reviews from you and followed users;
- Browse your own feed;
- Create review and request tickets;
- Write reviews, in response to tickets or independently;
- View, edit, or delete your own posts;
- Follow or unfollow other users.
