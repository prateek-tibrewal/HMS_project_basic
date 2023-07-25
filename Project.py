print('Welcome to HOSTEL MANAGEMENT SYSTEM')
beds2=int(input('Enter the Total number of Two Bed Rooms:- '))
beds3=int(input('Enter the Total number of Three Bed Rooms:- '))
beds4=int(input('Enter the Total number of Four Bed Rooms:- '))
roomtypeA=[]
roomtypeB=[]
roomtypeC=[]
for i in range (1,beds2+1):
    Kk= "A" + str(i)
    for j in range (1,3):
        if j ==1:
            Bed_no= str(Kk) + "-i"
        elif j ==2:
            Bed_no= str(Kk) + "-ii"
        roomtypeA.append(Bed_no)
for i in range (1,beds3+1):
    Kk= "B" + str(i)
    for j in range (1,4):
        if j ==1:
            Bed_no= str(Kk) + "-i"
        elif j ==2:
            Bed_no= str(Kk) + "-ii"
        elif j ==3:
            Bed_no= str(Kk) + "-iii"
        roomtypeB.append(Bed_no)
for i in range (1,beds4+1):
    Kk= "C" + str(i)
    for j in range (1,5):
        if j ==1:
            Bed_no= str(Kk) + "-i"
        elif j ==2:
            Bed_no= str(Kk) + "-ii"
        elif j ==3:
            Bed_no= str(Kk) + "-iii"
        elif j ==4:
            Bed_no= str(Kk) + "-iv"
        roomtypeC.append(Bed_no)
