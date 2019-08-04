import py8chan
import requests
import random 
import time
from fake_useragent import UserAgent
import os, random

session = requests.session()
session.proxies = {}
session.proxies['http'] = 'socks5h://localhost:9050'
session.proxies['https'] = 'socks5h://localhost:9050'

ua = UserAgent()
		

print("Started...")

while True:
	boards = [
		"v",
		"vichan",
		"b2",
		"leftypol",
		"x",
		"pol",
		"tv",
		"tech",
		"a",
		"cow",
		"hgg",
		"r9k",
		"tg",
		"fur",
		"vg",
		"b",
		"newsplus"
	]
	b = random.choice(boards)
	board = py8chan.Board(b)
	threads = board.get_all_thread_ids()
	#t = random.choice(threads)
	t = threads[random.randint(5,20)]
	
	msgs = [
		"suicide in 20 minutes gg/Xq2uYaa",
		"Leaked live nudes (all 18+ guaranteed) gg/Xq2uYaa",
		"goyim if you havent joined this server yet you are missing out gg/Xq2uYaa",
		"JION JOIN JOIN gg/Xq2uYaa",
		"best trap discord gg/Xq2uYaa",
		"gg/Xq2uYaa",
		"IF YOU'RE NOT A CUCK YOU WILL JOIN NOW gg/Xq2uYaa",
		"NO CP ALLOWED gg/Xq2uYaa",
		"join to see self harm gg/Xq2uYaa",
		"Official 8chan + 4chan Discord server gg/Xq2uYaa",
		"FREE STEAM GIVEAWAY gg/Xq2uYaa",
		"FREE PREMIUM SNAP GIVEAWAY gg/Xq2uYaa",
		"suicide youtube stream in 20 minutes gg/Xq2uYaa",
		"Awesome server for Anonymous, please join! gg/Xq2uYaa",
		"gg/Xq2uYaa gg/Xq2uYaa gg/Xq2uYaa gg/Xq2uYaa",
		"Furry server let's go raid! gg/Xq2uYaa",
		"Anonymous server with self-harm, traps, steam giveaways, premium snaps and minimal rules! gg/Xq2uYaa"
	]
	msg = random.choice(msgs)
	
	images = "anime_girls/"
	image_path = images + random.choice(os.listdir(images))
	image_filename = os.path.basename(image_path)
	file = (image_filename, open(image_path, 'rb'))
	file = ""
	multipart_form_data = {
		#'file2': ('custom_file_name.zip', open('myfile.zip', 'rb')),
		#'action': (None, 'store'),
		'thread': (None,  t),
		'board': (None, b),
		'name': (None, ''),
		'body': (None, str(random.randint(1000,9999)) + " " + msg),
		'password': (None, 'password'),
		'user_flag': (None, ''),
		'json_response': (None, '1'),
		'post': (None, 'New Reply'),
		'file': file,
		'file2': (None, 'undefined'),
		'file3': (None, 'undefined'),
		'file4': (None, 'undefined'),
		'file5': (None, 'undefined'),
	}
	headers= {
		'referer': "https://8ch.net",
		'User-Agent': ua.random,
	}
	response = requests.post('https://sys.8ch.net/post.php', files=multipart_form_data, headers=headers)
	print("POSTING IN " + b + ": " + str(response.content))
	time.sleep(random.randint(5,20))
