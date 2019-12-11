from flask import Flask, render_template, Response
import random
import time
from firebase import firebase

app = Flask(__name__)

firebase = firebase.FirebaseApplication('https://room-b58d2.firebaseio.com/', None)

@app.route("/graph")
def hello():
  number = random.randint(0, 100)
  return render_template("web.html", randInt=number)

@app.route('/progress')
def progress():
	def generate():
		while True:
			yield "data:" + str(callFirebase()) + "\n\n"
			time.sleep(2)

	return Response(generate(), mimetype='text/event-stream')

def callFirebase():
  result = firebase.get('/Room502', None)
  return result

callFirebase()

if __name__ == '__main__':
  app.run(debug=True, threaded=True)