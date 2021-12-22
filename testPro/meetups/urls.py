"""
This is the file that will hold the urls that belong to the meetups components.
It will be connected to the urls of the project wide scope.
"""
from django.urls import path  # This function allows us to register the urls per say.
from . import views


"""
This urlpatterns variable holds all the urls associated with this app and the respective view functions that should be
called when that url is reached. It's almost like thinking, each view/webpage you create must have a corresponding
url.

Takes 2 args, first arg describes the path after our domain for which the url/view should become active.
The second arg is the view function that the url path should execute when active. Remember to jus point to it and not
call the view function.
"""

"""
The slug in the url patterns below is so called converter and tells django that the dynamic value that we would have in
our path should match the format of the slug key in the dic we defined in the index view function.
"""
urlpatterns = [
    path('', views.index, name='home'),  # our-domain.com/meetups
    path('<slug:meetup_id>/success', views.confirm_registration, name='confirm-registration'),
    path('<slug:meetup_id>', views.meetup_details, name='meetup-detail'),  # our-domain.com/meetups/<dynamic-path-segment>, the val of
    # slug can be whatever I like.
]
