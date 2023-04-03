from sqlalchemy import create_engine, text
import os


bd = "mysql+pymysql://8j5752d6wgvr5pajo8f6:pscale_pw_Fj5tNwXW4gXeYCQpFeuE9syhZnW9xnO3S03ed4BTNn2@aws.connect.psdb.cloud/first-data-base?charset=utf8mb4"
engine = create_engine(
  bd , connect_args={
    "ssl":{
      "ssl_ca":"/etc/ssl/cert.pem"
    }
})

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(row)
    return jobs
  
  
def get_password():
    with engine.connect() as conn:
      result = conn.execute(text("select * from loge_in"))
      jobs = []
      for row in result.all():
        jobs.append(row)
    return jobs
  
  
# def add_information_in_db():
#       with engine.connect() as conn:
#       result = conn.execute(text("select * from loge_in"))
      
      
# def add_information_in_db():
#     with engine.connect() as conn:
#       result = conn.execute(text("INSERT INTO loge_in(email , passoward)VALUES(':email' , )"))
#       jobs = []
#       for row in result.all():
#         jobs.append(row)
#     return jobs

  
  
  