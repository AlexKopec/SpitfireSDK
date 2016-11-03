from __future__ import print_function
import os
import sys
import time
import swagger_client
from flask import Flask, render_template, request, redirect
from flask.ext.mysql import MySQL
from swagger_client.rest import ApiException
from flask_restful import Resource, Api, reqparse
from pprint import pprint

mysql = MySQL()
app = Flask(__name__)

#global variables
global client_instance
global username
global password
global user_details_dict
global conn

#Create landing page
@app.route("/")
def main():
	return render_template('index.html')

#create Sign in page
@app.route("/SignIn")
def sign_in():
	return render_template('SignIn.html')

#Get Login information
@app.route("/SignIn", methods=['POST'])
def sign_in_post(client_instance=None):
	#get username and password from html form input
	username = request.form['username']
	password = request.form['password']
	#create the client instance with provided login info
	client_instance = create_client_instance(username, password)
	#checking if login info is correct
	if type(client_instance) == str:
		return render_template('SignIn.html', client_instance=client_instance)
	else:
		return redirect("/" + str(username))

#create user landing page
@app.route("/<username>")
def user_page(username=None):
	#create global user details dictionary
	global user_details_dict
	user_details_dict = get_user_details(username)
	firstname = user_details_dict.get("first_name")
	lastname = user_details_dict.get("last_name")
	return render_template("UserPage.html", firstname=firstname, lastname=lastname)

#Create Load Data page
@app.route("/DBconn")
def db_conn():
	return render_template("DBconn.html")

#Post data from local DB to Server
@app.route("/DBconn", methods=['POST'])
def db_conn_post():
	# MySQL configurations
	db_user = request.form['db_user']
	db_pass = request.form['db_pass']
	db_name = request.form['db_name']
	db_host = request.form['db_host']
	app.config['MYSQL_DATABASE_USER'] = db_user
	app.config['MYSQL_DATABASE_PASSWORD'] = db_pass
	app.config['MYSQL_DATABASE_DB'] = db_name
	app.config['MYSQL_DATABASE_HOST'] = db_host
	mysql.init_app(app)
	try:
		global conn
		conn = mysql.connect()
		return redirect("/LoadData")
	except:
		return render_template('DBconn.html', error=True)


#create LoadData page
@app.route("/LoadData")
def load_data():
	return render_template("/LoadData.html")

#create page for loading data from local database to Server
@app.route("/LoadData", methods=['POST'])
def load_data_post():
		#user input which table they want to upload
		table = request.form['db_table']
		#connect to mysql
		conn = mysql.connect()
		#create a cursor from the connection
		cursor = conn.cursor()
		#have cursor get all data from table
		cursor.execute("SELECT * FROM " + str(table))
		data = cursor.fetchall()
		#have cursor get all table names from table
		cursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = \'" + str(table) + "\' ORDER BY ORDINAL_POSITION")
		tbl_names = cursor.fetchall()

		for i in range(len(data)):
			data_dict = create_data_dict(data[i],tbl_names)
			api_instance = swagger_client.MaterialresourceApi(api_client=client_instance)
			material_dto = swagger_client.MaterialDTO(**data_dict)
			# createMaterial
			api_response = api_instance.create_material_using_post(material_dto)

		return render_template("./LoadData.html" , complete = True)


### Non-binded functions ###
# Authorize and Create API instance with user login info
def create_client_instance(username, password):
	# create an instance of the API jwt class
	api_instance = swagger_client.UserjwtcontrollerApi()
	#set user login credentials
	login_dto = swagger_client.LoginDTO(password=password, username=username) # LoginDTO | loginDTO
	#get auth header by authorizing user
	try:
		api_header = api_instance.authorize_using_post_with_http_info(login_dto)
		#get just authorization from header
		api_auth = api_header[2]
		#create a ApiClient using user authorization
		global client_instance
		client_instance = swagger_client.ApiClient(header_name='authorization', header_value=api_auth['authorization'])
		return(client_instance)
	except ApiException as e:
		return ("Incorrect Login Information")

#get all user's details and put into a dictionary
def get_user_details(login):
	# create an instance of the API class
	api_instance = swagger_client.UserresourceApi(api_client=client_instance)
    # getUser
	api_response = api_instance.get_user_using_get(login)
	#convert model to a dictionary and assign it to global variable
	user_details_dict = api_response.to_dict()
	return (user_details_dict)

#create a dictionary for a database row
def create_data_dict(data,tbl_names):
	data_dict = {}
	col_num = len(tbl_names)
	for i in range(1,col_num):
		if data[i] == '\x01':
			data_dict[str(tbl_names[i][0])] = True
		elif data[i] == '\x00':
			data_dict[str(tbl_names[i][0])] = False
		else:
			data_dict[str(tbl_names[i][0])] = data[i]
	return data_dict

#Run the app
if __name__ == "__main__":
	app.run()
	#app.run(host, port, debug, options)

'''
#cursor = conn.cursor()
#cursor.execute("SELECT * FROM materials")
#data = cursor.fetchall()
#return render_template("DBconnSuccess.html", data=data)

'''
