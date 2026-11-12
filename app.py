import json
import os
from flask import Flask, render_template, abort

app = Flask(__name__)

DATA_PATH = os.path.join(os.path.dirname(__file__), "data", "projects.json")
with open(DATA_PATH) as f:
    PROJECTS = json.load(f)


@app.route("/")
def index():
    return render_template("index.html", projects=PROJECTS[:3])


@app.route("/projects")
def projects():
    return render_template("projects.html", projects=PROJECTS)


@app.route("/projects/<slug>")
def project_detail(slug):
    project = next((p for p in PROJECTS if p["slug"] == slug), None)
    if not project:
        abort(404)
    return render_template("project.html", project=project)


if __name__ == "__main__":
    app.run(debug=True)

    