from flask import Flask

app=Flask(__name__)

@app.route("/")
def home():
    return "Under Construction"

if __name__=="__main__":
    app.run(port=9828,debug=True)