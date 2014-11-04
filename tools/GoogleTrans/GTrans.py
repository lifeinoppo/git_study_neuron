#coding=utf8
# this is a python tiny program for translating, reference from the web
import urllib2
import json
import os,sys
reload(sys)
sys.setdefaultencoding("utf-8")
_reference_time = '2014-11-1'
class GTrans :   # which is known as google translate
	def google_translate(slef,sourcelanguage,targetlanguage,text) :
		text = urllib2.quote(text)
  # I think you will have to change the url, actually, use google translate once, and you will get the url you need
# we just find another url to execute this request, just in great web wall, language encode list is in bellow
#	url = "https://www.googleapis.com/language/translate/v2/?key=YOUR_KEY&target="+targetlanguage+"&q="+text
		url = "http://brisk.eu.org/api/translate.php?from="+sourcelanguage+"&to="+targetlanguage+"&text="+text
		res = urllib2.urlopen(urllib2.Request(url))
		dirt = json.JSONDecoder().decode(res.read())
		return dirt["res"]


if __name__=="__main__":
	trans = GTrans()
	value = trans.google_translate("zh-CN","en","你好")
	print "hello"

"""    the language decode list(the alias in api for each language)
Afrikaans	af
Albanian	sq
Arabic	ar
Azerbaijani	az
Basque	eu
Bengali	bn
Belarusian	be
Bulgarian	bg
Catalan	ca
Chinese Simplified	zh-CN
Chinese Traditional	zh-TW
Croatian	hr
Czech	cs
Danish	da
Dutch	nl
English	en
Esperanto	eo
Estonian	et
Filipino	tl
Finnish	fi
French	fr
Galician	gl
Georgian	ka
German	de
Greek	el
Gujarati	gu
Haitian Creole	ht
Hebrew	iw
Hindi	hi
Hungarian	hu
Icelandic	is
Indonesian	id
Irish	ga
Italian	it
Japanese	ja
Kannada	kn
Korean	ko
Latin	la
Latvian	lv
Lithuanian	lt
Macedonian	mk
Malay	ms
Maltese	mt
Norwegian	no
Persian	fa
Polish	pl
Portuguese	pt
Romanian	ro
Russian	ru
Serbian	sr
Slovak	sk
Slovenian	sl
Spanish	es
Swahili	sw
Swedish	sv
Tamil	ta
Telugu	te
Thai	th
Turkish	tr
Ukrainian	uk
Urdu	ur
Vietnamese	vi
Welsh	cy
Yiddish	yi
"""
