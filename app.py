
#import flask class
from flask import Flask, render_template, url_for

# set an instance of the Flask class application
app = Flask(__name__)
#to run the above app in your local server type $env:FLASK_APP="application_name.py"
#then type flask run
#endpoints and functions behind them


posts = [
    {
        'author':'Corey shafer',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'November 7, 2023'
    },
    {
        'author':'Jorden Monroe',
        'title': 'Blog post 2',
        'content': 'second post content',
        'date_posted': 'November 8, 2023'
    }
]

@app.route("/")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title="About")

@app.route("/PowerBI")
def PowerBI():
    return render_template('powerbi.html', title="Power BI")



if __name__ == '__main__':
    app.run(debug=True)