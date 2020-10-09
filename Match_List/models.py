from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model()


class Match_Details(models.Model):
    player1=models.ForeignKey(User,related_name='player1',on_delete=models.CASCADE)
    player2=models.ForeignKey(User,related_name='player2',on_delete=models.CASCADE)
    Winner=models.ForeignKey(User,related_name='winner',on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return f"{self.player1} VS {self.player2}"

class Match_Summary(models.Model):
    MAP_CHOICES = [
        ('DustII', 'DUST II'),
        ('Inferno', 'Inferno'),
        ('Mirage', 'Mirage'),
        ('Nuke', 'Nuke'),
        ('Overpass', 'Overpass'),
        ('Vertigo', 'Vertigo'),
    ]
    GUN_CHOICES = [
        ('AK', 'Ak'),
        ('AWP', 'AWP'),
        ('AUG', 'AUG'),
        ('GAY_GUN', 'SCAR'),
        ('Others', 'Others'),
    ]
    match=models.ForeignKey(Match_Details,related_name='match',on_delete=models.CASCADE)
    date=models.DateTimeField(null=True,blank=True)
    player1_points=models.IntegerField()
    player2_points=models.IntegerField()
    maps=models.CharField(max_length=15,choices=MAP_CHOICES,default="DustII")
    gun_banned_player1=models.CharField(max_length=15,choices=GUN_CHOICES)
    gun_banned_player2=models.CharField(max_length=15,choices=GUN_CHOICES)

    def __str__(self):
        return str(self.match)
