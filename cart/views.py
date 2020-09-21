from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, ListView, DetailView, FormView, UpdateView, DeleteView
from shop.models import Product
from .models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist
from .forms import AddToCartForm

# class CartLV(ListView):
#     model = Cart
#     # template_name = 'order/cart.html'
#     context_object_name = 'cart'
#
#     def get_queryset(self):
#         return Cart.objects.filter(tags__name=self.kwargs.get('p_name'))  # 태그명칭 전달
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['p_name'] = self.kwargs['p_name']
#         return context


def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id=_cart_id(request)
        )
        cart.save()

    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product=product,
            quantity=1,
            cart=cart
        )
        cart_item.save()
    return redirect('cart:cart_detail')


def minus_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = Cart.objects.get(cart_id=_cart_id(request))
    cart_item = CartItem.objects.get(product=product, cart=cart)

    if cart_item.quantity >= 2:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        pass
    return redirect('cart:cart_detail')


def cart_detail(request, total=0, counter=0, cart_items=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, active=True)

        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            counter += cart_item.quantity
    except ObjectDoesNotExist:
        pass

    return render(request, 'cart/cart.html',
                  dict(cart_items=cart_items, total=total, counter=counter, cart=cart))


def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id=_cart_id(request)
        )
        cart.save()

    if request.method == 'POST':
        form = AddToCartForm(request.POST)
        if form.is_valid():
            try:
                cart_item = CartItem.objects.get(product=product, cart=cart)
                cart_item.quantity += form.cleaned_data['quantity']
                cart_item.save()
            except CartItem.DoesNotExist:
                cart_item = CartItem.objects.create(
                    product=product,
                    quantity=form.cleaned_data['quantity'],
                    cart=cart
                )
                cart_item.save()
    return redirect('cart:cart_detail')


def remove_cart(request, product_id):
    cart = Cart.objects.get(cart_id = _cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    cart_item.delete()
    return redirect('cart:cart_detail')

# class OrderLV(ListView):
#     model = Order
#     template_name = 'order/order.html'
#     context_object_name = 'order'
#
#     def get_queryset(self):
#         return Order.objects.filter(tags__name=self.kwargs.get('p_name'))  # 태그명칭 전달
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['p_name'] = self.kwargs['p_name']
#         return context
