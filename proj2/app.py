from flask import Flask, render_template, Response, request
import cv2

app = Flask(__name__)
camera = cv2.VideoCapture(0)

def gen_frames(id):  # generate frame by frame from camera
    while True:
        # Capture frame-by-frame
        success, frame = camera.read()

        # read the camera frame
        # rects = find_faces(frame, face_model)
        frame = cv2.putText(frame, "hey", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (11, 11, 176),
                                2, cv2.LINE_AA)
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show results

@app.route('/')
def data():
    return render_template('guione.html', title="page")

@app.route('/video_feed')
def video_feed():
    # Video streaming route. Put this in the src attribute of an img tag
    return Response(gen_frames(id), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')