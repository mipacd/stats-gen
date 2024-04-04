from pyyoutube import Api
import argparse
import os
import csv
import re
from collections import defaultdict, Counter
import emoji
import dateutil.parser
import glob
import pytz
import vtuber_list
import sys
import time
import isodate
import statistics
import regex
from numpy import average
import argparse
from itertools import repeat
import pandas as pd

MONTH=3
YEAR=2024
LAST_STREAMING_HOURS = './vt-stat-graphs/csv/time/hl-2024-02_total.csv'
API_KEY = 'YTv3_API_KEY'
base_dir = "LOG_DIR"

api = Api(api_key=API_KEY)

name_list = vtuber_list.vtuber_tl_list
for name in name_list:
    name_list = name_list + (name.replace(':', ' :'),)
for letter in range(ord('a'), ord('z') + 1):
    name_list = name_list + ('[' + chr(letter) + ']',)

hljp_names=['AZki', 'Miko', 'Roboco', 'Sora', 'Suisei', 'Haato', 'Fubuki', 'Matsuri', 'Aki', 'Shion', 'Aqua',
    'Ayame', 'Choco', 'ChocoSub', 'Subaru', 'Korone', 'Mio', 'Okayu', 'Noel', 'Pekora', 'Flare', 'Marine',
    'Luna', 'Watame', 'Kanata', 'Towa', 'Lamy', 'Nene', 'Botan', 'Polka', "Laplus", "Lui", "Koyori", "Chloe", "Iroha", 'Hajime', 'Raden', 'Ao', 'Ririka', 'Kanade']

hljp_ids=['UU0TXe_LYZ4scaW2XMyi5_kw', 'UU-hM6YJuNYVAmUWxeIr9FeA', 'UUDqI2jOz0weumE8s7paEk6g', 'UUp6993wxpyDPHUpavwDFqgg',
    'UU5CwaMl1eIgY8h02uZw7u8A', 'UU1CfXB_kRs3C-zaeTG3oGyg', 'UUdn5BQ06XqgXoAxIhbqw5Rg',
    'UUQ0UDLQCjY0rmuxCDE38FGg', 'UUFTLzh12_nrtzqBPsTCqenA', 'UUXTpFs_3PqI41qX2d9tL2Rw', 'UU1opHUrw8rvnsadT-iGp7Cg',
    'UU7fk0CB07ly8oSl0aqKkqFg', 'UU1suqwovbL1kzsoaZgFZLKg', 'UUp3tgHXw_HI0QMk1K8qh3gQ', 'UUvzGlP9oQwU--Y0r9id_jnA',
    'UUhAnqc_AY5_I3Px5dig3X1Q', 'UUp-5t9SrOQwXMU7iIjQfARg', 'UUvaTdHTWBGv3MKj3KVqJVCw', 'UUdyqAaZDKHXg4Ahi7VENThQ',
    'UU1DCedRgGHBdm81E1llLhOQ', 'UUvInZx9h3jC2JzsIzoOebWg', 'UUCzUftO8KOVkV4wQG1vkUvg',
    'UUa9Y57gfeY0Zro_noHRVrnw', 'UUqm3BQLlJfvkTsX_hvm0UmA', 'UUZlDXzGoo7d44bwdNObFacg',
    'UU1uv2Oq6kNxgATlCiez59hw', 'UUFKOVgVbGmX65RxO3EtH3iw', 'UUAWSyEs_Io8MtpY3m-zqILA', 'UUUKD-uaobj9jiqB-VXt71mA',
    'UUK9V2B22uJYu3N7eR_BT9QA', 'UUENwRMx5Yh42zWpzURebzTw', 'UUs9_O1tRPMQTHQ-N_L6FU2g', 'UU6eWCld0KwmyHFbAqK3V-Rw', 'UUIBY1ollUsauvVi4hW4cumw', 'UU_vMYWcDjmfdpH6r4TTn1MQ', "UU1iA6_NT4mtAcIII6ygrvCw", "UUdXAk5MpyLD8594lm_OvtGQ", "UUMGfV7TVTmHhEErVJg1oHBQ", "UUtyWhCj3AqKh2dXctLkDtng","UUWQtYtq9EOB4-I5P-3fh8lA"]
    
