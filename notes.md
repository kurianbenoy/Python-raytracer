## Ray Tracing Tutorial

Arun Ravindran mentioned the challenges of using Python:

1. Like using Data Structures like - dict, classes, slots
2. Need to use shallow OOPS
3. Automatic int to float conversions.
4. The python is slow when using for CPU intensive(it's too slow)

## Episode 3

We need to have a sphere, draw
and render 3D balls from 2D image.

Requirement render a 3D red ball without shading
Ray sphere intersection formula. 

In this problem, we need to have a Ray to be used. The sphere
will always intersect  with a Ray.

sphere_to_ray = ray origin - sphere_center

On intersecting with Ray-sphere intersection, there are three cases:

a = 1
b = 2 * RAY direction * sphere_to_ray
c = sphere_to_ray * sphere_to_ray - (sphere_center^2)

discriminat = b^2 - 4*c

## Hit Position

ray(t) = ray(origin) + ray(direction) * dist
Aspect ratio(if rays of wrongly calculated) my 1920*1080
shopping off y-coordinate and then x-coordinate
Rendering sphere with 320 by 200 image, because it's commodoro resolution
camera positon: (0, 0, -1)
ball positon: (0, 0, 0) & 0.5

calculate the aspect ratio. Ray tracing is usually orbited in positive
axis, than in original axis.

Aspect ratio = width/height

## Episode 4

Our object in video 4 is to make the red ball which was in 2D shape,
with use of lambard shading + other theory to create a 3D shape
make it look with shading.

Color(surface) = L.N.M(diffuse).C(object)

Diffused shading model. The coefficent is adjusted based on color of objects

The color can be either seen in a bright way, or in a diminished way. The 
diffused components is something which is added at end of code

*Spectular Shading* - Reflections from tiny shots.Bling phong shading model

Phong shading model

Phong term is (V.R) ^ k

V is ray towards viewer, R is rays towards display. The main issue, the angle can
be fine it can reach above 90 degrees.

Phong-bing modification => H = L + V
                            & H = norm(H)

## Episode 5

The lesson talks about how we can get a tile and wonderful implementation of spheres.
The ray tracer programming is now having tiles and two spheres.

The light is also coming from two direction, with two balls and reflection
of sphere in mat surface. We are using python module to describe a scene and import in main program

The various examples of  Python as a config file is there in lot of projects like;

settings.py - Django
SetupTools - setup.py
Fabric - fabricfile
Ipython - ipython_config.py

## Episode 6