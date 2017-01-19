# coding: utf-8
from __future__ import unicode_literals
import wikipedia

wikipedia.set_lang("fr")
while True:
	try:
		print wikipedia.summary(wikipedia.random()).encode('utf-8')
		break

	except wikipedia.exceptions.DisambiguationError:
		pass
	except wikipedia.exceptions.PageError:
		pass