from sqlalchemy import create_engine, Float, ForeignKey, Column, Date, DateTime, String
from sqlalchemy.ext.declarative import declarative_base

db = create_engine('sqlite:///mke_adj_rec.db', echo = False)
Base = declarative_base()

class MkeMuniCourt(Base):

    __tablename__ = 'mke_muni_court'

    # Defendent Info
    d_case_no = Column(String, primary_key = True, nullable = False)
    d_name = Column(String)
    #d_last_known_addr = Column(String)
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
        #self.d_last_known_addr = d_last_known_addr
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

Base.metadata.create_all(db)
