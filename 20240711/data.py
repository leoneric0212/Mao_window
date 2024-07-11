from dotenv import load_dotenv
import psycopg2
import os
load_dotenv()


def get_areas(): 
    conn=psycopg2.connect(os.environ['POSTGRESQL_TOKEN'])    #建立連線
    with conn:
        with conn.cursor() as cursor:
            sql='''
            SELECT DISTINCT sarea
            FROM youbike;
            '''
            cursor.execute(sql)
            return(cursor.fetchall())
    conn.close()
    