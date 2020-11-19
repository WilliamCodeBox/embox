import pygmsh as msh


def poly():
    with msh.geo.Geometry() as geo:
        geo.add_polygon(
            [
                [0.0, 0.0],
                [1.0, -0.2],
                [1.1, 1.2],
                [0.1, 0.7]
            ],
            mesh_size=0.1
        )
        mesh = geo.generate_mesh()

        for c in mesh.cells:
            print(c.data)


def bspline():
    with msh.geo.Geometry() as geo:
        lcar = 0.1

        p1 = geo.add_point([0.0, 0.0], lcar)
        p2 = geo.add_point([1.0, 0.0], lcar)
        p3 = geo.add_point([1.0, 0.5], lcar)
        p4 = geo.add_point([1.0, 1.0], lcar)
        s1 = geo.add_bspline([p1, p2, p3, p4])
        geo.set_transfinite_curve()
        mesh = geo.generate_mesh()
        print(mesh.points)

def occ():
    with msh.occ.Geometry() as geo:
        geo.characteristic_length_max = 0.1
        r = 0.5


if __name__ == '__main__':
    bspline()
