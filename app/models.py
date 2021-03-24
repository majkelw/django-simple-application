from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    cats_number = models.IntegerField

    def __str__(self):
        return "%s %s" % (self.name, self.email)


class Cat(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    color = models.CharField(max_length=40)
    gender = models.BooleanField()

    def gender_type(self):
        return self.gender

    def __str__(self):
        return "%s %s %s" % (self.name, self.color, self.gender)


class UserCatOwner(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.user, self.cat)


class Prey(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=40)

    def __str__(self):
        return "%s" % self.type


class Hunting(models.Model):
    id = models.AutoField(primary_key=True)
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)
    duration = models.IntegerField(default=0)

    def __str__(self):
        return "%s %s" % (self.cat, self.duration)


class HuntingDetails(models.Model):
    id = models.AutoField(primary_key=True)
    hunting = models.ForeignKey(Hunting, on_delete=models.CASCADE)
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)
    prey = models.ForeignKey(Prey, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.hunting, self.prey)
