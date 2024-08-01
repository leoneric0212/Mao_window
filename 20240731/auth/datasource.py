import psycopg2
from dotenv import load_dotenv
from psycopg2.errors import UniqueViolation
from werkzeug.security import check_password_hash   #保護密碼
import os
load_dotenv()

class InvalidEmailException(Exception):
    pass
def insert_data(values:list[any]=None):
    conn=psycopg2.connect(os.environ['POSTGRESQL_TOKEN'])    #建立連線
    with conn:
        with conn.cursor() as cursor:
            sql='''
                insert into 使用者(姓名,性別,聯絡電話,電子郵件,isgetemail,出生年月日,自我介紹,密碼,連線密碼)
                Values(%s,%s,%s,%s,%s,%s,%s,%s,%s)
            '''
            try:
                cursor.execute(sql.values)
            except UniqueViolation:
                raise InvalidEmailException
            except Exception:
                raise RuntimeError
    conn.close()


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
            searchData:tuple[str,str] | None =cursor.fetchone()
            if searchData:
                hash_password = searchData[0]
                username = searchData[1]
                is_ok = check_password_hash(hash_password,password) #確認hash_password與password是否一致
                return is_ok,username
            else:
                return False,""
    conn.close()
