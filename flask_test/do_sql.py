# -*- coding: utf-8 -*-

from flaski.database import init_db
from flaski.database import db_session
from flaski.models import WikiContent

# init_dbでwikicontentsテーブル作成
# init_db()

# idは連番。title、textを指定。dateは日時が勝手に入る。
c1 = WikiContent("Flask", "micro framework")
db_session.add(c1)
db_session.commit()
c2 = WikiContent("python", "pppython")
c3 = WikiContent("kobito", "kakure-momojiri")
db_session.add(c2)
db_session.add(c3)
db_session.commit()

