from operator import attrgetter
import random
import time

#--------------------------------------
#----------------PART 1----------------
#--------------------------------------

#inicialization of variables

n = int(input("Enter the size of the knapsack problem:\n"))
n = round(n)
if 0>=n  : #this is used to avoid any problems
    while True:
        n = int(input("Please enter a valid value:\n"))
        n = round(n)
        if(0<n):
            break
v_max = int(input("Enter the value of V Max:\n"))
v_max = round(v_max)
if 0>=v_max  : #this is used to avoid any problems
    while True:
        v_max = int(input("Please enter a valid value for V Max:\n"))
        v_max = round(v_max)
        if(0<v_max):
            break
v_min = int(input("Enter the value of V Min:\n"))
v_min = round(v_min)
if v_min>=v_max  or 0>=v_min: 
    while True:
        v_min = int(input("Please enter a valid value for V Min:\n"))
        v_min = round(v_min)
        if(v_min<v_max and 0<v_min):
            break
w_max = int(input("Enter the value of W Max:\n"))
w_max = round(w_max)
if 0>=w_max  : #this is used to avoid any problems
    while True:
        w_max = int(input("Please enter a valid value for W Max:\n"))
        w_max = round(n)
        if(0<w_max):
            break
w_min = int(input("Enter the value of W Min:\n"))
w_min = round(w_min)
if w_min>=w_max or 0>=w_min:
    while True:
        w_min = int(input("Please enter a valid value for W Min:\n"))
        w_min = round(w_min)
        if(w_min<w_max and 0<w_min):
            break
weight =round((w_max+w_min)/2*(n*0.3))

main_array = []

k = int(input("Choose how many instances you would like to run:\n"))
k = round(k)
cont=0
if 0>=k  : #this is used to avoid any problems
    while True:
        k = int(input("Please enter a valid value:\n"))
        k = round(k)
        if(0<k):
            break
for i in range(k):
    cont=cont+1
#for creating objects
    class Array: 
        def __init__(self, v,w,r):
            self.v = v
            self.w = w
            self.r =  r

        def __repr__(self):
            return '{:f} : {:f} : {:f}'.format(self.v, self.w, self.r)

#creating the output file
    file = open("outputfile"+ str(cont) +".txt","w")
    file.write("" + str(n) + "     ")
    file.write("" + str(weight) + "\n")

    for i in range(n):
        v = random.randint(v_min,v_max)
        w = random.randint(w_min,w_max)
        r = (round(v/w,2))
        main_array.append(Array(v,w,r)) #this will be useful later on
    
     
        file.write("" + str(v) + "     ")
        file.write("" + str(w) + "\n")

    file.close()




#--------------------------------------
#----------------PART 2----------------
#--------------------------------------

    decision = int(input("Select your heuristic: [1. W]   [2. V]  [3. R]:\n"))

    if decision < 1 or decision > 3:
        while True:
            decision = int(input("Please enter a valid value for the heuristic [1. W]   [2. V]  [3. R:\n"))
            decision = (decision)
            if(decision>=1 and 3>=decision):
                break
    start_time = time.time()
    if decision ==1:

#****Heuristic W****

#for sorting from smallest value to the largest

        heuristic_w_sort = sorted(main_array, key =attrgetter('w'))

        main_array = heuristic_w_sort

        for i in range(0, len(main_array)-1):
            if (main_array[i].w) == (main_array[i+1].w):
                if (main_array[i].v) < (main_array[i+1].v):

                    (main_array[i].v), (main_array[i+1].v) = (main_array[i+1].v), (main_array[i].v)

        heuristic_w_sort = main_array



#for the sum and result of f(x) in heuristic w
        w_sum=0
        w_bar=0

        for i in range(0, len(main_array)):

            w_sum=w_sum+(main_array[i].v)
            w_bar=w_bar+(main_array[i].w)
            if weight<w_bar:
                w_sum=w_sum-(main_array[i].v)
                w_bar=w_bar-(main_array[i].w)
                break

        print("Heuristic W: f(x) " + str(w_sum) + "\n")


    if decision ==2:
#****Heuristic V****

        heuristic_v_sort = sorted(main_array, key =attrgetter('v'), reverse=True)

        main_array = heuristic_v_sort


        for i in range(0, len(main_array)-1):
            if (main_array[i].v) == (main_array[i+1].v):
                if (main_array[i].w) < (main_array[i+1].w):

                    (main_array[i].w), (main_array[i+1].w) = (main_array[i+1].w), (main_array[i].w)

        heuristic_v_sort = main_array


#sum of f(x) in heuristic v
        v_sum=0
        w_bar=0

        for i in range(0, len(main_array)):
            v_sum=v_sum+(main_array[i].v)
            w_bar=w_bar+(main_array[i].w)
            if weight<w_bar:
                v_sum=v_sum-(main_array[i].v)
                w_bar=w_bar-(main_array[i].w)

        print("Heuristic V: f(x) " + str(v_sum) + "\n")

    if decision ==3:
#****Heuristic R****

        heuristic_r_sort = sorted(main_array, key =attrgetter('r'), reverse=True)

        main_array = heuristic_r_sort


        for i in range(0, len(main_array)-1):
            if (main_array[i].r) == (main_array[i+1].r):
                if (main_array[i].w) < (main_array[i+1].w):

                    (main_array[i].w), (main_array[i+1].w) = (main_array[i+1].w), (main_array[i].w)

        heuristic_v_sort = main_array

#sum of f(x) in heuristic r
        r_sum=0
        w_bar=0


        for i in range(0, len(main_array)):

            r_sum=r_sum+(main_array[i].v)
            w_bar=w_bar+(main_array[i].w)
            if weight<w_bar:

                r_sum=r_sum-(main_array[i].v)
                w_bar=w_bar-(main_array[i].w)
        print("Heuristic R: f(x) " + str(r_sum) + "\n")


    end_time = time.time()
    final_time = round(end_time - start_time,1)

    print("Execution time: " + str(final_time) + "\n")




