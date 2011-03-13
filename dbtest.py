# -*- coding: utf-8 -*-

def test():
  con = sqlite3.connect(deone_db)
  con.text_factory=str
  cur = con.cursor()
  #s = '''create table %s(%s)'''%(tbl, s_cols.rstrip(','))
  s = '''create table %s(date text, trans text, symbol text, qty real, price real)'''%(tbl)
  
  s = '''insert into %s values (%s)'''%(tbl, s_cols.rstrip(','))
  cur.execute(s, t)
  con.commit()
  cur.close()

  t = u'深发展Ａ'.encode('utf-8')
  cur.execute(u'select * from StockHist where 股票名称=?'.encode('utf-8'), (t,))
  for row in cur.fetchall()[0:3]:
    today, open, high, low, close, volume=row[0], row[3], row[4], row[5], row[6], row[7]

if __name__ == '__main__':
  test()