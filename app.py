from flask import Flask, render_template, render_template_string, request, Response


app = Flask(__name__)

@app.route('/', methods = ['GET'])

def hello_word():
    return render_template('index.html')




if __name__ == "__main__":
    app.run(debug = True)
