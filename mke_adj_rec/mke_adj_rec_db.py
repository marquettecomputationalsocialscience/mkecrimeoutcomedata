from sqlalchemy import create_engine, Float, ForeignKey, Column, Date, DateTime, String
from sqlalchemy.ext.declarative import declarative_base

db = create_engine('sqlite:///mke_adj_db/mke_adj_rec.db', echo = False)
Base = declarative_base()

class MkeMuniCourt(Base):

    __tablename__ = 'mke_muni_court'

    # Defendant Info
    d_case_no = Column(String, primary_key = True, nullable = False)
    d_name = Column(String)
    d_mo_yr_birth = Column(Date)
    d_sex = Column(String)
    d_race = Column(String)

    # Case Info
    c_case_type = Column(String)
    c_violation = Column(String)
    c_violation_date = Column(DateTime)
    c_location = Column(String)
    c_plea = Column(String)
    c_plea_ent_by = Column(String)
    c_status = Column(String)
    c_citation_no = Column(String)
    c_deposit_amt = Column(Float)
    c_in_collection = Column(String)
    c_installment_plan = Column(String)

    # Judgement
    j_finding = Column(String)
    j_penalty = Column(Float)
    j_balance_due = Column(Float)
    j_date = Column(Date)
    j_due_on_date = Column(Date)
    j_branch = Column(String)

    def __init__(self, d_case_no, d_name, d_mo_yr_birth, d_sex, d_race, c_case_type,\
    c_violation, c_violation_date, c_location, c_plea, c_plea_ent_by, c_status,\
    c_citation_no, c_deposit_amt, c_in_collection, c_installment_plan, j_finding,\
    j_penalty, j_balance_due, j_date, j_due_on_date, j_branch):
        self.d_case_no = d_case_no
        self.d_name = d_name
        self.d_mo_yr_birth = d_mo_yr_birth
        self.d_sex = d_sex
        self.d_race = d_race
        self.c_case_type = c_case_type
        self.c_violation = c_violation
        self.c_violation_date = c_violation_date
        self.c_location = c_location
        self.c_plea = c_plea
        self.c_plea_ent_by = c_plea_ent_by
        self.c_status = c_status
        self.c_citation_no = c_citation_no
        self.c_deposit_amt = c_deposit_amt
        self.c_in_collection = c_in_collection
        self.c_installment_plan = c_installment_plan
        self.j_finding = j_finding
        self.j_penalty = j_penalty
        self.j_balance_due = j_balance_due
        self.j_date = j_date
        self.j_due_on_date = j_due_on_date
        self.j_branch = j_branch

class MiaMkeMuniCourt(Base):

    __tablename__ = 'mia_mke_muni_court'

    # Case Info
    mia_case_no = Column(String, primary_key = True, nullable = False)

    def __init__(self, mia_case_no):
        self.mia_case_no = mia_case_no

class BusMkeMuniCourt(Base):

    __tablename__ = 'bus_mke_muni_court'

    # Defendant Info
    d_case_no = Column(String, primary_key = True, nullable = False)
    d_name = Column(String)
    d_last_kno_addr = Column(String)

    # Case Info
    c_case_type = Column(String)
    c_violation = Column(String)
    c_violation_date = Column(DateTime)
    c_location = Column(String)
    c_plea = Column(String)
    c_plea_ent_by = Column(String)
    c_status = Column(String)
    c_so_no = Column(String)
    c_deposit_amt = Column(Float)
    c_in_collection = Column(String)
    c_installment_plan = Column(String)

    # Judgement Info
    j_finding = Column(String)
    j_penalty = Column(Float)
    j_balance_due = Column(Float)
    j_date = Column(Date)
    j_due_on_date = Column(Date)
    j_branch = Column(String)

    def __init__(self, d_case_no, d_name, d_last_kno_addr, c_case_type, c_violation,\
    c_violation_date, c_location, c_plea, c_plea_ent_by, c_status, c_so_no, c_deposit_amt,\
    c_in_collection, c_installment_plan, j_finding, j_penalty, j_balance_due, j_date,
    j_due_on_date, j_branch):
        self.d_case_no = d_case_no
        self.d_name = d_name
        self.d_last_kno_addr = d_last_kno_addr
        self.c_case_type = c_case_type
        self.c_violation = c_violation
        self.c_violation_date = c_violation_date
        self.c_location = c_location
        self.c_plea = c_plea
        self.c_plea_ent_by = c_plea_ent_by
        self.c_status = c_status
        self.c_so_no = c_so_no
        self.c_deposit_amt = c_deposit_amt
        self.c_in_collection = c_in_collection
        self.c_installment_plan = c_installment_plan
        self.j_finding = j_finding
        self.j_penalty = j_penalty
        self.j_balance_due = j_balance_due
        self.j_date = j_date
        self.j_due_on_date = j_due_on_date
        self.j_branch = j_branch

