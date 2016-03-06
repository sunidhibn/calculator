from flask import Flask,render_template,request

app=Flask("find",static_url_path="/static")
data=[]

@app.route('/',methods=['GET','POST'])
def get_info():
	if request.method=='POST':
		num_1=request.form['num1']
		num_2=request.form['num2']
		option=request.form['opn']
		num_1=int(num_1)
		num_2=int(num_2)
		result=0
		
		if option=="add":
			result=num_1+num_2
			option="+"
		
		elif option=="subtract":
			result=num_1-num_2
			option="-"
		
		elif option=="multiply":
			result=num_1*num_2
			option="*"
		
		else:
			result=num_1/num2
			option="/"
	
		data.append({"num1":num_1 ,"num2":num_2, "op":option ,"res":result})
		return render_template('cal.html',info=data)
	
	else:
		return render_template('cal.html')

app.run(debug=True)