from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from datetime import datetime

from gis_san_lst import gis_san_lst_0
from mke_adj_rec_db import *

import googlemaps
import sqlite3
import sys
import time

sys.setrecursionlimit(100000)

db = create_engine('sqlite:///mke_adj_db/mke_adj_rec.db', echo = False)

Session = sessionmaker(bind = db)
session = Session()

gm = googlemaps.Client(key = 'api_key')

def gis_mke_muni_adj(case_lst):

    if type(case_lst) is list:
        for case in case_lst:
            gis_mke_muni_adj(case)
            print(case, ' passed @ ', datetime.time(datetime.now()))

    else:

        query = session.query(MkeMuniCourt).filter(MkeMuniCourt.d_case_no == case_lst)
        data = query.first()
        addr = data.c_location.upper() + ' MILWAUKEE, WI'
        f_addr = gis_san_lst_0(addr)

        try:

            gc = gm.geocode(f_addr)
            lat = gc[0]['geometry']['location']['lat']
            lng = gc[0]['geometry']['location']['lng']
            gf_addr = gc[0]['formatted_address']

            new_record = GisMkeMuniCourt(case_lst, lat, lng, f_addr, gf_addr, data.c_case_type,\
            data.c_violation, data.c_violation_date, data.j_finding)
            session.add(new_record)
            session.commit()

            print(case_lst, ' GIS entered.')

        except:

            new_record = GisMkeMuniCourt(case_lst, 0, 0, f_addr, None, None, None, None, None)
            session.add(new_record)
            session.commit()

            print(case_lst, ' entered, but has conflicts.')

def filter():

    conn = sqlite3.connect('mke_adj_db/mke_adj_rec.db')
    cur = conn.cursor()
    cur.execute('''select d_case_no from mke_muni_court where c_location not like "% / %" and c_location not like "% /"''')
    data = cur.fetchall()
    lst = [i[0] for i in data]
    lst = list(map(int, lst))
    return lst

if __name__ == '__main__':

    fil = filter()

    adj_case_lst = [int(i[0]) for i in sorted(session.query(MkeMuniCourt.d_case_no).filter(MkeMuniCourt.c_location != None))]
    gis_case_lst = [int(i[0]) for i in sorted(session.query(GisMkeMuniCourt.g_case_no).filter(GisMkeMuniCourt.g_case_no != None))]
    f_case_lst = sorted(list(set(fil) - set(gis_case_lst)))

    gis_mke_muni_adj(f_case_lst[:2400])
