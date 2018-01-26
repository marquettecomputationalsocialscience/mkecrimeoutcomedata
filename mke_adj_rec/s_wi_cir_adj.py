from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from mke_adj_rec_db import *

import random
import sys
import time

sys.setrecursionlimit(20000)

db = create_engine('sqlite:///mke_adj_rec.db', echo = False)

Session = sessionmaker(bind = db)
session = Session()

ch_opt = webdriver.ChromeOptions()
#ch_opt.add_argument('headless')
ch_opt.add_argument('user-agent = UserAgent().random')

ch_dr = webdriver.Chrome(chrome_options = ch_opt)

def s_wi_cir_adj(c_no):

    c_no_in = str(c_no).zfill(6)
    ch_dr.get('https://wccabeta.wicourts.gov/caseDetail.html?caseNo=2014CF'+ c_no_in + '&countyNo=40&mode=details')
    time.sleep(5)
    case_det = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[4]/div/button').click()
    time.sleep(5)

    try:

        d_case_no = ch_dr.find_element_by_xpath('//*[@id="case-header-info"]/h4/span[2]').text
        d_name = ch_dr.find_element_by_xpath('//*[@id="defendant"]/div[3]/div[1]/dl[1]/dd').text
        d_dob = ch_dr.find_element_by_xpath('//*[@id="defendant"]/div[3]/div[1]/dl[2]/dd').text
        d_sex = ch_dr.find_element_by_xpath('//*[@id="defendant"]/div[3]/div[1]/dl[3]/dd').text
        d_race = ch_dr.find_element_by_xpath('//*[@id="defendant"]/div[3]/div[1]/dl[4]/dd').text
        d_address = ch_dr.find_element_by_xpath('//*[@id="defendant"]/div[3]/div[1]/dl[5]/dd').text

        f_d_dob = '%m-%d-%Y'
        r_d_dob = datetime.strptime(d_dob, f_d_dob)

        record = WiCirCourtDefInfo(d_case_no, d_name, r_d_dob, d_sex, d_race, d_address)
        session.add(record)
        session.commit()

        print(d_case_no, ' entered--defendant info.')

    except:

        pass

    try:

        d_case_no = ch_dr.find_element_by_xpath('//*[@id="case-header-info"]/h4/span[2]').text
        c_case_type_1 = ch_dr.find_element_by_xpath('//*[@id="summary"]/div[2]/dl[2]/dd').text
        c_off_cnt_1 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[1]/td[1]').text
        c_off_date_1 = ch_dr.find_element_by_xpath('//*[@id="fullCharges"]/div[2]/div[1]/div/div[1]/dl[5]/dd').text
        c_statute_1 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[1]/td[2]').text
        c_desc_1 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[1]/td[3]').text
        c_severity_1 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[1]/td[4]').text
        c_dispo_1 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[1]/td[5]').text

        f_c_off_date_1 = '%m-%d-%Y'
        r_c_off_date_1 = datetime.strptime(c_off_date_1, f_c_off_date_1)

        record_1 = WiCirCourtCaseInfo(d_case_no, c_case_type_1, c_off_cnt_1, r_c_off_date_1, c_statute_1, c_desc_1, c_severity_1, c_dispo_1)
        session.add(record_1)
        session.commit()

        print(d_case_no, ' entered--offense 1.')

    except:

        pass

    try:

        d_case_no = ch_dr.find_element_by_xpath('//*[@id="case-header-info"]/h4/span[2]').text
        c_case_type_2 = ch_dr.find_element_by_xpath('//*[@id="summary"]/div[2]/dl[2]/dd').text
        c_off_cnt_2 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[2]/td[1]').text
        c_off_date_2 = ch_dr.find_element_by_xpath('//*[@id="fullCharges"]/div[2]/div[2]/div/div[1]/dl[5]/dd').text
        c_statute_2 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[2]/td[2]').text
        c_desc_2 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[2]/td[3]').text
        c_severity_2 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[2]/td[4]').text
        c_dispo_2 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[2]/td[5]').text

        f_c_off_date_2 = '%m-%d-%Y'
        r_c_off_date_2 = datetime.strptime(c_off_date_2, f_c_off_date_2)

        record_2 = WiCirCourtCaseInfo(d_case_no, c_case_type_2, c_off_cnt_2, r_c_off_date_2, c_statute_2, c_desc_2, c_severity_2, c_dispo_2)
        session.add(record_2)
        session.commit()

        print(d_case_no, ' entered--offense 2.')

    except:

        pass

    try:

        d_case_no = ch_dr.find_element_by_xpath('//*[@id="case-header-info"]/h4/span[2]').text
        c_case_type_3 = ch_dr.find_element_by_xpath('//*[@id="summary"]/div[2]/dl[2]/dd').text
        c_off_cnt_3 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[3]/td[1]').text
        c_off_date_3 = ch_dr.find_element_by_xpath('//*[@id="fullCharges"]/div[2]/div[3]/div/div[1]/dl[5]/dd').text
        c_statute_3 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[3]/td[2]').text
        c_desc_3 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[3]/td[3]').text
        c_severity_3 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[3]/td[4]').text
        c_dispo_3 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[3]/td[5]').text

        f_c_off_date_3 = '%m-%d-%Y'
        r_c_off_date_3 = datetime.strptime(c_off_date_3, f_c_off_date_3)

        record_3 = WiCirCourtCaseInfo(d_case_no, c_case_type_3, c_off_cnt_3, r_c_off_date_3, c_statute_3, c_desc_3, c_severity_3, c_dispo_3)
        session.add(record_3)
        session.commit()

        print(d_case_no, ' entered--offense 3.')

    except:

        pass

    try:

        d_case_no = ch_dr.find_element_by_xpath('//*[@id="case-header-info"]/h4/span[2]').text
        c_case_type_4 = ch_dr.find_element_by_xpath('//*[@id="summary"]/div[2]/dl[2]/dd').text
        c_off_cnt_4 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[4]/td[1]').text
        c_off_date_4 = ch_dr.find_element_by_xpath('//*[@id="fullCharges"]/div[2]/div[4]/div/div[1]/dl[5]/dd').text
        c_statute_4 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[4]/td[2]').text
        c_desc_4 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[4]/td[3]').text
        c_severity_4 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[4]/td[4]').text
        c_dispo_4 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[4]/td[5]').text

        f_c_off_date_4 = '%m-%d-%Y'
        r_c_off_date_4 = datetime.strptime(c_off_date_4, f_c_off_date_4)

        record_4 = WiCirCourtCaseInfo(d_case_no, c_case_type_4, c_off_cnt_4, r_c_off_date_4, c_statute_4, c_desc_4, c_severity_4, c_dispo_4)
        session.add(record_4)
        session.commit()

        print(d_case_no, ' entered--offense 4.')

    except:

        pass

    try:

        d_case_no = ch_dr.find_element_by_xpath('//*[@id="case-header-info"]/h4/span[2]').text
        c_case_type_5 = ch_dr.find_element_by_xpath('//*[@id="summary"]/div[2]/dl[2]/dd').text
        c_off_cnt_5 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[5]/td[1]').text
        c_off_date_5 = ch_dr.find_element_by_xpath('//*[@id="fullCharges"]/div[2]/div[5]/div/div[1]/dl[5]/dd').text
        c_statute_5 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[5]/td[2]').text
        c_desc_5 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[5]/td[3]').text
        c_severity_5 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[5]/td[4]').text
        c_dispo_5 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[5]/td[5]').text

        f_c_off_date_5 = '%m-%d-%Y'
        r_c_off_date_5 = datetime.strptime(c_off_date_5, f_c_off_date_5)

        record_5 = WiCirCourtCaseInfo(d_case_no, c_case_type_5, c_off_cnt_5, r_c_off_date_5, c_statute_5, c_desc_5, c_severity_5, c_dispo_5)
        session.add(record_5)
        session.commit()

        print(d_case_no, ' entered--offense 5.')

    except:

        pass

    try:

        d_case_no = ch_dr.find_element_by_xpath('//*[@id="case-header-info"]/h4/span[2]').text
        c_case_type_6 = ch_dr.find_element_by_xpath('//*[@id="summary"]/div[2]/dl[2]/dd').text
        c_off_cnt_6 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[6]/td[1]').text
        c_off_date_6 = ch_dr.find_element_by_xpath('//*[@id="fullCharges"]/div[2]/div[6]/div/div[1]/dl[5]/dd').text
        c_statute_6 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[6]/td[2]').text
        c_desc_6 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[6]/td[3]').text
        c_severity_6 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[6]/td[4]').text
        c_dispo_6 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[6]/td[5]').text

        f_c_off_date_6 = '%m-%d-%Y'
        r_c_off_date_6 = datetime.strptime(c_off_date_6, f_c_off_date_6)

        record_6 = WiCirCourtCaseInfo(d_case_no, c_case_type_6, c_off_cnt_6, r_c_off_date_6, c_statute_6, c_desc_6, c_severity_6, c_dispo_6)
        session.add(record_6)
        session.commit()

        print(d_case_no, ' entered--offense 6.')

    except:

        pass

    try:

        d_case_no = ch_dr.find_element_by_xpath('//*[@id="case-header-info"]/h4/span[2]').text
        c_case_type_7 = ch_dr.find_element_by_xpath('//*[@id="summary"]/div[2]/dl[2]/dd').text
        c_off_cnt_7 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[7]/td[1]').text
        c_off_date_7 = ch_dr.find_element_by_xpath('//*[@id="fullCharges"]/div[2]/div[7]/div/div[1]/dl[5]/dd').text
        c_statute_7 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[7]/td[2]').text
        c_desc_7 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[7]/td[3]').text
        c_severity_7 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[7]/td[4]').text
        c_dispo_7 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[7]/td[5]').text

        f_c_off_date_7 = '%m-%d-%Y'
        r_c_off_date_7 = datetime.strptime(c_off_date_7, f_c_off_date_7)

        record_7 = WiCirCourtCaseInfo(d_case_no, c_case_type_7, c_off_cnt_7, r_c_off_date_7, c_statute_7, c_desc_7, c_severity_7, c_dispo_7)
        session.add(record_7)
        session.commit()

        print(d_case_no, ' entered--offense 7.')

    except:

        pass

    try:

        d_case_no = ch_dr.find_element_by_xpath('//*[@id="case-header-info"]/h4/span[2]').text
        c_case_type_8 = ch_dr.find_element_by_xpath('//*[@id="summary"]/div[2]/dl[2]/dd').text
        c_off_cnt_8 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[8]/td[1]').text
        c_off_date_8 = ch_dr.find_element_by_xpath('//*[@id="fullCharges"]/div[2]/div[8]/div/div[1]/dl[5]/dd').text
        c_statute_8 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[8]/td[2]').text
        c_desc_8 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[8]/td[3]').text
        c_severity_8 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[8]/td[4]').text
        c_dispo_8 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[8]/td[5]').text

        f_c_off_date_8 = '%m-%d-%Y'
        r_c_off_date_8 = datetime.strptime(c_off_date_8, f_c_off_date_8)

        record_8 = WiCirCourtCaseInfo(d_case_no, c_case_type_8, c_off_cnt_8, r_c_off_date_8, c_statute_8, c_desc_8, c_severity_8, c_dispo_8)
        session.add(record_8)
        session.commit()

        print(d_case_no, ' entered--offense 8.')

    except:

        pass

    try:

        d_case_no = ch_dr.find_element_by_xpath('//*[@id="case-header-info"]/h4/span[2]').text
        c_case_type_9 = ch_dr.find_element_by_xpath('//*[@id="summary"]/div[2]/dl[2]/dd').text
        c_off_cnt_9 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[9]/td[1]').text
        c_off_date_9 = ch_dr.find_element_by_xpath('//*[@id="fullCharges"]/div[2]/div[9]/div/div[1]/dl[5]/dd').text
        c_statute_9 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[9]/td[2]').text
        c_desc_9 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[9]/td[3]').text
        c_severity_9 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[9]/td[4]').text
        c_dispo_9 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[9]/td[5]').text

        f_c_off_date_9 = '%m-%d-%Y'
        r_c_off_date_9 = datetime.strptime(c_off_date_9, f_c_off_date_9)

        record_9 = WiCirCourtCaseInfo(d_case_no, c_case_type_9, c_off_cnt_9, r_c_off_date_9, c_statute_9, c_desc_9, c_severity_9, c_dispo_9)
        session.add(record_9)
        session.commit()

        print(d_case_no, ' entered--offense 9.')

    except:

        pass

    try:

        d_case_no = ch_dr.find_element_by_xpath('//*[@id="case-header-info"]/h4/span[2]').text
        c_case_type_10 = ch_dr.find_element_by_xpath('//*[@id="summary"]/div[2]/dl[2]/dd').text
        c_off_cnt_10 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[10]/td[1]').text
        c_off_date_10 = ch_dr.find_element_by_xpath('//*[@id="fullCharges"]/div[2]/div[10]/div/div[1]/dl[5]/dd').text
        c_statute_10 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[10]/td[2]').text
        c_desc_10 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[10]/td[3]').text
        c_severity_10 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[10]/td[4]').text
        c_dispo_10 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[10]/td[5]').text

        f_c_off_date_10 = '%m-%d-%Y'
        r_c_off_date_10 = datetime.strptime(c_off_date_10, f_c_off_date_10)

        record_10 = WiCirCourtCaseInfo(d_case_no, c_case_type_10, c_off_cnt_10, r_c_off_date_10, c_statute_10, c_desc_10, c_severity_10, c_dispo_10)
        session.add(record_10)
        session.commit()

        print(d_case_no, ' entered--offense 10.')

    except:

        pass

    if c_no < n:

        time.sleep(3)
        s_wi_cir_adj(c_no + 1)

    else:

        ch_dr.close()

s_wi_cir_adj(n)
