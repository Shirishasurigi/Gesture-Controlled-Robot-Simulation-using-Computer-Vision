from simulator_stream import generate_simulator
from flask import Flask, render_template, Response
import camera_stream

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/video_feed")
def video_feed():
    return Response(
        camera_stream.generate_frames(),
        mimetype='multipart/x-mixed-replace; boundary=frame'
    )

@app.route("/gesture")
def gesture():
    return {
        "gesture": camera_stream.current_gesture
    }

@app.route("/simulator")
def simulator():

    return Response(
        generate_simulator(),
        mimetype="multipart/x-mixed-replace; boundary=frame"
    )

if __name__ == "__main__":
    app.run(debug=True)