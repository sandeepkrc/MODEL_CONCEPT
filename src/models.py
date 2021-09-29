from django.db import models


# #MANY TO MANY RELATIONSHIP

# class Publication(models.Model):
#RAJ.SANDIP96@GMAIL.COM
#     title = models.CharField(max_length=200)
#     class Meta:
#         ordering = ['title']   
#     def __str__(self):
#         return self.title
    
    
# class Article(models.Model):
#RAJ.SANDIP96@GMAIL.COM
#     headline = models.CharField(max_length=100)
#     publications = models.ManyToManyField(Publication)
    
#     class Meta:
#         ordering = ['headline']
#     def __str__(self):
#         return self.headline
    
#     #MANY TO ONE OR FOREIGNKEY CONCEPTS
# class Reporter(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     email = models.EmailField()

#     def __str__(self):
#         return "%s %s" % (self.first_name, self.last_name)
# #ARTICLE 
# class Art(models.Model):
#     headline = models.CharField(max_length=100)
#     pub_date = models.DateField()
#     reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
#RAJ.SANDIP96@GMAIL.COM
#     def __str__(self):
#         return self.headline

#     class Meta:
#         ordering = ['headline']