from flask import Flask,render_template,request,render_template
import pickle


app = Flask(__name__)

@app.route('/')
def hello():
    return 'Sangeetha'

if __name__ == '__main__':
    app.run()

