import asyncio
import dateutil.parser
import pytz
import time
import calendar
import numpy as np
from holodex.client import HolodexClient
from collections import defaultdict

HOLODEX_API_KEY=""

hljp_names=['AZki', 'Miko', 'Roboco', 'Sora', 'Suisei', 'Mel', 'Haato', 'Fubuki', 'Matsuri', 'Aki', 'Shion', 'Aqua',
    'Ayame', 'Choco', 'ChocoSub', 'Subaru', 'Korone', 'Mio', 'Okayu', 'Noel', 'Pekora', 'Flare', 'Marine',
    'Luna', 'Coco', 'Watame', 'Kanata', 'Towa', 'Lamy', 'Nene', 'Botan', 'Polka', "Laplus", "Lui", "Koyori", "Chloe", "Iroha", 'Hajime', 'Raden', 'Ao', 'Ririka', 'Kanade']

hljp_ids=['UC0TXe_LYZ4scaW2XMyi5_kw', 'UC-hM6YJuNYVAmUWxeIr9FeA', 'UCDqI2jOz0weumE8s7paEk6g', 'UCp6993wxpyDPHUpavwDFqgg',
    'UC5CwaMl1eIgY8h02uZw7u8A', 'UCD8HOxPs4Xvsm8H0ZxXGiBw', 'UC1CfXB_kRs3C-zaeTG3oGyg', 'UCdn5BQ06XqgXoAxIhbqw5Rg',
    'UCQ0UDLQCjY0rmuxCDE38FGg', 'UCFTLzh12_nrtzqBPsTCqenA', 'UCXTpFs_3PqI41qX2d9tL2Rw', 'UC1opHUrw8rvnsadT-iGp7Cg',
    'UC7fk0CB07ly8oSl0aqKkqFg', 'UC1suqwovbL1kzsoaZgFZLKg', 'UCp3tgHXw_HI0QMk1K8qh3gQ', 'UCvzGlP9oQwU--Y0r9id_jnA',
    'UChAnqc_AY5_I3Px5dig3X1Q', 'UCp-5t9SrOQwXMU7iIjQfARg', 'UCvaTdHTWBGv3MKj3KVqJVCw', 'UCdyqAaZDKHXg4Ahi7VENThQ',
    'UC1DCedRgGHBdm81E1llLhOQ', 'UCvInZx9h3jC2JzsIzoOebWg', 'UCCzUftO8KOVkV4wQG1vkUvg',
    'UCa9Y57gfeY0Zro_noHRVrnw', 'UCS9uQI-jC3DE0L4IpXyvr6w', 'UCqm3BQLlJfvkTsX_hvm0UmA', 'UCZlDXzGoo7d44bwdNObFacg',
    'UC1uv2Oq6kNxgATlCiez59hw', 'UCFKOVgVbGmX65RxO3EtH3iw', 'UCAWSyEs_Io8MtpY3m-zqILA', 'UCUKD-uaobj9jiqB-VXt71mA',
    'UCK9V2B22uJYu3N7eR_BT9QA', 'UCENwRMx5Yh42zWpzURebzTw', 'UCs9_O1tRPMQTHQ-N_L6FU2g', 'UC6eWCld0KwmyHFbAqK3V-Rw', 'UCIBY1ollUsauvVi4hW4cumw', 'UC_vMYWcDjmfdpH6r4TTn1MQ', "UC1iA6_NT4mtAcIII6ygrvCw", "UCdXAk5MpyLD8594lm_OvtGQ", "UCMGfV7TVTmHhEErVJg1oHBQ", "UCtyWhCj3AqKh2dXctLkDtng","UCWQtYtq9EOB4-I5P-3fh8lA"]
    
hlen_names = ['Calli', 'Kiara', 'Ina', 'Gura', 'Amelia', 'IRyS', 'Sana', 'Fauna', 'Kronii', 'Mumei', 'Baelz', 'KiaraSub', "Shiori", "Bijou", "Nerissa", "FuwaMoco"]

hlen_ids = ['UCL_qhgtOy0dy1Agp8vkySQg', 'UCHsx4Hqa-1ORjQTh9TYDhww', 'UCMwGHR0BTZuLsmjY_NT5Pwg', 'UCoSrY_IQQVpmIRZ9Xf-y93g', 'UCyl1z3jo3XHR1riLFKG5UAg', 'UC8rcEBzJSleTkf_-agPM20g', 'UCsUj0dszADCGbF3gNrQEuSQ', 'UCO_aKKYxn4tvrqPjcTzZ6EQ', 'UCmbs8T6MWqUHP1tIQvSgKrg', 'UC3n5uGu18FoCy23ggWWp8tA', 'UCgmPnx-EEeOrZSg5Tiw7ZRQ', 'UCq4ky2drohLT7W0DmDEw1dQ', 'UCgnfPPb9JI3e9A4cXHnWbyg', 'UC9p_lqQ0FEDz327Vgf5JwqA', 'UC_sFNM0z0MWm9A6WlKPuMMg',
'UCt9H_RpQzhxzlyBxFqrdHqA']
    

