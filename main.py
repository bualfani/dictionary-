from flask import Flask, render_template
import pandas as pd
app = Flask(__name__)


filename = 'dictionary.csv'
df = pd.read_csv(filename)
@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<word>/")
def about(word):
    detail = df.loc[df['word'] == word]['definition'].squeeze()
    return {"Description": detail,
                "Word": word}


if __name__ == "__main__":
    app.run(debug=True)