format long; clear all; clc;
x = 1;
% origin of NED coordinate system in GPS coordinates
ned_orig = [37.835145 * (pi/180); -77.414640 * (pi/180)]; % phi (rad); lambda (rad)
count = [21, 11, 43, 18, 245, 14, 41, 235, 74, 13, 20, 17, 21, 62, 13, 20, 1139, 14, 13, 16, 14, 24, 30, 954, 34, 18, 314, 33, 28, 86, 13, 12, 31, 15, 53, 41, 32, 39, 9, 19, 40, 16, 16, 23, 14, 49, 36, 24, 43, 20, 15, 12, 49, 21, 48, 14, 114, 15, 54, 9064, 835, 15, 12157, 165, 23, 12, 15, 242, 45, 107, 1741, 17, 221, 11, 1129, 360, 402, 18, 4, 14, 45, 37, 21, 29, 88, 11, 18, 684, 21, 21, 20, 866, 29, 13, 90, 12, 658, 96, 608, 17, 2483, 41, 14, 21, 28, 109, 23, 587, 224, 18, 60, 129, 16, 50, 148, 8, 15, 5513, 13, 19, 87, 13, 16, 23, 15, 33, 8, 44, 18, 14, 804, 27, 6, 77, 14, 11, 19, 41, 115, 4776, 16, 332, 32, 21, 337, 17, 13, 12, 29, 16, 10, 32, 73, 406, 27, 21, 79, 18, 538, 17, 15, 16, 14, 15, 313, 23, 270, 14, 68, 23, 575, 12, 16, 6020, 145, 16, 20, 15, 970, 18, 124, 13, 30, 16, 34, 166, 22, 17, 13, 21, 16, 18, 117, 67, 35, 16, 12, 83, 119, 18, 15, 20, 134, 14, 74, 12, 9, 222, 25, 13, 515, 165, 67, 30, 12, 161, 14, 23, 19, 14, 44, 29, 20, 31, 37, 43, 37, 16, 1526, 102, 21, 240, 13, 110, 28, 17, 44, 13, 17, 18, 14, 513, 18, 15, 46, 13, 13, 17, 321, 69, 13, 26, 19, 2317, 26, 13, 12, 62, 18, 13, 126, 36, 21, 14, 227, 12, 26, 14, 15, 16, 19, 77, 19, 345, 575, 373, 12, 15, 49, 11, 20, 14, 19, 12, 73, 11, 5774, 44, 36, 13, 16, 16, 46, 230, 59, 12, 1584, 31, 92, 14, 332, 1284, 16, 57, 12, 22, 12, 18, 25, 17, 32, 13, 11035, 14, 23, 19, 36, 5, 15, 32, 121, 27, 15, 43, 40, 16, 23, 15, 18, 14, 12, 17, 23, 2836, 50, 16, 16, 16, 23, 5476, 16, 40, 34, 19, 12, 30, 15, 20, 23, 13446, 30, 19, 17, 25, 26, 83, 53, 60, 27, 13, 50, 72, 83, 16, 42, 16, 19, 27, 22, 48, 14, 70, 50, 17, 11, 19, 28, 17, 26, 13, 26, 12, 33, 35, 52, 15, 26, 15, 13, 754, 22, 26, 46, 13, 11, 28, 15, 18, 25, 15, 11, 9, 13, 20, 16, 16, 11, 95, 25, 16, 5236, 16, 28, 19, 42, 14, 19, 18, 23, 17, 16, 11, 19, 932, 33, 7, 44, 44, 28, 20, 18, 6, 20, 17, 40, 80, 16, 23, 32, 16, 30, 29, 163, 10, 51, 6143, 22, 22, 43, 18, 20, 24, 24, 27, 16, 43, 28, 27, 13, 482, 17, 13, 25, 21, 21, 25, 17, 20, 8227, 5, 15, 6942, 21, 24, 36, 13, 31, 22, 19, 20, 29, 5, 30, 14, 9, 27, 25, 10, 21, 17, 13, 125, 22, 18, 17, 15, 75, 72, 33, 22, 7, 38285, 13, 20, 1377, 31, 15, 13, 51, 18, 38, 24, 38, 85, 18, 37, 32, 60, 13, 1680, 27, 20, 6, 9, 51, 40, 727, 15, 12, 40, 73, 27, 2992, 27, 14, 36, 20, 22, 28, 17, 462, 96, 338, 48, 70, 21, 9, 20, 196, 575, 20, 7160, 57, 23, 22, 16, 6615, 40, 18092, 18, 34, 11, 25, 38, 17, 25, 29, 53, 15695, 31, 26, 15, 46, 33, 11, 28, 26, 44, 16, 75, 18, 1272, 17, 74, 16, 16, 17, 64, 21, 25, 17, 15, 34, 25, 49, 9, 9, 22, 23, 32, 23, 53, 29, 9, 1221, 35, 47, 28, 19, 24, 20, 5190, 134, 21, 25, 45, 60, 106, 16, 29, 29, 26, 26, 17, 9, 31, 31, 26, 10, 19, 25, 8, 27, 27, 21, 22, 71, 23, 49, 139, 150, 25, 22, 9, 18, 9, 451, 9, 26, 22, 24, 80, 28884, 23, 20, 667, 9, 28, 4, 30, 17, 160, 13, 21, 31, 19, 10, 10, 9, 8, 20, 48, 20, 25, 21, 22, 34, 20, 137, 21, 19, 22, 145, 10, 28, 43, 45, 17, 9, 9, 474, 41, 20, 18, 23, 18, 23855, 15, 19, 11121, 23, 32, 9, 14, 22, 27, 22, 19, 9, 195, 62, 23, 9, 9, 10, 9, 10, 61, 34, 54, 8, 53, 82, 23, 39, 9, 21, 33, 22, 25, 18, 108, 19, 5, 6, 112, 7, 8, 5, 70, 5, 8, 6, 9, 10, 10, 27, 8, 7, 6, 8, 13, 134, 16, 9, 9, 10, 7, 13, 8, 5, 12, 19, 11, 86, 79, 10, 22, 8, 1411, 15, 16, 10, 9, 6, 6, 6, 11, 10, 6, 6, 5, 74, 7, 13, 7, 9, 8349, 77, 2786, 8, 63, 392, 107, 10, 11, 10, 6, 229, 18, 10, 10, 173, 6800, 218, 6, 9, 9, 11, 12, 15, 179, 762, 90, 116, 8, 59, 8, 16, 37, 10, 104, 44, 22, 27, 978, 13, 287, 53, 10, 11, 9, 66, 2659, 5812, 4785, 7, 3976, 493, 9, 18, 21, 9, 6, 21, 19, 15, 20, 12, 102, 5, 1385, 12, 6, 107, 16, 15, 16, 28, 18, 52, 6, 10, 35, 17, 14, 11, 5, 7, 8962, 23, 8, 16, 8, 16, 31, 73, 5, 9, 16, 20, 16, 6, 8, 21, 16, 47, 5, 402, 13500, 7, 7, 10, 943, 5358, 11, 7, 7, 9, 186, 7, 6, 12, 23, 8, 11, 7, 25, 31, 9, 9, 92, 7, 38, 6, 7, 10, 8, 9, 13, 7, 9, 11, 7, 11, 308, 5, 6, 7, 5691, 7, 7, 8, 123, 15, 10, 9, 16, 9, 9, 7, 7, 112, 7, 7, 9, 9, 7, 57, 52, 7, 28, 7, 9, 15, 57, 9, 10, 7, 11, 17, 15, 30, 731, 7, 7, 2340, 8, 22, 19, 16, 35, 35, 9, 9, 6, 6, 8, 93, 7, 6, 14, 7, 560, 14, 9, 10, 7, 22, 7, 10, 7, 9, 7, 26, 25, 10, 31, 71, 10, 7, 7, 9, 7, 7, 9, 7, 10, 47, 1457, 13, 5, 11, 21, 12, 15, 5, 5159, 6, 6, 11, 15, 5, 5, 133, 10, 147, 7, 18, 9, 713, 23, 256, 6, 9, 24, 6, 5, 298, 6, 4, 8, 5, 22, 7, 7, 14, 7, 10, 6, 42, 11, 38, 13, 30, 48, 9, 9, 20, 7, 5, 15, 6, 5, 6, 10, 5, 6, 17, 28, 20, 125, 7, 32, 91, 2209, 34, 34, 14, 12, 8, 5, 27, 6, 37, 5, 7, 5, 65, 15, 13, 5, 13, 15, 21, 10, 5, 8, 5, 77, 34, 6, 28, 8, 11, 4433, 1355, 60, 8, 9, 5, 5, 20, 37, 14, 9, 6, 48, 129, 10, 8, 14, 11, 104, 8, 28, 11, 35, 29, 33, 78, 28, 13, 11, 16, 19, 20, 483, 13, 6, 11, 6, 8, 5, 94, 14, 5, 7, 15, 9, 29, 5, 95, 1816, 130, 82, 110, 18, 8, 11, 569, 19, 8, 12, 13, 12, 13, 21, 5, 10, 9, 7, 8, 7, 153, 52, 52, 41, 27, 2718, 37, 6, 22, 6, 8, 662, 9, 11, 6, 5, 6, 5, 155, 263, 6, 11, 30, 5, 5, 18, 10, 12, 6, 45, 21, 151, 7, 8, 75, 276, 49, 1074, 26, 10, 18, 12, 11, 9, 12, 25, 32, 5, 10, 13, 171, 11, 8, 11, 10, 10, 15, 6, 9, 6, 12, 8, 11, 7, 11, 13, 13, 22, 11, 8, 12, 9, 10, 8, 53, 27, 13, 8, 10, 13, 15, 11, 38, 24, 12, 130, 30, 64, 47, 12, 9, 17902, 16, 13, 6, 9, 11, 10, 13, 59, 29, 10, 11, 10, 12, 997, 6, 9, 11, 11, 56, 11, 5, 44, 13, 14, 30, 16, 6, 8, 12, 10, 41, 16, 12, 6, 14, 46, 2239, 14, 13, 13, 13, 328, 3464, 153, 60, 859, 172, 18, 66, 113, 662, 12, 12, 12, 11, 11, 18, 42, 127, 17254, 3056, 274, 480, 20, 19, 28, 295, 149, 19, 8, 371, 152, 24, 20, 106, 20, 16, 8, 18, 14, 4078, 21957, 14664, 5402, 22, 26, 391, 71, 161, 15, 21, 5, 10, 7, 327, 5, 17, 41, 5, 15, 15, 16, 13, 2452, 12, 19, 164, 44, 7, 11, 13, 430, 11, 8, 9, 10, 244, 24, 20, 15, 37, 18, 16, 536, 22, 5, 17, 25, 1121, 11, 11, 12, 5, 18, 70, 164, 11, 12, 272, 3676, 18, 408, 8319, 2680, 1469, 5, 1942, 4429, 33, 20, 84, 28, 24, 17, 27, 28, 44, 13, 22, 6, 37, 13, 23, 34, 10023, 23, 13, 35, 17, 23, 49, 30, 20, 28, 14, 26, 21, 21, 20, 19, 17, 28, 35, 28, 35, 22, 32, 14597, 7578, 225, 7, 8, 7, 12, 9, 18, 27, 11, 11, 19, 26, 11, 23, 12, 7, 10, 7, 9, 9, 234, 4214, 15, 91, 43, 16, 8, 7, 14, 24, 22, 667, 9, 9, 10, 11, 12, 667, 11, 9, 10, 17, 9, 13, 11, 288, 31, 25, 11, 15, 11, 15, 12, 15, 17, 41, 20, 31, 1272, 9108, 10, 215, 10, 13, 5, 13, 6, 6, 17, 17, 11, 6, 95, 6, 19, 13, 6, 14, 9, 5, 7, 23, 6, 5, 31, 9, 162, 7, 31, 5, 64, 7, 9, 25, 15, 7, 21, 9, 18, 6, 7, 19, 15, 21, 6, 5, 5, 5, 6, 36, 19, 5, 25, 6, 15258, 5, 4563, 17, 18, 16, 23, 1861, 285, 22, 58, 17, 22, 14, 60, 28, 295, 28, 16, 12, 13, 25, 79, 14, 14, 17, 9, 21, 13, 32, 17, 1275, 37, 266, 27, 23, 31, 21, 986, 198, 14, 11, 24, 26, 11, 24, 16, 22, 22, 14, 297, 24, 27, 10445, 2666, 18, 10, 14, 16, 77, 43, 703, 22, 21, 28, 22, 621, 2488, 25, 21, 14, 17, 18, 329, 15, 69, 19, 1073, 14, 18, 15, 1214, 15, 14, 41, 23, 19, 17452, 129, 17464, 2605, 21, 6, 7, 7, 115, 5, 5416, 23, 7, 5, 15, 19, 31, 10, 6, 5, 5, 5, 6, 8, 5, 6, 340, 6, 400, 7, 6, 6, 5, 5, 30, 31, 9, 7, 5, 5, 27, 19, 10193, 11, 5, 9, 8, 17, 36, 5, 5, 5, 5, 5, 10, 6, 15, 5, 5, 5, 5, 5, 5, 5, 156, 4196, 16, 6, 5, 7, 5, 6, 5, 22, 45, 1101, 26, 5, 1089, 8, 6, 8, 9, 5, 11, 7, 5, 7, 7, 7658, 6, 5, 5, 11, 2917, 958, 12, 5, 1077, 5, 5, 8, 6, 7, 6, 74, 5, 32, 9, 146, 13, 15, 169, 67, 208, 21, 11, 12, 15, 14, 10, 86, 4294, 11, 19, 31, 54, 120, 20, 60, 78, 14, 58, 33, 18, 12, 96, 12, 7, 12, 14, 44, 454, 12, 21, 13, 16, 18, 13, 32, 16, 13, 13, 5217, 3813, 7, 10, 20, 13, 6, 18, 18, 10, 36, 4, 15, 27, 23, 58, 44, 33, 15, 8, 15, 15, 16, 21, 18, 11, 14, 13, 6, 5, 21, 5, 23, 45, 13, 49, 14, 12, 21, 13, 10, 15, 317, 16, 21, 20, 146, 12, 8614, 15, 44, 617, 5, 17, 15, 14, 5, 67, 7, 43, 89, 21, 125, 10, 5, 8, 2976, 3045, 10, 16, 17, 27, 26, 18, 29, 15, 15, 28, 11, 82, 9, 14, 55, 12, 14, 33, 9, 12, 12, 13, 15, 23, 9, 30, 12, 26, 10, 14, 11, 3212, 35, 28, 21, 42, 10, 43, 15, 9, 35, 19, 201, 23, 21, 3071, 7417, 17, 13, 21, 69, 10, 24, 26, 35, 18, 28, 43, 20, 41, 18, 9, 18, 6, 13, 39, 23, 14, 11, 5, 12, 10, 11, 17, 6, 11, 16, 7, 29, 22, 7, 39, 18, 12, 46, 37, 5731, 42, 9, 27, 14, 12, 128, 59, 25, 12, 142, 13, 9, 15, 10, 19, 156, 49, 9, 17, 41, 58, 6, 16, 304, 15, 14, 21, 202, 20, 17, 20, 51, 39, 37, 30, 7, 76, 35, 10, 10, 14, 10, 75, 15, 23, 29, 13, 38, 24, 1434, 865, 151, 7179, 30, 39, 9, 9, 18, 60, 152, 14, 22, 330, 673, 5, 12, 124, 26, 11, 15, 42, 26, 21, 2536, 76, 73, 50, 16, 36, 15, 15, 43, 26, 24, 12, 17, 14, 34, 17, 5, 29, 347, 56, 16, 22, 782, 25, 35];
max_count = max(count);
% 1) conversion of GPS coordinates to NED coordinates
% GPS coordinates to be converted
disp(count(1));
x_ned_poly = [];
x_ned_poly_x = [];
x_ned_poly_y = [];
matrix_poly_coord = [];
polygon = [];
disp(length(count))
% 1) conversion of GPS coordinates to NED coordinates
matrix_coord = csvread('output.csv');
%count_coord = csvread('number.csv');
disp(matrix_coord(1,2))
% GPS coordinates to be converted
counter = count(x);
%fid = fopen('MyFile.txt', 'a');
for n = 1:length(matrix_coord)
    
    x_lla = [matrix_coord(n,2) * (pi/180); matrix_coord(n,1) * (pi/180)]; % phi (rad); lambda (rad)
    x_ecef = lla2ecef([x_lla(1); x_lla(2); 0]);
    x_ned = ecef2ned(ned_orig, x_ecef); % cartesian coordinates in NED coordinate system
    %x_ned = ecef2ned2(ned_orig, x_ecef); % cartesian coordinates in NED coordinate system
    
    %disp(x_ned(1));    
    x_ned_poly_x = [x_ned_poly_x;x_ned(1)];
    x_ned_poly_y = [x_ned_poly_y;x_ned(2)];
    %disp(x_ned(1))
    %polygon = str2num('Polygon'+counter);
    x_ned_poly   = [x_ned_poly,x_ned(1) x_ned(2)];
    if (mod(n,counter) == 0)
        %disp(x_ned_poly(1));
        %disp(x_ned_poly(2));
        axis([0 160000 0 160000])        
        plot(x_ned_poly_y, x_ned_poly_x);
        %plot([x_ned_poly(1),x_ned_poly(4),x_ned_poly(7),x_ned_poly(10),x_ned_poly(13),x_ned_poly(16),x_ned_poly(19),x_ned_poly(22),x_ned_poly(25),x_ned_poly(28),x_ned_poly(31),x_ned_poly(34),x_ned_poly(37),x_ned_poly(40),x_ned_poly(43),x_ned_poly(46),x_ned_poly(49),x_ned_poly(52),x_ned_poly(55),x_ned_poly(58),x_ned_poly(61)],[x_ned_poly(2),x_ned_poly(5),x_ned_poly(8),x_ned_poly(11),x_ned_poly(14),x_ned_poly(17),x_ned_poly(20),x_ned_poly(23),x_ned_poly(26),x_ned_poly(29),x_ned_poly(32),x_ned_poly(35),x_ned_poly(38),x_ned_poly(41),x_ned_poly(44),x_ned_poly(47),x_ned_poly(50),x_ned_poly(53),x_ned_poly(56),x_ned_poly(59),x_ned_poly(62)]);
        hold on
        %fprintf(fid, '%f \n \n', x_ned_poly);
        dlmwrite('fileName.csv',x_ned_poly,'-append')
%       matrix_poly_coord = [matrix_poly_coord;x_ned_poly];
        x_ned_poly = [];
        x_ned_poly_x = [];
        x_ned_poly_y = [];
        if (x ~= length(count))
            x = x + 1;
            counter = n + count(x);
        end    
     end 
end
%fclose(fid);
%csvwrite('csvlist.csv',matrix_poly_coord);


%x_lla = [26.017025 * (pi/180); -80.120411 * (pi/180)]; % phi (rad); lambda (rad)

%x_ecef = lla2ecef([x_lla(1); x_lla(2); 0]);
%x_ned = ecef2ned(ned_orig, x_ecef) % cartesian coordinates in NED coordinate system

% 2) conversion of NED coordinates to GPS coordinates

% NED coordinates to be converted
%x_ned = [100 175 0]';
%--
%x_ecef = ned2ecef(ned_orig, x_ned);
%x_lla = ecef2lla(x_ecef);
%phi = x_lla(1) * (180/pi)
%lambda = x_lla(2) * (180/pi)
%