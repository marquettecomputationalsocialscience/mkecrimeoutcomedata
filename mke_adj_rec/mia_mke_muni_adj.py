from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from mke_adj_rec_db import *

import sys
import time

sys.setrecursionlimit(100000)

db = create_engine('sqlite:///mke_adj_rec.db', echo = False)

Session = sessionmaker(bind = db)
session = Session()

ch_opt = webdriver.ChromeOptions()
#ch_opt.add_argument('headless')
ch_opt.add_argument('user-agent = UserAgent().random')

ch_dr = webdriver.Chrome(chrome_options = ch_opt)

def mia_mke_muni_adj(case_lst):

    if type(case_lst) is list:
        for item in case_lst:
            mia_mke_muni_adj(item)

    else:

        ch_dr.get('https://query.municourt.milwaukee.gov/')
        case_no_in = ch_dr.find_element_by_id('QuerySection_DisclaimerSection_DisclaimerAgree')
        time.sleep(2)
        case_no_in.send_keys(Keys.RETURN)
        case_no = ch_dr.find_element_by_id('QuerySection_MainSearchSection_txtCaseNumber')
        case_no.send_keys(case_lst)
        time.sleep(2)
        case_no.send_keys(Keys.RETURN)
        time.sleep(2)

        try:

            d_case_no = ch_dr.find_element_by_xpath('//*[@id="QuerySection_CaseDetailSection_lblCaseNumber"]').text
            print(case_lst, ' exists.  Further action required.')

        except:

            mia_case_no = ch_dr.find_element_by_xpath('//*[@id="QuerySection_ResultNotFoundSection_lblExplanationFooter"]').text

            old_record = session.query(MkeMuniCourt).filter(MkeMuniCourt.d_case_no == str(case_lst))
            old_record.delete()

            new_record = MiaMkeMuniCourt(str(case_lst))
            session.add(new_record)

            session.commit()

            print(case_lst, ' does not exist--recorded to proper schema.')

case_lst = [int(i[0]) for i in sorted(session.query(MkeMuniCourt.d_case_no).filter(MkeMuniCourt.d_name == None))]

mia_mke_muni_adj(case_lst)
