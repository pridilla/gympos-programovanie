def matica3 (v):
    return v[0][0]*v[1][1]*v[2][2] + v[0][1]*v[1][2]*v[2][0] + v[0][2]*v[1][0]*v[2][1] - v[0][2]*v[1][1]*v[2][0] - v[0][0]*v[1][2]*v[2][1] - v[0][1]*v[1][0]*v[2][2]

vv = [[1,2,3], [0,0,0], [-3,5,4]]
print(matica3(vv))