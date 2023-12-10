import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
import os

creds = 'tempfile.temp'


# Sign up Definition
def Signup():
    global pwordE
    global nameE
    global roots

    # New Window Sign up
    roots = Tk()
    roots.title('Signup')
    roots.geometry("750x350")
    roots.configure(background="#aefff8")

    intruction = Label(roots, text='       Please Enter New Credentials\n', bg="#aefff8", fg="#000000",
                       font="cambria 32 bold")
    intruction.grid(row=0, column=0, columnspan=4, sticky=N)

    # Name and Password
    nameL = Label(roots, text='New Username: ', bg="#aefff8", fg="#000000", font="cambria 20")
    pwordL = Label(roots, text='New Password: ', bg="#aefff8", fg="#000000", font="cambria 20")
    nameL.grid(row=1, column=1, sticky=W, )
    pwordL.grid(row=2, column=1, sticky=W, )

    nameE = Entry(roots, font="cambria 18 bold", justify="center")
    pwordE = Entry(roots, show='*', font="cambria 18 bold", justify="center")
    nameE.grid(row=1, column=2, )
    pwordE.grid(row=2, column=2, )

    nameA = Label(roots, text='\n', bg="#aefff8", fg="#000000", font="cambria 20")
    nameA.grid(row=3, column=1, )

    # Sign Up Button
    signupButton = Button(roots, text='Signup', command=FSSignup, font="cambria 18 bold")
    signupButton.grid(row=4, column=0, columnspan=4, sticky=S)
    roots.mainloop()


def FSSignup():
    with open(creds, 'w') as f:
        f.write(nameE.get())
        f.write('\n')
        f.write(pwordE.get())
        f.close()

    roots.destroy()
    Login()


def Login():
    global nameEL
    global pwordEL
    global rootA

    rootA = Tk()
    rootA.title('Login')
    rootA.geometry("600x350")
    rootA.configure(background="#aefff8")

    intruction = Label(rootA, text='Please Login\n', bg="#aefff8", fg="#000000", font="cambria 32 bold")
    intruction.grid(row=0, column=0, columnspan=4, )

    nameL = Label(rootA, text='       Username: ', bg="#aefff8", fg="#000000", font="cambria 20")
    pwordL = Label(rootA, text='       Password: ', bg="#aefff8", fg="#000000", font="cambria 20")
    nameL.grid(row=1, column=1, )
    pwordL.grid(row=2, column=1, )

    nameEL = Entry(rootA, font="cambria 20 bold", justify="center")
    pwordEL = Entry(rootA, show='*', font="cambria 20 bold", justify="center")
    nameEL.grid(row=1, column=2, )
    pwordEL.grid(row=2, column=2, )

    nameB = Label(rootA, text='\n', bg="#aefff8", fg="#000000", font="cambria 10")
    nameB.grid(row=3, column=1, )

    loginB = Button(rootA, text='Login', command=CheckLogin, font="cambria 15 bold")
    loginB.grid(row=4, column=0, columnspan=4, )

    rmuser = Button(rootA, text='Delete User', fg='red', command=DelUser, font="cambria 15 bold")
    rmuser.grid(row=5, column=0, columnspan=4, )
    rootA.mainloop()


def CheckLogin():
    with open(creds) as f:
        data = f.readlines()
        uname = data[0].rstrip()
        pword = data[1].rstrip()

    if nameEL.get() == uname and pwordEL.get() == pword:
        r = Tk()
        r.title(':D')
        r.geometry('250x100')
        r.configure(background="#aefff8")
        rlbl = Label(r, text='\n[+] Logged In. Please exit the 2 windows \nto proceed to the Menu Page', bg="#aefff8",
                     fg="#000000")
        rlbl.pack()
        r.mainloop()

    else:
        r = Tk()
        r.title('D:')
        r.geometry('250x100')
        r.configure(background="#aefff8")
        rlbl = Label(r, text='\n[!] Invalid Login. \nPlease Try Again.', bg="#aefff8", fg="#000000")
        rlbl.pack()
        r.mainloop()


def DelUser():
    os.remove(creds)
    rootA.destroy()
    Signup()


if os.path.isfile(creds):
    Login()
else:
    Signup()


