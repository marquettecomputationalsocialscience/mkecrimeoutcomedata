from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from datetime import datetime

from gis_san_lst import gis_san_lst_0
from mke_adj_rec_db import *

import googlemaps
import sys
import time

sys.setrecursionlimit(100000)

db = create_engine('sqlite:///mke_adj_db/mke_adj_rec.db', echo = False)

Session = sessionmaker(bind = db)
session = Session()

gm = googlemaps.Client(key = 'key')

def gis_mke_muni_adj(case_lst):

    if type(case_lst) is list:
        for case in case_lst:
            gis_mke_muni_adj(case)
            print(case, ' passed @ ', datetime.time(datetime.now()))
            time.sleep(1)

    else:

        query = session.query(MkeMuniCourt.c_location).filter(MkeMuniCourt.d_case_no == case_lst)
        data = query.first()
        addr = data.c_location.upper() + ' MILWAUKEE, WI'
        f_addr = gis_san_lst_0(addr)

        try:

            gc = gm.geocode(f_addr)
            lat = gc[0]['geometry']['location']['lat']
            lng = gc[0]['geometry']['location']['lng']
            gf_addr = gc[0]['formatted_address']

            new_record = GisMkeMuniCourt(case_lst, lat, lng, f_addr, gf_addr)
            session.add(new_record)
            session.commit()

            print(case_lst, ' GIS entered.')

        except:

            new_record = GisMkeMuniCourt(case_lst, 0, 0, f_addr, None)
            session.add(new_record)
            session.commit()

            print(case_lst, ' entered, but has conflicts.')

adj_case_lst = [int(i[0]) for i in sorted(session.query(MkeMuniCourt.d_case_no).filter(MkeMuniCourt.c_location != None))]
gis_case_lst = [int(i[0]) for i in sorted(session.query(GisMkeMuniCourt.g_case_no).filter(GisMkeMuniCourt.g_case_no != None))]
f_case_lst = sorted(list(set(adj_case_lst) - set(gis_case_lst)))

gis_mke_muni_adj(adj_case_lst[:500])