from flask import Flask
# import config as config

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Welcome to the Application with updated code! new new test webhook'


@app.route('/stub')
def stub():
    # Stub value replaced by Jenkins Pipeline dynamically in config.py
    return 'ttttttt'
    # return 'Value of Stub: ' + str(config.STUB_VARIABLE)


if __name__ == '__main__':
    app.run()
