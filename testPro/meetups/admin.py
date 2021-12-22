from django.contrib import admin
from .models import Location, Meetup, Participant

# Register your models here.


class MeetupAdmin(admin.ModelAdmin):
    """
    This class is used to define how the objects of the model will look and behave in the admin. For this example I will
    add columns to show all the fields the model has.
    """
    list_display = ('title', 'location', 'date', 'image', )  # Shows the attributes as columns
    list_filter = ('location', 'date')   # Creates a filter on the admin with the values of which you can filter with.
    # For this example, we can filter by title and/or slug.
    # Say you want to auto-populate the slug field based on the title, django has that see example below
    prepopulated_fields = {'slug': ('title', )}  # takes a dict with key being the field to prepopulated and value being
    # a tuple of the field that will be used and concatenated to create the prepopulated text.
    # It looks at the value of the slug in the model and uses that to infer the correct format to auto populate


admin.site.register(Meetup, MeetupAdmin)  # Added MeetupAdmin here, so django knows to apply my config to the model
# when displaying it on the admin site.
admin.site.register(Location)
admin.site.register(Participant)
