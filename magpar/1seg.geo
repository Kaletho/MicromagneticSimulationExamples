General.Verbosity = 4; // Default 5

// all units in nanometers

L1 = 200;
D1 = 75; R1 = 0.5*D1;

// Mesh characteristics

lc = 1.7;
Mesh.CharacteristicLengthMax = lc+0.1;
Mesh.CharacteristicLengthMin = lc-0.1;
Mesh.CharacteristicLengthExtendFromBoundary = 0;

Mesh.Smoothing = 100;
Mesh.Optimize = 1;
Mesh.OptimizeNetgen = 1;

// If "Cannot find vertex" error, change 2D meshing algorithm
Mesh.Algorithm = 5; // Delaunay
Mesh.Algorithm3D = 5; // Frontal 

// 'Positive' cylinder (cylinder 1)

Point(1) = {0 , 0, 0, lc};
Point(2) = {R1 , 0, 0, lc};
Point(3) = {0 , R1, 0, lc};
Point(4) = {-R1, 0, 0, lc};
Point(5) = {0, -R1, 0, lc};

Circle(1) = {2,1,3};
Circle(2) = {3,1,4};
Circle(3) = {4,1,5};
Circle(4) = {5,1,2};

Line Loop(5) = {1,2,3,4};
Plane Surface(6) = {5};

out1[] = Extrude {0,0,L1} {
   Surface{6};
   Layers{L1/lc};
//   Recombine;
};

Physical Volume (1) = {out1[]};


