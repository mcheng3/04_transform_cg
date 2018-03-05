from display import *
from draw import *
from parser import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()

#print_matrix(make_translate(3, 12, -3))
parse_file( 'script', edges, transform, screen, color )
#display(edges)