from flask import Flask, render_template
import cv2


app = Flask(__name__)



@app.route('/', methods = ['GET'])

def hello_word():
    return render_template('index.html')

@app.route('/mask', methods = ['POST', 'GET'])
def mask_or_no_mask():
    return render_template('mask.html')



if __name__ == "__main__":
    app.run(debug = True)
