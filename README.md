# mkecrimeoutcomedata
Creating a dataset to understand the crime analysis pipeline from mapping to sentencing

# Adjudication Record Scrapes

| Updated: 2018.01.26

| mke_adj_rec

  | mke_adj_rec_db.py
    | Builds schema
      | Mke Municipal Court records
      | WI Circuit Court defendant info records
      | WI Circuit Court case info records
    | Built with 'SQLAlchemy'

  | s_mke_muni_adj.py
    | Recursive scrape of Mke Municipal Court records
    | Built with 'Selenium' & 'fake-useragent'

  | s_wi_cir_adj.py
    | Recursive scrape of WI Circuit Court records
    | Built with 'Selenium' & 'fake-useragent'

| Future Implementations

  | Refactor scrapes
    | Introduce additional recursive formulas
    | Address CAPTCHA/reCAPTCHA
