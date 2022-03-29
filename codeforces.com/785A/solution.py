number_of_polyhedrons = int(input())

polyhedrons_faces = {
    'Tetrahedron': 4,
    'Cube': 6,
    'Octahedron': 8,
    'Dodecahedron': 12,
    'Icosahedron': 20
}

print(sum([polyhedrons_faces.get(input()) for i in range(number_of_polyhedrons)]))
