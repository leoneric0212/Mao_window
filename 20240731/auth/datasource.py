import psycopg2
from dotenv import load_dotenv
import os
load_dotenv()

def validateUser(email:str,password:str)  -> tuple[bool,str]:
    conn=psycopg2.connect(os.environ['POSTGRESQL_TOKEN'])    #建立連線
    with conn:
        with conn.cursor() as cursor:
            sql='''
            select 密碼,姓名
            from 使用者
            where 電子郵件 = %s
            '''
            cursor.execute(sql,[email])
            searchData:tuple[str,str]=cursor.fetchone()
            database_password = searchData[0]
            username = searchData[1]
            return password==database_password,username #由於前面要求傳出值為BOOL+str的tuple
    conn.close()