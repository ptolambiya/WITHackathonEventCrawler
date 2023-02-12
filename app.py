from flask import Flask, render_template
import MeetupTech

app = Flask(__name__, template_folder='uitemplates',static_folder='uitemplates')

@app.route("/")
def index():
    tech_events = MeetupTech.get_all_meetups()
    return render_template("index.html", events=tech_events)

@app.route("/tech")
def tech():
    tech_events = MeetupTech.get_all_meetups()
    return render_template("tech.html", events=tech_events)

@app.route("/sports")
def sports():
    sports_events = [
        {"name": "World Cup 2022", "date": "2022-06-01"},
        {"name": "Summer Olympics 2023", "date": "2023-08-01"},
        {"name": "Super Bowl 2024", "date": "2024-02-01"},
    ]
    return render_template("sports.html", events=sports_events)

if __name__ == "__main__":
    app.run()
