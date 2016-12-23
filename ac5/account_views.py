import account.views

import ac5.account_forms


class SignupView(account.views.SignupView):

   form_class = ac5.account_forms.SignupForm

   def after_signup(self, form):
       self.created_user.first_name = form.cleaned_data["first_name"]
       self.created_user.last_name = form.cleaned_data["last_name"]
       self.created_user.save()
       #self.create_profile(form)
       super(SignupView, self).after_signup(form)

   #  def create_profile(self, form):
   #      profile = self.created_user.artist  # replace with your reverse one-to-one profile attribute
   #      profile.first_name = form.cleaned_data["first_name"]
   #      profile.last_name = form.cleaned_data["last_name"]
   #      profile.save()
