from flask import Flask, request, make_response, redirect, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route("/index")
def index():
    user_ip_information = request.remote_addr
    response = make_response(redirect("/show_information_address"))
    response.set_cookie("user_ip_information", user_ip_information)
    return response


items = [
    "ITEM 1",
    "ITEM 2",
    "ITEM 3",
    "ITEM 4",
]


@app.errorhandler(404)
def not_found_endpoint(error):
    return render_template("404.html", error=error)


@app.route("/show_information_address")
def show_information():
    user_ip = request.cookies.get("user_ip_information")
    context = {"user_ip": user_ip, "items": items}
    return render_template("ip_information.html", **context)


app.run(host="0.0.0.0", port=5000, debug=True)
