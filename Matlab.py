
from numpy import array,dot
from math import pi,sqrt,sin,cos,tan,atan

# def ecef2lla(x_ecef):
# # % ECEF2LLH Converts from earth-centered, earth-fixed Cartesian coordinates to latitude, longitude, and altitude
# # % INPUT: x_ecef=[x,y,z]' (m) earth-centered, earth-fixed Cartesian coordinates
# # % OUTPUT: x_lla=[phi, lambda, h]' (rad, rad, m) GPS coordinates
#     a = 6378137 # equatorial radius of ellipsoid (semi-major axis) (m)
#     b = 6356752 # polar axis radius of ellipsoid (semi-minor axis) (m)

#     x = x_ecef[0]
#     y = x_ecef[1]
#     z = x_ecef[2]
    
#     # define auxiliary parameters e and f
#     f = (a-b)/a
#     e = f*(2-f)
    
#     m = atan(y/x)
#     phi = atan(inv(1-e^2)*z/sqrt(x^2+y^2))
#     N = a/sqrt(1-(e*sin(phi))^2)
#     h = sqrt(x^2+y^2)/cos(phi)-N
    
#     x_lla = array([phi, m, h]).transpose()
#     return x_lla


def ecef2ned(ned_lla, x_ecef):
# % ECEF2NED Converts from earth-centered, earth-fixed Cartesian coordinates to tangent plane
# % INPUT:
# % 1) x_ecef=[x,y,z]' (m) earth-centered, earth-fixed Cartesian coordinates
# % 2) ned_lla=[phi,lambda]' consiting of latitude phi (rad), longitude lambda (rad) of NED origin
# % OUTPUT:
# % 1) x_ned=[x,y,z]' (m) in NED coordinate system with the origin [phi,lambda]'
    #print 'ned_lla' + str(ned_lla)
    phi = ned_lla[0]
    m = ned_lla[1]
    T = array([[-sin(phi)*cos(m),-sin(phi)*sin(m),cos(phi)],[-sin(m),cos(m),0],[cos(phi)*cos(m),cos(phi)*sin(m), sin(phi)]])
    diff = x_ecef-lla2ecef(array([phi, m, 0])).transpose()
    # print 'diff = ' + str(diff)
    # raw_input()
    x_ned = dot(T,diff) # convert to NED
    x_ned[2] = -x_ned[2];
    return x_ned


def lla2ecef(x_lla):
	# % LLE2ECEF: Converts from geodetic latitude, longitude, and altitude to earth-centered earth-fixed Cartesian coordinates
	# % INPUT: latitude phi (rad), longitude lambda (rad), altitude h (m)
	# % OUTPUT: [x, y, z]' (m) earth-centered earth-fixed Cartesian coordinates
    a = 6378137; # equatorial radius of ellipsoid (semi-major axis) (m)
    b = 6356752; # polar axis radius of ellipsoid (semi-minor axis) (m)
    phi = x_lla[0];
    m = x_lla[1];
    h = x_lla[2];
    f = (a-b)/a;
    e = f*(2-f);
    N = a/sqrt(1-(e*sin(phi))**2);
    x_ecef = array([(N+h)*cos(phi)*cos(m), (N+h)*cos(phi)*sin(m), (N*(1-e**2)+h)*sin(phi)]).transpose();
    return x_ecef

def ned2ecef(ned_lla, x_ned):
# % NED2ECEF 
# % INPUT:
# % 1) x_ned=[x,y,z]' (m) NED coordinates
# % 2) ned_lla=[phi,lambda]' consiting of latitude phi (rad) and longitude lambda (rad) of NED origin
# % OUTPUT:
# % 1) x_ecef=[x,y,z]' (m) in earth-centered, earth-fixed coordinate system with the origin [phi,lambda]'
	phi = ned_lla[0];
	m = ned_lla[1];
	#transformation  matrix
	T = array([[-sin(phi)*cos(m),-sin(phi)*sin(m),cos(phi)],
         [-sin(m)           ,cos(m)           ,0],
         [cos(phi)*cos(m)   ,cos(phi)*sin(m) , sin(phi)]]);


	x_ecef = dot(T.transpose(),x_ned) + lla2ecef(array([phi, m, 0]).transpose());
	return x_ecef
