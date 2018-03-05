from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix - 
        takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
     ident: set the transform matrix to the identity matrix - 
     scale: create a scale matrix, 
        then multiply the transform matrix by the scale matrix - 
        takes 3 arguments (sx, sy, sz)
     move: create a translation matrix, 
        then multiply the transform matrix by the translation matrix - 
        takes 3 arguments (tx, ty, tz)
     rotate: create a rotation matrix,
        then multiply the transform matrix by the rotation matrix -
        takes 2 arguments (axis, theta) axis should be x, y or z
     apply: apply the current transformation matrix to the 
        edge matrix
     display: draw the lines of the edge matrix to the screen
        display the screen
     save: draw the lines of the edge matrix to the screen
        save the screen to a file -
        takes 1 argument (file name)
     quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
    f = open(fname, "r")
    while True:
        cmd = f.readline()
        if cmd == "quit":
            break
        cmd = cmd[:cmd.find('\n')]
        #print cmd
        if cmd == "quit" or cmd == "":
            break
        elif cmd == "line":
            e = f.readline().split()
            add_edge(points, int(e[0]), int(e[1]), int(e[2]), int(e[3]), int(e[4]), int(e[5]))
            #print_matrix(points)
        elif cmd == "ident":
            ident(transform)
        elif cmd == "scale":
            e = f.readline().split()
            matrix_mult(make_scale(int(e[0]), int(e[1]), int(e[2])),transform)
            #print_matrix(transform)
        elif cmd == "move":
            e = f.readline().split()
            matrix_mult(make_translate(int(e[0]), int(e[1]), int(e[2])),transform)
        elif cmd == "rotate":
            e = f.readline().split()
            if e[0] == "x":
                matrix_mult(make_rotX(int(e[1])), transform)
                #print_matrix(transform)
            elif e[0] == "y":
                matrix_mult(make_rotY(int(e[1])), transform)
            elif e[0] == "z":
                matrix_mult(make_rotZ(int(e[1])), transform)
                #print_matrix(transform)
        elif cmd == "apply":
            matrix_mult(transform, points)
        elif cmd == "display":
            #print "display"
            clear_screen(screen)
            draw_lines(points, screen, color)
            display(screen)       
        elif cmd == "save":
            name = f.readline()
            save_extension(screen, name[:name.find('\n')])
    print "quit"
        