hlen_names = ['Calli', 'Kiara', 'Ina', 'Gura', 'Amelia', 'IRyS', 'Fauna', 'Kronii', 'Mumei', 'Baelz', 'KiaraSub', "Shiori", "Bijou", "Nerissa", "FuwaMoco"]

hlen_ids = ['UUL_qhgtOy0dy1Agp8vkySQg', 'UUHsx4Hqa-1ORjQTh9TYDhww', 'UUMwGHR0BTZuLsmjY_NT5Pwg', 'UUoSrY_IQQVpmIRZ9Xf-y93g', 'UUyl1z3jo3XHR1riLFKG5UAg', 'UU8rcEBzJSleTkf_-agPM20g', 'UUO_aKKYxn4tvrqPjcTzZ6EQ', 'UUmbs8T6MWqUHP1tIQvSgKrg', 'UU3n5uGu18FoCy23ggWWp8tA', 'UUgmPnx-EEeOrZSg5Tiw7ZRQ', 'UUq4ky2drohLT7W0DmDEw1dQ',
'UUgnfPPb9JI3e9A4cXHnWbyg', 'UU9p_lqQ0FEDz327Vgf5JwqA', 'UU_sFNM0z0MWm9A6WlKPuMMg',
'UUt9H_RpQzhxzlyBxFqrdHqA']
    

hlid_names=['Risu', 'Moona', 'Iofi', 'Reine', 'Anya', 'Ollie', 'Zeta', 'Kaela', 'Kobo']

hlid_ids=['UUOyYb1c43VlX9rc_lT6NKQw', 'UUP0BspO_AMEe3aQqqpo89Dg', 'UUAoy6rzhSf4ydcYjJw3WoVg', 'UUhgTyjG-pdNvxxhdsXfHQ5Q', 'UU727SQYUvx5pDDGQpTICNWg', 'UUYz_5n-uDuChHtLo7My1HnQ', 'UUTvHWSfBZgtxE4sILOaurIQ', 'UUZLZ8Jjx_RN2CXloOmgTHVg', 'UUjLEmnpCNeisMxy134KPwWw']

    
os.chdir(base_dir)
logs = glob.glob("**/logs/*")
output_csv = open(os.path.join(base_dir, "non_jp_stats.csv"), 'w')
non_jp_strm_csv = open(os.path.join(base_dir, "non_jp_stream.csv"), 'w')
tl_output_csv = open(os.path.join(base_dir, "tl_stats.csv"), 'w')
tl_strm_csv = open(os.path.join(base_dir, "tl_stream.csv"), 'w')
rate_count_csv = open(os.path.join(base_dir, "non_jp_rate.csv"), 'w')
stream_log_csv = open(os.path.join(base_dir, "stream_log.csv"), 'w')
makeup_csv = open(os.path.join(base_dir, "makeup.csv"), 'w')
wr_csv = csv.writer(output_csv, delimiter=',')
wr_csv.writerow(['streamer', 'month', '%'])
wr_strm = csv.writer(non_jp_strm_csv, delimiter=',')
wr_strm.writerow(['streamer', 'stream', '%'])
wr_tl = csv.writer(tl_output_csv, delimiter=',')
wr_tl.writerow(['streamer', 'month', 'tpm', 'count', 'total'])
wr_tl_strm = csv.writer(tl_strm_csv, delimiter=',')
wr_tl_strm.writerow(['streamer', 'stream', 'tpm', 'id'])
wr_non_jp_rate = csv.writer(rate_count_csv, delimiter=',')
wr_non_jp_rate.writerow(['streamer', 'JP/NonJP Rate'])
wr_makeup = csv.writer(makeup_csv, delimiter=',')
wr_makeup.writerow(['streamer', 'EN/ES/ID/etc.', 'JP', 'KR', 'RU', 'Emote'])
wr_st = csv.writer(stream_log_csv, delimiter=',')
wr_st.writerow(['streamer', 'date', 'stream', 'id', 'minutes'])

NAMES = hljp_names + hlen_names + hlid_names
PLAYLIST_IDS = hljp_ids + hlen_ids + hlid_ids


pl_idx = 0
playlists = {}
jp_regex = "[\u3040-\u30ff\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff\uff66-\uff9f]"
ru_regex = "[\u0400-\u04ff]"
kr_regex = "[\u3130-\u318F\uAC00-\uD7AF]"
for name in NAMES:
    playlists[name] = []
    playlists[name] = api.get_playlist_items(playlist_id=PLAYLIST_IDS[pl_idx], count=None)
    pl_idx += 1
    
