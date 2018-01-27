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

    c_no_in = '2016CF' + str(c_no).zfill(6)
    ch_dr.get('https://wccabeta.wicourts.gov/caseDetail.html?caseNo='+ c_no_in + '&countyNo=40&mode=details')
    time.sleep(5)

    try:

        case_det = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[4]/div/button').click()
        time.sleep(5)

        d_case_type = ch_dr.find_element_by_xpath('//*[@id="summary"]/div[2]/dl[2]/dd').text
        d_name = ch_dr.find_element_by_xpath('//*[@id="defendant"]/div[3]/div[1]/dl[1]/dd').text
        d_dob = ch_dr.find_element_by_xpath('//*[@id="defendant"]/div[3]/div[1]/dl[2]/dd').text
        d_sex = ch_dr.find_element_by_xpath('//*[@id="defendant"]/div[3]/div[1]/dl[3]/dd').text
        d_race = ch_dr.find_element_by_xpath('//*[@id="defendant"]/div[3]/div[1]/dl[4]/dd').text
        d_address = ch_dr.find_element_by_xpath('//*[@id="defendant"]/div[3]/div[1]/dl[5]/dd').text
        d_filing_date = ch_dr.find_element_by_xpath('//*[@id="summary"]/div[2]/dl[1]/dd').text
        d_case_status = ch_dr.find_element_by_xpath('//*[@id="summary"]/div[2]/dl[3]/dd').text
        d_branch_id = ch_dr.find_element_by_xpath('//*[@id="summary"]/div[3]/dl[3]/dd').text

        f_d_dob = '%m-%d-%Y'
        r_d_dob = datetime.strptime(d_dob, f_d_dob)
        f_d_filing_date = '%m-%d-%Y'
        r_d_filing_date = datetime.strptime(d_filing_date, f_d_filing_date)

        record = WiCirCourtDefInfo(c_no_in, d_case_type, d_name.upper(), r_d_dob,\
        d_sex, d_race, d_address, r_d_filing_date, d_case_status, d_branch_id)
        session.add(record)
        session.commit()

        print(c_no_in, ' entered--defendant info.')

    except:

        record = WiCirCourtDefInfo(c_no_in, None, None, None, None, None, None,\
        None, None, None)
        session.add(record)
        session.commit()
        ptiny(c_no_in, ' entered--case may not exist or an error has occurred.')
        pass

    try:

        c_off_cnt_1 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[1]/td[1]').text
        c_off_date_1 = ch_dr.find_element_by_xpath('//*[@id="fullCharges"]/div[2]/div[1]/div/div[1]/dl[5]/dd').text
        c_statute_1 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[1]/td[2]').text
        c_desc_1 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[1]/td[3]').text
        c_severity_1 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[1]/td[4]').text
        c_dispo_1 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[1]/td[5]').text

        f_c_off_date_1 = '%m-%d-%Y'
        r_c_off_date_1 = datetime.strptime(c_off_date_1, f_c_off_date_1)

        record_1 = WiCirCourtCaseInfo(c_no_in, c_off_cnt_1, r_c_off_date_1, c_statute_1, c_desc_1, c_severity_1, c_dispo_1)
        session.add(record_1)
        session.commit()

        print(c_no_in, ' entered--offense 1.')

    except:

        pass

    try:

        c_off_cnt_2 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[2]/td[1]').text
        c_off_date_2 = ch_dr.find_element_by_xpath('//*[@id="fullCharges"]/div[2]/div[2]/div/div[1]/dl[5]/dd').text
        c_statute_2 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[2]/td[2]').text
        c_desc_2 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[2]/td[3]').text
        c_severity_2 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[2]/td[4]').text
        c_dispo_2 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[2]/td[5]').text

        f_c_off_date_2 = '%m-%d-%Y'
        r_c_off_date_2 = datetime.strptime(c_off_date_2, f_c_off_date_2)

        record_2 = WiCirCourtCaseInfo(c_no_in, c_off_cnt_2, r_c_off_date_2, c_statute_2, c_desc_2, c_severity_2, c_dispo_2)
        session.add(record_2)
        session.commit()

        print(c_no_in, ' entered--offense 2.')

    except:

        pass

    try:

        c_off_cnt_3 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[3]/td[1]').text
        c_off_date_3 = ch_dr.find_element_by_xpath('//*[@id="fullCharges"]/div[2]/div[3]/div/div[1]/dl[5]/dd').text
        c_statute_3 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[3]/td[2]').text
        c_desc_3 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[3]/td[3]').text
        c_severity_3 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[3]/td[4]').text
        c_dispo_3 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[3]/td[5]').text

        f_c_off_date_3 = '%m-%d-%Y'
        r_c_off_date_3 = datetime.strptime(c_off_date_3, f_c_off_date_3)

        record_3 = WiCirCourtCaseInfo(c_no_in, c_off_cnt_3, r_c_off_date_3, c_statute_3, c_desc_3, c_severity_3, c_dispo_3)
        session.add(record_3)
        session.commit()

        print(c_no_in, ' entered--offense 3.')

    except:

        pass

    try:

        c_off_cnt_4 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[4]/td[1]').text
        c_off_date_4 = ch_dr.find_element_by_xpath('//*[@id="fullCharges"]/div[2]/div[4]/div/div[1]/dl[5]/dd').text
        c_statute_4 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[4]/td[2]').text
        c_desc_4 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[4]/td[3]').text
        c_severity_4 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[4]/td[4]').text
        c_dispo_4 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[4]/td[5]').text

        f_c_off_date_4 = '%m-%d-%Y'
        r_c_off_date_4 = datetime.strptime(c_off_date_4, f_c_off_date_4)

        record_4 = WiCirCourtCaseInfo(c_no_in, c_off_cnt_4, r_c_off_date_4, c_statute_4, c_desc_4, c_severity_4, c_dispo_4)
        session.add(record_4)
        session.commit()

        print(c_no_in, ' entered--offense 4.')

    except:

        pass

    try:

        c_off_cnt_5 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[5]/td[1]').text
        c_off_date_5 = ch_dr.find_element_by_xpath('//*[@id="fullCharges"]/div[2]/div[5]/div/div[1]/dl[5]/dd').text
        c_statute_5 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[5]/td[2]').text
        c_desc_5 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[5]/td[3]').text
        c_severity_5 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[5]/td[4]').text
        c_dispo_5 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[5]/td[5]').text

        f_c_off_date_5 = '%m-%d-%Y'
        r_c_off_date_5 = datetime.strptime(c_off_date_5, f_c_off_date_5)

        record_5 = WiCirCourtCaseInfo(c_no_in, c_off_cnt_5, r_c_off_date_5, c_statute_5, c_desc_5, c_severity_5, c_dispo_5)
        session.add(record_5)
        session.commit()

        print(c_no_in, ' entered--offense 5.')

    except:

        pass

    try:

        c_off_cnt_6 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[6]/td[1]').text
        c_off_date_6 = ch_dr.find_element_by_xpath('//*[@id="fullCharges"]/div[2]/div[6]/div/div[1]/dl[5]/dd').text
        c_statute_6 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[6]/td[2]').text
        c_desc_6 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[6]/td[3]').text
        c_severity_6 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[6]/td[4]').text
        c_dispo_6 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[6]/td[5]').text

        f_c_off_date_6 = '%m-%d-%Y'
        r_c_off_date_6 = datetime.strptime(c_off_date_6, f_c_off_date_6)

        record_6 = WiCirCourtCaseInfo(c_no_in, c_off_cnt_6, r_c_off_date_6, c_statute_6, c_desc_6, c_severity_6, c_dispo_6)
        session.add(record_6)
        session.commit()

        print(c_no_in, ' entered--offense 6.')

    except:

        pass

    try:

        c_off_cnt_7 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[7]/td[1]').text
        c_off_date_7 = ch_dr.find_element_by_xpath('//*[@id="fullCharges"]/div[2]/div[7]/div/div[1]/dl[5]/dd').text
        c_statute_7 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[7]/td[2]').text
        c_desc_7 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[7]/td[3]').text
        c_severity_7 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[7]/td[4]').text
        c_dispo_7 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[7]/td[5]').text

        f_c_off_date_7 = '%m-%d-%Y'
        r_c_off_date_7 = datetime.strptime(c_off_date_7, f_c_off_date_7)

        record_7 = WiCirCourtCaseInfo(c_no_in, c_off_cnt_7, r_c_off_date_7, c_statute_7, c_desc_7, c_severity_7, c_dispo_7)
        session.add(record_7)
        session.commit()

        print(c_no_in, ' entered--offense 7.')

    except:

        pass

    try:

        c_off_cnt_8 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[8]/td[1]').text
        c_off_date_8 = ch_dr.find_element_by_xpath('//*[@id="fullCharges"]/div[2]/div[8]/div/div[1]/dl[5]/dd').text
        c_statute_8 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[8]/td[2]').text
        c_desc_8 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[8]/td[3]').text
        c_severity_8 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[8]/td[4]').text
        c_dispo_8 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[8]/td[5]').text

        f_c_off_date_8 = '%m-%d-%Y'
        r_c_off_date_8 = datetime.strptime(c_off_date_8, f_c_off_date_8)

        record_8 = WiCirCourtCaseInfo(c_no_in, c_off_cnt_8, r_c_off_date_8, c_statute_8, c_desc_8, c_severity_8, c_dispo_8)
        session.add(record_8)
        session.commit()

        print(c_no_in, ' entered--offense 8.')

    except:

        pass

    try:

        c_off_cnt_9 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[9]/td[1]').text
        c_off_date_9 = ch_dr.find_element_by_xpath('//*[@id="fullCharges"]/div[2]/div[9]/div/div[1]/dl[5]/dd').text
        c_statute_9 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[9]/td[2]').text
        c_desc_9 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[9]/td[3]').text
        c_severity_9 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[9]/td[4]').text
        c_dispo_9 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[9]/td[5]').text

        f_c_off_date_9 = '%m-%d-%Y'
        r_c_off_date_9 = datetime.strptime(c_off_date_9, f_c_off_date_9)

        record_9 = WiCirCourtCaseInfo(c_no_in, c_off_cnt_9, r_c_off_date_9, c_statute_9, c_desc_9, c_severity_9, c_dispo_9)
        session.add(record_9)
        session.commit()

        print(c_no_in, ' entered--offense 9.')

    except:

        pass

    try:

        c_off_cnt_10 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[10]/td[1]').text
        c_off_date_10 = ch_dr.find_element_by_xpath('//*[@id="fullCharges"]/div[2]/div[10]/div/div[1]/dl[5]/dd').text
        c_statute_10 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[10]/td[2]').text
        c_desc_10 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[10]/td[3]').text
        c_severity_10 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[10]/td[4]').text
        c_dispo_10 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[10]/td[5]').text

        f_c_off_date_10 = '%m-%d-%Y'
        r_c_off_date_10 = datetime.strptime(c_off_date_10, f_c_off_date_10)

        record_10 = WiCirCourtCaseInfo(c_no_in, c_off_cnt_10, r_c_off_date_10, c_statute_10, c_desc_10, c_severity_10, c_dispo_10)
        session.add(record_10)
        session.commit()

        print(c_no_in, ' entered--offense 10.')

    except:

        pass

    try:

        c_off_cnt_11 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[11]/td[1]').text
        c_off_date_11 = ch_dr.find_element_by_xpath('//*[@id="fullCharges"]/div[2]/div[11]/div/div[1]/dl[5]/dd').text
        c_statute_11 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[11]/td[2]').text
        c_desc_11 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[11]/td[3]').text
        c_severity_11 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[11]/td[4]').text
        c_dispo_11 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[11]/td[5]').text

        f_c_off_date_11 = '%m-%d-%Y'
        r_c_off_date_11 = datetime.strptime(c_off_date_11, f_c_off_date_11)

        record_11 = WiCirCourtCaseInfo(c_no_in, c_off_cnt_11, r_c_off_date_11, c_statute_11, c_desc_11, c_severity_11, c_dispo_11)
        session.add(record_11)
        session.commit()

        print(c_no_in, ' entered--offense 11.')

    except:

        pass

    try:

        c_off_cnt_12 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[12]/td[1]').text
        c_off_date_12 = ch_dr.find_element_by_xpath('//*[@id="fullCharges"]/div[2]/div[12]/div/div[1]/dl[5]/dd').text
        c_statute_12 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[12]/td[2]').text
        c_desc_12 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[12]/td[3]').text
        c_severity_12 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[12]/td[4]').text
        c_dispo_12 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[12]/td[5]').text

        f_c_off_date_12 = '%m-%d-%Y'
        r_c_off_date_12 = datetime.strptime(c_off_date_12, f_c_off_date_12)

        record_12 = WiCirCourtCaseInfo(c_no_in, c_off_cnt_12, r_c_off_date_12, c_statute_12, c_desc_12, c_severity_12, c_dispo_12)
        session.add(record_12)
        session.commit()

        print(c_no_in, ' entered--offense 12.')

    except:

        pass

    try:

        c_off_cnt_13 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[13]/td[1]').text
        c_off_date_13 = ch_dr.find_element_by_xpath('//*[@id="fullCharges"]/div[2]/div[13]/div/div[1]/dl[5]/dd').text
        c_statute_13 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[13]/td[2]').text
        c_desc_13 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[13]/td[3]').text
        c_severity_13 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[13]/td[4]').text
        c_dispo_13 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[13]/td[5]').text

        f_c_off_date_13 = '%m-%d-%Y'
        r_c_off_date_13 = datetime.strptime(c_off_date_13, f_c_off_date_13)

        record_13 = WiCirCourtCaseInfo(c_no_in, c_off_cnt_13, r_c_off_date_13, c_statute_13, c_desc_13, c_severity_13, c_dispo_13)
        session.add(record_13)
        session.commit()

        print(c_no_in, ' entered--offense 13.')

    except:

        pass

    try:

        c_off_cnt_14 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[14]/td[1]').text
        c_off_date_14 = ch_dr.find_element_by_xpath('//*[@id="fullCharges"]/div[2]/div[14]/div/div[1]/dl[5]/dd').text
        c_statute_14 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[14]/td[2]').text
        c_desc_14 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[14]/td[3]').text
        c_severity_14 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[14]/td[4]').text
        c_dispo_14 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[14]/td[5]').text

        f_c_off_date_14 = '%m-%d-%Y'
        r_c_off_date_14 = datetime.strptime(c_off_date_14, f_c_off_date_14)

        record_14 = WiCirCourtCaseInfo(c_no_in, c_off_cnt_14, r_c_off_date_14, c_statute_14, c_desc_14, c_severity_14, c_dispo_14)
        session.add(record_14)
        session.commit()

        print(c_no_in, ' entered--offense 14.')

    except:

        pass

    try:

        c_off_cnt_15 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[15]/td[1]').text
        c_off_date_15 = ch_dr.find_element_by_xpath('//*[@id="fullCharges"]/div[2]/div[15]/div/div[1]/dl[5]/dd').text
        c_statute_15 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[15]/td[2]').text
        c_desc_15 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[15]/td[3]').text
        c_severity_15 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[15]/td[4]').text
        c_dispo_15 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[15]/td[5]').text

        f_c_off_date_15 = '%m-%d-%Y'
        r_c_off_date_15 = datetime.strptime(c_off_date_15, f_c_off_date_15)

        record_15 = WiCirCourtCaseInfo(c_no_in, c_off_cnt_15, r_c_off_date_15, c_statute_15, c_desc_15, c_severity_15, c_dispo_15)
        session.add(record_15)
        session.commit()

        print(c_no_in, ' entered--offense 15.')

    except:

        pass

    try:

        c_off_cnt_16 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[16]/td[1]').text
        c_off_date_16 = ch_dr.find_element_by_xpath('//*[@id="fullCharges"]/div[2]/div[16]/div/div[1]/dl[5]/dd').text
        c_statute_16 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[16]/td[2]').text
        c_desc_16 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[16]/td[3]').text
        c_severity_16 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[16]/td[4]').text
        c_dispo_16 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[16]/td[5]').text

        f_c_off_date_16 = '%m-%d-%Y'
        r_c_off_date_16 = datetime.strptime(c_off_date_16, f_c_off_date_16)

        record_16 = WiCirCourtCaseInfo(c_no_in, c_off_cnt_16, r_c_off_date_16, c_statute_16, c_desc_16, c_severity_16, c_dispo_16)
        session.add(record_16)
        session.commit()

        print(c_no_in, ' entered--offense 16.')

    except:

        pass

    try:

        c_off_cnt_17 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[17]/td[1]').text
        c_off_date_17 = ch_dr.find_element_by_xpath('//*[@id="fullCharges"]/div[2]/div[17]/div/div[1]/dl[5]/dd').text
        c_statute_17 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[17]/td[2]').text
        c_desc_17 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[17]/td[3]').text
        c_severity_17 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[17]/td[4]').text
        c_dispo_17 = ch_dr.find_element_by_xpath('//*[@id="charges"]/div[2]/div[3]/div/dl/dd/table/tbody/tr[17]/td[5]').text

        f_c_off_date_17 = '%m-%d-%Y'
        r_c_off_date_17 = datetime.strptime(c_off_date_17, f_c_off_date_17)

        record_17 = WiCirCourtCaseInfo(c_no_in, c_off_cnt_17, r_c_off_date_17, c_statute_17, c_desc_17, c_severity_17, c_dispo_17)
        session.add(record_17)
        session.commit()

        print(c_no_in, ' entered--offense 17.')

    except:

        pass

    if c_no < 250:

        time.sleep(3)
        s_wi_cir_adj(c_no + 1)

    else:

        ch_dr.close()

s_wi_cir_adj(201)
