from flask import Flask
from utils import load_name_candidates, page_profile, page_skills

app = Flask(__name__)


@app.route("/")
def pages_index():
    return load_name_candidates()


@app.route("/candidates/<int:index>")
def pages_profile(index):
    return page_profile(index)


@app.route("/skills/<skill>")
def pages_skills(skill):
    return page_skills(skill)


app.run()
