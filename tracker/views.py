

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from .models import Transaction
from .forms import TransactionForm
from datetime import date


@login_required
def dashboard(request):
    transactions = Transaction.objects.filter(user=request.user).order_by('-date')
    transaction_type = request.GET.get('type')
    category = request.GET.get('category')

    if transaction_type:
        transactions = transactions.filter(transaction_type=transaction_type)

    if category:
        transactions = transactions.filter(category=category)

    today = date.today()

    monthly_transactions = Transaction.objects.filter(
        user=request.user,
        date__year=today.year,
        date__month=today.month
    )
    monthly_income = 0
    monthly_expense = 0

    for mt in monthly_transactions:
        if mt.transaction_type == 'Income':
            monthly_income += mt.amount
        else:
            monthly_expense += mt.amount

    monthly_savings = monthly_income - monthly_expense


    total_income = 0
    total_expense = 0

    for t in transactions:
        if t.transaction_type == 'Income':
            total_income += t.amount
        else:
            total_expense += t.amount

    balance = total_income - total_expense

    return render(request, 'tracker/dashboard.html', {
        'transactions': transactions,
        'total_income': total_income,
        'total_expense': total_expense,
        'balance': balance,
        'monthly_income': monthly_income,
        'monthly_expense': monthly_expense,
        'monthly_savings': monthly_savings,
    })


@login_required
def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return redirect('dashboard')
    else:
        form = TransactionForm()

    return render(request, 'tracker/add_transaction.html', {'form': form})


@login_required
def edit_transaction(request, id):
    transaction = get_object_or_404(Transaction, id=id, user=request.user)

    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = TransactionForm(instance=transaction)

    return render(request, 'tracker/edit_transaction.html', {'form': form})


@login_required
def delete_transaction(request, id):
    transaction = get_object_or_404(Transaction, id=id, user=request.user)
    transaction.delete()
    return redirect('dashboard')


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'tracker/register.html', {'form': form})


def login_view(request):
    error = None

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            error = 'Invalid username or password'

    return render(request, 'tracker/login.html', {'error': error})


def logout_view(request):
    logout(request)
    return redirect('login')