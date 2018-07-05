import random
import secrets
import math

#SIMULATED ANNEALING --KEVIN CORPENY CS461 UMKC
###########################################
####    AGENT & ENVIORNMENT SETUP     #####
x = 1
class Student(object):
    def __init__(self,stu_num,file1):
        self.fin = file1
        self.preferences = dict()
        self.stu_num = 0
        self.added = False

        clean_line = self.fin.readline().strip().split()
        x=1

        #NUM_CHARS = 10
        for char in clean_line:
            if char not in {"A","B","C","D","E","X"}:
                self.stu_num = str(self.stu_num) + str(char)
            else:
                if char == "X":
                    break
                self.preferences[char] = x
                x+=1
        self.stu_num = int(self.stu_num)

    def add_class(self):
        self.added = True

    def rem_class(self):
        self.added = False

    def is_added(self):
        return self.added

    def display_prefs(self):
        print(self.preferences)
        print(self.stu_num)

    def get_prefs(self):
        return self.preferences

    def get_num(self):
        return self.stu_num



#FIX THIS SHIT
class Schedule(object):
    def __init__(self,stuLST,labs = {}):
        self.labs = {"A":[],"B":[],"C":[],"D":[],"E":[] }
        self.stuLST = stuLST
        self.score = 0
        '''THIS SHOULD FILL THE LABS DICTIONARY W/ APPROPRIATE STUDENTS
                        IT WILL ASSIGN W/ A DEGREE OF ETROPY
        '''
        #   FOR OPTIMIZATION
        #S = 100 (num of students in stu_list)
        for stud in stuLST:
            labsLst = ["A","B","C","D","E"]
            #P = 5
            for item in labsLst:
                if stud.is_added():
                    break
                #this 'entropy' variable will be used to change the enviornment upon each init
                #print(key,value)

                entropy = secrets.randbelow(5)
                if entropy == 2:
                    continue

                #print(stud.get_prefs()[x])
                if (len(self.labs[item])<20) and (stud.is_added() == False):
                    try:
                        self.labs[item].append(stud)
                        stud.add_class()
                        #print(stud.get_prefs())
                        self.score += (stud.get_prefs()[item]**2)
                    except KeyError:
                        continue

            if stud.is_added() == False:
                for key,value in self.labs.items():
                    if (len(self.labs[key])<20) and (key in stud.get_prefs().items()):
                        self.labs[key].append(stud)
                        stud.add_class()
                        self.score += stud.get_prefs()[key]**2


        #print("Score: {}".format(self.score))
        for item in self.stuLST:
            item.rem_class()


    def get_labs(self):
        for x in {"A","B","C","D","E"}:
            print(len(self.labs[x]))

            for stud in self.labs[x]:
                #print("LAB {}".format(x),file = self.output)
                #print(str(stud.get_num()),file = self.output)
                print(" ")

    def get_score(self):
        self.score = 0
        for x in ["A","B","C","D","E"]:
            for stud in self.labs[x]:
                #this hack may be error-prone
                if(x in set(stud.get_prefs().keys())):
                    self.score += stud.get_prefs()[x]**2
                    print(stud.get_num())
                    #print("HI")
        print(self.score)
        return self.score

    def gimme_score(self):
        return self.score

    def new_swap(self):
        lab_choices  = ["A","B","C","D","E"]
        first_lab = lab_choices[secrets.randbelow(5)]
        second_lab = lab_choices[secrets.randbelow(5)]

        if(first_lab == second_lab):
            self.new_swap()

        first_student = self.labs[first_lab][random.randint(0,len(self.labs[first_lab])-1)]
        second_student = self.labs[second_lab][random.randint(0,len(self.labs[second_lab])-1)]


        available_labs = set(first_student.get_prefs().keys()).intersection(set(second_student.get_prefs().keys()))

        if available_labs != {}:
            holder = self.labs[first_lab][random.randint(0,len(self.labs[first_lab])-1)]
            first_student = second_student
            second_student = holder
            self.get_score()
            return self
        else:
            self.new_swap()


    '''
    def swap(self):
        lab_choices  = ["A","B","C","D","E"]

        #get the keys for which labs to search
        lab1_swap = lab_choices[secrets.randbelow(5)]
        lab2_swap = lab_choices[secrets.randbelow(5)]
        print(lab1_swap)
        print(lab2_swap)

        #we want to change lab sections so we can't have equality here
        if((lab1_swap == lab2_swap) or (len(self.labs[lab1_swap]) == 0) or (len(self.labs[lab2_swap]) == 0)):
            #recursive call
            return self.swap()


        #this ought to grab two different random students
        if((len(self.labs[lab1_swap]) > 1) and (len(self.labs[lab2_swap]) > 1)):
            person1_swap = self.labs[lab1_swap][random.randint(0,len(self.labs[lab1_swap])-1)]
            person2_swap = self.labs[lab2_swap][random.randint(0,len(self.labs[lab2_swap])-1)]
        else:
            person1_swap = self.labs[lab1_swap][0]
            person2_swap = self.labs[lab2_swap][0]

        if(person1_swap == person2_swap):
            return self.swap()

        print(person1_swap)
        print(person2_swap)

        #the intersection of the sets of keys between the selected STUDENTS
        #will give a set with the lab sections available to both.
        allowable_labs = set()
        allowable_labs = set(person1_swap.get_prefs().keys()).intersection(set(person2_swap.get_prefs().keys()))
        print(allowable_labs)

        #holder needed for swap obviously
        holder = person1_swap

        #making sure each student can in fact change labs
        if(allowable_labs != {}):
            person2_swap = person1_swap
            person1_swap = holder
            #self.labs[lab1_swap][secrets.randbelow(len(self.labs[lab1_swap]))] = person2_swap
            #self.labs[lab2_swap][secrets.randbelow(len(self.labs[lab2_swap]))] = holder
            self.get_score()
        else:
            return self.swap()

        return self
    '''



#EVALUATION FUNCTIONALITY
my_file = open("input1.txt","r")
my_file2 = open("input2.txt","r")
output = open("output.txt","w")
stu_lst = []

#getting students from both files
for x in range(100):
    holder = Student(0,my_file)
    stu_lst.append(holder)

out = open("output.txt", "w")
iters = 0
changes = 0
#in case no changes are made
noChange = 0
rando = 20
TEMP = 100
#Env1.get_labs()
#Env1.get_score()
best = Schedule(stu_lst)

while True:
    print("Changes: {}\nIterations: {}".format(changes,iters))
    if(best.gimme_score() < 25):
        print("unknown error")

        quit()
    if(best.gimme_score() < 200):
        break
    iters+=1
    if(iters == 10000):
        TEMP *= .95
        iters = 0
    Env1 = Schedule(stu_lst)

    try:
        accepted = math.exp((-(Env1.gimme_score() - best.gimme_score())) / TEMP )
    except OverflowError:
        #print(error)
        continue
    print(accepted)
    if((Env1.gimme_score() < best.gimme_score()) or (accepted > random.random())):
        best = Env1
        changes += 1

    if(noChange == 4000):
        break
    if(changes == 1000):
        TEMP *= .95
        changes = 0
        noChange = 0
    if(TEMP < 1):
        break
    #print(iters)
    print("Current Best Score: {}".format(best.gimme_score()))
    print(TEMP)
    noChange +=1
best.get_labs()
print(str(best.gimme_score()),file = output)
my_file.close()
my_file2.close()
