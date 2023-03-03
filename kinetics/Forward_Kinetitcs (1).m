%Parametros del robot 

L1 = 10;
L2 = 10;
L3 = 5;

%Longitud total del brazo 
Ltot = L1 +L2 + L3;

for c = 1: 180 
    X1(c)=Ltot*cos(c*pi/180);
    Y1(c)=Ltot*sin(c*pi/180);
end

% Plot del caso A

figure('Name','Plot caso A')
title('Plot caso A')
plot(X1,Y1);
xlabel('posicion en x ') 
ylabel('posicion en y') 
axis equal

%Longitud de la segunda parte del brazo
Ltot2 = L2+L3;

for c = 1:180
    X2(c)= L1*cos(c*pi/180)+Ltot2*cos(2*c*pi/180);
    Y2(c)= L1*sin(c*pi/180)+Ltot2*sin(2*c*pi/180);
end

% Plot del caso B

figure('Name','Plot caso B')
title('Plot caso B')
plot(X2,Y2);
xlabel('posicion en x ') 
ylabel('posicion en y') 
axis equal
