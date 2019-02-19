#!/usr/bin/python
"""
Graham's scan: 
Solves the convex-hull problem by maintaining a stack S
of candidate points. It pushes each point of the input set Q onto the
stack one time, and it eventually pops from the stack each point that 
is not a vertex of CH(Q). When the algorithm terminates, stack S 
contains exactly the vertices of CH(Q), in counterclockwise order of 
their appearance on the boundary.

Algorithm: 
1. Choose point p with the lowest y-coordinate; in case of a tie,
   choose the leftmost point. Since no point is below p, it must
   be a vertex on the convex hull.
2. Sort the remaining points in order of increasing polar angle from p.
   If two or more points have the same polar angle, choose the farthest point.
3. Initialize the stack with anchor point p and the first element in the 
   sorted list.
4. Iterate over each point in the sorted list; each time we find a vertex
   at which we make a nonleft (CW) turn, pop the vertex from the stack (i.e.,
   remove from the convex hull). (Note: by checking for a nonleft turn instead of a right turn, this test
   precludes the possibility of a straiht angle at a vertex.) After popping all
   vertices that have nonleft turns when heading toward point p, push p on to the stack.
"""