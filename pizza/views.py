from django.shortcuts import render
# import the form to be used
from .forms import PizzaForm
from .models import Pizza
from django.forms import formset_factory

# Create your views here.
def home(request):
    return render(request, 'pizza/home.html')


def order(request):
    #multiple_form = MultiplePizzaForm()
    # handle different things, post and get request
    if request.method == 'POST':
        # get all information from the form 'based on the form'
        filled_form = PizzaForm(request.POST)
        # check if the information is valid
        if filled_form.is_valid():
            # save the order on the database --- created pizza and them pk
            created_pizza = filled_form.save()
            #accessing the id
            created_pizza_pk = created_pizza.id
            note = 'Thank you for ordering. Your %s %s and %s pizza is on its way' %(filled_form.cleaned_data['size'],
            filled_form.cleaned_data['topping1'],filled_form.cleaned_data['topping2'],)
            filled_form = PizzaForm()
        else:
            created_pizza_pk = None
            note = 'pizza order failed try again'
        return render(request, 'pizza/order.html', {'pizzaform': filled_form, 'created_pizza_pk': created_pizza_pk, 'note':note} )

    else:
        form = PizzaForm()
        return render(request, 'pizza/order.html', {'pizzaform': form })

def edit_order(request, pk):
    pizza = Pizza.objects.get(pk=pk)
    form = PizzaForm(instance=pizza)
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST, instance=pizza)
        if filled_form.is_valid():
            filled_form.save()
            form = filled_form
            note = 'order has been updated '
            return render(request, 'pizza/edit_order.html', {'note':note, 'pizzaform': form, 'pizza':pizza})
    return render(request, 'pizza/edit_order.html', {'pizzaform': form, 'pizza':pizza})