import xlrd
import pandas
wb = xlrd.open_workbook("C:\\Users\\Administrator\\Downloads\\1.xlsx")
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
print(data)
#print(dex)
wx = xlrd.open_workbook("C:\\Users\\Administrator\\Downloads\\2.xlsx")
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
print(datax)
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

print(result)
yue = dex[5]
for r in range(tb.nrows):
	for item in error:	
		if tb.cell_value(r,yue) == item[2]:
			print("对账错误",item)
		else:
			print("对账成功")