ques='Yes'
Student_Data={}
while ques=='Yes':
    print('What you want to do? Enter Your Choice')
    Choice=input('A: Add new student details\nB: Get Student Details\nC: Delete a Student Record\nD: Update Student Details\nE: Print Bill :- ')
    if (Choice=='A'):
        data={}
        print("PLEASE ENTER ALL THE INFORMATION CAREFULLY AND CORRECTLY")
        name=str(input("Enter the Name of the student/candidate:- "))
        rollno=int(input("Enter the student/canditate's Roll ID (XXXXX):- "))
        fname=str(input("Enter the Name of the student/candidate's Father:- "))
        dob=input("Enter the Date Of Birth (Day-Month-Year):- ")
        adrno=int(input("Enter the student/canditate's Aadhar No.(XXXXXXXXXXXX):- "))
        food=input('Enter the food preferences (Veg/Non-Veg):- ')
        phoneno=int(input("Enter the contact number:- "))
        Address=input("Enter the current home address of the student/candidate:- ")
        Library=input("Is library alloted (Yes/No):- ")
        Course=input("Enter the Name and Year of the Course/Degree:- ")
        print("Enter Entry Date, i.e., date of arrival (DD/MM/YYYY):- ")
        w=tuple(int(x) for x in input("").split("/"))
        print("Enter Exit Date, i.e., date of leaving (DD/MM/YYYY):- ")
        e=tuple(int(x) for x in input("").split("/"))
        d = e[0]- w[0]
        m = e[1]- w[1]
        y = e[2]- w[2]
        if(d<0):
            d = w[0]- e[0]
            numberofdaysofstay= (m*30)+(y*365)-d
        elif(m<0):
            m = w[1]- e[1]
            numberofdaysofstay= (y*365)+d-(m*30)
        elif(d<0)and(m<0):
            d = w[0]- e[0]
            m = w[1]- e[1]
            numberofdaysofstay= (y*365)-(m*30)-d
        elif(d<0)and(m<0)and(y<0):
            print("INCORRECT INPUT")
        elif(y<0):
            print("INCORRECT INPUT")
        else:
            numberofdaysofstay= (y*365)+(m*30)+d
        print("Therefore no. of days to be stayed is = ",numberofdaysofstay)
        a=999
        b=699
        c=399
        cs=''
        data['Name']=name
        data["Father's Name"]=fname
        data['Roll No.']=rollno
        data['Address']=Address
        data['Aadhar No.']=adrno
        data['Phone No.']=phoneno
        data['Course Details']=Course
        while cs != 'A' and cs != 'B' and cs != 'C':
            print("Enter the type of room required. (PLEASE FILL CAREFULLY)")
            print("A- 2 Bed Room - Rs.999/- per month\nB- 3 Bed Room - Rs.699/- per month\nC- 4 Bed Room - Rs.399/- per month")
            cs=str(input("Enter the corresponding letter of the bedroom choice you require:- "))
            if cs=='A':
                total= numberofdaysofstay*a/30
                rbts=roomtypeA[0]
                data["Room Number"]=rbts[0]+rbts[1]
                data['Room-Bed Number']=roomtypeA[0]
                print("The assigned Bed No. is:- ",roomtypeA[0])
                del roomtypeA[0]
            elif cs=='B':
                total= numberofdaysofstay*b/30
                rbts=roomtypeB[0]
                data["Room Number"]=rbts[0]+rbts[1]
                data['Room-Bed Number']=roomtypeB[0]
                print("The assigned Bed No. is:- ",roomtypeB[0])
                del roomtypeB[0]
            elif cs=='C':
                total= numberofdaysofstay*c/30
                rbts=roomtypeC[0]
                data["Room Number"]=rbts[0]+rbts[1]
                data['Room-Bed Number']=roomtypeC[0]
                print("The assigned Bed No. is:- ",roomtypeC[0])
                del roomtypeC[0]
            else:
                print("|INCORRECT INPUT. PLEASE ENTER THE DETAILS CAREFULLY|")
        data['Food Type']=food
        data['Library']=Library
        data['Date of Birth']=dob
        data['Selected Room type']=cs
        data['Number of Days of Stay']=numberofdaysofstay
        data['Entry date']=w
        data['Exit date']=e
        Student_Data[rollno]=data
        print(Student_Data[rollno])
        ques=input('Do you want to continue:(Yes/No):- ')
    elif (Choice == 'B'):
        roll=int(input('Enter the Roll No. of the student whose data is to be retrieved:- '))
        print('The student details is as follows:- ')
        print(Student_Data[roll])
        ques=input('Do you want to continue:(Yes/No):- ')
    elif (Choice == 'C'):
        roll=int(input("Enter the Roll No. of the student whose data is to be deleted:- "))
        Student_Data.pop(roll)
        ques=input('Do you want to continue:(Yes/No):- ')
    elif (Choice == 'D'):
        roll=int(input('Enter the Roll No. of the student whose data is required to be updated:- '))
        update_dict=Student_Data[roll]
        r1=int(input("Enter what needs to be updated:-\n1: Name\n2: Father's name\n3: Address\n4: Aadhar No.\n5: Phone No.\n6: Course Details \n7: Food Type \n8: Library \n9: Date of Birth :- "))
        r2={1: 'Name', 2: "Father's Name", 3: 'Address', 4: 'Aadhar No.', 5: 'Phone No.', 6: 'Course Details', 7: 'Food Type', 8: 'Library', 9: 'Date of Birth'}
        r3=r2[r1]
        print("Enter the change You want in",r3)
        strg=input('')
        r4=r2[r1]
        update_dict[r4]=strg
        Student_Data[roll]=update_dict
        ques=input('Do you want to continue (Yes/No):- ')
    elif (Choice == 'E'):
        roomtype=""
        cost_per_month=0
        roll=int(input('Enter the Roll No. of the student whose bill is to be printed:- '))
        r5=int(input('Enter what you want to print:- \n1:Monthly Bill    2:Total Bill :- '))
        r6=Student_Data[roll]
        r7=r6['Number of Days of Stay']
        r8=r6['Entry date']
        r9=r6['Exit date']
        r10=r6['Name']
        r11=r6["Father's Name"]
        r12=r6['Food Type']
        r13=r6['Phone No.']
        r14=r6['Course Details']
        r15=r6['Library']
        r16=r6['Selected Room type']
        r17=r6['Room-Bed Number']
        if r16=='A':
            roomtype="Two Bed Room"
            cost_per_month=999
        elif r16=='B':
            roomtype="Three Bed Room"
            cost_per_month=699
        elif r16=='C':
            roomtype="Four Bed Room"
            cost_per_month=399
        if r5==1:
            print("===== HOSTEL BILL =====")
            print("Name:-", r10,"       Fathers Name:-", r11)
            print("Entry date:-", r8[0],'-', r8[1],'-', r8[2],)
            print("Exit date:-", r9[0],'-', r9[1],'-', r9[2],)
            print("Contact Number:-",r13,"       Food Preference:-",r11)
            print("Number of Days of Stay:-",r7,"      Library:-",Library)
            print("Room Type:-",roomtype,"       Course Details:-",r14,"     Room-Bed Number:-",r17)
            print("Monthly room rent:- Rs.",cost_per_month)
            print("Monthly mess fees:- Rs. 999")
            print("Total (excluding tax):- Rs.", cost_per_month+999)
            print("GST  12% :- Rs.", (cost_per_month+999)*12/100)
            print("Total (including tax) :- Rs.", (cost_per_month+999)*112/100)
        elif r5==2:
            print("===== HOSTEL BILL =====")
            print("Name:-", r10,"       Fathers Name:-", r11)
            print("Entry date:-", r8[0],'-', r8[1],'-', r8[2],)
            print("Exit date:-", r9[0],'-', r9[1],'-', r9[2],)
            print("Phone Number:-",r13,"       Food Type:-",r11)
            print("Number of Days of Stay:-",r7,"      Library:-",Library)
            print("Room Type:-",roomtype,"       Course Details:-",r14,"     Room-Bed Number:-",r17)
            print("Monthly room rent:- Rs.",cost_per_month)
            print("Total room rent:- Rs.", cost_per_month*r7/30)
            print("Monthly mess fees:- Rs. 999")
            print("Total mess fees:- Rs.", 999*r7/30)
            print("Total (excluding tax):- Rs.", (cost_per_month*r7/30)+(999*r7/30))
            print("Discounted Price (5%_discount):- Rs.", ((cost_per_month*r7/30)+(999*r7/30))*95/100)
            print("GST  12%:- Rs. ", (((cost_per_month*r7/30)+(999*r7/30))*95/100)*12/100)
            print("Total (including tax):- Rs.", (((cost_per_month*r7/30)+(999*r7/30))*95/100)*112/100)
        else:
            print("|YOU ARE REQUESTED TO ENTER EITHER '1' OR '2'. PLEASE ENTER THE VALUE CAREFULLY|")
        ques=input("Do you want to continue (Yes/No):- ")
    else:
        print("|WRONG INPUT FOUND. PLEASE RE-ENTER|")
        ques='Yes'
