#AUTHOR: DIDIER HERNANDEZ.
#YOU CAN RUN THIS FILE LIKE:
#python3 iproduct.py or python3 iproduct.py



import xmlrpclib
import csv

#==>SET THE PARAMETERS
username = "USERNAME"
pwd = 'PWD123'
dbname = "DB_NAME"

sock_common = xmlrpclib.ServerProxy("http://IP_SERVER:PORT/xmlrpc/common")

uid = sock_common.login(dbname, username, pwd)

sock = xmlrpclib.ServerProxy("http://IP_SERVER:PORT/xmlrpc/object")

#==>SET THE FILE WITH THE ROWS TO IMPORT.
reader = csv.reader(open('file.csv','rb'))
for row in reader:
    print row[1]
    product_template = {
        'default_code': row[1],
        'name': row[2],
        'barcode': row[3],
        'supplier_taxes_id':row[4],
        'taxes_id':row[5],
        'categ_id':row[6],
        'standard_price':row[7],
        'list_price':row[8],
        'type':'product'}
    template_id=sock.execute(dbname, uid,pwd, 'product.template','create',product_template)

    product_product = {
        'product_tmpl_id':template_id,
        'default_code':row[0],
        'active': True,
        }
    product_id = sock.execute(dbname,uid,pwd,'product.product','create',product_product)
