from django.db import models

class Cards(models.Model):
    name = models.CharField('Название', max_length=30)
    requisites = models.CharField('Реквезиты', unique=True)

    class Meta:
        verbose_name = "Карта"
        verbose_name_plural = "Карты"

    def __str__(self):
        return f"{self.name}"

class Clients(models.Model):
    name = models.CharField('Имя', max_length=15)
    surname = models.CharField('Фамилия', max_length=15)
    middle_name = models.CharField('Отчество', max_length=20)
    nik = models.CharField('Ник', max_length=20)
    email = models.EmailField('Email')
    phone_number = models.CharField('Номер телефона', max_length=12, unique=True)
    birthday = models.DateField('Дата рождения', blank=True)
    city = models.CharField('Город', max_length=25)
    id_cards = models.ForeignKey(Cards, verbose_name='Карта', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    def __str__(self):
        return f"{self.nik}"

class Purchases(models.Model):
    name = models.CharField('Название', max_length=30)
    img = models.CharField('Товар', max_length=60)
    id_clients = models.ForeignKey(Clients, verbose_name='Клиент', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Покупка"
        verbose_name_plural = "Покупки"

    def __str__(self):
        return f"{self.img}{self.name}"

class Catalogs(models.Model):
    name = models.CharField('Название', max_length=30)

    class Meta:
        verbose_name = "Каталог"
        verbose_name_plural = "Каталоги"

    def __str__(self):
        return f"{self.name}"

class Products(models.Model):
    name = models.CharField('Название', max_length=30)
    img = models.CharField('Товар', max_length=60)
    price = models.DecimalField ('Цена', max_digits=20, decimal_places=2)
    description = models.TextField('Описание', max_length=150)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return f"{self.img}{self.name}"

class Products_catalogs(models.Model):
    id_products = models.ForeignKey(Products, verbose_name='Товар', on_delete=models.CASCADE)
    id_catalogs = models.ForeignKey(Catalogs, verbose_name='Каталог', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Товар в каталоге"
        verbose_name_plural = "Товары в каталогах"

    def __str__(self):
        return f"{self.id}"

class Special_offers(models.Model):
    id_products = models.ForeignKey(Products, verbose_name='Товар', on_delete=models.CASCADE)
    description = models.TextField('Описание', max_length=300)

    class Meta:
        verbose_name = "Специальное предложение"
        verbose_name_plural = "Специальные предложения"

    def __str__(self):
        return f"{self.id}"

class Products_purchases(models.Model):
    id_products = models.ForeignKey(Products, verbose_name='Товар', on_delete=models.CASCADE)
    id_purchases = models.ForeignKey(Purchases, verbose_name='Заказ', on_delete=models.CASCADE)
    count = models.CharField('Количество', max_length=3)

    class Meta:
        verbose_name = "Товар в покупке"
        verbose_name_plural = "Товары в покупках"

    def __str__(self):
        return f"{self.id}"

class Orders(models.Model):
    ST = [
        ("Оформляется" , "Оформляется"),
        ("В пути", "В пути"),
        ("На пункте выдачи", "На пункте выдачи")
    ]
    id_products = models.ForeignKey(Products, verbose_name='Товар', on_delete=models.CASCADE)
    total_amount = models.DecimalField ('Итоговая цена', max_digits=20, decimal_places=2)
    id_clients = models.ForeignKey(Clients, verbose_name='Клиент', on_delete=models.CASCADE)
    status = models.CharField('Статус', max_length=1020, choices=ST)
    address = models.CharField('Адрес', max_length=25)
    payment = models.ForeignKey(Cards, verbose_name='Оплата', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return f"{self.id}"