count_dict = defaultdict(dict)
ru_count_dict = defaultdict(dict)
kr_count_dict = defaultdict(dict)
emo_count_dict = defaultdict(dict)
total_dict = defaultdict(dict)
read_dict = defaultdict(dict)
read_total_dict = defaultdict(dict)

tl_count_dict = defaultdict(dict)
tl_min_dict = defaultdict(dict)
count = 1

user_str_dict = defaultdict(list)
user_str_dict3 = defaultdict(list)
user_str_dict5 = defaultdict(list)
jp_percent_stm_dict = defaultdict(dict)
jp_percent_weight_dict = defaultdict(dict)
user_member_dict = defaultdict(dict)

streaming_hours_dict = defaultdict(list)
hlen_jp_list = []
hlid_jp_list = []
hljprg_nonjp_list = []

def is_emoji(char):
    return char in emoji.UNICODE_EMOJI
    
vidlist = []
    
for key, val in playlists.items():
    if key == "ChocoSub": key = "Choco"
    if key == "KiaraSub": key = "Kiara"
    if key == "ChocoSubM": key = "ChocoM"
    for vid in val.items:
        if vid in vidlist:
            continue
        vidlist.append(vid)
        pub_date = vid.contentDetails.videoPublishedAt
        if not pub_date:
            continue
        pub_dt = dateutil.parser.isoparse(pub_date).astimezone(pytz.timezone("Asia/Tokyo"))
        title_lower = vid.snippet.title.lower()
        log_item = [x for x in logs if x.endswith(vid.snippet.resourceId.videoId)]
        if not len(log_item):
           continue
        #write stream log
        if pub_dt.month == MONTH and pub_dt.year == YEAR:
           date = str(pub_dt.year) + '-' + str(pub_dt.month) + '-' + str(pub_dt.day)
           vid_by_id = api.get_video_by_id(video_id=vid.snippet.resourceId.videoId, hl="en")
           vid_duration = isodate.parse_duration(vid_by_id.items[0].contentDetails.duration).seconds
           minutes = round(vid_duration / 60, 2)
           wr_st.writerow([key, date, vid_by_id.items[0].snippet.localized.title, vid.snippet.resourceId.videoId, str(minutes)])
           streaming_hours_dict[key].append(minutes)
        if log_item and pub_dt.month == MONTH and pub_dt.year == YEAR and "member's only" not in title_lower:
            print("Parsing log " + str(count))
            count += 1
            month_year = str(pub_dt.month) + '-' + str(pub_dt.year)
            success = False
            while not success:
                try:
                    log_file = open(log_item[0])
                    chat = log_file.readlines()
                except:
                    print("Unable to read file, waiting 5 seconds...")
                    time.sleep(5)
                else:
                    success = True
            tl_name_list = defaultdict(int)
            user_name_list = defaultdict(int)
            msg_total = 0
            non_jp_total = 0
            read_total = 0
            all_users = []
            
            for msg in chat:
                try:
                    msg_lower = msg.split(',', 3)[2].lower().rstrip()
                except:
                    print("Parse failed")
                    print(log_item[0] + ': ' + msg_lower) 
                    sys.exit(1)
                author = msg.split(',', 2)[1]
                
                #assign member rank to each chat user
                if msg.strip().endswith("New member"):
                    mem_rank = 1
                elif msg.strip().endswith("Member (1 month)"):
                    mem_rank = 2
                elif msg.strip().endswith("Member (2 months)"):
                    mem_rank = 3
                elif msg.strip().endswith("Member (6 months)"):
                    mem_rank = 4
                elif msg.strip().endswith("Member (1 year)"):
                    mem_rank = 5
                elif msg.strip().endswith("Member (2 years)"):
                    mem_rank = 6
                elif msg.strip().endswith("Member (3 years)"):
                    mem_rank = 7
                elif msg.strip().endswith("Member (4 years)"):
                    mem_rank = 8
                else:
                    mem_rank = 0
                        
                is_not_jp = not re.search(jp_regex, msg_lower)
                is_ru = re.search(ru_regex, msg_lower)
                is_kr = re.search(kr_regex, msg_lower)
                is_not_null = len(msg_lower) >= 1
                if is_not_null:
                    all_users.append(author)
                    is_not_yt_emoji = not (msg_lower.startswith(':') and msg_lower.endswith(':'))
                    is_not_utf_emoji = not (is_emoji(msg_lower[0]) and is_emoji(msg_lower[-1]))
                    is_not_number = not msg_lower.isnumeric()
                    
                    if key not in tl_count_dict:
                        tl_count_dict[key] = {}
                    if month_year not in tl_count_dict[key]:
                        tl_count_dict[key][month_year] = 0
                    if key not in user_str_dict:
                        user_str_dict[key] = []
                        
                    if key not in user_member_dict:
                        user_member_dict[key] = {}
                    if author in user_member_dict[key]:
                        if user_member_dict[key][author] < mem_rank:
                            user_member_dict[key][author] = mem_rank
                    else:
                        user_member_dict[key][author] = mem_rank
                        
                    user_str_dict[key].append(author)
                    
                    #detect translation
                    if "cover" not in title_lower and "わためのうた" not in title_lower or "music video" not in title_lower:
                        tl_tags = ('en:', 'eng:', 'en :', 'eng :', 'en-', 'tl:', 'tl eng:', 'tl :', 'tl eng :', 'tl en:', 'tl en :')
                        if 'en]' in msg_lower or '[en' in msg_lower or '【en' in msg_lower or '(en' in msg_lower or 'eng]' in msg_lower or 'en)' in msg_lower or 'eng)' in msg_lower or 'trans]' in msg_lower or 'en】' in msg_lower or msg_lower.startswith(tl_tags) or msg_lower.startswith(name_list) or author.startswith("Watame TL"):
                            if msg_lower.count("*") != 2 or not msg_lower.endswith("noises") or not author.startswith(vtuber_list.tl_blist):
                                tl_name_list[author] += 1
                                
                    
                    if is_not_yt_emoji and is_not_utf_emoji and is_not_number:
                        if key not in total_dict:
                            total_dict[key] = {}
                        if month_year not in total_dict[key]:
                            total_dict[key][month_year] = 0
                        total_dict[key][month_year] += 1
                        msg_total += 1
                        if is_not_jp:
                            if key not in count_dict:
                                count_dict[key] = {}
                            if month_year not in count_dict[key]:
                                count_dict[key][month_year] = 0
                            count_dict[key][month_year] += 1
                            non_jp_total += 1
                        if is_ru:
                            if key not in ru_count_dict:
                                ru_count_dict[key] = {}
                            if month_year not in ru_count_dict[key]:
                                ru_count_dict[key][month_year] = 0
                            ru_count_dict[key][month_year] += 1
                        if is_kr:
                            if key not in kr_count_dict:
                                kr_count_dict[key] = {}
                            if month_year not in kr_count_dict[key]:
                                kr_count_dict[key][month_year] = 0
                            kr_count_dict[key][month_year] += 1
                    else:
                        if key not in emo_count_dict:
                            emo_count_dict[key] = {}
                        if month_year not in emo_count_dict[key]:
                            emo_count_dict[key][month_year] = 0
                        emo_count_dict[key][month_year] += 1
                            
                                         
            if key not in tl_min_dict:
                tl_min_dict[key] = {}
            if month_year not in tl_min_dict[key]:
                tl_min_dict[key][month_year] = 0
            if msg_total == 0:
                continue
            #skip post chat msgs in unix time
            minute = 0
            total_tl = 0
            for line in reversed(chat):
                minute = int(float(line.split(',', 1)[0])) / 60
                if minute <= 720:
                    tl_min_dict[key][month_year] += minute
                    break
            for val in tl_name_list.values():
                if val >= 3:
                    tl_count_dict[key][month_year] += val
                    total_tl += val
            str_tpm = round((total_tl / minute), 2)
            if str_tpm >= 1:
                wr_tl_strm.writerow([key, vid.snippet.title, str(str_tpm), vid.snippet.resourceId.videoId])
            wr_strm.writerow([key, vid.snippet.title, str(round((non_jp_total / msg_total)*100, 2))])
            