class WarMkeMuniCourt(Base):

    __tablename__ = 'war_mke_muni_court'

    # Defendant Info
    d_case_no = Column(String, primary_key = True, nullable = False)
    d_name = Column(String)
    d_mo_yr_birth = Column(Date)
    d_sex = Column(String)
    d_race = Column(String)

    # Case Info
    c_case_type = Column(String)
    c_violation = Column(String)
    c_violation_date = Column(DateTime)
    c_location = Column(String)
    c_plea = Column(String)
    c_status = Column(String)
    c_citation_no = Column(String)
    c_deposit_amt = Column(Float)
    c_in_collection = Column(String)
    c_installment_plan = Column(String)

    # Warrant Info
    w_last_writ_iss = Column(String)
    w_status = Column(String)

    def __init__(self, d_case_no, d_name, d_mo_yr_birth, d_sex, d_race, c_case_type,\
    c_violation, c_violation_date, c_location, c_plea, c_status, c_citation_no,\
    c_deposit_amt, c_in_collection, c_installment_plan, w_last_writ_iss, w_status):
        self.d_case_no = d_case_no
        self.d_name = d_name
        self.d_mo_yr_birth = d_mo_yr_birth
        self.d_sex = d_sex
        self.d_race = d_race
        self.c_case_type = c_case_type
        self.c_violation = c_violation
        self.c_violation_date = c_violation_date
        self.c_location = c_location
        self.c_plea = c_plea
        self.c_status = c_status
        self.c_citation_no = c_citation_no
        self.c_deposit_amt = c_deposit_amt
        self.c_in_collection = c_in_collection
        self.c_installment_plan = c_installment_plan
        self.w_last_writ_iss = w_last_writ_iss
        self.w_status = w_status

class PkMkeMuniCourt(Base):

    __tablename__ = 'pk_mke_muni_court'

    # Defendant Info
    d_case_no = Column(String, primary_key = True, nullable = False)
    d_name = Column(String)
    d_mo_yr_birth = Column(Date)
    d_sex = Column(String)
    d_race = Column(String)

    # Case Info
    c_case_type = Column(String)
    c_violation = Column(String)
    c_violation_date = Column(DateTime)
    c_plea = Column(String)
    c_plea_ent_by = Column(String)
    c_status = Column(String)
    c_deposit_amt = Column(Float)
    c_in_collection = Column(String)
    c_installment_plan = Column(String)

    # Judgement
    j_finding = Column(String)
    j_penalty = Column(Float)
    j_balance_due = Column(Float)
    j_date = Column(Date)
    j_due_on_date = Column(Date)
    j_branch = Column(String)

    def __init__(self, d_case_no, d_name, d_mo_yr_birth, d_sex, d_race, c_case_type,\
    c_violation, c_violation_date, c_plea, c_plea_ent_by, c_status, c_deposit_amt,\
    c_in_collection, c_installment_plan, j_finding, j_penalty, j_balance_due, j_date,\
    j_due_on_date, j_branch):
        self.d_case_no = d_case_no
        self.d_name = d_name
        self.d_mo_yr_birth = d_mo_yr_birth
        self.d_sex = d_sex
        self.d_race = d_race
        self.c_case_type = c_case_type
        self.c_violation = c_violation
        self.c_violation_date = c_violation_date
        self.c_plea = c_plea
        self.c_plea_ent_by = c_plea_ent_by
        self.c_status = c_status
        self.c_deposit_amt = c_deposit_amt
        self.c_in_collection = c_in_collection
        self.c_installment_plan = c_installment_plan
        self.j_finding = j_finding
        self.j_penalty = j_penalty
        self.j_balance_due = j_balance_due
        self.j_date = j_date
        self.j_due_on_date = j_due_on_date
        self.j_branch = j_branch

class WiCirCourtDefInfo(Base):

    __tablename__ = 'wi_cir_court_di'

    # Defendant Info
    d_case_no = Column(String, primary_key = True, nullable = False)
    d_case_type = Column(String)
    d_name = Column(String)
    d_dob = Column(Date)
    d_sex = Column(String)
    d_race = Column(String)
    d_address = Column(String)
    d_filing_date = Column(Date)
    d_case_status = Column(String)
    d_branch_id = Column(String)

    def __init__(self, d_case_no, d_case_type, d_name, d_dob, d_sex, d_race, d_address,\
    d_filing_date, d_case_status, d_branch_id):
        self.d_case_no = d_case_no
        self.d_case_type = d_case_type
        self.d_name = d_name
        self.d_dob = d_dob
        self.d_sex = d_sex
        self.d_race = d_race
        self.d_address = d_address
        self.d_filing_date = d_filing_date
        self.d_case_status = d_case_status
        self.d_branch_id = d_branch_id

class WiCirCourtCaseInfo(Base):

    __tablename__ = "wi_cir_court_ci"

    # Case Info
    c_case_no = Column(String, ForeignKey('wi_cir_court_di.d_case_no'), primary_key = True, nullable = False)
    c_off_cnt = Column(String, primary_key = True, nullable = False)
    c_off_date = Column(Date)
    c_statute = Column(String)
    c_desc = Column(String)
    c_severity = Column(String)
    c_dispo = Column(String)

    def __init__(self, c_case_no, c_off_cnt, c_off_date, c_statute, c_desc, c_severity,\
    c_dispo):
        self.c_case_no = c_case_no
        self.c_off_cnt = c_off_cnt
        self.c_off_date = c_off_date
        self.c_statute = c_statute
        self.c_desc = c_desc
        self.c_severity = c_severity
        self.c_dispo = c_dispo

Base.metadata.create_all(db)
