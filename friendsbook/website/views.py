from . forms import UserForm 	 	
from django.views import generic
from django.views.generic import View
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from . models import Profile


class IndexView(generic.ListView):
	template_name = 'website/index.html'

	def get_queryset(self):
		return Profile.objects.all()


class DetailsView(generic.DetailView):
	model = Profile
	template_name = 'website/details.html'
	context_object_name = 'person'	


class UserFormView(View):
	form_class = UserForm
	template_name = 'website/signup_form.html'

	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form': form})

	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():

			user = form.save(commit=False)

			username = form.cleaned_data['username']
			password = form.cleaned_data['password']	
			user.set_password(password)
			user.save()

			user = authenticate(username=username, password=password)

			if user is not None:

				if user.is_active:
					login(request, user)
					return redirect('website:index')

		return render(request, self.template_name, {'form': form})			