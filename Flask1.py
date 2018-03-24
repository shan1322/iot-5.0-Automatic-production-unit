from flask import Flask
import serial
ser = serial.Serial('COM5',9600,timeout=1)
read=ser.readline().decode()
app = Flask(__name__)
@app.route('/')
def main():
    return read
if (__name__ == "__main__"):
    app.run(debug=True,host='0.0.0.0')
