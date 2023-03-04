# Circular Maze Algorithm Notes

## Parameters
- Path count (how many circular path maze contains, determines the size of the maze)
- Difficulty Easy/Medium/Hard (determines fake paths & obstacle wall amount)

## Build Parameters
- The thickness of the walls will be 0.1, offset will be 0
- All wall length will be 0.5
- The thickness of floor object will be 0.2
- Vertices of the floor object = (path count * 15)

## Algorithm Implementation

1. Create a floor cylinder object by considering radius unit. The equation is r = path count + 0.5
2. Create slices (slice size = path count) and rings for the floor object (circle = path count)
3. Create another slice with size of 0.5. This will represent initial position of the ball and this part will be same for all mazes.
4. Extrude walls for all rings and separate them from floor object
5. Thicken all the walls by adding Solidify component
6. Cut appropriate number of vertices for the first cylinder wall (starting from 45° to 135°)
_Until 6th point, the process will be the same for all maze type._

7. For ball to pass between circular paths, appropriate number of vertices will be cut. The length of cut will have size of X that is constant in all parts of the maze. Count of cuts for ball pass will increase for greater ring walls. 
8. Initially, the escape path should be determined before other cuts are made. To do that, each ring wall is cut from a single place. 
9. Then, to prevent to get inside the escape path, the circular path should be blocked with flat walls. There should be single way to go through the escape path. Those flat walls prevent to go along the circular path. They face exactly perpendicular to the center of the maze.  
10. _The implementation until this point is the first and easy half of the add-on._ 






