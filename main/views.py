from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView,DetailView
from .models import *
from django.contrib import messages
from main.forms import *
from django.contrib.auth import authenticate,login,logout
from rest_framework.generics import RetrieveUpdateDestroyAPIView,ListCreateAPIView
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, BasePermission
from django.urls import reverse
from django.core.mail import EmailMessage
from shopping.settings import EMAIL_HOST_USER
from .permissions import *
from rest_framework.exceptions import PermissionDenied
from django.db.models import Avg





class HomeListView(ListView):
    template_name='index.html'

    def get(self,request):

        fisrtcarousel=UserInfos.objects.first()
        carousel=HomeCarousel.objects.all()
        categorp=Category.objects.filter(id__in=[1,2,3,4,5,6,7,8])
        carouselpanel_active=AllProductModel.objects.filter(id__in=[1,2,3])
        allproducts=AllProductModel.objects.filter(id__in=[4,5,6])
        caregoryf=Category.objects.first()
        allproduct=AllProductModel.objects.all().order_by('-id')
        govazd=Govazd.objects.first()


        # ABS
        basicinfo=BaseInfo.objects.get()
        category=Category.objects.filter(id__in=[1,2,3,4,5,6,7,8,9,10])


        xanut=UserInfos.objects.all()
        context={
            'basicinfo':basicinfo,
            'fisrtcarousel':fisrtcarousel,
            'carousel':carousel,
            'category':category,
            'xanut':xanut,
            'allproduct':allproduct,
            'caregoryf':caregoryf,
            'categorp':categorp,
            'carouselpanel_active':carouselpanel_active,
            'allproducts':allproducts,
            'govazd':govazd,



            
                }

        return render(request,self.template_name,context)
    
def HomeSearch(request):
    fisrtcarousel=UserInfos.objects.first()
    carousel=HomeCarousel.objects.all()
    categorp=Category.objects.filter(id__in=[1,2,3,4,5,6,7,8])
    carouselpanel_active=AllProductModel.objects.filter(id__in=[1,2,3])
    allproducts=AllProductModel.objects.filter(id__in=[4,5,6])
    caregoryf=Category.objects.first()
    basicinfo=BaseInfo.objects.get()
    category=Category.objects.filter()
    xanut=UserInfos.objects.all()
    govazd=Govazd.objects.first()


    allproduct=AllProductModel.objects.filter(id__icontains=request.GET.get('id'),
                                            name__icontains=request.GET.get('name'),)
    
    return render(request,'index.html',{'basicinfo':basicinfo,
                                         'category':category,
                                         'xanut':xanut,
                                         'fisrtcarousel':fisrtcarousel,
                                         'categorp':categorp,
                                         'allproduct':allproduct,
                                         'carouselpanel_active':carouselpanel_active,
                                         'allproducts':allproducts,
                                         'caregoryf':caregoryf,
                                         'carousel':carousel,
                                         'govazd':govazd,

                                         })
    

def RegisterPage(request):
    basicinfo=BaseInfo.objects.get()
    xanut=UserInfos.objects.all()

    form=RegisterForm
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            messages.warning(request,'Կան դատարկ կամ թերի լրացված դաշտեր')
    
    return render(request,'register.html',{'form':form,'basicinfo':basicinfo,'xanut':xanut})




def LoginPage(request):
    basicinfo = BaseInfo.objects.get()
    xanut=UserInfos.objects.all()

    if request.method == 'POST':
        username = request.POST.get('username')

        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            next_param = request.POST.get('next', None)
            print(f'Next Param: {next_param}') 
            if next_param:
                return redirect(next_param)
            else:
                return redirect('home')
        else:
            messages.warning(request, 'Սխալ մուտքանուն կամ գաղտնաբառ')

    return render(request, 'login.html', {'basicinfo': basicinfo,'xanut':xanut,})



def LogoutPage(request):
    logout(request)
    return redirect('home')





