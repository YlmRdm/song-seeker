# song-seeker
It is a web based track search tool using Spotify API.

You can also see the live demo:

## Base Requirements

Python          3.10.1
Flask           2.0.22
gunicorn        20.1.0
jedi            0.18.1
Jinja2          3.0.3s
python-dotenv   0.19.2
click           8.0.3
requests        2.26.0
spotipy         2.19.0

You can also take a look at the all libraries that I used from [here](data/freeze.txt).
## Installation

It is recommended to work with virtualenv. To do that, you should apply with commands below:

> `pip install virtualenv`

> `virtualenv venv`

> `source venv/bin/activate`

After activated your virtual environment, you can install the requirements with command below:

> `pip install -r requirements.txt`

Thus, we are ready to run our flask server:

> `python app.py`

**NOTE: You can name your virtual environment whatever you want.**
