from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

@app.route('/<random_string>')
def random_string(random_string):
    return "".join(reversed(random_string))


@app.route('/get-mode')
def get_mode():
    return os.getenv('MODE')


# WHAT UP

if __name__ == '__main__':
    app.run(port=5000)