import mysql.connector
import time
def create_database():
    cnx = mysql.connector.connect(user='root', password='u3nZED2tr2ygrTAAHeib',host='data-txx-service')
    cursor = cnx.cursor()
    #cursor.execute("DROP database IF EXISTS data")
    cursor.execute("create database if not exists data")
    cursor.execute("use data")
    cursor.execute("CREATE TABLE IF NOT EXISTS users(cid VARCHAR(100),id VARCHAR(100),rem int(100))")
    cursor.execute("CREATE TABLE IF NOT EXISTS words(word VARCHAR(100))")
    cursor.execute("""CREATE TABLE IF NOT EXISTS translations(text TEXT, 
                   language VARCHAR(50), 
                   language_target VARCHAR(50), 
                   mid int(100));""")
    cursor.execute("CREATE TABLE IF NOT EXISTS sales(cid VARCHAR(100),mid int(100))")
    cursor.execute("""CREATE TABLE IF NOT EXISTS product(
                   photo_id TEXT, 
                   id INT AUTO_INCREMENT PRIMARY KEY,
                   title VARCHAR(500),
                   details TEXT, 
                   price INT);""")
    print("created")
    cursor.close()
    cnx.commit()

def insert_product(photo_id,title,details,price):
    cnx = mysql.connector.connect(user='root', password='u3nZED2tr2ygrTAAHeib',host='data-txx-service',database="data")
    cursor = cnx.cursor(dictionary=True)
    cursor.execute(f"insert into product (photo_id,title,details,price) values ('{photo_id}','{title}','{details}',{price});")
    cursor.close()
    cnx.commit()
def use_product():
    cnx = mysql.connector.connect(user='root', password='u3nZED2tr2ygrTAAHeib',host='data-txx-service',database="data")
    cursor = cnx.cursor(dictionary=True)
    cursor.execute(f"select * from product") 
    dict_product=cursor.fetchall()
    cursor.close()
    cnx.commit()
    return dict_product
def use_product_id(id):
    cnx = mysql.connector.connect(user='root', password='u3nZED2tr2ygrTAAHeib',host='data-txx-service',database="data")
    cursor = cnx.cursor(dictionary=True)
    cursor.execute(f"select * from product where id='{id}'")  
    f = cursor.fetchall()
    return f













def insert_users(cid,id,rem):
    cnx = mysql.connector.connect(user='root', password='u3nZED2tr2ygrTAAHeib',host='data-txx-service',database="data")
    cursor = cnx.cursor(dictionary=True)
    cursor.execute(f"select * from users where cid={cid}")  
    f = cursor.fetchall()
    if len(f)==0:
        cursor.execute(f"insert into users (cid,id,rem) values ('{cid}','{id}',{rem});")
        cursor.close()
        cnx.commit()
        return "yes"
    cursor.close()
    cnx.commit()
    return "no"

def use_users_cid(cid):
    cnx = mysql.connector.connect(user='root', password='u3nZED2tr2ygrTAAHeib',host='data-txx-service',database="data")
    cursor = cnx.cursor(dictionary=True)
    cursor.execute(f"select * from users where cid='{cid}'")  
    f = cursor.fetchall()
    return f

def insert_words(word):
    cnx = mysql.connector.connect(user='root', password='u3nZED2tr2ygrTAAHeib',host='data-txx-service',database="data")
    cursor = cnx.cursor(dictionary=True)
    cursor.execute(f"insert into words (word) values ('{word}');")
    cursor.close()
    cnx.commit()

def use_words():
    cnx = mysql.connector.connect(user='root', password='u3nZED2tr2ygrTAAHeib',host='data-txx-service',database="data")
    cursor = cnx.cursor(dictionary=True)
    cursor.execute(f"select * from words") 
    dict_product=cursor.fetchall()
    cursor.close()
    cnx.commit()
    return dict_product


def use_users_id(id):
    cnx = mysql.connector.connect(user='root', password='u3nZED2tr2ygrTAAHeib',host='data-txx-service',database="data")
    cursor = cnx.cursor(dictionary=True)
    cursor.execute(f"select * from users where id='{id}'")  
    f = cursor.fetchall()
    return f


def updete_users(cid,rem):
    cnx = mysql.connector.connect(user='root', password='u3nZED2tr2ygrTAAHeib',host='data-txx-service',database="data")
    cursor = cnx.cursor(dictionary=True)
    cursor.execute(f"update users set rem={rem} where cid={cid}")
    cursor.close()
    cnx.commit()

def delete_users(cid):
    cnx = mysql.connector.connect(user='root', password='u3nZED2tr2ygrTAAHeib',host='data-txx-service',database="data")
    cursor = cnx.cursor(dictionary=True)
    cursor.execute(f"delete from users where cid={cid}") 
    cursor.close()
    cnx.commit()

def use_users():
    cnx = mysql.connector.connect(user='root', password='u3nZED2tr2ygrTAAHeib',host='data-txx-service',database="data")
    cursor = cnx.cursor(dictionary=True)
    cursor.execute(f"select * from users") 
    dict_product=cursor.fetchall()
    cursor.close()
    cnx.commit()
    return dict_product

def insert_translations(text,language,language_target,mid):
    cnx = mysql.connector.connect(user='root', password='u3nZED2tr2ygrTAAHeib',host='data-txx-service',database="data")
    cursor = cnx.cursor(dictionary=True)
    cursor.execute(f"insert into translations (text,language,language_target,mid) values ('{text}','{language}','{language_target}',{mid})")
    cursor.close()
    cnx.commit()

def use_translations(text,language,language_target):
    cnx = mysql.connector.connect(user='root', password='u3nZED2tr2ygrTAAHeib',host='data-txx-service',database="data")
    cursor = cnx.cursor(dictionary=True)
    cursor.execute(f"select * from translations where text='{text}' AND language='{language}' AND language_target='{language_target}'")   
    dict_product=cursor.fetchall()
    cursor.close()
    cnx.commit()
    return dict_product

def use_selse_list():
    cnx = mysql.connector.connect(user='root', password='u3nZED2tr2ygrTAAHeib',host='data-txx-service',database="data")
    cursor = cnx.cursor(dictionary=True)
    cursor.execute(f"select * from sales")  
    f = cursor.fetchall()
    return f

def insert_seles(cid,mid):
    cnx = mysql.connector.connect(user='root', password='u3nZED2tr2ygrTAAHeib',host='data-txx-service',database="data")
    cursor = cnx.cursor(dictionary=True)
    cursor.execute(f"insert into sales (cid,mid) values ('{cid}',{mid});")
    cursor.close()
    cnx.commit()

# create_database()
# insert_users(5446)
# insert_users(5446000000)
# insert_users(5446035663600000)
