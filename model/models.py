from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from database import Base

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

class Show(Base):
    __tablename__ = 'show'
    id = Column(Integer, primary_key=True)
    channelId = Column(Integer, ForeignKey("channels.channelId"))
    title = Column(String(50), unique=False)
    startTime = Column(DateTime)
    endTime = Column(DateTime)
    description = Column(String(400))
    isNewSeries = Column(Boolean)
    isRepeat = Column(Boolean)

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