for name in NAMES:
    if name in count_dict:
        for key, val in count_dict[name].items():
            if key in emo_count_dict[name]:
                emo_count = emo_count_dict[name][key]
            else:
                emo_count = 0
            try:
                kr_count = kr_count_dict[name][key]
            except:
                kr_count = 0
            try:
                ru_count = ru_count_dict[name][key]
            except:
                ru_count = 0
            wr_csv.writerow([name, key, str(round((count_dict[name][key] / total_dict[name][key]) * 100, 2))])
            non_jp_rate = count_dict[name][key] / tl_min_dict[name][key]
            jp_rate = (total_dict[name][key] - count_dict[name][key]) / tl_min_dict[name][key]
            kr_rate = kr_count / tl_min_dict[name][key]
            ru_rate = ru_count / tl_min_dict[name][key]
            roman_rate = non_jp_rate - (kr_rate + ru_rate)
            emote_rate = emo_count / tl_min_dict[name][key]
            wr_makeup.writerow([name, str(round(roman_rate, 2)), str(round(jp_rate, 2)), str(round(kr_rate, 2)), str(round(ru_rate, 2)), str(round(emote_rate, 2))])
            if name in hlen_names or name in hlid_names:
                wr_non_jp_rate.writerow([name, str(round(jp_rate, 2))])
            else:
                wr_non_jp_rate.writerow([name, str(round(non_jp_rate, 2))])
            if name in hlen_names:
                hlen_jp_list.append(jp_rate)
            elif name in hlid_names:
                hlid_jp_list.append(jp_rate)
            elif name in hljp_names:
                hljprg_nonjp_list.append(non_jp_rate)
        for key, val in tl_count_dict[name].items():
            wr_tl.writerow([name, key, str(round(tl_count_dict[name][key] / tl_min_dict[name][key], 2)), str(tl_count_dict[name][key]), str(tl_min_dict[name][key])])

    if name in user_str_dict:
        count = Counter(user_str_dict[name])
        user_str_dict3[name] = list(set([name for item, n in count.items() if n >= 3 for name in repeat(item, n)]))
        user_str_dict5[name] = list(set([name for item, n in count.items() if n >= 10 for name in repeat(item, n)]))
        user_str_dict[name] = list(set(user_str_dict[name]))