class ProductListView(ListView):
    template_name='filter.html'

    def get(self,request,id):
        basicinfo = BaseInfo.objects.get()
        category=Category.objects.all()
        xanut=UserInfos.objects.all()
        subcategory=Category.objects.filter(pk=id)
        categoryp=Category.objects.filter(id__in=[1,2,3,4,5,6,7,8])
        caregoryf=Category.objects.first()
        context={
            'category':category,
            'subcategory':subcategory,
            'basicinfo':basicinfo,
            'xanut':xanut,
            'categoryp':categoryp,
            'caregoryf':caregoryf,
                }

        return render(request,self.template_name,context)
    

class ProductDetailView(DetailView):
    template_name='product-details.html'

    def get(self,request,id):
        basicinfo=BaseInfo.objects.get()

        category=Category.objects.all()
        subcategory=AllProductModel.objects.get(pk=id)
        xanut=UserInfos.objects.all()
        categorp=Category.objects.filter(id__in=[1,2,3,4,5,6,7,8])
        caregoryf=Category.objects.first()
        carouselpanel_active=AllProductModel.objects.filter(id__in=[1,2,3])
        userr=request.user
        form=ReviewForm
        comments=ReviewModel.objects.filter(product=subcategory)
        in_detail_user=str(request.user) == str(subcategory.user)
        order=OrderForm
        allproduct=AllProductModel.objects.filter(cate=subcategory.cate)
        govazd=Govazd.objects.first()

        prod_1=ReviewModel.objects.filter(product=subcategory).aggregate(Avg('rate')).values()
        qanak=ReviewModel.objects.filter(product=subcategory).count()
        if ReviewModel.objects.filter(product=subcategory).count() !=0:
            prod = round(list(prod_1)[0], 1).__ceil__()
        else:
            prod = 0

        context={
            'subcategory':subcategory,
            'category':category,
            'xanut':xanut,
            'govazd':govazd,
            'basicinfo':basicinfo,
            'categorp':categorp,
            'caregoryf':caregoryf,
            'carouselpanel_active':carouselpanel_active,
            'userr':userr,
            'form':form,
            'comments':comments,
            'in_detail_user':in_detail_user,
            'order':order,
            'allproduct':allproduct,
            'prod':prod,
            'qanak':qanak



                }
        
        return render(request,self.template_name,context)
    
    def post(self,request,id):
        categorp=Category.objects.filter(id__in=[1,2,3,4,5,6,7,8])
        caregoryf=Category.objects.first()
        basicinfo=BaseInfo.objects.get()
        category=Category.objects.all()
        govazd=Govazd.objects.first()

        subcategory=AllProductModel.objects.get(pk=id)
        prod_1=ReviewModel.objects.filter(product=subcategory).aggregate(Avg('rate')).values()
        qanak=ReviewModel.objects.filter(product=subcategory).count()
        if ReviewModel.objects.filter(product=subcategory).count() !=0:
            prod = round(list(prod_1)[0], 1).__ceil__()
        else:
            prod = 0
        comments=ReviewModel.objects.filter(product=subcategory)
        order=OrderForm(request.POST)
        if order.is_valid():
            obj=order.save(commit=False)
            obj.product=subcategory
            obj.user=request.user
            obj.save()
            email=EmailMessage(
                subject=f'Նոր նամակ ARM-ZONA-ից',
                body=f"Գնորդ-{request.POST.get('name')} \n Ապրանք-{subcategory.name} \n ID - {subcategory.id} \n Հեռախոսահամար - {request.POST.get('phone')} \n օգտատեր-{request.user}",
                from_email=EMAIL_HOST_USER,
                to=[subcategory.email],
            )
            email.send()
            return redirect(reverse('detail', args=[subcategory.id]))

            
        else:
            order=OrderForm()
        form=ReviewForm(request.POST,request.FILES)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.product=subcategory
            obj.save()
            return redirect(reverse('detail', args=[subcategory.id]))


        context={
            'govazd':govazd,
            'basicinfo':basicinfo,
            'category':category,
            'form':form,
            'subcategory':subcategory,
            'comments':comments,
            'order':order,
            'categorp':categorp,
            'caregoryf':caregoryf,
            'qanak':qanak,
            'prod':prod,
                }


        return render(request,self.template_name,context)
    


