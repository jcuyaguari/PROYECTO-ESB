from flask import Flask, request
import mysql.connector

app = Flask(__name__)
cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='productos')
cursor = cnx.cursor()


@app.route('/')
def hello_world():
    return "Hola Mund"

"""
Los productos son almacenados en 
la base de datos y posterior pueden 
ser consultados.
"""
@app.route('/get_productos', methods=['GET'])
def productos():
    mydict = {}
    cant1 = request.args.get('cant1')
    cant2 = request.args.get('cant2')
    stock = request.args.get('stock')
    sql = """UPDATE producto SET stock = stock - %s
            where precio between %s and %s;
          """
    cursor.execute(sql, (stock, cant1, cant2))
    cnx.commit()
    query = (""" select * from producto
                 where precio between %s and %s; """)
    cursor.execute(query, (cant1, cant2))
    for (ID, NOM, PRE, STK) in cursor:
        mydict[str(ID)] = {"id": ID, "nombre": NOM, "precio": PRE, "stock": STK}
    return mydict


if __name__ == '__main__':
    app.run(port=2323)