jp_non_jp_avg = sum(hljprg_nonjp_list) / len(hljprg_nonjp_list)
en_jp_avg = sum(hlen_jp_list) / len(hlen_jp_list)
id_jp_avg = sum(hlid_jp_list) / len(hlid_jp_list)
jp_non_jp_std = statistics.stdev(hljprg_nonjp_list)
en_jp_std = statistics.stdev(hlen_jp_list)
id_jp_std = statistics.stdev(hlid_jp_list)
wr_non_jp_rate.writerow(["JP NonJP Avg", str(round(jp_non_jp_avg, 2))])
wr_non_jp_rate.writerow(["EN JP Avg", str(round(en_jp_avg, 2))])
wr_non_jp_rate.writerow(["ID JP Avg", str(round(id_jp_avg, 2))])
wr_non_jp_rate.writerow(["JP NonJP Std. Dev.", str(round(jp_non_jp_std, 2))])
wr_non_jp_rate.writerow(["EN JP Std. Dev.", str(round(en_jp_std, 2))])
wr_non_jp_rate.writerow(["ID JP Std. Dev.", str(round(id_jp_std, 2))])
            
            
common_file_jp = open(base_dir + "/common_jp.csv", "w")
common_file_en = open(base_dir + "/common_en.csv", "w")
common_file_id = open(base_dir + "/common_id.csv", "w")

common_file_3_jp = open(base_dir + "/common_3_jp.csv", "w")
common_file_3_en = open(base_dir + "/common_3_en.csv", "w")
common_file_3_id = open(base_dir + "/common_3_id.csv", "w")

common_file_10_jp = open(base_dir + "/common_10_jp.csv", "w")
common_file_10_en = open(base_dir + "/common_10_en.csv", "w")
common_file_10_id = open(base_dir + "/common_10_id.csv", "w")

common_member_en = open(base_dir + "/common_member_en.csv", "w")
common_member_id = open(base_dir + "/common_member_id.csv", "w")
common_member_jp = open(base_dir + "/common_member_jp.csv", "w")


