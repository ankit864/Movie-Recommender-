# -*- coding: utf-8 -*-
from flask import Flask
import tablib
import os
from flask import Flask,redirect,url_for,request,make_response
from flask import render_template
from subprocess import call
import os
import subprocess
import imdbs_rec
app = Flask (__name__)

#fun var

#dataset = tablib.Dataset()
#with open(os.path.join(os.path.dirname(__file__),'data.csv')) as f:
#	 dataset.csv = f.read()


@app.route("/list")
def list():
	dataset = tablib.Dataset()
	with open(os.path.join(os.path.dirname(__file__),'data.csv')) as f:
        	 dataset.csv = f.read()
	return dataset.html

@app.route("/recomend",methods = ['POST','GET'])
def recomend():
    if request.method == 'POST':
        question1 = request.form['group1']
        question2 = request.form["group2"]
        question3 = request.form['group3']
	question4 = request.form['group4']
        if not len(question1) or not len(question2) or not len(question3):
            return render_template('registerpage.html',error = "please fill all the field listed")
        print question1 
	print question2
	print question3
	main_list = []
	if question1 == "yes":
		print "yeah u love music"
		main_list.append("Music")
		main_list.append("Drama")
	else:	
		main_list.append("War")
		main_list.append("Biography")
		print "ok"
	if question2 == "family":
                main_list.append("Family")
                main_list.append("Animation")
        elif question2 == "gforbf":
                main_list.append("Romance")
                main_list.append("Comedy")
                print "ok"
	else:
		main_list.append("Adventure")
                main_list.append("Thriller")
                main_list.append("Sci-Fi")

	if question3 == "yes":
                main_list.append("Animation")
                main_list.append("Sci-Fi")
		main_list.append("Fantasy")

        else:
                main_list.append("War")
                main_list.append("Crime")
                print "ok"
	main_list.append(question4)
	imdbs_rec.calculate(main_list)
        #if password != confirm_password:
         #   return render_template('registerpage.html',error = "password and confirm password must be same.")
        #stu = students.query.filter(students.name == name).count()
        #if stu == 1:
         #   return render_template('registerpage.html',error = "user already exist")
        #print "check2"
        #student = students(name,password)
        #db.session.add(student)
        #db.session.commit()
        return redirect(url_for('list'))
    else:
        return render_template('registerpage.html')


if __name__ == '__main__':
	app.debug = True
    	app.run(
        host="0.0.0.0",
        port=int("8080")
  	)

