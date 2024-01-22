from datetime import date
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Asana
from users.models import Profile
from django.views.decorators.csrf import csrf_exempt
import numpy as np
import os
import pickle

base=os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(base, 'heart_disease.pickle.dat')   #full path to text.
file_path1 = os.path.join(base,"diabetes.sav")


heart_model = pickle.load(open(file_path, "rb"))
diabetes_model = pickle.load(open(file_path1, 'rb'))




def underweight(amr):
    pr = (15 / 100) * amr
    pr = "Protein Intake : {:.2f} Cal".format(pr)
    ca = (55 / 100) * amr
    ca = "Carbs Intake : {:.2f} Cal".format(ca)
    fa = (25 / 100) * amr
    fa = "Fat Intake : {:.2f} Cal".format(fa)

    dict = ["TIPS",
            pr,
            ca,
            fa,
            "Eating at least 5 portions of a variety of fruit and vegetables every day.",
            "Basing meals on potatoes, bread, rice, pasta or other starchy carbohydrates. Choose wholegrain where possible.",
            "Having some dairy or dairy alternatives (such as soya drinks and yoghurts). Have whole (full-fat) milk until you build your weight back up.",
            "Eating some beans, pulses, fish, eggs, meat and other protein. Aim for 2 portions of fish every week – 1 of which should be oily, such as salmon or mackerel.",
            "Choosing unsaturated oils and spreads, such as sunflower or rapeseed, and eating them in small amounts.",
            "Drinking plenty of fluids. The government recommends 6 to 8 glasses a day. But try not to have drinks just before meals to avoid feeling too full to eat."
            ]
    return dict


def overweight(amr):
    pr = (15 / 100) * amr
    pr = "Protein Intake : {:.2f} Cal".format(pr)
    ca = (55 / 100) * amr
    ca = "Carbs Intake : {:.2f} Cal".format(ca)
    fa = (25 / 100) * amr
    fa = "Fat Intake : {:.2f} Cal".format(fa)

    dict = [
        "TIPS",
        pr,
        ca,
        fa,
        "Skip the sugary drinks. Sugary drinks, such as soda, juice, sweet tea, and sports drinks, add extra calories with little or no nutritional value. ",
        "People who regularly drink sugary beverages are more likely to be overweight. Choose water or low-fat milk most of the time.",
        "Exercise. Regular physical activity burns calories and builds muscle — both of which help you look and feel good and can help keep weight off.",
        "Walking the family dog, cycling to school, and doing other things that increase your daily level of activity can make a difference.",
        "If you want to burn more calories, increase the intensity of your workout and add some strength exercises to build muscle.",
        "Reduce screen time. People who spend a lot of time in front of screens are more likely to be overweight. Set reasonable limits on the amount of time you spend watching TV, playing video games, and using computers, phones, and tablets not related to school work. Turn off all screens at least an hour before bedtime so you can get enough sleep.",
        "Watch portion sizes. Big portions pile on extra calories that can cause weight gain.",
        "Choose smaller portions, especially when eating high-calorie snacks. When eating away from home, try sharing an entree or save half your meal to take home.",
        "Eat 5 servings of fruits and veggies a day. Fruits and veggies are about more than just vitamins and minerals.",
        "They're also packed with fiber, which means they fill you up. And when you fill up on fruits and veggies, you're less likely to overeat.",
    ]
    return dict


def normal(amr):
    pr = (15 / 100) * amr
    pr = "Protein Intake : {:.2f} Cal".format(pr)
    ca = (55 / 100) * amr
    ca = "Carbs Intake : {:.2f} Cal".format(ca)
    fa = (25 / 100) * amr
    fa = "Fat Intake : {:.2f} Cal".format(fa)
    dict = [
        "TIPS",
        pr,
        ca,
        fa,
    ]
    return dict


