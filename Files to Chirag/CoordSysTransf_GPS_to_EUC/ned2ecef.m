function x_ecef = ned2ecef(ned_lla, x_ned)
% NED2ECEF 
% INPUT:
% 1) x_ned=[x,y,z]' (m) NED coordinates
% 2) ned_lla=[phi,lambda]' consiting of latitude phi (rad) and longitude lambda (rad) of NED origin
% OUTPUT:
% 1) x_ecef=[x,y,z]' (m) in earth-centered, earth-fixed coordinate system with the origin [phi,lambda]'

    phi = ned_lla(1);
    lambda = ned_lla(2);

    % transformation  matrix
    T = [-sin(phi)*cos(lambda) -sin(phi)*sin(lambda)  cos(phi)
         -sin(lambda)           cos(lambda)           0
          cos(phi)*cos(lambda)   cos(phi)*sin(lambda)  sin(phi)];
    
    x_ecef = T'*x_ned + lla2ecef([phi, lambda, 0]');
end