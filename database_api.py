import pandas as pd
import ibm_db

def DatabaseAPI(e_id, user_name, output):
    dsn_hostname = "dashdb-txn-sbox-yp-lon02-01.services.eu-gb.bluemix.net"
    dsn_uid = "xjb70901"
    dsn_pwd = "vcmz2hzl7rlq90@7"
    dsn_driver = "{IBM DB2 ODBC DRIVER}"
    dsn_database = "BLUDB"
    dsn_port = "50000"
    dsn_protocol = "TCPIP"

    dsn = ("DRIVER={0};" "DATABASE={1};" "HOSTNAME={2};" "PORT={3};" "PROTOCOL={4};" "UID={5};" "PWD={6};").format(
        dsn_driver, dsn_database, dsn_hostname, dsn_port, dsn_protocol, dsn_uid, dsn_pwd)

    connection=ibm_db.connect(dsn,"","")

    query="insert into chatbot_data (E_ID,USER_NAME,OUTPUT_RESULT) values ('{}','{}','{}');".format(e_id,user_name,output)
    statement=ibm_db.exec_immediate(connection,query)

    ibm_db.close(connection)

if __name__=="__main__":
    DatabaseAPI('exxxxxx','rahul','5')
