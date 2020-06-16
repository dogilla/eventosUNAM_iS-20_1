from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from .utils import IsNotAuthenticatedMixin
#from Post.models import Post
from .forms import LoginForm, OrgForm, DelForm, UserProfileForm, PasswordResetF


from django.contrib.auth.models import User
from django.core.mail import send_mail
from Home.models import UserProfile, PasswordF


from django.contrib.auth.forms import PasswordResetForm
from django.contrib import messages

from django.core.files.storage import default_storage
from django.template import loader
import qrcode
import random 
import string

# Function Views
def index(request):
    """
        Index in my Web Page.
    """
    print(request.method)
    template = 'Home/index.html'
    context = {}
    return render(request, template, context)



# Class-based Views
class Index(View):
    """
        Index in my Web Page but with Clased based views.
    """
    template = 'Home/index.html'
    context = {'title': 'Home - PUMA Eventos'}

    def get(self, request):
        """
            Get in my Index.
        """
        #all_posts = Post.objects.all()
        #self.context['posts'] = all_posts
        return render(request, self.template, self.context)
        

class RegistrarU(View):
    """
        Index in my Web Page but with Clased based views.
    """
    template = 'Home/registrarU.html'
    context = {'title': 'Registro - PUMA Eventos'}

    def get(self, request):
        """
            Get in my Index.
        """
        #all_posts = Post.objects.all()
        #self.context['posts'] = all_posts
        return render(request, self.template, self.context)


    def post(self, request):
        """
            Validates and do the login
        """
        form = UserProfileForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            avatar = request.POST.get('avatar', None)
            print(avatar)
            try:
                form.save()
                nombre = request.POST.get('nombre', '')
                correo = request.POST.get('correo', '')
                password = request.POST.get('password', '')
                entidad = request.POST.get('entidad', '')
                avatar = request.FILES.get('avatar', '')


                if("unam.mx" in correo):
                    user = User.objects.create_user(username = correo, password = password, email = correo, first_name = 'Estudiante', last_name = nombre)
                    userprofile = UserProfile.objects.create( user = user, nombre = nombre,  entidad = entidad)  
                    try:
                        userprofile.avatar = avatar
                        userprofile.save()
                    except: 
                        print("Error al upload")

                    html_message = loader.render_to_string(
                        'Home/link.html'
                    )
                    send_mail(
                    'Confirmacion de cuenta',
                    'Da click para confirmar tu registro',
                    'pumaeventosunam@gmail.com',
                    [correo],
                    fail_silently=True,
                    html_message=html_message,
                    )        
                    messages.info(request, 'Te has registrado con éxito!')
                    print("exito en el registro") 
                else:
                    messages.info(request, 'No se ha podido concluir tu registro!')
                    print("Correo invalido")   
            except Exception as e: 
                messages.info(request, e)
                print(e)  

        else:
            print("registro invalido")    


        self.context['form'] = form

        return redirect("Home:login")
        #return render(request, self.template, self.context)


class Home(View):
    """
        Index in my Web Page but with Clased based views.
    """
    template = 'Home/home.html'
    context = {'title': 'Home - PUMA Eventos'}

    def get(self, request):
        """
            Get in my Index.
        """
        #all_posts = Post.objects.all()
        #self.context['posts'] = all_posts
        return render(request, self.template, self.context)


def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


class RegistrarO(View):
    """
        Index in my Web Page but with Clased based views.
    """
    template = 'Home/registrarO.html'
    context = {'title': 'RegistrarO - PUMA Eventos'}

    def get(self, request):
        """
            Get in my Index.
        """
        #all_posts = Post.objects.all()
        #self.context['posts'] = all_posts
        return render(request, self.template, self.context)

    def post(self, request):
        """
            Validates and do the login
        """
        form = OrgForm(request.POST)
        if form.is_valid():

            try:

                #user = User.objects.create_user(username=form.cleaned_data['correo'],email=form.cleaned_data['correo'],password='default', last_name = form.cleaned_data['nombre'], first_name = 'Organizador')            
                x = randomString(10)
                username = form.cleaned_data['correo']
                PasswordF.objects.create(correo = username, token = x)
                html_message = loader.render_to_string(
                    'Home/pass.html',
                    {
                        'token': x,
                        'correo': username,
                        
                    }
                )
                send_mail(
                    'Se te ha asignado como organizador',
                    'Ingresa ahora!',
                    'pumaeventosunam@gmail.com',
                    [username],
                    fail_silently=False,
                    html_message = html_message,
                    ) 
                messages.info(request, "Se ha enviado un correo para que el usuario establezca la contraseña")

            except Exception as e: 
                messages.info(request, e)
                print(e)


        self.context['form'] = form

        return redirect("Home:registrarO")
        #return render(request, self.template, self.context)


