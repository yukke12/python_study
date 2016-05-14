# -*- coding: utf-8 -*-

from flaski.database import init_db
from flaski.database import db_session
from flaski.models import WikiContent

# init_dbでwikicontentsテーブル作成
# init_db()

# idは連番。title、textを指定。dateは日時が勝手に入る(model.pyのデフォルト設定により)。
c1 = WikiContent("Flask", "micro framework")  # カラム1:'Flask' カラム2:'micro framework'を指定してインスタンス作成
db_session.add(c1)                            # insert実行
db_session.commit()                           # commit実行
c2 = WikiContent("python", "pppython")        # 以下同上
c3 = WikiContent("kobito", "kakure-momojiri")
db_session.add(c2)
db_session.add(c3)
db_session.commit()

