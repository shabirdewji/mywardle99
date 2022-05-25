from flask import Flask, request, render_template
from processing import do_calculation

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    print('IN INDEX')
    return render_template('index.html')


@app.route('/main', methods = ['GET', 'POST'])
def main():
    print('IN MAIN')

    if request.method == 'POST':
        # value = request.form.get('btn') # gives text from `value="Button 1"` 
        w1 = w2 = w3 = w4 = w5 = None 
   
        word  = None
        nword = None
        must  = None

        w1 = request.form["w1"]
        w2 = request.form["w2"]
        w3 = request.form["w3"]
        w4 = request.form["w4"]
        w5 = request.form["w5"]
        must = request.form["must"]
        nword = request.form["nword"]
        
        if request.form["w1"] == "" :  w1="*"
        if request.form["w2"] == "" :  w2="*"
        if request.form["w3"] == "" :  w3="*"
        if request.form["w4"] == "" :  w4="*"
        if request.form["w5"] == "" :  w5="*"
        
        word = w1+w2+w3+w4+w5    
        
        # print("word: ",word," nword: ",nword," must: ",must)    
        # print('calling process')
            
        list = do_calculation(word, nword, must)
        
        if w1 == "*" : w1 =""
        if w2 == "*" : w2 =""
        if w3 == "*" : w3 =""
        if w4 == "*" : w4 =""
        if w5 == "*" : w5 =""
        
        color = ['002aff','e1eb34','28fc03','fc1703', 'b503fc']
    
        

        
        return render_template('index.html', list=list, w1=w1,w2=w2,w3=w3,w4=w4,w5=w5,nword=nword,must=must, color=color)
        # return render_template('index.html', list=list) 