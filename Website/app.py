# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, render_template
from flask import request
from werkzeug.utils import secure_filename
import os
from test import get_predictions
# from test import get_predictions
# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
# @app.route('/')
# # ‘/’ URL is bound with hello_world() function.
# def hello_world():
# 	return 'Hello World'

@app.route('/', methods=['GET', 'POST'])
def classify():
    error = None
    print(request.method)

    if request.method == 'POST':
        print(request.files)
        file = request.files["fileupload"]
        filename = secure_filename(file.filename)
        print(file, filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        pred = get_predictions(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        data_original = pred[0]
        data = []
        for val in data_original:
             data.append(str(val))
        return render_template('index.html', data=data, ok=True)
    return render_template('index.html', error=error)

# main driver function
if __name__ == '__main__':

	# run() method of Flask class runs the application
	# on the local development server.
	app.run()
