from flask import Flask
from requests import request
import rhino3dm as rhino
import ghhops_server as hs

app = Flask(__name__)
hops = hs.Hops(app)

@hops.component(
    name = 'calculate_the_angle',
    description = "cal_the_angle",
    inputs = [
        hs.HopsNumber('p1','p1','p1'),
        hs.HopsNumber('p2','p2','p2'),
        hs.HopsNumber('p3','p3','p3')
    ],
    outputs = [
        hs.HopsNumber("the_angle")
    ]
)

@app.route('/')
def hello_world():
    return 'Hello hello hello hello Hello!'


@app.route('/abcd')
def abcd():
    return 'have no idea yet'

@app.route('calculate_the_angle')
def calculate_triangle_angle(p1,p2,p3):
    import math
    args = request.args
    variables = dict(args)


#    let { x: x1, y: y1, z: z1 } = p1;
 #   let { x: x2, y: y2, z: z2 } = p2;
  #  let { x: x3, y: y3, z: z3 } = p3;
    
    v_p1_p2 = math.sqrt((p1[1] - p1[0])**2 + (p2[1]-p2[0])**2 +p3[1]-p3[0] **2)
    v_p2_p3 = math.sqrt((p1[2] - p1[1])**2 + (p2[2]-p2[1])**2 +p3[2]-p3[1] **2)

    aaa = (p1[0] - p1[1])*(p1[2] - p1[1])+(p2[0]-p2[1])*(p2[2] - p2[1])+(p3[0] - p3[1])*(p3[2]-p3[1])

    the_angle = (math.acos(aaa/(v_p1_p2 *v_p2_p3))/math.pi) * 180
    return the_angle

if __name__ == '__main__':
    app.run()
    