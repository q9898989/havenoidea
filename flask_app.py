from flask import Flask
#from requests import request
#import rhino3dm as rhino
import ghhops_server as hs

app = Flask(__name__)
hops = hs.Hops(app)

@hops.component(
    #http://127.0.0.1:5000/cal_angles
    "/cal_angles",
    name = 'cal_angles',
    description = "cal_angles",
    inputs = [
        #access = hs.HopsParamAccess.LIST
        hs.HopsNumber("l1"),
        hs.HopsNumber("l2"),
        hs.HopsNumber("l3")
    ],
    outputs = [
        hs.HopsNumber("a1"),
        hs.HopsNumber("a2"),
        hs.HopsNumber("a3")
    ]
)

@app.route('/cal_angles')
def calculate_the_length(l1,l2,l3):
    import math
    a1 = math.degrees(math.acos(((l3**2) + (l2 **2) - (l1**2))/(2*l2*l3)))
    a2 = math.degrees(math.acos(((l3**2) + (l1 **2) - (l2**2))/(2*l1*l3)))
    a3 = math.degrees(math.acos(((l1**2) + (l2 **2) - (l3**2))/(2*l2*l1)))

    return a1,a2,a3


if __name__ == '__main__':
    app.run()


@app.route('/hello')
def hello():
    return 'Hello hello hello, Welcome'
    