class Firstpage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background="#aefff8")
        Label = tk.Label(self, text="HEALTH TRACKER", font="cambria 25 bold", bg="#aefff8", fg="#000000")
        Label.grid(row=0, column=1)
        Label = tk.Label(self,
                         text="\n There are two main components on this application:\nBody Statistics: BMI and Calorie Calculator\nActions to be fit: Workout planner",
                         font="cambria 18", bg="#aefff8", fg="#000000")
        Label.grid(row=2, column=1)
        Label = tk.Label(self, text="\nChoose the program you want...", font="cambria 18", bg="#aefff8", fg="#000000")
        Label.grid(row=3, column=1)

        Button = tk.Button(self, text="BMI Calculator", font="cambria 15 bold", bg="#7F7D9C",
                           command=lambda: controller.show_frame(Secondpage))
        Button.grid(row=5, column=0, padx="50", pady="20")

        Button = tk.Button(self, text="Calorie Calculator", font="cambria 15 bold", bg="#7F7D9C",
                           command=lambda: controller.show_frame(Thirdpage))
        Button.grid(row=5, column=1, pady="20")

        Button = tk.Button(self, text="Workout Planner", font="cambria 15 bold", bg="#7F7D9C",
                           command=lambda: controller.show_frame(Fourthpage))
        Button.grid(row=5, column=2, padx="20", pady="20")


