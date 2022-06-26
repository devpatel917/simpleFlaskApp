from flask import Flask, render_template, Response
import cv2


app = Flask(__name__)
# camera = cv2.VideoCapture(0)

# def generate_frames():
#     while True:
#         sucess,frame = camera.read()
#         if not sucess:
#             break
#         else:
#             ret,buffer = cv2.imencode('.jpg',frame)
#             frame = buffer.tobytes()

#         yield(b'--frame\r\n'
#                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/', methods = ['GET'])

def hello_word():
    return render_template('index.html')

@app.route('/mask', methods = ['POST', 'GET'])
def mask_or_no_mask():
    return render_template('mask.html')



if __name__ == "__main__":
    app.run(debug = True)
