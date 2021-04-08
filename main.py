from flask import Flask
from flask import request, redirect, send_file


app = Flask(__name__, static_url_path='/')

@app.route("/")
def home():
    return """
     <form action="/action" method="GET">
      <label for="path">Path:</label><br>
      <input type="text" id="path" name="path"><br>
      <input type="submit" value="Submit" class="pathSubmit">
    </form>
    """

@app.route("/action", methods=["GET"])
def path():
    print(request.args['path'])
    path = request.args['path']
    try:
        return send_file("/home/kit4/web/flask/" + path)
    except FileNotFoundError:
        return "no such file((("

if __name__ == "__main__":
    app.run(port=80)