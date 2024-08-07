from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from stylehome.apps.client.models import User,Municipality
from django.contrib import messages

# Create your views here.
class LoginView(TemplateView):
    """ Login page view """
    template_name = 'login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
def post(request):
    print("post")
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email, password)
    
        if email and password:
            try:
                user = User.objects.get(email=email, password=password)
                request.session['user_id'] = user.id
                messages.success(request, 'Login successful')
                return redirect('profile')
            except user.DoesNotExist:
                messages.error(request, 'Invalid email or password')
    
    return render(request, 'login.html')
    

class RegisterView(TemplateView):
    """ Register page view """
    template_name = 'register.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        municipalities = Municipality.objects.all()
        context['municipalities'] = municipalities
        return context
    
def register(request):
    print("Aqui tor")
    if request.method == 'GET':
        name = request.GET.get('name')
        last_name = request.GET.get('last_name')
        email = request.GET.get('email')
        password = request.GET.get('password')
        confirmed_password = request.GET.get('confirmed_password')
        municipality = request.GET.get('municipality')
        
        print(f"Datos recibidos - Nombre: {name}, Apellidos: {last_name}, Correo: {email}, Contraseña: {password}")

        if password != confirmed_password:
            messages.error(request, 'Las contraseñas no coinciden')
            return render(request, 'register.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'El correo ya está registrado')
            return render(request, 'register.html')

        user = User.objects.create(municipality=municipality, first_name=name, last_name=last_name, email=email, password=password)
        messages.success(request, 'Registro exitoso')
        return redirect('login')
    
    municipalities = Municipality.objects.all()
    return render(request, 'register.html', {'municipalities': municipalities})

class ProfileView(TemplateView):
    """ profile page view """
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        print(user)
        context['user'] = user
        return context
