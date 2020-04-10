from flask import Flask
from flask import send_file
from flask import make_response
import not1
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/plots/intro', methods=['GET'])
def intro():
    bytes_obj = not1.intro() 
    return bytes_obj

@app.route('/plots/0', methods=['GET'])
def scatterplot0():
    bytes_obj = not1.plot0() 
    return bytes_obj

@app.route('/plots/1', methods=['GET'])
def scatterplot1():
    bytes_obj = not1.plot1() 
    return bytes_obj

@app.route('/plots/5', methods=['GET'])
def scatterplot2():
    bytes_obj = not1.plot2() 
    return bytes_obj

@app.route('/plots/4', methods=['GET'])
def scatterplot3():
    bytes_obj = not1.plot3() 
    return bytes_obj
                    
@app.route('/plots/3', methods=['GET'])
def scatterplot4():
    bytes_obj = not1.plot4() 
    return bytes_obj
                    
@app.route('/plots/6', methods=['GET'])
def violin():
    bytes_obj = not1.plot5() 
    return bytes_obj

@app.route('/plots/7', methods=['GET'])
def hist1():
    bytes_obj = not1.plot6() 
    return bytes_obj

@app.route('/plots/8', methods=['GET'])
def box1():
    bytes_obj = not1.plot7() 
    return bytes_obj

@app.route('/plots/9', methods=['GET'])
def bar1():
    bytes_obj = not1.plot8() 
    return bytes_obj

@app.route('/plots/10', methods=['GET'])
def bar2():
    bytes_obj = not1.plot9() 
    return bytes_obj
    
@app.route('/plots/11', methods=['GET'])
def bar3():
    bytes_obj = not1.plot10() 
    return bytes_obj

@app.route('/plots/14', methods=['GET'])
def bar4():
    bytes_obj = not1.plot11() 
    return bytes_obj

@app.route('/plots/13', methods=['GET'])
def stackbar5():
    bytes_obj = not1.plot12() 
    return bytes_obj

@app.route('/plots/15', methods=['GET'])
def stackbar6():
    bytes_obj = not1.plot13() 
    return bytes_obj

@app.route('/plots/16', methods=['GET'])
def stackbar7():
    bytes_obj = not1.plot14() 
    return bytes_obj

@app.route('/plots/17', methods=['GET'])
def groupbar1():
    bytes_obj = not1.plot15() 
    return bytes_obj

@app.route('/plots/18', methods=['GET'])
def groupbar2():
    bytes_obj = not1.plot16() 
    return bytes_obj

@app.route('/plots/19', methods=['GET'])
def groupbar3():
    bytes_obj = not1.plot17() 
    return bytes_obj

@app.route('/plots/20', methods=['GET'])
def pie1():
    bytes_obj = not1.plot18() 
    return bytes_obj
@app.route('/plots/21', methods=['GET'])
def pie2():
    bytes_obj = not1.plot19() 
    return bytes_obj
@app.route('/plots/22', methods=['GET'])
def pie3():
    bytes_obj = not1.plot20() 
    return bytes_obj

@app.route('/plots/23', methods=['GET'])
def pie4():
    bytes_obj = not1.plot21() 
    return bytes_obj
@app.route('/plots/24', methods=['GET'])
def pie5():
    bytes_obj = not1.plot22() 
    return bytes_obj

    


if __name__ == '__main__':
    app.run(debug=False)