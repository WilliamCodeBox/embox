import pygmsh as msh

def meshio_logo():
    geo = msh.occ.Geometry()
    container = geo.add_rectangle([0.0, 0.0, 0.0], 10.0, 10.0)
    letter_i = geo.add_rectangle([2.0, 2.0, 0.0], 1.0, 4.5)
    i_dot = geo.add_disk([2.5, 7.5, 0.0], 0.6)

    disk1 = geo.add_disk([6.25, 4.5, 0.0], 2.5)
    disk2 = geo.add_disk([6.25, 4.5, 0.0], 1.5)

    letter_o = geo.boolean_difference(disk1, disk2)

    geo.boolean_difference(container, geo.boolean_union([letter_i, letter_o, i_dot]))

    mesh = geo.generate_mesh()
    ref = 81.9131851877
    assert abs(compute_volume(mesh) - ref) < 1.0E-2 * ref
    return mesh

def compute_volume()