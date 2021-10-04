from brscr import brainly
from unidecode import unidecode
import os
import sys

def scrapeAnswer(qq):
    scrap=brainly(qq, 1)
        for i in scrap:
            qtxt = unidecode(i.question.content)
            for answer in i.answers:
                return jsonify({qtxt : unidecode(answer.content)})