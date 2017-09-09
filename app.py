import os.path
import re

from flask import Flask, Response, render_template,send_from_directory, redirect, url_for, request


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


def is_valid(phone_n):
    regex = r'^(?:(?:\+?1\s*(?:[.-]\s*)?)?(?:\(\s*([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9])\s*\)|([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9]))\s*(?:[.-]\s*)?)?([2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2})\s*(?:[.-]\s*)?([0-9]{4})(?:\s*(?:#|x\.?|ext\.?|extension)\s*(\d+))?$'
    return re.match(regex, phone_n)
//test




@app.route('/',methods = ['POST', 'GET'])
def test():
    if request.method == 'POST':
        isValid= is_valid(request.form["userInput"])
        if isValid:
            return render_template("success.html")
        else:
            return render_template("failure.html")
    else:
        return render_template("index.html")


if __name__ == '__main__':  # pragma: no cover
    app.run(debug = True, port = 80)

