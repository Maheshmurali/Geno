# ivedae undakkunna model adminil register cheyyanam 
# dbyil varan terminalil  model undakki kazhinj python manage.py makemigrations athukazhinj python manage.py migrate adikkanam
from django.db import models

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
