# GofL
Command line implementation for Conway's Game of Life

**birth** - 3 neighbors  
**survival** to the next step - 2 or 3 neighbors  
**death** from overpopulation - 4 neighbors  
**death** from loneliness - 1 or less neighbors   

# Install
pip install -r requirements.txt

# How to run:

Run 20 by 20 field with 40% live cells for 3 iterations with out putting in-line animation at 0.5 sec per frame.
```
python life.py -s 20 -d 40 -fd 0.5 -i 3
```
Help  
```
python life.py -h
```

```
usage: life.py [-h] [-s SIZE] [-d CELL_DENSITY] [-na] [-fd FDELAY] [-i ITERS]
               [-rn RNSEED]

optional arguments:
  -h, --help            show this help message and exit
  -s SIZE, --size SIZE  size of square game field
  -d CELL_DENSITY, --cell_density CELL_DENSITY
                        percent of live cells at start
  -na, --noanimation    run without command line animation
  -fd FDELAY, --fdelay FDELAY
                        animation frame delay
  -i ITERS, --iters ITERS
                        number of game repeats
  -rn RNSEED, --rnseed RNSEED
                        select random seed to start

```
Limits for arguments  
```
'size': (2, 51),
'cell_density': (10, 90),
'fdelay': (0.1, 1),
'iters': (1, 1001),
'rnseed':(0, 1000)
```

# References
https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
