from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from django.dispatch import receiver
import datetime
from django.utils import timezone



class BaseInfo(models.Model):
    name=models.CharField('Site name',max_length=20)
    phone=PhoneNumberField('Phone',max_length=12,blank=True)
    emailname=models.EmailField('Email Name')
    emaillink=models.URLField("Email url",null=True)
    facebook=models.URLField('Facebook link',blank=True)
    telegram=models.URLField('Telegram link',blank=True)
    instagram=models.URLField('Instagram link',blank=True)
    main_icon=models.ImageField('Kayqi Nkar',upload_to='icons_imagers')


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name='Main Information'
        verbose_name_plural='Main Information'


class HomeCarousel(models.Model):
    name=models.CharField('Կայքի անվանում',max_length=50)
    shortinfo=models.TextField('Կարճ տեղեկություն')
    longinfo=models.TextField('ամբողջական տեղեկություն')
    img=models.ImageField('Imagers',upload_to='carousel media')


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name='Carousel'
        verbose_name_plural='Carousel'
        ordering=['?']

class Category(models.Model):
    name=models.CharField('Ապրանքի տեսակ',max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name='Category'
        verbose_name_plural='Categories'
        ordering=['?']

    

class UserInfos(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    main_icon=models.ImageField('User icon',upload_to='icons_imagers')
    emailname=models.EmailField('Email Name',null=True)
    emaillink=models.URLField("Email url",null=True)
    facebook=models.URLField('Facebook link',blank=True)
    telegram=models.URLField('Telegram link',blank=True)
    instagram=models.URLField('Instagram link',blank=True)

    def __str__(self):
        return f'{self.user}'
    
    class Meta:
        verbose_name='Superuser'
        verbose_name_plural='Superusers'
    

class AllProductModel(models.Model):
    user=models.ForeignKey(UserInfos,on_delete=models.CASCADE,related_name='only')
    cate=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='productr')
    img=models.ImageField('Գլխավոր նկար',upload_to='products imagers')
    img1=models.ImageField('Նկար ',upload_to='products imagers',null=True)
    img2=models.ImageField('Նկար ',upload_to='products imagers',null=True)
    name=models.CharField('Անվանում',max_length=100)
    price_old=models.IntegerField('Գին')
    price_now=models.IntegerField('Գինը զեղջված',default=0)
    dt=models.DateField(auto_now_add=True,null=True)
    info=models.TextField('Տեղեկություն',null=True,max_length=250)
    dissave=models.BooleanField(default=True,null=True)
    email=models.EmailField('email',null=True)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name='Ապրանք'
        verbose_name_plural='Ապրանքներ'
        ordering=['-id']




class Saved(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    prouduct=models.ForeignKey(AllProductModel,on_delete=models.CASCADE,related_name='saver')



class ReviewModel(models.Model):
    product = models.ForeignKey(AllProductModel, on_delete=models.CASCADE, related_name='commentr')
    name = models.CharField('name', max_length=50)
    surname = models.CharField('surname', max_length=50)
    comment = models.TextField('Comment')
    img = models.ImageField('imagers', upload_to='comment_imagers')
    rate=models.IntegerField('rate',null=True)
    datenow=models.DateField(auto_now_add=True,blank=True)




    def __str__(self):
        return f'{self.name} {self.surname}'


class ContactUsModel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField('name',max_length=50)
    email=models.EmailField('Email')
    subject=models.TextField('Subject')
    message=models.TextField('Message')

    def __str__(self):
        return f'{self.user} {self.name} {self.email}'



class Ordering(models.Model):
    product=models.ForeignKey(AllProductModel,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField('name',max_length=50)
    phone=PhoneNumberField('phone')

    def __str__(self):
        return f'{self.name} {self.phone} {self.user}'




class AboutShop(models.Model):
    secure=models.TextField('Գաղտնիության քաղաքականություն')
    offset=models.TextField('փոխհատուցման քաղաքականություն')
    pay=models.TextField('Վճարման համակարգ')
    infos=models.TextField('Ընկերության տվյալներ')
    place=models.TextField('Գտնվելու վայրը')
    connect=models.TextField('Ինչպես միանալ')


class Govazd(models.Model):
    name=models.CharField('Սեղեկություններ', max_length=50)
    img=models.ImageField('Նկար',upload_to='govazd')

    def __str__(self) -> str:
        return self.name
    
