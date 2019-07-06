from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    publicationdate = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

        #here db str ko call karega so jo name hai blog post ke ,so usi name se store hongs db mein instead of the object1,objct2

    def summary(self):
        return self.body[:100]



    def pub_date_pretty(self):
        return self.publicationdate.strftime('%b %e %Y')    