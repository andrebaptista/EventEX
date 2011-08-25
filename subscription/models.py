#*-* coding: utf-8 *-*
from django.db import models

class Subscription(models.Model):
    name = models.CharField(u"Nome", max_length=150)
    email = models.EmailField(verbose_name=u"E-mail", unique=True)
    cpf = models.CharField(u"CPF", max_length=14, unique=True)
    phone = models.CharField(u"Telefone", max_length=14)
    created_at = models.DateTimeField(verbose_name=u"Criado em", auto_now_add=True)
    
    class Meta:
        verbose_name = u"Inscrição"
	verbose_name_plural = u"Inscrições"

    def __unicode__(self):
	return u"%s - %s" % (self.name, self.email)
