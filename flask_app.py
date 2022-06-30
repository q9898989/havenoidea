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

#@hops.component(
    #http://127.0.0.1:5000/calculate_the_angle
    #using coordinate to angle angle
 #   "/calculate_the_angle",
 #   name = 'calculate_the_angle',
 #   description = "calculate_the_angle",
 #   inputs = [
        #access = hs.HopsParamAccess.LIST
 #       hs.HopsNumber("p_1",hs.HopsParamAccess.LIST),
 #       hs.HopsNumber("p_2",hs.HopsParamAccess.LIST),
 #       hs.HopsNumber("p_3",hs.HopsParamAccess.LIST)
 #   ],
 #   outputs = [
 #       hs.HopsNumber("angle")
 #   ]
#)

#@app.route('/')
#def hello_world():
 #   return 'Hello hello hello hello Hello!'

#@app.route('/cal_the_angle')
#def calculate_the_angle(p_1,p_2,p_3):
    #import math
   # args = request.args
   # variables = dict(args)
    #float(p1)
    #float(p2)
    #float(p3)
    #p1 = []
    #for num in p_1:
        #p1.append(float(num))

    #p2 = []
    #for num in p_2:
        #p2.append(float(num))

    #p3 = []
    #for num in p_3:
        #p3.append(float(num))

    #v_p1_p2 = math.sqrt((p1[1] - p1[0])**2 + (p2[1]-p2[0])**2 +(p3[1]-p3[0]) **2)
    #v_p2_p3 = math.sqrt((p1[2] - p1[1])**2 + (p2[2]-p2[1])**2 +(p3[2]-p3[1])**2)

    #aaa = (p1[0] - p1[1])*(p1[2] - p1[1])+(p2[0]-p2[1])*(p2[2] - p2[1])+(p3[0] - p3[1])*(p3[2]-p3[1])

    #angle = (math.acos(aaa/(v_p1_p2 *v_p2_p3))/math.pi) * 180
    #angle = p1+p2+p3
    #return angle
    