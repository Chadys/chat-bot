# coding: utf-8
from __future__ import unicode_literals
import urllib2, os, sys, re
from bs4 import BeautifulSoup

if len(sys.argv) < 3:
		print "Error in file use, 'python man_fr.py [man_entry] [man_category_number]'"
		quit()

try: # http://www.linux-france.org/article/man-fr/
	page =  BeautifulSoup(urllib2.urlopen('http://www.linux-france.org/article/man-fr/man'+sys.argv[2]+'/'+sys.argv[1]+'-'+sys.argv[2]+'.html'), "html.parser")
	text = page.body.get_text()
	text = re.sub(r"(?msx)^(.*?(?=NOM))",'',text)
	text = re.sub(r"""(?x)\s+?\n .+? [ \t]+
		\d{1,2}\ [A-Z][a-zéû]+\ \d{4} #date
		[ \t]+ \d+\s+
		(?:.+\n)?""",'',text)

except urllib2.HTTPError:
	try: # http://www.man-linux-magique.net/
		page =  BeautifulSoup(urllib2.urlopen('http://www.man-linux-magique.net/man'+sys.argv[2]+'/'+sys.argv[1]+'.html'), "html.parser")
		text = page.find(id="texte-man").get_text()
	
	except urllib2.HTTPError:
		try: # http://jp.barralis.com/linux-man/
			page =  BeautifulSoup(urllib2.urlopen('http://jp.barralis.com/linux-man/man'+sys.argv[2]+'/'+sys.argv[1]+'.'+sys.argv[2]+'.php'), "html.parser")
			text = page.body.get_text()
		except urllib2.HTTPError:
			print u"Défaillance du système, je n'ai pas pu consulter le manuel".encode('utf-8')

print (sys.argv[1]+'('+sys.argv[2]+')\n\n'+text).encode('utf-8')
