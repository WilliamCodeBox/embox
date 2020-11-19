import pygmsh as msh

def meshio_logo():
    geo = msh.occ.Geometry()
    container = geo.add_rectangle([0.0, 0.0, 0.0], 10.0, 10.0)
    letter_i = geo.add_rectangle([2.0, 2.0, 0.0], 1.0, 4.5)
    i_dot = geo.add_disk([2.5, 7.5, 0.0], 0.6)
