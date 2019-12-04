from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact
from django.views.generic import ListView, DetailView  # For Class Based Views
# For creating CRUD for contacts
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# For creating a new user through Signup
from django.contrib.auth.forms import UserCreationForm
# To check whether the user is logged in or not
from django.contrib.auth.mixins import LoginRequiredMixin
# Reverse-Lazy function - redirects urls based on their name
from django.urls import reverse_lazy
# Import messages (From partials) to show success/warning messages in the page
from django.contrib import messages

# Create your views here.
# LoginRequiredMixin - This is used to check user loging for class based views
# login_required - This is used to check user login for function based views
########################### Function based Views ################################
# Function for Home Page


def home(request):
    context = {
        'contacts': Contact.objects.all()
    }
    return render(request, "index.html", context)


# Function for search details page
def search(request):
    if request.POST:
        search_data = request.POST['search_str']
        search_results = Contact.objects.filter(name__icontains=search_data)
        context = {
            'data': search_data,
            # Get contacts of logeed-in user
            'contacts': search_results.filter(manager=request.user)
        }
        return render(request, 'search.html', context)
    else:
        return redirect('home')


# Function for details page
def detail(request, id):
    context = {
        'contact': get_object_or_404(Contact, pk=id)
    }
    return render(request, 'detail.html', context)

################################### End of Function based Views #############################


#################################### Class Based Views ########################################
# We are using same index.html & detail.html pages for both FBV & CBVs
class HomePageView(ListView):
    template_name = 'index.html'
    model = Contact
    context_object_name = 'contacts'

    # Get list of all contacts only for logged-in user
    def get_queryset(self):
        contacts = super().get_queryset()
        return contacts.filter(manager=self.request.user)


class DetailPageView(LoginRequiredMixin, DetailView):
    template_name = 'detail.html'
    model = Contact
    context_object_name = 'contact'


# Function to create a new contact
class ContactCreateView(LoginRequiredMixin, CreateView):
    model = Contact
    template_name = 'create.html'
    fields = ['name', 'phone', 'email', 'info', 'gender', 'image']
    #success_url = '/'

    # we are saving current user id to as a manager to the new contact
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.manager = self.request.user
        instance.save()
        messages.success(
            self.request, 'Your contact has been saved successfully')
        return redirect('home')


# Function to update details
class ContactUpdateView(LoginRequiredMixin, UpdateView):
    model = Contact
    template_name = 'update.html'
    fields = ['name', 'phone', 'email', 'info', 'gender', 'image']
    # success_url = '/' #Goes to home page after updating

    # This will redirect page to details page after updating user details
    def form_valid(self, form):
        instance = form.save()
        messages.success(
            self.request, 'Your contact has been updated successfully')
        return redirect('detail', instance.pk)


# Function to delete contact
class ContactDeleteView(LoginRequiredMixin, DeleteView):
    model = Contact
    template_name = 'delete.html'
    success_url = '/'  # Goes to home page after updating

    # method to over-write the default delete function (from DeleteView)
    def delete(self, request, *args, **kwargs):
        messages.success(
            self.request, 'Your contact has been deleted successfully')
        return super().delete(self, request, *args, **kwargs)

# Function for New user Signup


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('home')
####################### End of Class based Views ###############################
