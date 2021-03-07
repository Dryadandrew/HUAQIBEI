from flask import Flask
from flask import render_template, request, send_file, send_from_directory
from flask import redirect, url_for
from werkzeug.utils import secure_filename 

import xlrd
import pandas
from reportlab.pdfgen import canvas

from flask_cors import CORS, cross_origin
import time

import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/usr/local/server/uwsgi-2.0.19.1/Web/upload'
app.config['RESULT_FOLDER'] = '/usr/local/server/uwsgi-2.0.19.1/Web/result'
# path1 = ''
# path2 = ''

def match(path1="/usr/local/server/uwsgi-2.0.19.1/Web/upload/Bank.xlsx", path2="/usr/local/server/uwsgi-2.0.19.1/Web/upload/Company.xlsx"):
	wb = xlrd.open_workbook(path1)
	#wb=wb.replace(['\n',' '],'')
	#wb=wb.replace('','0')
	tb=wb.sheets()[0]
	data=[]

	dex=[0]*6
	for r in range(tb.ncols):
		if tb.cell_value(0,r) == "凭证号":
			dex[1] = r
		#if tb.cell_value(1,r) == "对方账号":
		#	dui = r
		#if tb.cell_value(1,r) == "本方账号":
		#	ben = r
		if tb.cell_value(0,r) == "日期":
			dex[2] = r
			
		if tb.cell_value(0,r) == "借方发生额":
			dex[3] = r
		if tb.cell_value(0,r) == "贷方发生额":
			dex[4] = r
		if tb.cell_value(0,r) == "余额":
			dex[5] = r
	#pin=dex[1]
	dat=dex[2]
	jie=dex[3]
	dai=dex[4]
	yue=dex[5]
	#pin=3
	#dat=0
	#jie=7
	#dai=8
	#yue=9
	for q in range(tb.nrows):
		val=[]
		#val.append(tb.cell_value(q,pin))
		#val.append(tb.cell_value(q,dui))
		#val.append(tb.cell_value(q,ben))
		#val.append(tb.cell_value(q,dat))
		if isinstance(tb.cell_value(q,jie),str):
			val.append(0)
		else:
			val.append(tb.cell_value(q,jie))
		if isinstance(tb.cell_value(q,dai),str):
			val.append(0)
		else:
			val.append(tb.cell_value(q,dai))
		val.append(tb.cell_value(q,yue))
		data.append(tuple(val))
	# print(data)
	#print(dex)
	wx = xlrd.open_workbook(path2)
	tx=wx.sheets()[0]
	datax=[]
	dexx=[0]*6
	for r in range(tx.ncols):
		if tx.cell_value(1,r) == "凭证号":
			dexx[1] = r
		#if tb.cell_value(1,r) == "对方账号":
		#	dui = r
		#if tb.cell_value(1,r) == "本方账号":
		#	ben = r
		if tx.cell_value(1,r) == "交易时间":
			dexx[2] = r
			
		if tx.cell_value(1,r) == "借方发生额":
			dexx[3] = r
		if tx.cell_value(1,r) == "贷方发生额":
			dexx[4] = r
		if tx.cell_value(1,r) == "余额":
			dexx[5] = r
	#pin=dex[1]
	dat=dexx[2]
	jie=dexx[3]
	dai=dexx[4]
	yue=dexx[5]
	for d in range(tx.nrows):
		valx=[]
		#valx.append(tx.cell_value(d,0))
		#valx.append(tx.cell_value(d,3))
		if isinstance(tx.cell_value(d,jie),str):
			valx.append(0)
		else:
			valx.append(tx.cell_value(d,jie))
		if isinstance(tx.cell_value(d,dai),str):
			valx.append(0)
		else:
			valx.append(tx.cell_value(d,dai))
		valx.append(tx.cell_value(d,yue))
		datax.append(tuple(valx))
	# print(datax)
	result=[]
	error=[]
	for item in data:
		i=0
		for jtem in datax:
			if item == jtem:
				i=i+1
		result.append(i)
		if i == 0:
			error.append(item)

	# print(result)
	yue = dex[5]
	re_message = 'No result'
	for r in range(tb.nrows):
		if (len(error) == 0):
			re_message = 'No mistake'
		else:
			re_message = ''
			for item in error:	
				if tb.cell_value(r,yue) == item[2]:
					re_message += 'Mistake' + str(item) + '\n'
					# print("对账错误",item)
				else:
					re_message = 'Success'
					# print("对账成功")

	c = canvas.Canvas(os.path.join(app.config['RESULT_FOLDER'],secure_filename('result.pdf')))
	c.drawString(250, 500, re_message)
	c.showPage()
	c.save()

@app.route('/upload')
def upload_file():
   return render_template('index.html')

@app.route('/uploadBank', methods = ['GET', 'POST'])
@cross_origin()
def uploadBank():
   global path1
   if request.method == 'POST':
      f = request.files['file']
      f.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename('Bank.xlsx')))
      # process('./upload/'+f.filename)
    #   path1 = os.path.join(app.config['UPLOAD_FOLDER'],secure_filename('Bank.xlsx'))
      return "succcess upload"

@app.route('/uploadCompany', methods = ['GET', 'POST'])
@cross_origin()
def uploadCampany():
   global path2
   if request.method == 'POST':
      f = request.files['file']
      f.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename('Company.xlsx')))
    #   path2 = os.path.join(app.config['UPLOAD_FOLDER'],secure_filename('Company.xlsx'))
      return "succcess upload"


@app.route("/download",methods=['GET'])
def download_file():
   return send_file(os.path.join(app.config['RESULT_FOLDER'],secure_filename('result.pdf')))

@app.route('/')
def home_page():
    return 'Home page'

@app.route('/submit',methods=['GET'])
@cross_origin()
def submit():
    if request.args.get('cmd') == 'run':
        # time.sleep(3)
        # global path1
        # global path2
        match()
    	# c = canvas.Canvas("/usr/local/server/uwsgi-2.0.19.1/Web/result.pdf")
        # c.drawString(100, 100, "helloWorld")
        # c.showPage()
        # c.save()
        return 'OK'

if __name__ == '__main__':
    app.run()
    CORS(app)
   # app.run(host="172.17.59.121", port=5000, debug=False)


# @app.route('/hello/<name>')
# def hello_name(name):
#     return 'Hello %s!' % name

# @app.route('/admin')
# def hello_admin():
#    return 'Hello Admin'

# @app.route('/guest/<guest>')

# def hello_guest(guest):
#    return 'Hello %s as Guest' % guest


# @app.route('/user/<name>')
# def hello_user(name):
#    if name =='admin':
#       return redirect(url_for('hello_admin'))
#    else:
#       return redirect(url_for('hello_guest',guest = name))