member_rank_counts = open(base_dir + "/member_count.csv", "w")
streaming_hours = open(base_dir + "/streaming_hours.csv", "w")
member_percent = open(base_dir + "/member_percent.csv", "w")
user_counts = defaultdict(int)

excl_file = open(base_dir + "/excl.csv", "w")

header = "from,to,value\n"
en_line1 = "Amelia,Amelia\n"
jp_line1 = "Aki,Aki\n"
id_line1 = "Anya,Anya\n"
common_file_jp.write(header)
common_file_en.write(header)
common_file_id.write(header)
common_file_3_jp.write(header)
common_file_3_en.write(header)
common_file_3_id.write(header)
common_file_10_jp.write(header)
common_file_10_en.write(header)
common_file_10_id.write(header)
common_member_jp.write(header)
common_member_en.write(header)
common_member_id.write(header)

common_file_jp.write(jp_line1)
common_file_en.write(en_line1)
common_file_id.write(id_line1)
common_file_3_jp.write(jp_line1)
common_file_3_en.write(en_line1)
common_file_3_id.write(id_line1)
common_file_10_jp.write(jp_line1)
common_file_10_en.write(en_line1)
common_file_10_id.write(id_line1)
common_member_jp.write(jp_line1)
common_member_en.write(en_line1)
common_member_id.write(id_line1)

member_percent.write("Member,Percent")

for key, val in user_str_dict.items():
   user_count = len(val)
   user_counts[key] = user_count
   other_list = []
   for key2, val2 in user_str_dict.items():
       if key2 != key:
           if key in hljp_names and key2 in hljp_names:
               common_file_jp.write(key + ',' + key2 + "," + str(round((len(list(set(val) & set(val2))) / user_count) * 100, 2)) + '\n')
           elif key in hlen_names and key2 in hlen_names:
               common_file_en.write(key + ',' + key2 + "," + str(round((len(list(set(val) & set(val2))) / user_count) * 100, 2)) + '\n')
           elif key in hlid_names and key2 in hlid_names:
               common_file_id.write(key + ',' + key2 + "," + str(round((len(list(set(val) & set(val2))) / user_count) * 100, 2)) + '\n')
           other_list += val2
   excl_file.write(key + ',Nobody,' + str(round((len(list(set(val) - set(other_list))) / user_count) * 100, 2)) + '\n')
   members_with_rank = {}
   if key in user_member_dict:
        for member, rank in user_member_dict[key].items():
            if rank > 0:
                members_with_rank[member] = rank
   members = set(members_with_rank.keys())
   total_chatters = set(val)
   member_count = len(members.intersection(total_chatters))
   if total_chatters:
        percentage = (member_count / len(total_chatters)) * 100
        member_percent.write(key + "," + str(round(percentage, 2)) + "\n")
for key, val in user_str_dict3.items():
   user_count = len(val)
   other_list = []
   for key2, val2 in user_str_dict3.items():
       if key2 != key:
           if key in hljp_names and key2 in hljp_names:
               common_file_3_jp.write(key + ',' + key2 + "," + str(round((len(list(set(val) & set(val2))) / user_count) * 100, 2)) + '\n')
           elif key in hlen_names and key2 in hlen_names:
               common_file_3_en.write(key + ',' + key2 + "," + str(round((len(list(set(val) & set(val2))) / user_count) * 100, 2)) + '\n')
           elif key in hlid_names and key2 in hlid_names:
               common_file_3_id.write(key + ',' + key2 + "," + str(round((len(list(set(val) & set(val2))) / user_count) * 100, 2)) + '\n')
for key, val in user_str_dict5.items():
   user_count = len(val)
   other_list = []
   for key2, val2 in user_str_dict5.items():
       if key2 != key:
           if key in hljp_names and key2 in hljp_names:
               common_file_10_jp.write(key + ',' + key2 + "," + str(round((len(list(set(val) & set(val2))) / user_count) * 100, 2)) + '\n')
           elif key in hlen_names and key2 in hlen_names:
               common_file_10_en.write(key + ',' + key2 + "," + str(round((len(list(set(val) & set(val2))) / user_count) * 100, 2)) + '\n')
           elif key in hlid_names and key2 in hlid_names:
               common_file_10_id.write(key + ',' + key2 + "," + str(round((len(list(set(val) & set(val2))) / user_count) * 100, 2)) + '\n')
               