class Secondpage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background="#aefff8")

        def name(self):
            name = tk.StringVar

        # Labels
        Label = tk.Label(self, text="BMI Calculator", font="cambria 20 bold", bg="#aefff8", fg="#000000")
        Label.grid(row=0, column=0, )
        Label = tk.Label(self, text="\nWelcome to the BMI Calculator!", font="cambria 18", bg="#aefff8", fg="#000000")
        Label.grid(row=1, column=0, )
        Label = tk.Label(self,
                         text="\nAllow us to assist you in calculating your Body Mass Index (BMI). \nBMI is a statistical measure of an individual's weight scaled by height that is \nused to determine whether a person is underweight, normal, overweight, or obese.  \nBMI is measured in kilograms per square meter. \nBMI is calculated as: bmi = weight/(height*height) \n\nLET US NOW COMPUTE YOURS!",
                         font="cambria 13", bg="#aefff8", fg="#000000")
        Label.grid(row=2, column=0, pady="20", padx="20", )

        Label = tk.Label(self, text="Name: ", font="cambria 13 bold", bg="#aefff8", fg="#000000")
        Label.grid(row=3, column=0, padx="20")
        Label = tk.Label(self, text="(Gender)Type 'm' if male while 'f' if female: ", font="cambria 13 bold",
                         bg="#aefff8", fg="#000000")
        Label.grid(row=4, column=0, pady="20", padx="20")
        Label = tk.Label(self, text="Enter your height in meters: ", font="cambria 13 bold", bg="#aefff8", fg="#000000")
        Label.grid(row=5, column=0, pady="20", padx="20")
        Label = tk.Label(self, text="Enter your weight in kilograms: ", font="cambria 13 bold", bg="#aefff8",
                         fg="#000000")
        Label.grid(row=6, column=0, pady="20", padx="20")

        # Entrybar
        my_name = tk.StringVar()
        self.entry1 = tk.Entry(self, font="cambria 13 bold", justify="center", textvariable=my_name)
        self.entry1.grid(row=3, column=1, columnspan=4)

        my_gender = tk.StringVar()
        self.entry2 = tk.Entry(self, font="cambria 13 bold", justify="center", textvariable=my_gender)
        self.entry2.grid(row=4, column=1, columnspan=4)

        my_height = tk.StringVar()
        self.entry3 = tk.Entry(self, text="", font="cambria 13 bold", justify="center", textvariable=my_height)
        self.entry3.grid(row=5, column=1, columnspan=4)

        my_weight = tk.StringVar()
        self.entry4 = tk.Entry(self, text="", font="cambria 13 bold", justify="center", textvariable=my_weight)
        self.entry4.grid(row=6, column=1, columnspan=4)

        # Buttons
        Button1 = tk.Button(self, text="Home", font="cambria 18 bold", bg="#7F7D9C",
                            command=lambda: controller.show_frame(Firstpage))
        Button1.grid(row=7, column=1, )

        Button2 = tk.Button(self, text="Compute", font="cambria 18 bold", bg="#7F7D96", command=self.computeClick)
        Button2.grid(row=7, column=2)

        self.clear_button = tk.Button(self, text="Reset", font="cambria 18 bold", bg="#7F7D96", command=self.clear_text)
        self.clear_button.grid(row=7, column=3, )

        # Definition

    def computeClick(self):
        global computeLabel
        bmi = float(self.entry4.get()) / (float(self.entry3.get()) ** 2)
        gender = str(self.entry2.get())
        if bmi < 18.5 and gender == "f":
            self.computeLabel = tk.Label(self, text="You are underweight since your BMI is:" + str(bmi),
                                         font="cambria 13 bold", bg="#aefff8", fg="#000000")
            self.computeLabel.grid(row=7, column=0)
        elif bmi < 18.5 and gender == "m":
            self.computeLabel = tk.Label(self, text="You are underweight since your BMI is:" + str(bmi),
                                         font="cambria 13 bold", bg="#aefff8", fg="#000000")
            self.computeLabel.grid(row=7, column=0)
        elif bmi >= 18.5 and bmi <= 24.9 and gender == "f":
            self.computeLabel = tk.Label(self, text="You are normal since your BMI is:" + str(bmi),
                                         font="cambria 13 bold", bg="#aefff8", fg="#000000")
            self.computeLabel.grid(row=7, column=0)
        elif bmi >= 18.5 and bmi <= 22.9 and gender == "m":
            self.computeLabel = tk.Label(self, text="You are normal since your BMI is:" + str(bmi),
                                         font="cambria 13 bold", bg="#aefff8", fg="#000000")
            self.computeLabel.grid(row=7, column=0)
        elif bmi >= 25 and bmi <= 29.9 and gender == "f":
            self.computeLabel = tk.Label(self, text="You are overweight since your BMI is:" + str(bmi),
                                         font="cambria 13 bold", bg="#aefff8", fg="#000000")
            self.computeLabel.grid(row=7, column=0)
        elif bmi >= 23 and bmi <= 24.9 and gender == "m":
            self.computeLabel = tk.Label(self, text="You are at risk to overweight since your BMI is:" + str(bmi),
                                         font="cambria 13 bold", bg="#aefff8", fg="#000000")
            self.computeLabel.grid(row=7, column=0)
        elif bmi >= 30 and gender == "f":
            self.computeLabel = tk.Label(self, text="You are obese since your BMI is:" + str(bmi),
                                         font="cambria 13 bold", bg="#aefff8", fg="#000000")
            self.computeLabel.grid(row=7, column=0)
        elif bmi >= 25 and bmi <= 29.9 and gender == "m":
            self.computeLabel = tk.Label(self, text="You are overweight since your BMI is:" + str(bmi),
                                        font="cambria 13 bold", bg="#aefff8", fg="#000000")
            self.computeLabel.grid(row=7, column=0)
        elif bmi >= 30 and gender == "m":
            self.computeLabel = tk.Label(self, text="You are obese since your BMI is:" + str(bmi),
                                         font="cambria 13 bold", bg="#aefff8", fg="#000000")
            self.computeLabel.grid(row=7, column=0)

        else:
            self.computeLabel = tk.Label(self, text="There is an error with your input", font="cambria 13 bold",
                                         bg="#aefff8", fg="#000000")
            self.computeLabel.grid(row=7, column=0)

    def clear_text(self):
        self.entry1.delete(0, 'end')
        self.entry2.delete(0, 'end')
        self.entry3.delete(0, 'end')
        self.entry4.delete(0, 'end')
        self.computeLabel.destroy()


