class Estudiante:
    def __init__(self, id, nombre, edad, correo, materias=None):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.correo = correo
        self.materias = materias or {}

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "edad": self.edad,
            "correo": self.correo,
            "materias": self.materias
        }

    @staticmethod
    def from_dict(data):
        return Estudiante(
            id=data['id'],
            nombre=data['nombre'],
            edad=data['edad'],
            correo=data['correo'],
            materias=data.get('materias', {})
        )
