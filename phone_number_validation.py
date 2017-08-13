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

# def get_resource(path):  # pragma: no cover
#     mimetypes = {
#         ".css": "text/css",
#         ".html": "text/html",
#         ".js": "application/javascript",
#     }
#     complete_path = os.path.join(root_dir(), path)
#     ext = os.path.splitext(path)[1]
#     mimetype = mimetypes.get(ext, "text/html")
#     content = get_file(complete_path)
#    


if __name__ == '__main__':  # pragma: no cover
    app.run(host='0.0.0.0',debug = True)