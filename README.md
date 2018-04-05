# SimpleMazeSolver
Program that takes a .txt file with a maze (built of # and _ characters) and finds a path through.

Maze needs to be in the following general format:
```
###_###  
#_____#  
#_##_##  
#_##__#  
#_#####  
#_#####  
```
With the Entrance and Exit being the Top and Bottom exits, respectively (top = Entrance, bottom = Exit).

Path must be made of underscores ("\_") or change the 'PATH' variable to PATH = " " instead of PATH = "\_"

Walls can be anything.

Also goes through the alphabet from exit -> start in ascending order (a->z then loops back around)
