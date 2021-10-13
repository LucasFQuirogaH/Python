import clases

perfil1 = clases.Persona()
perfil1.setNombre("Lucas")
perfil1.setApellido("Quiroga")
perfil1.setEdad(38)
perfil1.setAltura(1.69)

print (perfil1.getNombre())
print (perfil1.Hablar())

informatico1 = clases.Informatico()
informatico1.setNombre("Juan")
informatico1.setApellido("Salomon")
informatico1.setAltura(1.60)

print(informatico1.getLenguajes())
print(informatico1.getExperiencia())
