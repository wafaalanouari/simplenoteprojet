from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=200) # ce qui signifie qu'il stocke du texte avec une longueur
    # maximale de 200 caractères. 
    # Ce champ est utilisé pour stocker le titre de la note.
    content = models.TextField() #ce qui signifie qu'il peut stocker un grand volume de texte. 
    #Ce champ est utilisé pour stocker le contenu de la note.
    created_at = models.DateTimeField(auto_now_add=True)# Le paramètre auto_now_add=True indique que la date 
    #et l'heure actuelles seront automatiquement ajoutées lors de la création d'une 
    #nouvelle note. Ce champ est utilisé pour enregistrer la date et l'heure de création de la note
    updated_at = models.DateTimeField(auto_now=True)#signifie que la date et l'heure actuelles seront automatiquement 
    #mises à jour chaque fois que la note est modifiée. Ce champ
    #est utilisé pour enregistrer la date et l'heure de la dernière mise à jour de la note.
    tags = models.CharField(max_length=200, blank=True) #Ce champ est utilisé pour stocker des tags ou des
    #étiquettes associés à la note pour faciliter l'organisation et la recherche.
  

    def __str__(self):
        return self.title