class PasswordReset(View):
    """
        Index in my Web Page but with Clased based views.
    """
    template = 'Home/password.html'
    context = {'title': 'Password - PUMA Eventos'}

    def get(self, request, user_mail, tok):
        """
            Get in my Index.
        """
        #all_posts = Post.objects.all()
        #self.context['posts'] = all_posts
        return render(request, self.template, self.context)

    def post(self, request, user_mail, tok):
        """
            Validates and do the login
        """
        form = PasswordResetF(request.POST)
        if form.is_valid():
            print("aoeuoeau")
            try:
                token = tok
                correo = user_mail
                password = request.POST.get('password', '')
                
                x = PasswordF.objects.get(correo = correo, token = token)
                print(x)
                
                user = User.objects.create_user(username= correo,email=correo,password=password,first_name = 'Organizador')            
                messages.info(request, "Usuario Registrado")
                return redirect("Home:login")

            except Exception as e: 
                messages.info(request, "Url invalida para elegir contraseña")
                print(e)


        self.context['form'] = form

        return redirect("Home:passwordR", user_mail = user_mail, tok = tok)
        #return render(request, self.template, self.context)



def del_user(request, username):    
    try:
        u = User.objects.get(username = username)
        u.delete()
        print( "The user is deleted")
    except:
        print(request, "The user not found")    
    return redirect("Home:home")

class ConfirmarU(View):
    """
        Index in my Web Page but with Clased based views.
    """
    template = 'Home/confirmarU.html'
    context = {'title': 'Confirmacion - PUMA Eventos'}

    def get(self, request):
        """
            Get in my Index.
        """
        #all_posts = Post.objects.all()
        #self.context['posts'] = all_posts
        return render(request, self.template, self.context)



    def post(self, request):
        """
            Validates and do the login
        """
        form = DelForm(request.POST)
        if form.is_valid():
                correo = request.POST.get('correo', '')

                try:
                    #post = UserProfile.objects.get(email=mail)
                    usuario = User.objects.get(username = correo)
                    
                    profile = UserProfile.objects.get(user = usuario)
                    
                    profile.nombre = 'confirmado'
                    profile.save()

                    print("Correo confirmado")
                    messages.info(request, 'Correo confirmado')
                except Exception as e: 
                    messages.info(request, e)
                    print(e)


        self.context['form'] = form


        html_message = loader.render_to_string(
            'Home/linkconfirmacion.html',
            {
                
                
            }
        )
        send_mail(
        'Subject here',
        'Here is the message.',
        'pumaeventosunam@gmail.com',
        [correo],
        fail_silently=False,
        html_message = html_message,
        )
        return redirect("Home:confirmarU")
        #return render(request, self.template, self.context)


class About(View):
    """
        About me page.
    """
    template = 'Home/about.html'
    context = {'title': 'About me'}

    def get(self, request):
        """
            Get in About me.
        """
        return render(request, self.template, self.context)


class Login(IsNotAuthenticatedMixin, View):
    """
        Admin login
    """
    template = 'Home/login.html'
    context = {'title': 'Login - PUMA Eventos'}

    def get(self, request):
        """
            Shows the form to login
        """
        form = LoginForm()
        self.context['form'] = form

        return render(request, self.template, self.context)

    def post(self, request):
        """
            Validates and do the login
        """
        form = LoginForm(request.POST)
        print(form)
        if form.is_valid():


            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                img = qrcode.make('Some data here')
                print(type(img))
                print(img.size)
                img.save('Home/static/Home/img/aoeu.png')
                try:
                    usuario = User.objects.get(username = form.cleaned_data["username"])
                    profile = UserProfile.objects.get(user = usuario)
                    if( profile.nombre == 'confirmado'):
    

                        login(request, user)
                        if request.GET.get("next", None) is not None:
                            return redirect(request.GET.get("next"))
                        
                        return redirect("Home:home")
                    else:
                        messages.info(request, 'Registrate o confirma tu correo')
                        return redirect("Home:login")

                except Exception as e: 
                    messages.info(request,e)
                    login(request, user)
                    if request.GET.get("next", None) is not None:
                        return redirect(request.GET.get("next"))
                    
                    return redirect("Home:home")
                

            else:
                messages.info(request,"Error en el login: con " + str(form.cleaned_data['username'] + ' como usuario y ' + str(form.cleaned_data['password'] + " como contraseña.")))

        self.context['form'] = form
        return render(request, self.template, self.context)


class Logout(LoginRequiredMixin, View):
    """
        Does the logout
    """
    def get(self, request):
        logout(request)
        return redirect("Home:index")
