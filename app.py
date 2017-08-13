import os.path

from flask import Flask, Response, render_template,send_from_directory


app = Flask(__name__)
app.config.from_object(__name__)


def root_dir():  # pragma: no cover
    return os.path.abspath(os.path.dirname(__file__))


def get_file(filename):  # pragma: no cover
    try:
        src = os.path.join(root_dir(), filename)
        # Figure out how flask returns static files
        # Tried:
        # - render_template
        # - send_file
        # This should not be so non-obvious
        return open(src).read()
    except IOError as exc:
        return str(exc)


@app.route('/', methods=['GET'])
def home():  # pragma: no cover
     return render_template("index.html")


@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('static/', path)



if __name__ == '__main__':  # pragma: no cover
    app.run(debug = True)