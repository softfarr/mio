from flask import Flask

app= Flask (__name__)

@app.route('/')
def casa ():
    print ("cualquiercosa") 
    return "ok"
print ("cualquiercosa", __name__) 
if __name__=='__main__':
    app.run(debug=True, port=8080)