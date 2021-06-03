# Get Comicbook Character

A simple REST API using Flask to retrieve comic book characters.
Currently, only requesting data from Marvel Comics.

## Getting Started

Clone repo.

To connect to the Marvel Comics API, you will need to
get a **Public Key** and **Private Key**; these will be created
when you apply to **Get A Key** at the [Marvel Comics Developer Portal](https://developer.marvel.com/)

Once you have the required keys, rename **sample.env** to **.env**
and input the values there.

In the root directory:

```bash
# setup up environment
python -m virtualenv .

# activate
source ./Scripts/activate

# if necessary, install dependencies
pip install requests
pip install python-dotenv
pip install flask

# initialize app
python app.py

# app should be running on
# http://127.0.0.1:5000/

```

## Request a Character

To test, go to: [http://127.0.0.1:5000/character](http://127.0.0.1:5000/character)
and add a Marvel Comics character to the URL like so:

```bash
# pattern: http://127.0.0.1:5000/character/<character>
http://127.0.0.1:5000/character/deadpool

```

This should render a JSON object containing details on that character.