member_keys = list(user_member_dict.keys())

for i in range(len(member_keys)):
    for j in range(len(member_keys)):
        if i == j:
            continue
        vtuber1, vtuber2 = member_keys[i], member_keys[j]
        
        branch = ""
        if vtuber1 in hljp_names and vtuber2 in hljp_names:
            branch = "jp"
        elif vtuber1 in hlen_names and vtuber2 in hlen_names:
            branch = "en"
        elif vtuber1 in hlid_names and vtuber2 in hlid_names:
            branch = "id"
        else:
            branch = ""
            continue
        members1 = {member for member, rank in user_member_dict[vtuber1].items() if rank > 0}
        members2 = {member for member, rank in user_member_dict[vtuber2].items() if rank > 0}
        
        common_members = members1.intersection(members2)
        common_percentage = (len(common_members) / len(members1)) * 100

        
        if branch == "jp":
            common_member_jp.write(vtuber1 + ',' + vtuber2 + ',' + str(round(common_percentage, 2)) + '\n')
        elif branch == "en":
            common_member_en.write(vtuber1 + ',' + vtuber2 + ',' + str(round(common_percentage, 2)) + '\n')
        elif branch == "id":
            common_member_id.write(vtuber1 + ',' + vtuber2 + ',' + str(round(common_percentage, 2)) + '\n')
               
common_file_jp.close()
common_file_en.close()
common_file_id.close()
common_file_3_jp.close()
common_file_3_en.close()
common_file_3_id.close()
common_file_10_jp.close()
common_file_10_en.close()
common_file_10_id.close()
common_member_jp.close()
common_member_en.close()
common_member_id.close()
 
#sort common csvs
common_files = ['common_jp.csv', 'common_en.csv', 'common_id.csv', 'common_3_jp.csv', 'common_3_en.csv', 'common_3_id.csv', 'common_10_jp.csv', 'common_10_en.csv', 'common_10_id.csv', 'common_member_en.csv', 'common_member_id.csv', 'common_member_jp.csv']
for cfile in common_files:
    df = pd.read_csv(base_dir + "/" + cfile, delimiter=',')
    df = df.sort_values(['to', 'from'], ascending=[True, True])
    df.to_csv(base_dir + "/" + cfile, index=False)
               
member_rank_counts.write("member,New Members,1 Month,2 Month,6 Month,1 Year,2 Year,3 Year,4 Year\n")
for key, val in user_member_dict.items():
    member = key
    mem_count = len(val)
    rank_counts = defaultdict(int)
    member_percentage = round((mem_count / user_counts[key]) * 100, 2)
    for key2, val2 in val.items():
        rank_counts[val2] += 1
    member_rank_counts.write(member + ',' + str(rank_counts[1]) + ',' + str(rank_counts[2]) + ',' + str(rank_counts[3]) + ',' + str(rank_counts[4]) + ',' + str(rank_counts[5]) + ',' + str(rank_counts[6]) + ',' + str(rank_counts[7]) + ',' + str(rank_counts[8]) + '\n')
    
streaming_hours.write("member,total,max,avg>=5,diff")
jp_sum = 0
en_sum = 0
id_sum = 0
last_dict = {}
#load previous month
with open(LAST_STREAMING_HOURS, 'r') as file:
    reader = csv.reader(file)
    last_dict = {rows[0]:rows[1] for rows in reader}
for key, val in streaming_hours_dict.items():
    member = key
    total = sum(val) / 60
    if member in hljp_names:
        jp_sum += total
    elif member in hlen_names:
        en_sum += total
    elif member in hlid_names:
        id_sum += total
    max_stream = max(val) / 60
    #conditional avg
    avg_list = [item for item in val if item >= 5]
    avg = (sum(avg_list) / len(avg_list)) / 60
    diff = 0
    if key in last_dict:
        diff = round(total, 2) - round(float(last_dict[key]), 2)
    streaming_hours.write(member + ',' + str(round(total, 2)) + ',' + str(round(max_stream, 2)) + ',' + str(round(avg, 2)) + ',' + str(diff) + '\n')
streaming_hours.write("JP Sum," + str(jp_sum) + '\n')
streaming_hours.write("EN Sum," + str(en_sum) + '\n')
streaming_hours.write("ID Sum," + str(id_sum) + '\n')