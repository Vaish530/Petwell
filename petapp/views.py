from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
import django.contrib.auth as auth
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from . models import Login,Appointment
# Create your views here.





from chatterbot import ChatBot 
from chatterbot.trainers import ListTrainer

bot=ChatBot('chatbot',read_only=False,logic_adapters=[
  
  {
  
     'import_path':'chatterbot.logic.BestMatch',
     'default_response':'Sorry I dont know whart that means',
     'maximum_similarity_threshold':0.90
  }



])
list_to_train=[
   
    "hi",
    "hi there!",
    "what's the use of you?",
    "Iam here you to assist about pet dog nutrionous food and heatlh care of your pet..",
    
    "What is the best food for a puppy?", "Puppies need high-quality puppy food rich in protein, fats, vitamins, and minerals for growth. Look for food labeled 'for puppies' or 'for all life stages.',",
    
    "How often should I feed my adult dog?", "Most adult dogs do well with two meals a day. However, some small or high-energy dogs may need three meals.,",
    
    "Can dogs eat fruits and vegetables?", "Yes, dogs can eat certain fruits and veggies like apples, carrots, and blueberries. Avoid grapes, raisins, and onions as they can be toxic.,",
    
    "How do I know if my pet is overweight?", "Signs of overweight pets include difficulty feeling the ribs, lack of a visible waist, and trouble moving. A vet can confirm with a body condition score.,",
    
    "What are some healthy treats for dogs?", "Healthy treats include small amounts of carrots, cucumber, sweet potatoes, and specially formulated low-calorie dog treats.,",
    
    "How much water should my dog drink daily?", "Dogs generally need about one ounce of water per pound of body weight daily. Ensure they always have fresh water available.,",
    
    "Can I feed my dog human food?", "Certain human foods are safe, but some are harmful. Safe foods include plain cooked chicken, rice, and some vegetables. Avoid chocolate, onions, garlic, and salty foods.,",
    
    "What kind of diet should a senior dog have?", "Senior dogs benefit from a diet with lower calories, moderate protein, and added joint-support ingredients like glucosamine.,",
    
    "Is raw food safe for dogs?", "Raw diets can work but come with risks of bacterial contamination. Consult your vet if you’re considering a raw diet.,",
    
    "My dog has a sensitive stomach. What food should I choose?", "Choose foods formulated for sensitive digestion, usually with limited ingredients, and avoid common allergens like grains or chicken.,",
    
    "How can I prevent my pet from getting fleas and ticks?", "Use regular flea and tick preventatives like topical treatments, oral tablets, or collars, as recommended by your vet.,",
    
    "What vaccinations does my dog need?", "Core vaccines for dogs include rabies, distemper, parvovirus, and adenovirus. Your vet may also recommend additional vaccines based on lifestyle.,",
    
    "How can I tell if my dog has food allergies?", "Signs include itching, digestive issues, or ear infections. If you suspect allergies, try a limited-ingredient diet and consult your vet.,",
    
    "Can I give my dog bones to chew?", "Raw bones can be safe for some dogs, but avoid cooked bones as they can splinter. Always supervise your dog when chewing bones.,",
    
    "How do I know if my dog is in pain?", "Signs of pain in dogs include limping, reduced activity, whimpering, and changes in appetite or behavior.,",
    
    "Are grains bad for dogs?", "Not necessarily. Some dogs have grain allergies, but most dogs can digest grains like rice and oats without issues.,",
    
    "How often should my dog have a check-up?", "Most healthy dogs benefit from an annual check-up. Senior dogs or pets with health issues may need visits every six months.,",
    
    "Can dogs eat dairy products?", "Some dogs are lactose intolerant. Small amounts of plain yogurt or cheese may be okay, but avoid large servings of milk.,",
    
    "What can I do to improve my dog’s dental health?", "Regular tooth brushing, dental treats, and chews can help. Some dogs benefit from professional cleanings.,",
    
    "How can I keep my dog at a healthy weight?", "Measure food portions, provide daily exercise, and avoid overfeeding treats. Check weight regularly and consult your vet for guidance.,"





]

trainer=ListTrainer(bot)
trainer.train(list_to_train)

def index(request):
  return render(request,"index.html")
def services(request):
  return render(request,"services.html")
def bowlsparadise(request):
  return render(request,"bowlsparadise.html")

def training(request):
  return render(request,"Training.html")
def mapindex(request):
  return render(request,"mapindex.html")

def healthline(request):
  return render(request,"healthline.html")
def user_login(request):
  if request.method=='POST':
   ownername=request.POST['ownername']
   email=request.POST['email']
   password=request.POST['password']
   confirmpassword=request.POST['confirmpassword']
   s=Login(ownername=ownername,email=email,password=password,confirmpassword=confirmpassword)
   s.save()
   return render(request,"index.html")
  else:
    return render(request,"login.html")
def appointment(request):
  if request.method=='POST':
    nameofowner=request.POST['nameofowner']
    emailid=request.POST['emailid']
    contactno=request.POST['contactno']
    petbreed=request.POST['petbreed']
    gender=request.POST['gender']
    age=request.POST['age']
    description=request.POST['description']
    a=Appointment(nameofowner= nameofowner,emailid=emailid, contactno= contactno, petbreed= petbreed,gender=gender,age=age,description=description)
    a.save()
    messages.success(request, "Appointment created successfully!")
    return render(request,"healthline.html")    
  else:
       
    return render(request,"appointment.html")

def chatbot(request):
  return render(request,"chatbot.html")

def getUserResponse(request):
    userMessage = request.GET.get('userMessage')
    if userMessage:
        chatResponse = str(bot.get_response(userMessage))
        return HttpResponse(chatResponse)
    else:
        # Return an appropriate response if userMessage is missing
        return HttpResponse("No message provided.", status=400)
 



  
                                


 





