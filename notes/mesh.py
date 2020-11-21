import math
import os
import sys

import gmsh
import pygmsh as msh


def gmsh_usage():
    geo = gmsh.model.occ()
    p1 = geo.addPoint(0.0, 0.0, 0.0, 0.1)
    p2 = geo.addPoint(0.0, 0.0, 1.0, 0.1)
    tag = geo.addLine(p1, p2)
    mesh = geo.mesh()


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


def gmsh_spline():
    import gmsh
    import math
    import sys

    gmsh.initialize()

    gmsh.model.add("spline")

    for i in range(1, 11):
        gmsh.model.occ.addPoint(i, math.sin(i / 9. * 2. * math.pi), 0, 0.1, i)

    gmsh.model.occ.addSpline(range(1, 11), 1)
    gmsh.model.occ.addBSpline(range(1, 11), 2)
    gmsh.model.occ.addBezier(range(1, 11), 3)

    gmsh.model.occ.addPoint(0.2, -1.6, 0, 0.1, 101)
    gmsh.model.occ.addPoint(1.2, -1.6, 0, 0.1, 102)
    gmsh.model.occ.addPoint(1.2, -1.1, 0, 0.1, 103)
    gmsh.model.occ.addPoint(0.3, -1.1, 0, 0.1, 104)
    gmsh.model.occ.addPoint(0.7, -1, 0, 0.1, 105)

    # periodic bspline through the control points
    gmsh.model.occ.addSpline([103, 102, 101, 104, 105, 103], 100)

    # periodic bspline from given control points and default parameters - will
    # create a new vertex
    gmsh.model.occ.addBSpline([103, 102, 101, 104, 105, 103], 101)

    # general bspline with explicit degree, knots and multiplicities
    gmsh.model.occ.addPoint(0, -2, 0, 0.1, 201)
    gmsh.model.occ.addPoint(1, -2, 0, 0.1, 202)
    gmsh.model.occ.addPoint(1, -3, 0, 0.1, 203)
    gmsh.model.occ.addPoint(0, -3, 0, 0.1, 204)
    gmsh.model.occ.addBSpline([201, 202, 203, 204], 200, 2, [], [0, 0.5, 1],
                              [3, 1, 3])

    gmsh.model.occ.synchronize()
    if '-nopopup' not in sys.argv:
        gmsh.fltk.run()
    gmsh.finalize()


def gmsh_glue_remesh_stl():
    gmsh.initialize()

    # load two STL surfaces
    path = os.path.dirname(os.path.abspath(__file__))
    gmsh.merge(os.path.join(path, 'models/surface1.stl'))
    gmsh.merge(os.path.join(path, 'models/surface2.stl'))

    # merge nodes that are at the same position up to some tol
    gmsh.option.setNumber('Geometry.Tolerance', 1e-4)
    gmsh.model.mesh.removeDuplicateNodes()

    # classify surface mesh according to given angle, and create discrete model
    # entities (surfaces, curves and points) accordingly
    gmsh.model.mesh.classifySurfaces(math.pi / 2)

    # Notes:
    #
    # - for more complicated surfaces `forReparametrization=True` could be specified
    # to force the creation of reparametrizable patches
    #
    # - in this simple case, since the two surfaces were simple and already colored,
    # one could have also simply used `gmsh.model.mesh.createTopology()` instead of
    # `gmsh.model.mesh.classifySurfaces()`

    # create a geometry for the discrete curves and surfaces (comment this if you
    # don't want to remesh the surfaces and simply use the original mesh)
    gmsh.model.mesh.createGeometry()

    # get all the surfaces in the model
    s = gmsh.model.getEntities(2)

    # create a surface loop and a volume from these surfaces
    l = gmsh.model.geo.addSurfaceLoop([s[i][1] for i in range(len(s))])
    gmsh.model.geo.addVolume([l])

    # synchronize the new volume with the model
    gmsh.model.geo.synchronize()

    # mesh
    gmsh.option.setNumber("Mesh.Algorithm", 6)
    gmsh.option.setNumber("Mesh.MeshSizeMin", 0.4)
    gmsh.option.setNumber("Mesh.MeshSizeMax", 0.4)
    gmsh.model.mesh.generate(3)

    if '-nopopup' not in sys.argv:
        gmsh.fltk.run()
    gmsh.finalize()


if __name__ == '__main__':
    gmsh_glue_remesh_stl()
