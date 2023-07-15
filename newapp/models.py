from django.db import models



# Create your models here.

STATUS = (
    ('active','Active'),
    ('deactive','Deactive'),
)


class Information(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField()
    photo = models.ImageField()

    status = models.CharField(max_length=20, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class  Meta:
        verbose_name = 'Biz haqimizda ma\'lumot '
        verbose_name_plural = 'Biz haqimizda ma\'lumotlar'
        ordering = ('-created_at','status')


class Category1(models.Model):
    name = models.CharField(max_length=50)

    status = models.CharField(max_length=20, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class  Meta:
        verbose_name = 'Mahsulot sotish uchun Kategoriya'
        verbose_name_plural = 'Sotish uchun Kategoriyalar'
        ordering = ('-created_at','status')
    
    def __str__(self) -> str:
        return self.name


class Category2(models.Model):
    name = models.CharField(max_length=50)

    status = models.CharField(max_length=20, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class  Meta:
        verbose_name = 'Sotilgan maxsulotlar uchun kategoriya'
        verbose_name_plural = 'Sotilgan maxsulotlar uchun  kategoriyalar'
        ordering = ('-created_at','status')
    
    def __str__(self) -> str:
        return self.name

  
class Statistika(models.Model):
    name = models.CharField(max_length=30)
    number = models.PositiveIntegerField(default=1)

    status = models.CharField(max_length=20, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class  Meta:
        verbose_name = 'statistika'
        ordering = ('-created_at','status')


class Product1(models.Model):
    category1 = models.ForeignKey(Category1, on_delete=models.CASCADE, related_name='product1_category1', verbose_name='Sotish uchun maxsulot kategoriyasi') 

    name = models.CharField(max_length=30)
    body = models.TextField()
    photo = models.ImageField(upload_to='1product_photo/%Y/%m/%d/', verbose_name="Maxsulot rasmi")
    
    status = models.CharField(max_length=20, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class  Meta:
        verbose_name = 'Sotish uchun maxsulot '
        verbose_name_plural = 'Sotish uchun maxsulotlar'
        ordering = ('-created_at','status')
    
    def __str__(self) -> str:
        return self.name
    

class Product2(models.Model):
    category2 = models.ForeignKey(Category2, on_delete=models.CASCADE, related_name='product1_category2', verbose_name='Sotilgan maxsulot kategoriyasi') 

    name = models.CharField(max_length=30)
    body = models.TextField()
    photo = models.ImageField(upload_to='2product_photo/%Y/%m/%d/', verbose_name="Maxsulot rasmi")
    
    status = models.CharField(max_length=20, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class  Meta:
        verbose_name = 'Sotilgan maxsulot '
        verbose_name_plural = 'Sotilgan maxsulotlar'
        ordering = ('-created_at','status')
    
    def __str__(self) -> str:
        return self.name

 
class Partner(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='partner_photo/%Y/%m/%d/', verbose_name="Hamkor rasmi")
    email = models.EmailField(blank=True, null=True)

    
    status = models.CharField(max_length=20, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class  Meta:
        verbose_name = 'Hamkor'
        verbose_name_plural = 'Hamkorlar'
        ordering = ('-created_at','status')
    
    def __str__(self) -> str:
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='team_photo/%Y/%m/%d/', verbose_name="jamoa a'zosining rasmi")
    number = models.CharField(max_length=15,verbose_name="jamoa a'xosining raqami")

    
    status = models.CharField(max_length=20, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class  Meta:
        verbose_name = "Jamoa a'zosi"
        verbose_name_plural = "Jamoa a'zolari"
        ordering = ('-created_at','status')
    
    def __str__(self) -> str:
        return self.name


class Comment(models.Model):
    full_name = models.CharField(max_length=30)
    text = models.TextField()

    status = models.CharField(max_length=20, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class  Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Commentlar"
        ordering = ('-created_at','status')
    
    def __str__(self) -> str:
        return self.full_name
    

class Connection(models.Model):
    full_name = models.CharField(max_length=50)
    number = models.CharField(max_length=15)
    text = models.TextField()

    status = models.CharField(max_length=20, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

