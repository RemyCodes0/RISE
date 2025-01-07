from django.shortcuts import redirect, render
from . import models
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return redirect('logins') 
    questions = models.Question.objects.all()
    all_questions = questions.count()

    if all_questions == 0: 
        ratio = 0
    else:
        answered = models.Valid.objects.filter(user=request.user).count()
        ratio = answered / all_questions
    percentage = ratio * 100
    return render(request, "taxo/index.html", {'level': questions, "percentage": percentage })
def play(request, user_id):
    
    if request.user.is_authenticated:
        questions = models.Question.objects.all() 
        all_questions =questions.count()
        answered = models.Valid.objects.filter(user = request.user).count()
        ratio = answered/all_questions
        percentage = ratio*100
        user = request.user
        asked = models.Question.objects.get(pk =1)
        try:
            my = models.Valid.objects.get(user= user, asked= asked, finish = True)
        except models.Valid.DoesNotExist:
            change = models.Valid.objects.create(user= user, asked= asked, finish = True)
            change.save() 
        back = models.Useful.objects.get(pk=1)
        level = models.Question.objects.all()
        correct = [ str(level.asked) for level in models.Valid.objects.filter(user = user_id)]
        for i in level:
            for j in correct:
                if i.level == j:
                    print("okay")
        return render(request, 'taxo/play.html', {'stage':level, 'correct':correct, 'back':back, "percentage":percentage})
    else:
        return redirect("indexed")

def question(request, question_id):
    level = models.Question.objects.get(pk = question_id)
    back = models.Useful.objects.get(pk=1)
    if request.method == "POST":
        answer = request.POST.get('answer')
        if answer == level.answer:
            user = request.user
            try:
                asked = models.Question.objects.get(pk = question_id+1)
            except:
                asked = models.Question.objects.get(pk = question_id)
            try:
                my = models.Valid.objects.get(user= user, asked= asked, finish = True)
            except models.Valid.DoesNotExist:
                change = models.Valid.objects.create(user= user, asked= asked, finish = True)
                change.save()
            return redirect('correct', level.pk)        
        else:
            message ='bad'
            return render(request, 'taxo/question.html', {'stage':level, "back":back, 'message':message})
    return render(request, 'taxo/question.html', {'stage':level, 'back':back})


def correct(request, correct_id):
    try:
        next = models.Question.objects.get(pk = correct_id+1)
    except:
        next = 0
    back = models.Useful.objects.get(pk=1)
    level = models.Question.objects.get(pk = correct_id)
    return render(request, 'taxo/correct.html', {"stage": level, "next": next, 'back':back})

def answer(request, answer_id):
    try:
        next = models.Question.objects.get(pk = answer_id+1)
    except:
        next = 0
    user = request.user
    asked = models.Question.objects.get(pk = answer_id+1)
    try:
        my = models.Valid.objects.get(user= user, asked= asked, finish = True)
    except models.Valid.DoesNotExist:
        change = models.Valid.objects.create(user= user, asked= asked, finish = True)
        change.save()
    back = models.Useful.objects.get(pk=1)
    answer = models.Question.objects.get(pk = answer_id)
    return render(request, "taxo/answer.html", {'stage':answer, "next":next, 'back':back})

def option(request):
    back = models.Useful.objects.get(pk=1)
    if request.method == "POST":
        my_progression= models.Valid.objects.filter(user = request.user)
        my_progression.delete()
        return redirect('index')
    return render(request, 'taxo/option.html', {'back':back})

def about(request):
    return render(request, 'taxo/about.html')

def indexed(request):
    if not request.user.is_authenticated:
        print("not authenticated")
        return redirect("logins") 
    return redirect("index")

def logins(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request.POST, username= username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            form = AuthenticationForm()
            return render(request, "taxo/registration/logins.html", {'message':'login'})
    return render(request, "taxo/registration/logins.html")

def logouts(request):
    logout(request)
    return redirect("logins")

def signup(request):
    if request.method == 'POST':
        form= UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('logins')
    else:
        form = UserCreationForm()
        
    return render(request, "taxo/registration/signup.html", {"form": form})
        
