function [x_lla] = ecef2lla(x_ecef)
% ECEF2LLH Converts from earth-centered, earth-fixed Cartesian coordinates to latitude, longitude, and altitude
% INPUT: x_ecef=[x,y,z]' (m) earth-centered, earth-fixed Cartesian coordinates
% OUTPUT: x_lla=[phi, lambda, h]' (rad, rad, m) GPS coordinates
    a = 6378137; % equatorial radius of ellipsoid (semi-major axis) (m)
    b = 6356752; % polar axis radius of ellipsoid (semi-minor axis) (m)

    x = x_ecef(1);
    y = x_ecef(2);
    z = x_ecef(3);
    
    % define auxiliary parameters e and f
    f = (a-b)/a;
    e = f*(2-f);
    
    lambda = atan(y/x);
    phi = atan(inv(1-e^2)*z/sqrt(x^2+y^2));
    N = a/sqrt(1-(e*sin(phi))^2);
    h = sqrt(x^2+y^2)/cos(phi)-N;
    
    x_lla = [phi; lambda; h];
end