class ChangeProducts(RetrieveUpdateDestroyAPIView):
    queryset = AllProductModel.objects.all()
    serializer_class = AllProductsSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]

    def get_object(self):
        instance = super().get_object()

        if str(self.request.user) != str(instance.user):
            raise PermissionDenied("You do not have permission to access this instance.")
            

        return instance


def Addproducts(request):
    form = AddProductForm
    basicinfo = BaseInfo.objects.get()

    userinfo, created = UserInfos.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)

            obj.user = userinfo
            obj.save()
            return redirect('home')
        else:
            messages.warning(request,'Դաշտերը ճիշտ լրացված չեն։')

    return render(request, 'addproducts.html', {'form': form, 'basicinfo': basicinfo})


class UserProfile(ListView):
    template_name='user_profile.html'

    def get(self,request,id):
        basicinfo=get_object_or_404(UserInfos,pk=id)
        xanut=UserInfos.objects.all()
        category=Category.objects.all()
        categorp=Category.objects.filter(id__in=[1,2,3,4,5,6,7,8])
        caregoryf=Category.objects.first()
        subproduct=UserInfos.objects.filter(pk=id)
        user=request.user


        context={
            'basicinfo':basicinfo,
            'xanut':xanut,
            'subproduct':subproduct,
            'categorp':categorp,
            'caregoryf':caregoryf,
            'category':category,
            'user':user,

                }
        
        return render(request,self.template_name,context)
    

def Saves(request, id):
    product = AllProductModel.objects.get(pk=id)
    user = request.user
    saved = Saved.objects.filter(user=user, prouduct=product).first()

    if not saved:
        Saved.objects.create(user=user, prouduct=product)
        product.dissave = False
    else:
        saved.delete()
        product.dissave = True

    product.save()

    return redirect(reverse('detail', args=[product.id]))


class SavePage(ListView):
    template_name='cart.html'

    def get(self,request):
        user=request.user
        prouduct=Saved.objects.filter(user=user)
        basicinfo=BaseInfo.objects.get()
        category=Category.objects.filter()
        xanut=UserInfos.objects.all()



        context={
            'prouduct':prouduct,
            'basicinfo':basicinfo,
            'category':category,
            'xanut':xanut,

                }
        
        return render(request,self.template_name,context)
    

class ContactUs(DetailView):
    template_name='contact-us.html'

    def get(self,request):

        basicinfo=BaseInfo.objects.get()
        category=Category.objects.filter()
        xanut=UserInfos.objects.all()
        form=ContactUsForm
        context={
            'basicinfo':basicinfo,
            'category':category,
            'xanut':xanut,
            'form':form,

                }
        
        return render(request,self.template_name,context)
    
    def post(self,request):
        basicinfo=BaseInfo.objects.get()
        category=Category.objects.filter()
        xanut=UserInfos.objects.all()
        form=ContactUsForm(request.POST)
        if form.is_valid():
            subject=f"Բարև {request.POST.get('name')}"
            body='ձեր կարծիքը կարևոր է մեզ համար \n Մենք շուտով կպատասխանենք ձեր հարցմանը։'
            email=EmailMessage(
                subject=subject,
                body=body,
                from_email=EMAIL_HOST_USER,
                to=[request.POST.get('email')],
            )
            email.send()
            obj=form.save(commit=False)
            obj.user=request.user
            obj.save()
            return redirect('home')
        else:
            messages.warning(request,'Կան թերի կամ ոչ ճիշտ լրացված դաշտեր')
        context={
            'basicinfo':basicinfo,
            'category':category,
            'xanut':xanut,
            'form':form,
            
                }
        
        return render(request,self.template_name,context)
    
class AboutUs(DetailView):
    template_name='blog.html'

    def get(self,request):
        aboutshop=AboutShop.objects.get()
        basicinfo=BaseInfo.objects.get()
        category=Category.objects.filter()
        xanut=UserInfos.objects.all()

        context={
            'basicinfo':basicinfo,
            'category':category,
            'xanut':xanut,      
            'aboutshop':aboutshop,
                  
                }
        
        return render(request,self.template_name,context)
    
    
