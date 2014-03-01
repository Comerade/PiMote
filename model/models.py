from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship, backref
from database import Base

def jsonDatetime(value):
    """Deserialize datetime object into string form for JSON processing."""
    if value is None:
        return None
    return [value.strftime("%Y-%m-%d"), value.strftime("%H:%M:%S")]


class Channel(Base):
    __tablename__ = 'channels'
    channelId = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    rtid = Column(Integer, unique=True)

    def __init__(self, name=None, rtid=None):
        self.name = name
        self.rtid = rtid

    def __repr__(self):
        return '<Name %r>' % (self.name)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'channelId' : self.channelId,
            'name'      : self.name,
            'rtid'      : self.rtid,
            'shows'     : self.serializedShows
        }

    @property
    def serializedShows(self):
        return [ show.serialize for show in self.shows]


class Show(Base):
    __tablename__ = 'show'
    showId = Column(Integer, primary_key=True)
    channelId = Column(Integer, ForeignKey("channels.channelId"))
    title = Column(String(50), unique=False)
    startTime = Column(DateTime)
    endTime = Column(DateTime)
    description = Column(String(1000))
    isNewSeries = Column(Boolean)
    isRepeat = Column(Boolean)

    channel = relationship("Channel", backref=backref('shows'))

    def __init__(self, channelId, title=None, startTime=None, endTime=None, description=None, isNewSeries=None, isRepeat=None):
        self.channelId = channelId
        self.title = title
        self.startTime = startTime
        self.endTime = endTime
        self.description = description
        self.isNewSeries = isNewSeries
        self.isRepeat = isRepeat

    def __repr__(self):
        return '<title %r>' % (self.title)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'showId'        : self.showId,
            'channelId'     : self.channelId,
            'title'         : self.title,
            'startTime'     : jsonDatetime(self.startTime),
            'endTime'       : jsonDatetime(self.endTime),
            'description'   : self.description,
            'isNewSeries'   : self.isNewSeries,
            'isRepeat'      : self.isRepeat
        }