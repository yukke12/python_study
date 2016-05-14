# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String, Text, DateTime
from flaski.database import Base
from datetime import datetime


class WikiContent(Base):
    __tablename__ = 'wikicontents'                  # テーブル名
    id = Column(Integer, primary_key=True)          # カラム１(id)
    title = Column(String(128), unique=True)        # カラム２(title)
    body = Column(Text)                             # カラム3(body)
    date = Column(DateTime, default=datetime.now()) # カラム４(date) デフォルト現在日時を設定

    def __init__(self, title=None, body=None, date=None):
        self.title = title
        self.body = body
        self.date = date

    def __repr__(self):
        return '<Title %r>' % (self.title)
