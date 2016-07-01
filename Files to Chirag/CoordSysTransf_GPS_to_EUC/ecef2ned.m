function [x_ned] = ecef2ned(ned_lla, x_ecef)
% ECEF2NED Converts from earth-centered, earth-fixed Cartesian coordinates to tangent plane
% INPUT:
% 1) x_ecef=[x,y,z]' (m) earth-centered, earth-fixed Cartesian coordinates
% 2) ned_lla=[phi,lambda]' consiting of latitude phi (rad), longitude lambda (rad) of NED origin
% OUTPUT:
% 1) x_ned=[x,y,z]' (m) in NED coordinate system with the origin [phi,lambda]'

    phi = ned_lla(1);
    lambda = ned_lla(2);

    % transformation  matrix
    T = [-sin(phi)*cos(lambda) -sin(phi)*sin(lambda)  cos(phi)
         -sin(lambda)           cos(lambda)           0
          cos(phi)*cos(lambda)   cos(phi)*sin(lambda)  sin(phi)];

     x_ned = T*(x_ecef-lla2ecef([phi, lambda, 0]')); % convert to NED
     x_ned(3) = -x_ned(3);
end