class Thirdpage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background="#aefff8")

        def name(self):
            name = tk.StringVar

        # Labels
        Label = tk.Label(self, text="Calorie Calculator", font="cambria 20 bold", bg="#aefff8", fg="#000000")
        Label.grid(row=0, column=0, )
        Label = tk.Label(self, text="Welcome to the Calorie Calculator!", font="cambria 18", bg="#aefff8", fg="#000000")
        Label.grid(row=1, column=0, )
        Label = tk.Label(self,
                         text="Allow us to help you in knowing the right amount of calories you need to intake daily.\nThe formula we'll use is the Harris-Benedict formula. \nThere are two parts: first is finding your basic calorie consumption or your BMR; \nand then calculating your total calorie consumption which is based on how active you are.",
                         font="cambria 13", bg="#aefff8", fg="#000000")
        Label.grid(row=2, column=0, pady="10", padx="10")

        Label = tk.Label(self, text="Name: ", font="cambria 13 bold", bg="#aefff8", fg="#000000")
        Label.grid(row=3, column=0, padx="20")
        Label = tk.Label(self, text="(Gender)Type 'm' if male while 'f' if female: ", font="cambria 13 bold",
                         bg="#aefff8", fg="#000000", justify=RIGHT)
        Label.grid(row=4, column=0, pady="5", padx="20")
        Label = tk.Label(self, text="Enter your height in meters: ", font="cambria 13 bold", bg="#aefff8", fg="#000000",
                         justify=RIGHT)
        Label.grid(row=5, column=0, pady="5", padx="20")
        Label = tk.Label(self, text="Enter your weight in kilograms: ", font="cambria 13 bold", bg="#aefff8",
                         fg="#000000", justify=RIGHT)
        Label.grid(row=6, column=0, pady="5", padx="20")
        Label = tk.Label(self, text="Enter your age: ", font="cambria 13 bold", bg="#aefff8", fg="#000000",
                         justify=RIGHT)
        Label.grid(row=7, column=0, pady="5", padx="20")
        Label = tk.Label(self, text="How active are you?: ", font="cambria 13 bold", bg="#aefff8", fg="#000000",
                         justify=RIGHT)
        Label.grid(row=8, column=0)
        Label = tk.Label(self, text="If sedentary, Input 1", font="cambria 13 bold", bg="#aefff8", fg="#000000",
                         justify=RIGHT)
        Label.grid(row=9, column=0)
        Label = tk.Label(self, text="If lightly active, Input 2", font="cambria 13 bold", bg="#aefff8", fg="#000000",
                         justify=RIGHT)
        Label.grid(row=10, column=0)
        Label = tk.Label(self, text="If moderately active, Input 3", font="cambria 13 bold", bg="#aefff8", fg="#000000",
                         justify=RIGHT)
        Label.grid(row=11, column=0)
        Label = tk.Label(self, text="If you are going on an intensive traning, Input 4", font="cambria 13 bold",
                         bg="#aefff8", fg="#000000", justify=RIGHT)
        Label.grid(row=12, column=0)
        Label = tk.Label(self, text="If you're a professional athlete, Input 5", font="cambria 13 bold", bg="#aefff8",
                         fg="#000000", justify=RIGHT)
        Label.grid(row=13, column=0)

        # Entrybar
        my_name = tk.StringVar()
        self.entry1 = tk.Entry(self, font="cambria 13 bold", justify="center", textvariable=my_name)
        self.entry1.grid(row=3, column=1, columnspan=4)

        my_gender = tk.StringVar()
        self.entry2 = tk.Entry(self, font="cambria 13 bold", justify="center", textvariable=my_gender)
        self.entry2.grid(row=4, column=1, columnspan=4)

        my_height = tk.StringVar()
        self.entry3 = tk.Entry(self, text="", font="cambria 13 bold", justify="center", textvariable=my_height)
        self.entry3.grid(row=5, column=1, columnspan=4)

        my_weight = tk.StringVar()
        self.entry4 = tk.Entry(self, text="", font="cambria 13 bold", justify="center", textvariable=my_weight)
        self.entry4.grid(row=6, column=1, columnspan=4)

        my_age = tk.StringVar()
        self.entry5 = tk.Entry(self, text="", font="cambria 13 bold", justify="center", textvariable=my_age)
        self.entry5.grid(row=7, column=1, columnspan=4)

        my_active = tk.StringVar()
        self.entry6 = tk.Entry(self, text="", font="cambria 13 bold", justify="center", textvariable=my_active)
        self.entry6.grid(row=8, column=1, columnspan=4)

        # Buttons
        Button1 = tk.Button(self, text="Home", font="cambria 18 bold", bg="#7F7D9C",
                            command=lambda: controller.show_frame(Firstpage))
        Button1.grid(row=15, column=1, )

        Button2 = tk.Button(self, text="Compute", font="cambria 18 bold", bg="#7F7D9C", command=self.computeClick)
        Button2.grid(row=15, column=2)

        self.clear_button = tk.Button(self, text="Reset", font="cambria 18 bold", bg="#7F7D9C", command=self.clear_text)
        self.clear_button.grid(row=15, column=3, )

    def computeClick(self):
        global computeLabel
        global computeLabel1
        gender = str(self.entry2.get())
        p = float(self.entry6.get())
        weight = float(self.entry3.get())
        height = float(self.entry4.get())
        age = float(self.entry5.get())
        if (p > 0) and (p < 6):
            if p == 1:
                o = 1.2
            if p == 2:
                o = 1.375
            if p == 3:
                o = 1.55
            if p == 4:
                o = 1.725
            if p == 5:
                o = 1.9
        else:
            self.computeLabel = tk.Label(self, text="You inputted a wrong number...Try again.", font="cambria 13 bold",
                                         bg="#aefff8", fg="#000000")
            self.computeLabel.grid(row=14, column=0)
        if gender == "m" or gender == "f":
            if gender == "m":
                x = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
                y = x * o
            if gender == "f":
                x = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
                y = x * o
        else:
            self.computeLabel = tk.Label(self, text="An error has occured, you maybe inputted wrong data...Try again.",
                                         font="cambria 13 bold", bg="#aefff8", fg="#000000")
            self.computeLabel.grid(row=14, column=0)
            # Results
        self.computeLabel1 = tk.Label(self, text="\nYour BMR is " + str(x), font="cambria 13 bold", bg="#aefff8",
                                      fg="#000000")
        self.computeLabel1.grid(row=14, column=0)
        self.computeLabel = tk.Label(self, text="The calories you need daily is " + str(y), font="cambria 13 bold",
                                     bg="#aefff8", fg="#000000")
        self.computeLabel.grid(row=15, column=0)

    def clear_text(self):
        self.entry1.delete(0, 'end')
        self.entry2.delete(0, 'end')
        self.entry3.delete(0, 'end')
        self.entry4.delete(0, 'end')
        self.entry5.delete(0, 'end')
        self.entry6.delete(0, 'end')
        self.computeLabel.destroy()
        self.computeLabel1.destroy()


