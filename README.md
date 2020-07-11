# GofL
Command line implementation for Conway's Game of Life

# Install
pip install -r requirements.txt

# How to run:
```
python life.py -h
```
Output
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
# References
https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
