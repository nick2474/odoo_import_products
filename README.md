
# odoo_import_products
#This is just an simple Script to import products from csv file to odoo. 
#You can add more files and complex features as needed.

1.Match the fields
  row : is the record on file.

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

2.File .csv structure.
   default_code,name,barcode,supplier_taxes_id,taxes_id,categ_id,standard_price,list_price,type
   123,CINTA EPSON PUNTO DE VENTA NEGRO,10343812628,Purchase Tax,Sales Tax,All,1.00,999,product

3.Execute command on the same folder.

  python iproduct.py
  
#Enjoy it!
