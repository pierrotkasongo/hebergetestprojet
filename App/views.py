from django.shortcuts import render,redirect,get_object_or_404 
from django.contrib import messages
from .models import *
# Create your views here.
def home(request):
    if request.method == 'POST':
        image= request.FILES['image']
        name = request.POST['name'].lower()
        price = request.POST['price']
        productSave = Product.objects.create(image=image, name=name, price=price)
        productSave.save()
        messages.success(request, "Produit ajouté avec succès !")
   
        
    products = Product.objects.all()
    context ={
        'products':products
    }
    return render(request, "home.html",context)
     

def update_product(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        image= request.FILES['image']
        name = request.POST['name'].lower()
        price = request.POST['price']
        created_at=request.POST['created_at']
    
        objet = Product.objects.get(id=id)
        objet.image=image
        objet.name=name
        objet.price=price
        objet.created_at=created_at
        objet.save()
        messages.success(request, "Le produit a été modifier avec succès !")
        return redirect('home')
    return render(request, "update.html" , {'product': product})
        
def delete_product(request, id):
    product= get_object_or_404(Product, id=id)
    product.delete()
    return redirect('home')
  