from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import*
import pyttsx3 as pp
import threading


engine= pp.init()

voices = engine.getProperty('voices')
print(voices)

engine.setProperty('voices', voices[0].id)

def speak(word):
    engine.say(word)
    engine.runAndWait()


#pyttsx3
bot = ChatBot("My Bot")

convo = [

    'hello',
    'hi there!',
    'What is your name?',
    'My name is Ashot.',
    'what does that mean?',
    'I am a chatbot created by Miss Ashwini thatswhy my name is Ashot.' ,
    'how are you?',
    'I am good. what about you?',
    'In which city you live?',
    'I live in Mumbai',
    'In which language you talk?',
    'I mostly talk in English',
    'by',
    'Nice talking with you, Have a great day',
    'tell me about your college?',
    'Vivekanand Education Society Institute of Technology also known as VESIT or V. E. S. Institute of Technology, established in 1984, is a premier engineering college affiliated with the University of Mumbai. ',
    'who is the principal of VESIT?',
    'DR. (MRS.)J. M. NAIR is the principal of vivekananda education society institude of technology',
    'which companies comes in vesit placement?',
    'Morgan Stanley, Nomura, KPMG, Capgemini, Accenture, Tech Mahindra, ATOS, Diebold, JPMC, L&T, Cognizant, TCS, SAP, IVP, I-Gate and many other companies visit our campus.',
    'Who is the Head of Electronics  Department?',
    'Mrs.Kavita Tewari is the Head of Electronics  Department.',
    'Can you tell me about infrastructure of College?',
    'Amphitheater, Auditorium, Sports, Laboratory, Library, Hostel, Canteen, Language Lab',
    'How many branches of engineering are there in VESIT?',
    'Electronics, Computer, Electronics and Telecommunication, Instrumentation, Information & technology, Al & Data Science, Master of computer Applications, Humanities & Applied Science',
    'Cut off in Vivekanand Education Society Institute of technology?',
    'For JEE MAIN Round 2021 Cut-off by rank was 48950 and 58809 and for MHT CET Round Cut-off by score 2021 Cut-off by score for round 1 is 95.93 and round 2 is 95.38',
    'How are the fests at VESIT, Mumbai?',
    'Praxis, Spurti, Illusion, Utsav and Annual day',
    'Fee structure in VESIT?',
    'For M.C.A	₹1 Lakh (1st Year Fees)	Graduation, BE	₹1.13 Lakhs (1st Year Fees), M.E	₹1.05 Lakhs (1st Year Fees)	Pass in Graduation',
    'what is minimum package for etrx?',
    'Minimum package in VESIT is 3LPA.',
    'What is rank of the college of VESIT?'
    'It comes in NIRF Rank-band from 251-300 every year'

]

trainer = ListTrainer(bot)

# now training the bot with the help of trainer

trainer.train(convo)

# answer = bot.get_response("What is your name?")
# print(answer)

# print("Talk to bot")
# while True:
#     query=input()
#     if query == 'exit':
#         break
#     answer = bot.get_response(query)
#     print("bot: ", answer)

main = Tk()

main.geometry("500x650")

main.title("My Chatbot")
img = PhotoImage(file="bot.png")
 
photoL=Label(main, image=img)

photoL.pack(pady=5)


#take query: It takes audio as input from user and converts it to string..

'''
def takeQuery():
    sr = s.Recognizer()
    sr.pause_threshold = 1
    print("your bot is listening try to speak")
    with s.Microphone() as m:
        try:
            audio = sr.listen(m)
            query = sr.recognize_google(audio, language='eng-in')
            print(query)
            textF.delete(0,END)
            textF.insert(0,query)
            ask_from_bot()
        except Exception as e:
            print(e)
            print("not recognized")
'''


def ask_from_bot():
    query = textF.get()
    answer_from_bot = bot.get_response(query)
    msgs.insert(END,"YOU : " + query)
    print(type(answer_from_bot))
    msgs.insert(END, "BOT : "+ str(answer_from_bot))
    speak(answer_from_bot)
    textF.delete(0, END)
    msgs.yview(END)


frame=Frame(main)

sc = Scrollbar(frame)
msgs = Listbox(frame, width=80, height=20, yscrollcommand=sc.set)

sc.pack(side=RIGHT, fill=Y)

msgs.pack(side=LEFT, fill=BOTH, pady=10)

frame.pack()

#CREATING TEXT FIELD

textF=Entry(main, font=("Verdana", 20))
textF.pack(fill=X, pady=10)

btn=Button(main, text="Ask from bot", font=("Verdana",20), command=ask_from_bot)
btn.pack()


# creating a function 
def enter_function(event):
    btn.invoke()



#going to bind main window with enter key....
main.bind('<Return>', enter_function)

def repeatL():
    while True:
        takeQuery()




t = threading.Thread(target=repeatL)

t.start()

main.mainloop ()
