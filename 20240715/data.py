from dotenv import load_dotenv
import psycopg2
import os
load_dotenv()

def get_areas()  -> list[tuple]:
    conn=psycopg2.connect(os.environ['POSTGRESQL_TOKEN'])    #建立連線
    with conn:
        with conn.cursor() as cursor:
            sql='''
            SELECT DISTINCT sarea
            FROM youbike
            '''
            cursor.execute(sql)
            return(cursor.fetchall())
    conn.close()

def get_snaOfArea(area:str)  -> list[tuple]:
    conn=psycopg2.connect(os.environ['POSTGRESQL_TOKEN'])    #建立連線
    with conn:
        with conn.cursor() as cursor:
            sql='''
            SELECT sna 站點 ,total 總車輛數 ,rent_bikes 可借 ,return_bikes 可還 ,mday 時間
            FROM youbike
            WHERE (updatetime,sna) IN (
                SELECT MAX(updatetime),sna 
                FROM youbike
                WHERE sarea = (%s)
                GROUP BY sna)
            '''
            cursor.execute(sql,(area,))
            return(cursor.fetchall())
    conn.close()
    