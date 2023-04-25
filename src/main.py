from flask import Flask, render_template, url_for, request
app = Flask(__name__,static_url_path='/static')
@app.route('/',methods=['GET', 'POST'])
def GetFlag2():
  return render_template('GetFlag1.html')

@app.route('/ValidationFlag1', methods=['GET','POST'])
def submit_form1():
    # Handle form submission here
    flag=request.form.get('flag1')
    flag1="CTF{is fun}".lower()
    if(flag.lower()==flag1):
       return render_template('GetFlag2.html')
    else:
       return render_template('GetFlag1.html')

@app.route('/ValidationFlag2', methods=['GET','POST'])
def submit_form2():
    # Handle form submission here
    flag=request.form.get('flag2')
    flag2="CTF{3AE186C4-DCA9-11ED-AFA1-0242AC120002FLAG2}".lower()
    if(flag.lower()==flag2):
       return render_template('GetFlag3.html')
    else:
       return render_template('GetFlag2.html')
    
@app.route('/ValidationFlag3', methods=['GET','POST'])
def submit_form3():
    # Handle form submission here
    flag=request.form.get('flag3')
    flag3="CTF{5037b9b2-ddf3-11ed-b5ea-0242ac120002}".lower()
    if(flag==flag3):
       return render_template('GetFlag3.html')
    else:
       return render_template('Finish.html')


if __name__ == "__main__":
  app.run(host='0.0.0.0')
