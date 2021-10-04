import os
from flask import Flask, request, jsonify
from brscr import brainly
from unidecode import unidecode

app = Flask(__name__)

@app.route("/")
def handle_job():
    qq = request.args.get('question')
    if qq:
        scrap=brainly(qq, 1)
        for i in scrap:
            qtxt = unidecode(i.question.content)
            for answer in i.answers:
                return jsonify({qtxt : unidecode(answer.content)})
    else:
        return "Cannot GET"
    return output

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)