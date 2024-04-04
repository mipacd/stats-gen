# HoloChatStats Generator Scripts

## generate_stats.py

Generates most stats (translation, user stats, streaming hours, etc.). Requires pyyoutube, pandas, emoji, numpy, pytz, dateutil.

Download logs using the -d option of [auto-clip-tool](https://github.com/mipacd/auto-clip-tool). Due to memory constraints, it is recommended to download logs one week at a time.

Open generate_stats.py

Set MONTH and YEAR to the month and year to generate stats (script works only on monthly intervals).

LAST_STREAMING_HOURS is used to calculate the streaming hour delta from the previous month for each Holo (using the format used by HoloChatStats *_total csv files, see [here](https://github.com/mipacd/chat-stats/tree/master/csv/time).

API_KEY is your Youtube v3 API Key

base_dir is the output directory for the csv files generated. Logs should be in ./logs.

### Output files:

common_*: Percentage of common chat users. Generates files for 1, 3, and 10 user minimums for EN, ID, and JP branches, as well as common members.

excl: Percentage of chat users for each Holo member that did not participate in another members chat

makeup: Average chat composition by character set

member_count: Number of members by rank/badge level

member_percent: Percentage of detected chat users that are members

non_jp_rate: Non-JP messages per minute for JP members and JP messages per minute for EN/ID members. Includes averages and std. dev. at the bottom.

non_jp_stats: Percentage of chat messages that are Non-JP for all members.

non_jp_stream: Percentage of chat messages that are Non-JP for each stream (not currently used by HoloChatStats)

stream_log: Log of each stream. Includes streamer, date, stream title, Youtube video ID, and duration in minutes (not currently used by HoloChatStats)

streaming_hours: Contains streaming hour data for each Holo member. Total hours, duration of longest stream (max), average stream length (where duration is 5 minutes or longer), difference with the previous month.

tl_stats: English live translation stats for each Holo member. Includes translations per minute (TPM), translation count, and streaming time (in minutes)

tl_stream: List of streams where English translations per minute is 1 or greater, along with Youtube video ID

## consistency_score.py
Generates streaming consitency scores for each Holo member. This is calculated by dividing the mean streaming hours for each month by the standard deviation. Outputs files in 3 month, 6 month, and 1 year timeframes.

Requires pandas. Operates on the HoloChatStats streaming hours time series data (the hl-ts* csvs located [here](https://github.com/mipacd/chat-stats/tree/master/csv/time)).

## coverage.py
Outputs the percentage of days of a month where a Holo member streamed, released content, or participated in a collab. Uses the Holodex API and requires the Holodex Python client library and numpy.

Replace HOLODEX_API_KEY with your Holodex API key.

Although the output may include multiple months, this script only operates on the first JSON document for each Holomember (one for streams and the other for collabs), so data for older months may not be complete.





