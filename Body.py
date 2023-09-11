import bpy
import math
import mathutils

# Clear existing mesh objects
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.delete()

# Parameters for the bearing
outer_radius = 2.0
inner_radius = 1.0
ball_radius = 0.2
num_balls = 18

# Create the outer ring
bpy.ops.mesh.primitive_cylinder_add(radius=outer_radius, depth=0.2)
outer_ring = bpy.context.object

# Create the inner ring
bpy.ops.mesh.primitive_cylinder_add(radius=inner_radius, depth=0.2)
inner_ring = bpy.context.object

# Position the inner ring
inner_ring.location = (0, 0, 0.1)  # Adjust the Z coordinate as needed

# Create the balls
balls = []
for i in range(num_balls):
    angle = (2 * math.pi * i) / num_balls
    x = inner_radius * math.cos(angle)
    y = inner_radius * math.sin(angle)
    z = 0.1  # Adjust the Z coordinate as needed
    bpy.ops.mesh.primitive_uv_sphere_add(radius=ball_radius, location=(x, y, z))
    ball = bpy.context.object
    balls.append(ball)

# Parent the balls to the inner ring
for ball in balls:
    ball.select_set(True)
    bpy.context.view_layer.objects.active = inner_ring
    bpy.ops.object.parent_set(type='OBJECT')

# Set the bearing's material (you can create and assign materials as needed)

# Optionally, add the bearing to a collection
# bpy.data.collections['MyCollection'].objects.link(outer_ring)
