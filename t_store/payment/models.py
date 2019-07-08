from django.db import models
from bookstore.models import Book
from django.utils import timezone
class OrderDelivery (models.Model):

    CHOICES_PAYMENT = (
        ('cash', 'Cash'),
        ('card', 'Card'),
    )
    CHOICES_DATES = (('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'),
        ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'),
        ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'), ('25', '25'),
        ('26', '26'), ('27', '27'), ('28', '28'), ('29', '29'), ('30', '30'), ('31', '31'),)
    CHOICES_TIME = (('10:00 - 13:00', '10:00 - 13:00'), ('11:00 - 14:00', '11:00 - 14:00'), ('12:00 - 15:00', '12:00 - 15:00'),
                    ('13:00 - 16:00', '13:00 - 16:00'), ('14:00 - 17:00', '14:00 - 17:00'), ('15:00 - 18:00', '15:00 - 18:00'),
                    ('16:00 - 19:00', '16:00 - 19:00'), ('17:00 - 20:00', '17:00 - 20:00'), ('18:00 - 21:00', '18:00 - 21:00'),
                    ('19:00 - 22:00', '19:00 - 22:00'), ('20:00 - 22:30', '20:00 - 22:30'))

    id = models.AutoField(primary_key=True)
    payment_type = models.CharField(choices=CHOICES_PAYMENT, max_length=20)
    name = models.CharField(max_length=50, verbose_name='Your name')
    surname = models.CharField(max_length=50, verbose_name='Your surname')
    mobile_phone = models.IntegerField()
    email = models.EmailField(max_length=75)
    adres = models.CharField(max_length=300)
    date = models.CharField(choices=CHOICES_DATES, max_length=2)
    time = models.CharField(choices=CHOICES_TIME, max_length=13)
    time_of_order = models.DateTimeField(default=timezone.now)
    price = models.FloatField(null=True)
    product = models.CharField(max_length=300, null=True)

    def __str__(self):
        return 'ORDER WITH DELIVERY № ' + str(self.id)

class OrderNoDel (models.Model):
    CHOICES_PAYMENT = (
        ('cash', 'Cash'),
        ('card', 'Card'),
    )

    id = models.AutoField(primary_key=True)
    payment_type = models.CharField(choices=CHOICES_PAYMENT, max_length=4)
    name = models.CharField(max_length=50, verbose_name='Your name')
    surname = models.CharField(max_length=50, verbose_name='Your surname')
    mobile_phone = models.IntegerField()
    email = models.EmailField(max_length=75)
    time_of_order = models.DateTimeField(default=timezone.now)
    price = models.FloatField(null=True)
    product = models.CharField(max_length=300, null=True)

    def __str__(self):
        return 'ORDER WITHOUT DELIVERY № ' + str(self.id)
