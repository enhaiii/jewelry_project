from django.db import models

class Cards(models.Model):
    name = models.CharField('Title', max_length=30)
    requisites = models.CharField('Requisites', unique=True)

    class Meta:
        verbose_name = "Card"
        verbose_name_plural = "Cards"

    def __str__(self):
        return f"{self.name}"

class Clients(models.Model):
    name = models.CharField('Name', max_length=15)
    surname = models.CharField('Surname', max_length=15)
    middle_name = models.CharField('Middle Name', max_length=20)
    nickname = models.CharField('Nickname', max_length=20)
    email = models.EmailField('Email')
    phone_number = models.CharField('Phone number', max_length=15, unique=True)
    birthday = models.DateField('Birthday', blank=True)
    city = models.CharField('City', max_length=25)
    id_cards = models.ForeignKey(Cards, verbose_name='Card', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"

    def __str__(self):
        return f"{self.nickname}"

class Purchases(models.Model):
    img = models.ImageField(upload_to='Jewelry_imgs/', verbose_name='Foto')
    id_clients = models.ForeignKey(Clients, verbose_name='Client', on_delete=models.CASCADE)
    products = models.ManyToManyField('Products')

    class Meta:
        verbose_name = "Purchase"
        verbose_name_plural = "Purchases"

    def __str__(self):
        return f"{self.img}{self.id}"

class Catalogs(models.Model):
    name = models.CharField('Title', max_length=30)

    class Meta:
        verbose_name = "Catalog"
        verbose_name_plural = "Catalogs"

    def __str__(self):
        return f"{self.name}"

class Products(models.Model):
    name = models.CharField('Title', max_length=30)
    img = models.ImageField(upload_to='Jewelry_imgs/', verbose_name='Foto')
    price = models.DecimalField ('Price', max_digits=20, decimal_places=2)
    description = models.CharField('Desription', max_length=300, null=True, default="")
    old_price = models.DecimalField ('Old price', max_digits=20, decimal_places=2, default=45000)
    article = models.CharField('Article', max_length=12, default="000000000000")
    material = models.CharField('Material', max_length=50, default="Gold")
    insert = models.CharField('Insert', max_length=80, null=True)
    country = models.CharField('Country', max_length=64, default="Italy")
    weight = models.DecimalField('Weight', max_digits=5, decimal_places=2, default=2.24)
    catalogs = models.ManyToManyField('Catalogs')

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return f"{self.id}" f"{self.name}"

class Orders(models.Model):
    ST = [
        ("Being issued" , "Being issued"),
        ("On the way", "On the way"),
        ("At the pick-up point", "At the pick-up point")
    ]
    total_amount = models.DecimalField ('Final price', max_digits=20, decimal_places=2)
    id_clients = models.ForeignKey(Clients, verbose_name='Client', on_delete=models.CASCADE)
    status = models.CharField('Status', max_length=1020, choices=ST)
    address = models.CharField('Address', max_length=25)
    payment = models.ForeignKey(Cards, verbose_name='Payment', on_delete=models.CASCADE)
    products = models.ManyToManyField('Products')

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return f"{self.id}"