def obese(amr):
    pr = (15 / 100) * amr
    pr = "Protein Intake : {:.2f} Cal".format(pr)
    ca = (55 / 100) * amr
    ca = "Carbs Intake : {:.2f} Cal".format(ca)
    fa = (25 / 100) * amr
    fa = "Fat Intake : {:.2f} Cal".format(fa)
    dict = [
        "TIPS",
        pr,
        ca,
        fa,
    ]
    return dict


def index(request):
    return render(request, 'index.html')


@login_required(login_url='/users/login/')
def dashboard(request):
    asana = Asana.objects.all()
    uid = request.user.id
    c_user = Profile.objects.get(user_id=uid)
    today = date.today()
    age = today.year - c_user.dob.year
    diet = c_user.diet.all()

    # BMR CALCULATION
    if c_user.gender == 'Female':
        bmr = 655.1 + (9.563 * float(c_user.weight)) + (1.850 * float(c_user.height)) - (4.676 * float(age))
    else:
        bmr = 66.47 + (13.75 * float(c_user.weight)) + (5.003 * float(c_user.height)) - (6.755 * float(age))

    # AMR CALCULATION
    if c_user.exercise_frequency == '0':
        amr = bmr * 1.2
    elif c_user.exercise_frequency == '1':
        amr = bmr * 1.375
    elif c_user.exercise_frequency == '2':
        amr = bmr * 1.55
    elif c_user.exercise_frequency == '3':
        amr = bmr * 1.725
    else:
        amr = bmr * 1.9

    # BMI CALCULATION
    bmi = (c_user.weight / ((c_user.height / 100) ** 2))
    if bmi < 18.5:
        type = underweight(amr)
        bodytype = "Underweight"
    elif 18.5 <= bmi <= 24.9:
        type = normal(amr)
        bodytype = "Normal"
    elif 25 <= bmi <= 29.9:
        type = overweight(amr)
        bodytype = "Overweight"
    else:
        type = obese(amr)
        bodytype = "Obese"

    return render(request, 'dashboard.html', {'asana': asana,
                                              'diet': diet,
                                              'bmr': "{:.2f}".format(bmr),
                                              'amr': "{:.2f}".format(amr),
                                              'bmi': "{:.2f}".format(bmi),
                                              'type': type,
                                              'bodytype': bodytype})


@login_required(login_url='/dashboard/')
def yoga(request):
    return render(request, 'yoga.html')


@csrf_exempt
def heart(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        phone = request.POST['phone']
        gender = request.POST['gender']
        nmv = float(request.POST['nmv'])
        tcp = float(request.POST['tcp'])
        eia = float(request.POST['eia'])
        thal = float(request.POST['thal'])
        op = float(request.POST['op'])
        mhra = float(request.POST['mhra'])
        age = float(request.POST['age'])
        pred = heart_model.predict(
        np.array([nmv, tcp, eia, thal, op, mhra, age]).reshape(1, -1))
        return render(request, 'hresult.html',{ 'fn':firstname, 'ln':lastname, 'age':age, 'r':pred, "gender":gender})  
    else:
        return render(request, 'heart.html')
    
@csrf_exempt
def diabetes(request):
    if request.method == 'POST':
        
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        phone = request.POST['phone']
        gender = request.POST['gender']
        pregnancies = request.POST['pregnancies']
        glucose = request.POST['glucose']
        bloodpressure = request.POST['bloodpressure']
        insulin = request.POST['insulin']
        bmi = request.POST['bmi']
        diabetespedigree = request.POST['diabetespedigree']
        age = request.POST['age']
        skinthickness = request.POST['skin']
        pred = diabetes_model.predict(
            [[pregnancies, glucose, bloodpressure, skinthickness, insulin, bmi, diabetespedigree, age]])
        return render(request, 'dresult.html',{ 'fn':firstname, 'ln':lastname, 'age':age, 'r':pred, "gender":gender})  
    else:
        return render(request, 'diabetes.html')