import json
import urllib2
import time
import dateutil.parser
from model.models import Channel, Show
from model.database import db_session

# 23-02-2014%2001:00:00


#TODO turn into method

baseurl = 'http://www.radiotimes.com/rt-service/schedule/get?startDate={0}&hours={1}&channels={2}&totalWidthUnits=720'
channels = [26,40,45,47,94,105,131,132,134,147,158,160,180,182,185,197,213,248,262,264,288,292,482,483,801,922,1061,1201,1461,1601,1859,1882,1959,1961,1963,1981,2008,2050,2056,2062,2115,2122,2134,2179,2185,2189,2212,2603,2685,5072,5074,5097]


startdate = time.strftime("%d-%m-20%y %H:00:00")
startdate = startdate.replace(' ', '%20')


req = urllib2.urlopen(baseurl.format(startdate, 5, ','.join([str(x) for x in channels])))
data = json.load(req)

for channel in data['Channels']:
    if(Channel.query.filter(Channel.rtid == channel['Id']).count() == 0):

        print 'New Channel found: ' + channel['DisplayName']

        newChan = Channel(channel['DisplayName'], channel['Id'])
        db_session.add(newChan)
        db_session.commit()

    for show in channel['TvListings']:
        start = dateutil.parser.parse(show['StartTimeMF'])
        end = dateutil.parser.parse(show['EndTimeMF'])

        c = Channel.query.filter_by(rtid=channel['Id']).first()


        if(Show.query.filter(Show.channelId == c.channelId, Show.title == show['Title'], Show.startTime == start).count() == 0):

            print '{0} - {1}'.format(show['Title'], show['StartTimeMF'])

            newShow = Show(c.channelId,
                            show['Title'],
                            start,
                            end,
                            show['Description'],
                            show['IsNewSeries'],
                            show['IsRepeat'])

            db_session.add(newShow)

    db_session.commit()