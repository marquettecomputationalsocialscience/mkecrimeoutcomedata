from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from mke_adj_rec_db import *

import random
import time

db = create_engine('sqlite:///mke_adj_rec.db', echo = False)

Session = sessionmaker(bind = db)
session = Session()

ch_opt = webdriver.ChromeOptions()
ch_opt.add_argument('headless')
ch_opt.add_argument('user-agent = UserAgent().random')

ch_dr = webdriver.Chrome(chrome_options = ch_opt)

def s_mke_muni_adj(c_no):

    ch_dr.get("https://query.municourt.milwaukee.gov/")
    case_no_in = ch_dr.find_element_by_id("QuerySection_DisclaimerSection_DisclaimerAgree")
    case_no_in.send_keys(Keys.RETURN)
    case_no = ch_dr.find_element_by_id("QuerySection_MainSearchSection_txtCaseNumber")
    case_no.send_keys(c_no)
    case_no.send_keys(Keys.RETURN)

    try:

        #case_no = ch_dr.find_element_by_id("QuerySection_CaseDetailSection_lblCaseNumber").text
        d_name = ch_dr.find_element_by_id("QuerySection_CaseDetailSection_lblDefendantName").text
        #last_known_addr = ch_dr.find_element_by_id("QuerySection_CaseDetailSection_lblAddress").text
        d_mo_yr_birth = ch_dr.find_element_by_id("QuerySection_CaseDetailSection_lblBirthDate").text
        d_sex = ch_dr.find_element_by_id("QuerySection_CaseDetailSection_lblSex").text
        d_race = ch_dr.find_element_by_id("QuerySection_CaseDetailSection_lblRace").text

        c_case_type = ch_dr.find_element_by_id("QuerySection_CaseDetailSection_lblCaseType").text
        c_violation = ch_dr.find_element_by_id("QuerySection_CaseDetailSection_lblViolation").text
        c_violation_date = ch_dr.find_element_by_id("QuerySection_CaseDetailSection_lblViolationDateTime").text
        c_location = ch_dr.find_element_by_id("QuerySection_CaseDetailSection_lblLocation").text
        c_plea = ch_dr.find_element_by_id("QuerySection_CaseDetailSection_lblPlea").text
        c_plea_ent_by = ch_dr.find_element_by_id("QuerySection_CaseDetailSection_lblPleaEnteredBy").text
        c_status = ch_dr.find_element_by_id("QuerySection_CaseDetailSection_lblStatus").text
        c_citation_no = ch_dr.find_element_by_id("QuerySection_CaseDetailSection_lblCitationNumber").text
        c_deposit_amt = ch_dr.find_element_by_id("QuerySection_CaseDetailSection_lblDepositAmount").text
        c_in_collection = ch_dr.find_element_by_id("QuerySection_CaseDetailSection_lblCollection").text
        c_installment_plan = ch_dr.find_element_by_id("QuerySection_CaseDetailSection_lblInstallment").text

        j_finding = ch_dr.find_element_by_id("QuerySection_CaseDetailSection_lblFinding").text
        j_penalty = ch_dr.find_element_by_id("QuerySection_CaseDetailSection_lblTotalJudgmentAmt").text
        j_balance_due = ch_dr.find_element_by_id("QuerySection_CaseDetailSection_lblBalanceDue").text
        j_date = ch_dr.find_element_by_id("QuerySection_CaseDetailSection_lblJudgmentDate").text
        j_due_on_date = ch_dr.find_element_by_id("QuerySection_CaseDetailSection_lblDueOn").text
        j_branch = ch_dr.find_element_by_id("QuerySection_CaseDetailSection_lblBranch").text

        f_d_mo_yr_birth = '%m/%Y'
        d_1 = datetime.strptime(d_mo_yr_birth, f_d_mo_yr_birth)
        f_c_violation_date = '%m/%d/%Y %I:%M %p'
        d_2 = datetime.strptime(c_violation_date, f_c_violation_date)
        f_j_date = '%m/%d/%Y'
        d_3 = datetime.strptime(j_date, f_j_date)
        f_j_due_on_date = '%m/%d/%Y'
        d_4 = datetime.strptime(j_due_on_date, f_j_due_on_date)
        f_c_deposit_amt = float(c_deposit_amt[1:])
        f_j_penalty = float(j_penalty[1:])
        f_j_balance_due = float(j_balance_due[1:])


        record = MkeMuniCourt(c_no, d_name, d_1, d_sex, d_race, c_case_type, c_violation, d_2, c_location,\
        c_plea, c_plea_ent_by, c_status, c_citation_no, f_c_deposit_amt, c_in_collection, c_installment_plan,\
        j_finding, f_j_penalty, f_j_balance_due, d_3, d_4, j_branch)
        session.add(record)
        session.commit()

        print(c_no, ' passed.')
        time.sleep(3)

    except:

        record = MkeMuniCourt(c_no, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)
        session.add(record)
        session.commit()

        print(c_no, ' passed, but has conflicts.')
        time.sleep(3)
        pass

    if c_no < n:

        s_mke_muni_adj(c_no + 1)

s_mke_muni_adj(n)
