from django.db import models
from django.contrib.auth.models import User

class Xodimlar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.first_name

class Davomat(models.Model):
    xodim = models.ForeignKey(Xodimlar,on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.xodim.first_name} -- {self.data}"