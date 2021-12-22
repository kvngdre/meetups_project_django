from django.db import models

# Create your models here.


class Location(models.Model):
    """
    Location model/entity
    """
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=300)
    address = models.CharField(max_length=300)

    def __str__(self):
        """
        To define how this model will be displayed on the admin site.
        :return: str
        """
        return f'{self.city}, {self.country}'


class Participant(models.Model):
    """
    Participants model
    """
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email


class Meetup(models.Model):
    """
    Meetups model
    """
    title = models.CharField(max_length=200)
    organizer = models.EmailField()
    date = models.DateField()
    slug = models.SlugField(unique=True)
    description = models.TextField()  # after creating this model, we have to make_migrations.
    image = models.ImageField(upload_to='images')
    location = models.ForeignKey(Location, on_delete=models.CASCADE)  # This sets up a one to many, one location can be
    # present in many meetups. "on_delete"- defines what should happen if the location of the meetup is deleted.
    # CASCADE this means that if the related location is deleted, the meetup is deleted as well. You also use SET_NULL
    # this means the location field for the meetup is set to NULL.
    participants = models.ManyToManyField(Participant, blank=True, null=True)   # Many-to-Many relationship. Remember a relationship must point to the model it's related to

    def __str__(self):
        """
        This is default func that can be used in any python class. this defines how the instance of the class is printed
         if it's printed as a string. If we need the instance as a string.
        """
        return f'{self.title} || {self.slug}'



