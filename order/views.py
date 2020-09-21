from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, DetailView, FormView, UpdateView, DeleteView
from order.models import Order, OrderDetail
from cart.models import CartItem, Cart
# from cart.views import _cart_id
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Max
from register.models import User

# # Create your views here.
# def _order_id(request):
#     order = request.session.session_key
#     if not order:
#         order = request.session.create()
#     return order


def cart_to_order(request, cart_id):
    order = Order.objects.create(
        user_id=request.user.id
    )
    order.save()

    cart = Cart.objects.get(id=cart_id)
    cart_item_set = CartItem.objects.filter(cart_id=cart)

    total = 0
    for cart_item in cart_item_set:
        order_details = OrderDetail.objects.create(
            quantity=cart_item.quantity,
            order_id=order.id,
            product_id=cart_item.product_id
        )
        order_details.save()
        total += cart_item.product.price * cart_item.quantity

    order.total_price = total
    order.save()
    cart.delete()

    return redirect('order:detail_order')


def order_detail(request, total=0, counter=0, order_info_set=None):
    try:
        order = Order.objects.filter(user_id=request.user.id).last()
        order_info_set = OrderDetail.objects.filter(order_id=order.id)

        for order_info in order_info_set:
            total += (order_info.product.price * order_info.quantity)
            counter += order_info.quantity

    except ObjectDoesNotExist:
        pass

    return render(request, 'order.html',
                  dict(order_info_set=order_info_set, total=total, counter=counter))


def order_view(request):
    try:
        orders = Order.objects.filter(user_id=request.user.id)
        order_info_set = []
        for order in orders:
            order_info = OrderDetail.objects.filter(order_id=order.id)
            for info in order_info:
                order_info_set.append(info)
            #     OrderDetail.objects.filter(order_id=order.id)
            #     total += (order_info.product.price * order_info.quantity)
            #     counter += order_info.quantity

    except ObjectDoesNotExist:
        pass

    return render(request, 'order/order_list.html',
                  dict(orders=orders, order_info_set=order_info_set))
                  # dict(orders=orders, order_info_set=order_info_set, total=total, counter=counter))



# class OrderLV(ListView):
#     model = Order
#     template_name = 'order/order_all.html'
#     context_object_name = 'orders'
#     paginate_by = 10
#
#     def get_ordering(self):
#         sortby = self.request.GET.get("sort", "-order_dt")
#         return sortby
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         sortby = self.request.GET.get("sort", "-order_dt")
#         context["sortby"] = sortby
#         return context
#
#
# class OrderDV(DetailView):
#     model = OrderDetail
#     #
#     # def get_context_data(self, **kwargs):
#     #     context = super().get_context_data(**kwargs)
#     #     product = self.get_object()
#     #     product.save()
#     #     return context
#
#     context_object_name = 'order'



# def cart_detail(request, total=0, counter=0, cart_items = None):
#     try:
#         cart = Cart.objects.get(cart_id=_cart_id(request))
#         cart_items = CartItem.objects.filter(cart=cart, active=True)
#
#         for cart_item in cart_items:
#             total += (cart_item.product.price * cart_item.quantity)
#             counter += cart_item.quantity
#     except ObjectDoesNotExist:
#         pass
#
#     return render(request, 'cart.html',
#                   dict(cart_items=cart_items, total=total, counter=counter, cart=cart))


# class CartLV(ListView):
#     model = Cart
#     template_name = 'order/cart.html'
#     context_object_name = 'cart'
#
#     def get_queryset(self):
#         return Cart.objects.filter(tags__name=self.kwargs.get('p_name'))  # 태그명칭 전달
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['p_name'] = self.kwargs['p_name']
#         return context
#
#
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

# def cart_to_order(request, cart_id):
#     # # cart = CartItem.objects.get(id=cart_id)
#     # order = Order.objects.create(
#     #     order_id=_order_id(request)
#     # )
#     # order.save()
#
#     cart = Cart.objects.get(id=cart_id)
#     cart_item_set = CartItem.objects.filter(cart_id=cart)
#
#     for cart_item in cart_item_set:
#         order_details = OrderDetail.objects.create(
#             quantity=cart_item.quantity,
#             order_id=order.id,
#             product_id=cart_item.product_id
#         )
#         order_details.save()
#
#     cart.delete()
#
#     return redirect('order:detail_order')
#
