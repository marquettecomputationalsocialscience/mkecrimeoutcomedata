from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from datetime import datetime

from gis_san_lst import gis_san_lst_1
from mke_adj_rec_db import *

import googlemaps
import sys
import time

sys.setrecursionlimit(100000)

db = create_engine('sqlite:///mke_adj_db/mke_adj_rec.db', echo = False)

Session = sessionmaker(bind = db)
session = Session()

gm = googlemaps.Client(key = 'key')

def san_gis_mke_muni_adj(case_lst):

    if type(case_lst) is list:
        for case in case_lst:
            san_gis_mke_muni_adj(case)
            print(case, ' passed @ ', datetime.time(datetime.now()))
            time.sleep(1)

    else:

        query = session.query(GisMkeMuniCourt.f_addr).filter(GisMkeMuniCourt.g_case_no == case_lst)
        data = query.first()
        addr = data.f_addr
        f_addr = gis_san_lst_1(addr)

        try:

            gc = gm.geocode(f_addr)
            lat = gc[0]['geometry']['location']['lat']
            lng = gc[0]['geometry']['location']['lng']
            gf_addr = gc[0]['formatted_address']

            session.query(GisMkeMuniCourt).filter(GisMkeMuniCourt.g_case_no == case_lst).update({\
            'g_lat': lat, 'g_lng': lng, 'f_addr': f_addr, 'gf_addr': gf_addr})
            session.commit()

            print(case_lst, ' modified--recorded to its original schema.')

        except:

            print(c_no, ' has conflicts.')
            pass

gis_case_lst = [int(i[0]) for i in sorted(session.query(GisMkeMuniCourt.g_case_no).filter(GisMkeMuniCourt.g_lat == 0, GisMkeMuniCourt.g_lng == 0,))]

gis_case_lst = []

san_gis_mke_muni_adj(sorted(gis_case_lst))
