from flask import Flask,render_template,request
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os


app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!!! how are youuu"

@app.route("/index")
def indexpage():
    
    return "Hey i'm index page"
    #females = data.loc[data.Gender=='f']
    #males = data.loc[data.Gender=='m']

@app.route("/input", methods=["GET","POST"])
def userinput():
   
    if request.method == "POST":
        company = request.form.get("cname")
        typename = request.form.get("tname")
        ram = request.form.get("rname")
        price = request.form.get("currency")
        print("Your requirement is "+company + typename + ram + price)
    
        compdata = fetch_details_cpu(company,typename,ram,price)
        
        if compdata.empty:
            return render_template("noresults.html", text1 = company, text2 = typename, text3 = ram)
        else:
            
            compdata = compdata.drop(['TargetProduct'],1)
            maxprice = compdata[:11].max()
            minprice = compdata[:11].min()
            compmax = maxprice['Company']
            prodmax = maxprice['Product']
            screenmax = maxprice['ScreenResolution']
            memorymax = maxprice['Memory']
            cpumax = maxprice['Cpu']
            pricemax = maxprice[11]
            
            compmin = minprice['Company']
            prodmin = minprice['Product']
            screenmin = minprice['ScreenResolution']
            memorymin = minprice['Memory']
            cpumin = minprice['Cpu']
            pricemin = minprice[11]
            
            datalen = len(compdata)
            return render_template('index.html',tables=[compdata.to_html(classes='userdata')],maxpr=pricemax,maxscreen=screenmax,maxcomp = compmax,maxprod = prodmax,maxcpu=cpumax,maxmemory=memorymax,
                              minpr=pricemin,minscreen=screenmin,mincomp = compmin,minprod = prodmin,mincpu=cpumin,minmemory=memorymin,datal = datalen, titles = ['na', 'Userdata '])
            
    
        
        
    
    return render_template("userinput.html")

def fetch_details_cpu(a,b,c,d):
    #st.text("Enter the Company of which you want to go for ")
    #user_cmp = st.text_input("Enter :")
    DATA_URL = ('laptops.csv')
    data = pd.read_csv(DATA_URL)
    
    if(d=="rupees"):
        data=data.drop(['Price_euros','Price_in_Dollars'],axis=1)
    elif(d=="dollars"):
        data = data.drop(['Price_euros','Price_in_Rupees'],axis=1)
    else:
        data = data.drop(['Price_in_Rupees','Price_in_Dollars'],axis=1)
        
    compdatacpu = data.query('Company == "{}" and TypeName == "{}" and Ram == "{}"'.format(a
                                                                        ,b,c))
    return compdatacpu    
    


    

if __name__ == "__main__":
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    