hlid_names=['Risu', 'Moona', 'Iofi', 'Reine', 'Anya', 'Ollie', 'Zeta', 'Kaela', 'Kobo']

hlid_ids=['UCOyYb1c43VlX9rc_lT6NKQw', 'UCP0BspO_AMEe3aQqqpo89Dg', 'UCAoy6rzhSf4ydcYjJw3WoVg', 'UChgTyjG-pdNvxxhdsXfHQ5Q', 'UC727SQYUvx5pDDGQpTICNWg', 'UCYz_5n-uDuChHtLo7My1HnQ', 'UCTvHWSfBZgtxE4sILOaurIQ', 'UCZLZ8Jjx_RN2CXloOmgTHVg', 'UCjLEmnpCNeisMxy134KPwWw']

NAMES = hljp_names + hlen_names + hlid_names
PLAYLIST_IDS = hljp_ids + hlen_ids + hlid_ids

timedict = defaultdict(dict)
daydict = defaultdict(dict)
longestdict = defaultdict(dict)
avgdict = defaultdict(dict)

async def main():
	async with HolodexClient(key=HOLODEX_API_KEY) as client:
		channel_idx = 0
		for channel_id in PLAYLIST_IDS:
			offset = 0
			type = "videos"
			print(NAMES[channel_idx])
			videos1 = await client.videos_from_channel(channel_id, "videos", offset=offset, limit=50)
			videos2 = await client.videos_from_channel(channel_id, "collabs", offset=offset, limit=50)
			size = 0
			for video1 in videos1.contents:
				try:
					#set timezomes for each branch
					if channel_id in hljp_ids:
						pub_dt = dateutil.parser.isoparse(video1.published_at).astimezone(pytz.timezone("Asia/Tokyo"))
					elif channel_id in hlen_ids:
						pub_dt = dateutil.parser.isoparse(video1.published_at).astimezone(pytz.timezone("America/Los_Angeles"))
					else:
						pub_dt = dateutil.parser.isoparse(video1.published_at).astimezone(pytz.timezone("Asia/Jakarta"))
				except Exception as e:
					print(e)
					continue
				month_year = str(pub_dt.month) + '-' + str(pub_dt.year)
				
				if month_year not in daydict[NAMES[channel_idx]]:
					daydict[NAMES[channel_idx]][month_year] = []
					
				try:
					
					#add day to list if not exist
					if pub_dt.day not in daydict[NAMES[channel_idx]][month_year] and video1.duration != 0:
						daydict[NAMES[channel_idx]][month_year].append(pub_dt.day)
						
					
				except Exception as ex:
					print(ex)
					continue
				
				size += 1
				time.sleep(2)
			for video2 in videos2.contents:
				try:
					#set timezomes for each branch
					if channel_id in hljp_ids:
						pub_dt = dateutil.parser.isoparse(video2.published_at).astimezone(pytz.timezone("Asia/Tokyo"))
					elif channel_id in hlen_ids:
						pub_dt = dateutil.parser.isoparse(video2.published_at).astimezone(pytz.timezone("America/Los_Angeles"))
					else:
						pub_dt = dateutil.parser.isoparse(video2.published_at).astimezone(pytz.timezone("Asia/Jakarta"))
				except Exception as e:
					print(e)
					continue
				month_year = str(pub_dt.month) + '-' + str(pub_dt.year)
				
				if month_year not in daydict[NAMES[channel_idx]]:
					daydict[NAMES[channel_idx]][month_year] = []
					
				try:
					
					#add day to list if not exist
					if pub_dt.day not in daydict[NAMES[channel_idx]][month_year] and video2.duration != 0:
						daydict[NAMES[channel_idx]][month_year].append(pub_dt.day)
						
					
				except Exception as ex:
					print(ex)
					continue
				
				size += 1
				time.sleep(2)
					
			channel_idx += 1
		
asyncio.run(main())
	
	
#write month coverage percentages
month_cover = open("month_coverage.csv", "w")
for streamer in daydict.keys():
	for month in daydict[streamer].keys():
		year = int(month.split('-')[1])
		mon = int(month.split('-')[0])
		coverage = str(round((len(daydict[streamer][month]) / calendar.monthrange(year, mon)[1]) * 100, 2))
		month_cover.write(streamer + ',' + month + ',' + coverage + '\n')