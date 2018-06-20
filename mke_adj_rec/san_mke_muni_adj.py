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

sys.setrecursionlimit(100000)

db = create_engine('sqlite:///mke_adj_db/mke_adj_rec.db', echo = False)

Session = sessionmaker(bind = db)
session = Session()

ch_opt = webdriver.ChromeOptions()
ch_opt.add_argument('headless')
ch_opt.add_argument('user-agent = UserAgent().random')

ch_dr = webdriver.Chrome(chrome_options = ch_opt)

def san_mke_muni_adj(case_lst):

    if type(case_lst) is list:
        for item in case_lst:
            san_mke_muni_adj(item)
            print(item, ' passed @ ', datetime.time(datetime.now()))

    else:

        ch_dr.get('https://query.municourt.milwaukee.gov/')
        case_no_in = ch_dr.find_element_by_id('QuerySection_DisclaimerSection_DisclaimerAgree')
        #time.sleep(2)
        case_no_in.send_keys(Keys.RETURN)
        case_no = ch_dr.find_element_by_id('QuerySection_MainSearchSection_txtCaseNumber')
        case_no.send_keys(case_lst)
        #time.sleep(2)
        case_no.send_keys(Keys.RETURN)
        #time.sleep(2)

        try:

            d_name = ch_dr.find_element_by_id('QuerySection_CaseDetailSection_lblDefendantName').text
            d_mo_yr_birth = ch_dr.find_element_by_id('QuerySection_CaseDetailSection_lblBirthDate').text
            d_sex = ch_dr.find_element_by_id('QuerySection_CaseDetailSection_lblSex').text
            d_race = ch_dr.find_element_by_id('QuerySection_CaseDetailSection_lblRace').text

            c_case_type = ch_dr.find_element_by_id('QuerySection_CaseDetailSection_lblCaseType').text
            c_violation = ch_dr.find_element_by_id('QuerySection_CaseDetailSection_lblViolation').text
            c_violation_date = ch_dr.find_element_by_id('QuerySection_CaseDetailSection_lblViolationDateTime').text
            c_location = ch_dr.find_element_by_id('QuerySection_CaseDetailSection_lblLocation').text
            c_plea = ch_dr.find_element_by_id('QuerySection_CaseDetailSection_lblPlea').text
            c_plea_ent_by = ch_dr.find_element_by_id('QuerySection_CaseDetailSection_lblPleaEnteredBy').text
            c_status = ch_dr.find_element_by_id('QuerySection_CaseDetailSection_lblStatus').text
            c_citation_no = ch_dr.find_element_by_id('QuerySection_CaseDetailSection_lblCitationNumber').text
            c_deposit_amt = ch_dr.find_element_by_id('QuerySection_CaseDetailSection_lblDepositAmount').text
            c_in_collection = ch_dr.find_element_by_id('QuerySection_CaseDetailSection_lblCollection').text
            c_installment_plan = ch_dr.find_element_by_id('QuerySection_CaseDetailSection_lblInstallment').text

            j_finding = ch_dr.find_element_by_id('QuerySection_CaseDetailSection_lblFinding').text
            j_penalty = ch_dr.find_element_by_id('QuerySection_CaseDetailSection_lblTotalJudgmentAmt').text
            j_balance_due = ch_dr.find_element_by_id('QuerySection_CaseDetailSection_lblBalanceDue').text
            j_date = ch_dr.find_element_by_id('QuerySection_CaseDetailSection_lblJudgmentDate').text
            j_due_on_date = ch_dr.find_element_by_id('QuerySection_CaseDetailSection_lblDueOn').text
            j_branch = ch_dr.find_element_by_id('QuerySection_CaseDetailSection_lblBranch').text

            f_d_mo_yr_birth = '%m/%Y'
            d_1 = datetime.strptime(d_mo_yr_birth, f_d_mo_yr_birth)
            f_c_violation_date = '%m/%d/%Y %I:%M %p'
            d_2 = datetime.strptime(c_violation_date, f_c_violation_date)
            f_j_date = '%m/%d/%Y'
            d_3 = datetime.strptime(j_date, f_j_date)
            f_j_due_on_date = '%m/%d/%Y'
            d_4 = datetime.strptime(j_due_on_date, f_j_due_on_date)
            f_c_deposit_amt = float(c_deposit_amt[1:].replace(',', ''))
            f_j_penalty = float(j_penalty[1:].replace(',', ''))
            f_j_balance_due = float(j_balance_due[1:].replace(',', ''))

            session.query(MkeMuniCourt).filter(MkeMuniCourt.d_case_no == str(case_lst)).update({\
            'd_name': d_name, 'd_mo_yr_birth': d_1, 'd_sex': d_sex, 'd_race': d_race, 'c_case_type': c_case_type,\
            'c_violation': c_violation, 'c_violation_date': d_2, 'c_location': c_location, 'c_plea': c_plea,\
            'c_plea_ent_by': c_plea_ent_by, 'c_status': c_status, 'c_citation_no': c_citation_no,\
            'c_deposit_amt': f_c_deposit_amt, 'c_in_collection': c_in_collection, 'c_installment_plan': c_installment_plan,\
            'j_finding': j_finding, 'j_penalty': f_j_penalty, 'j_balance_due': f_j_balance_due, 'j_date': d_3,\
            'j_due_on_date': d_4, 'j_branch': j_branch})
            session.commit()

            print(case_lst, ' modified--recorded to its original schema.')

        except:

            pass

        try:

            qual_1 = ch_dr.find_element_by_id('QuerySection_CaseDetailSection_lblPleaEnteredBy').text

            if qual_1 == '':

                d_name = ch_dr.find_element_by_id('QuerySection_CaseDetailSection_lblDefendantName').text
                d_mo_yr_birth = ch_dr.find_element_by_id('QuerySection_CaseDetailSection_lblBirthDate').text
                d_sex = ch_dr.find_element_by_id('QuerySection_CaseDetailSection_lblSex').text
                d_race = ch_dr.find_element_by_id('QuerySection_CaseDetailSection_lblRace').text

                c_case_type = ch_dr.find_element_by_id('QuerySection_CaseDetailSection_lblCaseType').text
                c_violation = ch_dr.find_element_by_id('QuerySection_CaseDetailSection_lblViolation').text
                c_violation_date = ch_dr.find_element_by_id('QuerySection_CaseDetailSection_lblViolationDateTime').text
                c_location = ch_dr.find_element_by_id('QuerySection_CaseDetailSection_lblLocation').text
                c_plea = ch_dr.find_element_by_id('QuerySection_CaseDetailSection_lblPlea').text
                c_status = ch_dr.find_element_by_id('QuerySection_CaseDetailSection_lblStatus').text
                c_citation_no = ch_dr.find_element_by_id('QuerySection_CaseDetailSection_lblCitationNumber').text
                c_deposit_amt = ch_dr.find_element_by_id('QuerySection_CaseDetailSection_lblDepositAmount').text
                c_in_collection = ch_dr.find_element_by_id('QuerySection_CaseDetailSection_lblCollection').text
                c_installment_plan = ch_dr.find_element_by_id('QuerySection_CaseDetailSection_lblInstallment').text

                w_last_writ_iss = ch_dr.find_element_by_id('QuerySection_CaseDetailSection_lblLastWrit').text
                w_status = ch_dr.find_element_by_id('QuerySection_CaseDetailSection_lblWritStatus').text

                f_d_mo_yr_birth = '%m/%Y'
                d_1 = datetime.strptime(d_mo_yr_birth, f_d_mo_yr_birth)
                f_c_violation_date = '%m/%d/%Y %I:%M %p'
                d_2 = datetime.strptime(c_violation_date, f_c_violation_date)
                f_c_deposit_amt = float(c_deposit_amt[1:].replace(',', ''))

                old_record = session.query(MkeMuniCourt).filter(MkeMuniCourt.d_case_no == str(case_lst))
                old_record.delete()

                new_record = WarMkeMuniCourt(str(case_lst), d_name, d_1, d_sex, d_race, c_case_type, c_violation, d_2, c_location,\
                c_plea, c_status, c_citation_no, f_c_deposit_amt, c_in_collection, c_installment_plan, w_last_writ_iss, w_status)
                session.add(new_record)
                session.commit()

                print(case_lst, ' exists--recorded to outstanding warrants schema.')

        except:

            pass

        try:

            #qual_1 = ch_dr.find_element_by_id('QuerySection_CaseDetailSection_lblCitationLabel').text
            #qual_2 = ch_dr.find_element_by_id('QuerySection_CaseDetailSection_lblAddress').text
            qual_1 = ch_dr.find_element_by_id('QuerySection_CaseDetailSection_lblBirthDate').text
            qual_2 = ch_dr.find_element_by_id('QuerySection_CaseDetailSection_lblSex').text
            qual_3 = ch_dr.find_element_by_id('QuerySection_CaseDetailSection_lblRace').text

            if [qual_1, qual_2, qual_3] == ['N/A', 'N/A', 'N/A']:

                d_name = ch_dr.find_element_by_id('QuerySection_CaseDetailSection_lblDefendantName').text
                d_last_kno_addr = ch_dr.find_element_by_id('QuerySection_CaseDetailSection_lblAddress').text

                c_case_type = ch_dr.find_element_by_id('QuerySection_CaseDetailSection_lblCaseType').text
                c_violation = ch_dr.find_element_by_id('QuerySection_CaseDetailSection_lblViolation').text
                c_violation_date = ch_dr.find_element_by_id('QuerySection_CaseDetailSection_lblViolationDateTime').text
                c_location = ch_dr.find_element_by_id('QuerySection_CaseDetailSection_lblLocation').text
                c_plea = ch_dr.find_element_by_id('QuerySection_CaseDetailSection_lblPlea').text
                c_plea_ent_by = ch_dr.find_element_by_id('QuerySection_CaseDetailSection_lblPleaEnteredBy').text
                c_status = ch_dr.find_element_by_id('QuerySection_CaseDetailSection_lblStatus').text
                c_so_no = ch_dr.find_element_by_id('QuerySection_CaseDetailSection_lblCitationNumber').text
                c_deposit_amt = ch_dr.find_element_by_id('QuerySection_CaseDetailSection_lblDepositAmount').text
                c_in_collection = ch_dr.find_element_by_id('QuerySection_CaseDetailSection_lblCollection').text
                c_installment_plan = ch_dr.find_element_by_id('QuerySection_CaseDetailSection_lblInstallment').text

                j_finding = ch_dr.find_element_by_id('QuerySection_CaseDetailSection_lblFinding').text
                j_penalty = ch_dr.find_element_by_id('QuerySection_CaseDetailSection_lblTotalJudgmentAmt').text
                j_balance_due = ch_dr.find_element_by_id('QuerySection_CaseDetailSection_lblBalanceDue').text
                j_date = ch_dr.find_element_by_id('QuerySection_CaseDetailSection_lblJudgmentDate').text
                j_due_on_date = ch_dr.find_element_by_id('QuerySection_CaseDetailSection_lblDueOn').text
                j_branch = ch_dr.find_element_by_id('QuerySection_CaseDetailSection_lblBranch').text

                f_c_violation_date = '%m/%d/%Y %I:%M %p'
                d_1 = datetime.strptime(c_violation_date, f_c_violation_date)
                f_j_date = '%m/%d/%Y'
                d_2 = datetime.strptime(j_date, f_j_date)
                f_j_due_on_date = '%m/%d/%Y'
                d_3 = datetime.strptime(j_due_on_date, f_j_due_on_date)
                f_c_deposit_amt = float(c_deposit_amt[1:].replace(',', ''))
                f_j_penalty = float(j_penalty[1:].replace(',', ''))
                f_j_balance_due = float(j_balance_due[1:].replace(',', ''))

                old_record = session.query(MkeMuniCourt).filter(MkeMuniCourt.d_case_no == str(case_lst))
                old_record.delete()

                new_record = BusMkeMuniCourt(str(case_lst), d_name, d_last_kno_addr, c_case_type, c_violation, d_1, c_location,\
                c_plea, c_plea_ent_by, c_status, c_so_no, f_c_deposit_amt, c_in_collection, c_installment_plan, j_finding,\
                f_j_penalty, f_j_balance_due, d_2, d_3, j_branch)
                session.add(new_record)
                session.commit()

                print(case_lst, ' exists--recorded to business code violations schema.')

        except:

            pass

        try:

            mia_case_no = ch_dr.find_element_by_xpath('//*[@id="QuerySection_ResultNotFoundSection_lblExplanationFooter"]').text

            old_record = session.query(MkeMuniCourt).filter(MkeMuniCourt.d_case_no == str(case_lst))
            old_record.delete()

            new_record = MiaMkeMuniCourt(str(case_lst))
            session.add(new_record)
            session.commit()

            print(case_lst, ' does not exist--recorded to missing cases schema.')

        except:

            pass

if __name__ == '__main__':
    case_lst = [int(i[0]) for i in sorted(session.query(MkeMuniCourt.d_case_no).filter(MkeMuniCourt.d_name == None))]
    san_mke_muni_adj(case_lst)
