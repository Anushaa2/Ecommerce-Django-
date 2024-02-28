from django.shortcuts import render,redirect
from .models import Product,Category
from .forms import ProductForm,CategoryForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from userspage.auth import admin_only


# decorator->paila define gareko funciton @
# Create your views here.

@login_required
@admin_only
def index(request):
  products=Product.objects.all()
  context={
    'products':products
  }
  return render(request,'product/index.html',context)

@login_required
@admin_only
def post_product(request):
  #to insert product
  if request.method=='POST':
    form=ProductForm(request.POST,request.FILES)
#     isvalid le form ko value check garne
    if form.is_valid():
          form.save()
          messages.add_message(request,messages.SUCCESS,'product added successfully')
      #     redirect ma url ko name data insert vayepachi add direct ma jane
          return redirect('/products/addproduct/')
    else:
          messages.add_message(request,messages.ERROR,'please verify form fields')
          return render(request,'product/addproduct.html',{'forms':form})
    #to show add product form

    

  context={
    'forms':ProductForm
  }
  return render(request,'product/addproduct.html',context)

@login_required
@admin_only
def post_category(request):
      #to insert Category
  if request.method=='POST':
    form=CategoryForm(request.POST)
#     isvalid le form ko value check garne
    if form.is_valid():
          form.save()
          messages.add_message(request,messages.SUCCESS,'Category added successfully')
      #     redirect ma url ko name data insert vayepachi add direct ma jane
          return redirect('/products/addcategory/')
    else:
          messages.add_message(request,messages.ERROR,'please verify form fields')
          return render(request,'product/addcategory.html',{'forms':form})
    #to show add product form  

  context={
    'forms':CategoryForm
  }
  return render(request,'product/addcategory.html',context)

def show_category(request):
    category=Category.objects.all()
    context={
        'category':category

    }

    return render(request,'product/showcategory.html',context)



# to delete category
@login_required
@admin_only
def delete_category(request,category_id):
      category=Category.objects.get(id=category_id)
      category.delete()
      messages.add_message(request,messages.SUCCESS,'Category deleted')
      return redirect('/products/showcategory')


# to delete product
@login_required
@admin_only
def delete_product(request,product_id):
      product=Product.objects.get(id=product_id)
      product.delete()
      messages.add_message(request,messages.SUCCESS,'Product deleted')
      return redirect('/products')

#to edit category
@login_required
@admin_only
def update_category(request,category_id):
  instance=Category.objects.get(id=category_id)
  if request.method=='POST':
        form=CategoryForm(request.POST,request.FILES,instance=instance)
        if form.is_valid():
              form.save()
              messages.add_message(request,messages.SUCCESS,'category updated')
              return redirect('/products/showcategory/')
        else:
              messages.add_message(request,messages.ERROR,'pleae verify forms')
              return render(request,'/products/updatecategory.html',{'forms':form})
              
  context={
    'forms':CategoryForm(instance=instance)
  }
  return render(request,'product/updatecategory.html',context)






# to update product
@login_required
@admin_only
def update_product(request,product_id):
      instance=Product.objects.get(id=product_id)
      if request.method=='POST':
        form=ProductForm(request.POST,request.FILES,instance=instance)
        if form.is_valid():
              form.save()
              messages.add_message(request,messages.SUCCESS,'product updated')
              return redirect('/products')
        else:
              messages.add_message(request,messages.ERROR,'pleae verify forms')
              return render(request,'products/updateproduct.html',{'forms':form})
              
      context={
          'forms':ProductForm(instance=instance)
      }
      return render(request,'product/updateproduct.html',context)
