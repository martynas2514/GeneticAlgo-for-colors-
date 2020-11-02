# Genetic algorithm for Colors

this is genetic algorithm to generate color in x,y,z, which simbolise RGB color standart. where 0 < x,y,z < 255

## methods
 main method is colorGen(color, n, rate)
 * color - tuple of (x , y z) where 0 < x,y,z < 255
 * n - number of generations
 * rate - probability of generating random value where  0 < rate < 1

## example:
color = (10,10,10)

colorGen(color, 500, 0.2)

output:
Color: (10, 10, 10) SSE: 0.0
