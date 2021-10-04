from brscr import brainly
from unidecode import unidecode

scrap=brainly("Simplify: −3(4x + 5)(2x + 4)", 1)
for i in scrap:
	print(unidecode(i.question.content))
	for answer in i.answers:
		print(unidecode(answer.content))