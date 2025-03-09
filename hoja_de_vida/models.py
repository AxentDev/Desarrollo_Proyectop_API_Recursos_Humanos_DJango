from django.db import models

# Información personal
class PersonalInformation(models.Model):
    nombre_completo = models.CharField(max_length=200)
    direccion = models.CharField(max_length=250)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.nombre_completo

# Perfil profesional
class ProfessionalProfile(models.Model):
    perfil = models.OneToOneField(PersonalInformation, on_delete=models.CASCADE)
    descripcion = models.TextField()

    def __str__(self):
        return f"Perfil de {self.perfil.nombre_completo}"

# Educación
class Education(models.Model):
    perfil = models.ForeignKey(PersonalInformation, related_name='education', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    institucion = models.CharField(max_length=150)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return f"{self.titulo} en {self.institucion}"

# Experiencia laboral
class WorkExperience(models.Model):
    perfil = models.ForeignKey(PersonalInformation, related_name='work_experience', on_delete=models.CASCADE)
    puesto = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    responsabilidades = models.TextField()

    def __str__(self):
        return f"{self.puesto} en {self.empresa}"

# Rasgos de personalidad
class PersonalityTraits(models.Model):
    trait_name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.trait_name

# Idiomas
class Languages(models.Model):
    language_name = models.CharField(max_length=100)
    proficiency = models.CharField(max_length=50)

    def __str__(self):
        return self.language_name

# Habilidades
class Skills(models.Model):
    skill_name = models.CharField(max_length=100)
    proficiency = models.CharField(max_length=50)

    def __str__(self):
        return self.skill_name

# Proyectos destacados
class FeaturedProjects(models.Model):
    perfil = models.ForeignKey(PersonalInformation, related_name='featured_projects', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.titulo

# Logros clave
class KeyAchievements(models.Model):
    perfil = models.ForeignKey(PersonalInformation, related_name='key_achievements', on_delete=models.CASCADE)
    logro = models.TextField()

    def __str__(self):
        return self.logro[:50]  # Muestra los primeros 50 caracteres

# Referencias
class References(models.Model):
    perfil = models.ForeignKey(PersonalInformation, related_name='references', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    relacion = models.CharField(max_length=50)  # Ejemplo: Jefe, Colega
    contacto = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} ({self.relacion})"

# Propuesta de valor
class ValueProposition(models.Model):
    perfil = models.OneToOneField(PersonalInformation, on_delete=models.CASCADE)
    propuesta = models.TextField()

    def __str__(self):
        return f"Propuesta de valor de {self.perfil.nombre_completo}"