class Fourthpage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background="#aefff8")
        Label = tk.Label(self, text="Welcome to Workout Planner!", font="cambria 15 bold", justify=CENTER, bg="#aefff8",
                         fg="#000000")
        Label.grid(row=1, column=0, columnspan=7)
        Label = tk.Label(self,
                         text="The other two program is to know your body statistics; \nafter that,  what would you like to do next?",
                         font="cambria 15 bold", justify=CENTER, bg="#aefff8", fg="#000000")
        Label.grid(row=2, column=1, columnspan=7)

        # Buttons
        Button = tk.Button(self, text="Gain weight", font="cambria 15 bold", bg="#7F7D96", command=self.computeClick)
        Button.grid(row=5, column=1, padx="20", pady="20")

        Button1 = tk.Button(self, text="Home", font="cambria 15 bold", bg="#7F7D96",
                            command=lambda: controller.show_frame(Firstpage))
        Button1.grid(row=5, column=0, padx="20", pady="20")

        Button = tk.Button(self, text="Maintain weight", font="cambria 15 bold", bg="#7F7D96",
                           command=self.computeClick1)
        Button.grid(row=5, column=2, padx="20", pady="20")

        Button = tk.Button(self, text="Lose weight", font="cambria 15 bold", bg="#7D7F96", command=self.computeClick2)
        Button.grid(row=5, column=3, padx="20", pady="20")

    def computeClick(self):
        global computeLabel1
        global computeLabel2
        global computeLabel3

        self.computeLabel1 = tk.Label(self,
                                      text=" You choose to gain weight,For meal plan consider the following:\n 1. Drink and eat more calories such as milk and fruit & vegetable juices.\n 2. Eat more calories than your body burns. Make use of calorie calculator, aim for 300-500 calories more than you burn normally.\n 3. Eat plenty of protein, aim for 0.7-1 grams of protein per pound of body weight. Consider eating high-protein foods such as meats, fish, egss and dairy products.\n 4. Stay away or limit consumption of junk foods; eat nutritious foods instead like dairy, meat and beans.\n 5. Do not drink water before eating and make use of bigger plates.\n 6. Know your fats intake, look for good polyunsaturated and monounsaturated fats like avocados, walnuts, olive, walnuts and canola oils. \n 7.Indulge once in a while; an occasional slice of cake is fine to satisfy your sweet tooth. Just remember not to overdo it.\n\n For workout plan consider the following:\n1. Strength training can help one to gain weight by building up muscles, it may also stimulate your appetite.\n 2. Consider the following exercises that focuses on strength and muscle-building.\n\n Bodyweight exercises:\n  1. Squats, 2. Push-ups\n 3. Mountain climber, 4. Plank\n  5. Plank hops & jacks, 6. Reverse crunches\n  7. Leg lifts, 8. Scissor kicks\n  9. Flutter kicks\n\nWeighted exercises:\n 1. Lunge, 2. Overhead shoulder press\n  3. Floor press, 4. Set of dumbbells, 5. Bicep curls\n  6. Front raises, 7. Push ups with alternating rows\n",
                                      font="cambria 11 ", bd=1, relief="solid", justify=LEFT, bg="#aefff8",
                                      fg="#000000")
        self.computeLabel1.grid(row=7, column=0, pady="20", padx="20", columnspan=7)
        self.computeLabel2.destroy()
        self.computeLabel3.destroy()

    def computeClick1(self):
        self.computeLabel2 = tk.Label(self,
                                      text=" You choose to maintain weight\nSteps to manage your weight: \n 1. Build more lean muscle, maintain or increase metabolism by continuing to build lean muscle. \n 2. Fight off hunger with more filling foods specifically foods high in fiber; fruits, vgetables, whole grains and lean protein. \n 3. Avoid temptation, limit unhealthy and junk foods intake. \n 4. Count calories, calorie counter will be a huge help to keep track of calorie consumption. \n 5. When you cannot count calorie intake use Plate Method, at least half of your plate should be vegetables and the rest is divided between lean protein and grains \n 6. Weigh yourself regularly, to keep track of what you should consider doing to maintain your weight. \n 7. Eat breakfast, this is the most important meal of the day. Start out with a good breakfast to avoid splurging pr overeating for the rest of the day.",
                                      font="cambria 11 ", bd=1, relief="solid", justify=LEFT, bg="#aefff8",
                                      fg="#000000")
        self.computeLabel2.grid(row=7, column=0, pady="20", padx="20", columnspan=7)
        self.computeLabel1.destroy()
        self.computeLabel3.destroy()

    def computeClick2(self):
        self.computeLabel3 = tk.Label(self,
                                      text="You choose to lose weightFor meal plan consider the following:\n 1. Keep track of what you eat. This is the most common challenge for folks working on weight loss.\n 2. Boost your metabolism, drinking tea and apple cider vinegar is the best option.\n 3. Get enough protein, it helps boost metabolism that will help one lose help and make you feel full longer.\n 4. Cut back on processed foods. Try to get along with less peocssed meat, fast food, white bread, ice cream and pizza, countrol your portion.\n 5. Cut back on carbohydrates, the carbs you eat are converted to a type of blood sugar. You should avoid carbs from processed fruits\n 6. Make a habit of drinking water before eating so that you will feel full more easily.\n 7. Eat high-protein breakfast to boost yourself for the rest of the day.\n 8. Focus on getting good and balanced nutrition instead of going on a diet because diet is a short-term thing.\n 9. Consider the following foods to eat to lose weight:\n Whole eggs, Leafy greens, Lean Beef, \n Chicken Breast, Potatoes, Tuna, \n Beans, Legumes,  Avocadoes,\n Nuts, Chia Seeds, Fruits,\n Yogurt, Oatmeal, Coconut Oil, Low-carb vegetables\n\n For workout plan consider the following:\n 1. Walking is one of the easiest and best exrcises for losing weight.\n 2. Jogging and running are great exercises that can be done anywhere and are easy to incorporate to our daily routines.\n 3. Weight training can help in building strength and promote muscle growth.\n 4. Yoga burns a fair amount of calories and offers many additional health benefits that can promote weight loss.\n 5. Pilates improves strength, balance, flexibility, endurance and overall fitness level.\n 6. Jumping rope is a full body workout that helps to improve cardiovascular health.\n 7. If you want to focus on burning belly fat consider the following:\n Burpees, Mountain Climbers, Planking, \n Russian twists, Bicycle crunches, Flutter kicks,\n Reverse crunches, Bench hop, Jumping jacks,",
                                      font="cambria 11 ", bd=1, relief="solid", justify=LEFT, bg="#aefff8",
                                      fg="#000000")
        self.computeLabel3.grid(row=7, column=0, pady="20", padx="20", columnspan=7)
        self.computeLabel1.destroy()
        self.computeLabel2.destroy()


class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        window = tk.Frame(self)
        window.pack()
        window.grid_rowconfigure(0, minsize=350)
        window.grid_columnconfigure(0, minsize=350)

        self.frames = {}
        for F in (Firstpage, Secondpage, Thirdpage, Fourthpage):
            frame = F(window, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Firstpage)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()


app = Application()
app.mainloop()