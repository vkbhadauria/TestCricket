from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser
from common.models import Country
# Create your models here.


class PlayerManager(BaseUserManager):
    def create_user(self, email, username="", first_name="",
                    last_name="", password=None, **kwargs):

        user = Player.objects.filter(email__iexact=PlayerManager.normalize_email(email)).first()
        if not user:
            user = self.model(email=PlayerManager.normalize_email(email),
                            username=email,
                            first_name=first_name,
                            last_name=last_name)

            if password:
                user.set_password(password)
            user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email=email, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class Player(AbstractUser):
    email = models.EmailField(max_length=254, unique=True, error_messages={
        'unique': "sorry. that email is already in use. please use login or sign up with another email.", })
    username = models.CharField(max_length=254, blank=True)
    first_name = models.CharField(max_length=254, blank=True, null=True)
    last_name = models.CharField(max_length=254, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)

    # class Meta:
    #     db_table = 'user_players'
    #     verbose_name = 'Player'
    #     verbose_name_plural = 'Players'
    #     # swappable = 'AUTH_USER_MODEL'

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','password']

    def __str__(self):
        return self.email


class PlayerProfile(models.Model):
    player = models.OneToOneField(Player, related_name='profile',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='players/', blank=True)
    country = models.ForeignKey(Country, null=True, blank=True, on_delete=models.SET_NULL)
    fifties = models.PositiveIntegerField(default=0)
    hundered = models.PositiveIntegerField(default=0)
    total_runs = models.PositiveIntegerField(default=0)
    highest_score = models.PositiveIntegerField(default=0)
    total_match = models.PositiveIntegerField(default=0)
    joursey_number = models.CharField(max_length=254, blank=True, null=True)

    def __str__(self):
        return self.player.email if self.player else '' 
