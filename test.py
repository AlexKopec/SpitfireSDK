from __future__ import print_function
import os
import sys
import time
import swagger_client
from flask import Flask, render_template
from flask import request
from flask.ext.mysql import MySQL
from swagger_client.rest import ApiException
from pprint import pprint
mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'materialsmarketplace'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

# create an instance of the API jwt class
api_instance = swagger_client.UserjwtcontrollerApi()
#set user login credentials
login_dto = swagger_client.LoginDTO(password='admin', username='admin') # LoginDTO | loginDTO
#get auth header by authorizing user

api_header = api_instance.authorize_using_post_with_http_info(login_dto)
#get just authorization from header
api_auth = api_header[2]
#create a ApiClient using user authorization
client_instance = swagger_client.ApiClient(header_name='authorization', header_value=api_auth['authorization'])

api_instance = swagger_client.MaterialresourceApi(api_client=client_instance)


api_response = api_instance.get_all_materials_using_get()
#Add row
#INSERT INTO `materialsmarketplace`.`materials` (`id`, `name`, `description`, `price`, `currency`, `quantity`, `availability_type`, `frequency`, `size_description`, `components_description`, `disposal_method`, `hazardous`, `active`, `material_category_id`) VALUES ('3', 'A', 'B', '1', 'USD', '1', 'Available', 'Daily', 'Small', 'a', 'landfill', True, True, '1');
#api_response = list of swagger objects
#api_response[i].to_dict() changes swagger object to dictionary
a = api_response[0].to_dict()
keys = a.keys()

values = a.values()

mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()
#print()
#print(str(keys))
print()
print(str(keys)[1:-1])
print()
print(str(values)[1:-1])
print()
cursor.execute("INSERT INTO download_materials (" + str(keys)[1:-1] + ") VALUES (" + str(values)[1:-1] + ");")
