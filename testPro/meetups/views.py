"""
This is where to define the views/web pages of the meetups app.
"""
from django.shortcuts import render, redirect
from .models import Meetup, Participant
from.forms import RegistrationForm

# Create your views here.
# This is what determines what the user sees.


def index(request):  # This is a parameter that will be used in the HttpResponse class, I believe
    """
    This is the first view of the meetups app, more like the first web page of the meetups components.
    """
    meetups = Meetup.objects.all()
    return render(request, 'meetups/index.html', {'meetup_list': meetups,
                                                  })  # The third arg lets us render a var


def meetup_details(request, meetup_id):
    """
    Details view for the meetup requested.
    :param meetup_id:
    :param request:
    :return: html
    """
    try:
        selected_meetup = Meetup.objects.get(slug=meetup_id)
        if request.method == "GET":
            registration_form = RegistrationForm()
        else:
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                user_email = registration_form.cleaned_data['email']
                participant, was_created = Participant.objects.get_or_create(email=user_email)
                selected_meetup.participants.add(participant)
                return redirect('confirm-registration', meetup_id)

        return render(request, 'meetups/meetup-details.html', {
                'meetup_found': True,
                'meetup': selected_meetup,
                'form': registration_form,
            })
    except Exception as exc:
        print(exc)
        return render(request, 'meetups/meetup-details.html', {
                                                                'meetup_found': False,
        })


def confirm_registration(request, meetup_id):
    selected_meetup = Meetup.objects.get(slug=meetup_id)
    title = selected_meetup.title
    organizer = selected_meetup.organizer
    return render(request, "meetups/registration-success.html", {
        'title': title,
        'organizer_email': organizer,
    })
