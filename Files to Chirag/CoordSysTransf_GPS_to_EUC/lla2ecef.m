function x_ecef = lla2ecef(x_lla)
% LLE2ECEF: Converts from geodetic latitude, longitude, and altitude to earth-centered earth-fixed Cartesian coordinates
% INPUT: latitude phi (rad), longitude lambda (rad), altitude h (m)
% OUTPUT: [x, y, z]' (m) earth-centered earth-fixed Cartesian coordinates
    a = 6378137; % equatorial radius of ellipsoid (semi-major axis) (m)
    b = 6356752; % polar axis radius of ellipsoid (semi-minor axis) (m)

    phi = x_lla(1);
    lambda = x_lla(2);
    h = x_lla(3);
    
    % auxiliar quantities f, e, and N
    f = (a-b)/a;
    e = f*(2-f);
    N = a/sqrt(1-(e*sin(phi))^2);
    x_ecef = [(N+h)*cos(phi)*cos(lambda); (N+h)*cos(phi)*sin(lambda); (N*(1-e^2)+h)*sin(phi)];
end