import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_json('StreamingHistory0.json')
df['endTime'] = pd.to_datetime(df['endTime'], utc=True)
df = df.set_index('endTime')
df.index = df.index.tz_convert('US/Eastern')
df = df.reset_index()

df['msPlayed'] = pd.to_timedelta(df['msPlayed'])

df.dtypes  # add 'print()' to see the data types
intro = "Hello and welcome to my (short) Spotify streaming history analysis!"
print(intro)
print("The following is my most played song/track: ")
print(df.trackName.mode())
print(' ')

popular_track = df[df['trackName'].str.contains('LilaS')]
print("Here is the total number of times the track 'LilaS' was played: ")
print(popular_track['trackName'].count())  # the total number of times the track was played
print("To show you an example, here are some of the times that 'LilaS' was played: ")
print(popular_track.head(5))  # printing the first 5 lines of data
popular_track = popular_track[(popular_track['msPlayed'] > '0 days 00:00:00.000030000')]
print("For more accurate analysis, here are the total number of times 'LilaS' was played that exceeded 30 seconds: ")
print(popular_track['trackName'].count())  # the total number of times the track was played that exceeded 30s
print(' ')
print("The following is the total amount of time that 'LilaS' was played: ")
print(popular_track['msPlayed'].sum())  # the sum of all times the track was played
print("(approximately 5.5 hours)")
print(' ')

print("""And finally, here are some bar graphs depicting the weekdays/hours that 'LilaS' was played: 
(they will appear on your screen)""")

popular_track['weekday'] = popular_track['endTime'].dt.weekday
popular_track['hour'] = popular_track['endTime'].dt.hour
popular_track.head(5)  # add 'print()' to print the first 5 lines of data of weekday/hour played

# Here is the start of the code for the song/track bar graph (by weekdays)
popular_track['weekday'] = pd.Categorical(popular_track['weekday'], categories=
                                          [0,1,2,3,4,5,6],
                                          ordered=True)
popular_track_day = popular_track['weekday'].value_counts()
popular_track_day = popular_track_day.sort_index()
plt.rcParams.update({'font.size': 22})
popular_track_day.plot(kind='bar', figsize=(20,10), title="My Most Listened Spotify Song by Days")
plt.show()  # shows the bar graph!

# Here is the start of the code for the second song/track bar graph (by hour)
popular_track['hour'] = pd.Categorical(popular_track['hour'], categories=
                                       [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23],
                                       ordered=True)
popular_track_hour = popular_track['hour'].value_counts()
popular_track_hour = popular_track_hour.sort_index()
popular_track_hour.plot(kind='bar', figsize=(20,10), title="My Most Listened Spotify Song by Hours")
plt.show()

# Here marks the spot for information regarding the most listened artist
print(" ")
print("The following is my most listened to artist: ")
print(df.artistName.mode())

popular_artist = df[df['artistName'].str.contains('Yu-Peng Chen')]
print(" ")
print("Here is the total number of times the artist 'Yu-Peng Chen' was listened to: ")
print(popular_artist['artistName'].count())
print("To show you an example, here are some of the times that 'Yu-Peng Chen' was listened to: ")
print(popular_artist.head(5))
popular_artist = popular_artist[(popular_artist['msPlayed'] > '0 days 00:00:00.000030000')]
print(" ")
print("The following is the total amount of times that artist 'Yu-Peng Chen' was listened to that exceeded 30 seconds: ")
print(popular_artist['artistName'].count())
print(" ")
print("The total amount of time spent listening to tracks/songs by 'Yu-Peng Chen' was: ")
print(popular_artist['msPlayed'].sum())
print("(approximately 25.5 hours(1.07 days))")
print(" ")
print("Thanks for reading about my Spotify data!")