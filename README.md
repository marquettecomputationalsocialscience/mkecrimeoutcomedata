# mkecrimeoutcomedata
Creating a dataset to understand the crime analysis pipeline from mapping to sentencing

# Adjudication Record Scrapes

<div>
  <update>Update: Jan 26, 2018</update>
  <br>
  <folder> mke_adj_rec </folder>
  <br>
  <div>
    <prog1> mke_adj_rec_db.py </prog1>
    <purpose> Builds schema </purpose>
    <assist> Built with 'SQLAlchemy' </assist>
  </div>
  <br>
  <div>
    <prog2> s_mke_muni_adj.py </prog2>
    <purpose> Recursive scrape of Mke Municipal Court <purpose>
    <assist> Built with 'Selenium' & 'fake-useragent' </assist>
  </div>
  <br>
  <div>
    <prog3> s_wi_cir_adj.py </prog3>
    <purpose> ecursive scrape of WI Circuit Court <purpose>
    <assist> Built with 'Selenium' & 'fake-useragent' </assist>
  </div>
  <br>
  <div>
    <fi> Implement </fi>
    <fi1> Mke Municipal Court anomalies </fi1>
    <fi2> Refactor scrapes, additional recursive functions </fi2>
    <fi3> Address CAPTCHA/reCAPTCHA </fi3>
  </div>
</div>
