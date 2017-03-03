
import pyodbc

try:

	server = 'btrwebsitedata.database.windows.net'
	database = 'WebsiteData'
	username = 'btr.helpdesk'
	password = 'Benchmark123'
	driver= '{ODBC Driver 13 for SQL Server}'
	cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
	print('successful')
	cnxn.close()

except:
	print ('not successful')