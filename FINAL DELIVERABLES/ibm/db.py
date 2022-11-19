import ibm_db
try:
    conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=2d46b6b4-cbf6-40eb-bbce-6251e6ba0300.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=32328;SECURITY=SSL;SSlServerCertificate=DigiCertGlobalRootCA.crt;UID=tzp28629;PWD=TVm24LZqNge08eTF;", '', '')
    print("db is connected")
except:
    print("db is not connected")