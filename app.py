import re
from flask import Flask, request, render_template

app = Flask(__name__, template_folder="./")


@app.route("/", methods=["GET"])
def word_counter():
    input_content = request.args.get("textbody", "")
    message = ""
    if input_content:
        total_words_result = len(set(re.findall(r"[^\d\W]+", input_content)))
        message = f"Total of {total_words_result} words"
    return render_template("form.html", message=message)
