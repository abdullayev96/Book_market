from django.db import models
from django.contrib.auth import settings




class BaseModel(models.Model):
      created_at  = models.DateTimeField(auto_now_add=True, verbose_name="Ochilgan vaqti")
      update_at   = models.DateField(auto_now=True, verbose_name="Ozgargan vaqti")

      class Meta:
          abstract = True




class Category(BaseModel):
      name = models.CharField(max_length=400)

      def __str__(self):
          return self.name



class Author(BaseModel):
      full_name = models.CharField(max_length=40, verbose_name="Author ni ismi ")
      bio = models.TextField()

      def __str__(self):
          return self.full_name

      class Meta:
          verbose_name = "Muallif"
          verbose_name_plural = "Mualliflar"



class Book(BaseModel):
      name = models.CharField(max_length=50, verbose_name="Kitobni nomi")
      image = models.ImageField(upload_to="book/")
      title= models.TextField()
      price  = models.IntegerField()
      price1 = models.IntegerField()
      author  = models.ForeignKey(Author, on_delete=models.CASCADE)
      category  = models.ForeignKey(Category, on_delete=models.CASCADE)


      def __str__(self):
          return f'{self.name} || {self.author}'

      class Meta:
          verbose_name = "Kitob"
          verbose_name_plural = "Kitoblar"


class BlogImage(models.Model):
      image = models.ImageField(max_length=30)



class Blog(BaseModel):
      name= models.CharField(max_length=50, verbose_name="Blog nomi")
      title = models.TextField()
      images = models.ManyToManyField(BlogImage, related_name='images')


      def __str__(self):
          return self.name

      class Meta:
          verbose_name = "Yangilik"
          verbose_name_plural = "Yangiliklar"



class DiscountImage(models.Model):
      image = models.ImageField(upload_to='cher/')



class  Discount(BaseModel):
       discount= models.CharField(max_length=300, verbose_name="Chegirma narxi")
       images = models.ManyToManyField(DiscountImage, related_name='images')
       price = models.IntegerField()
       title = models.TextField()


       def __str__(self):
           return str(self.discount)

       class Meta:
                 verbose_name = "Chegirma"
                 verbose_name_plural = "Chegirmalar"




