TitleImagebool=False
Bg_Imagebool=False
WebTitle_Headingsbool=False
Form_Optionsbool=False
AddPageNavbool=False


#declaration test
'''
Option1NameValue="Tab 1"
Option1NameValue="Tab 2"
Option1NameValue="Tab 3"
'''
NavBarOptioncommentstart=""
NavBarOptioncommentend=""

from tkinter import*

mainwindow=Tk()
mainwindow.title("Web Pie")
mainwindow.iconbitmap(r'C:\Users\Administrator\Desktop\python projects\python_web_project\Images\pie.ico')
mainwindow.geometry("1400x700")

frame=Frame(mainwindow,relief=RIDGE, borderwidth=20,bg="LIGHTBLUE")
frame.pack(anchor=E,fill=BOTH,expand=True)

#inserting image on background
#bg= PhotoImage(file="BgImage01.png",width=1090,height=605)
#Label1= Label(frame,image= bg)
#Label1.place(x=0,y=0)



#defining functions for radio :
lable=Label(frame)
lable.place(x=3,y=610)


def selection1():
    selection = "You selected the option ------> " + var1.get()  
    lable.config(text = selection)

    #from here second radiobutton starts
    selected=var1.get()
    print(selected)

    #For getting option for only selected option
    if selected=="TitleImage":
        TitleImagebool=True
        Bg_Imagebool=False
        WebTitle_Headingsbool=False
        Form_Optionsbool=False
        AddPageNavbool=False
    elif selected=="Bg_Image":
        TitleImagebool=False
        Bg_Imagebool=True
        WebTitle_Headingsbool=False
        Form_Optionsbool=False
        AddPageNavbool=False
    elif selected=="WebTitle_Headings":
        TitleImagebool=False
        Bg_Imagebool=False
        WebTitle_Headingsbool=True
        Form_Optionsbool=False
        AddPageNavbool=False
    elif selected=="Form_Options":
        TitleImagebool=False
        Bg_Imagebool=False
        WebTitle_Headingsbool=False
        Form_Optionsbool=True
        AddPageNavbool=False
    elif selected=="AddPageNav" :
        TitleImagebool=False
        Bg_Imagebool=False
        WebTitle_Headingsbool=False
        Form_Optionsbool=False
        AddPageNavbool=True

    else:
        TitleImagebool=False
        Bg_Imagebool=False
        WebTitle_Headingsbool=False
        Form_Optionsbool=False
        AddPageNavbool=False


    #getting radiobutton according to selected
    if TitleImagebool is True:
        global option11, option12, option13, option14 ,var2 ,lable11 ,dropForImageSize ,selectedImageSize ,ImageSizelabel, option15

        lable11=Label(frame)
        lable11.place(x=250,y=610)

        var2=StringVar()

        option11=Radiobutton(master=frame,image=option1Img,variable=var2,value="basketball",relief=RAISED,  command=selection2)
        option12=Radiobutton(master=frame,image=option2Img,variable=var2,value="swimming",relief=RAISED,   command=selection2)
        option13=Radiobutton(master=frame,image=option3Img,variable=var2,value="football",relief=RAISED,   command=selection2)
        option14=Radiobutton(master=frame,image=option4Img,variable=var2,value="Karata",relief=RAISED,   command=selection2)
        option15=Radiobutton(master=frame,image=option5Img,variable=var2,value="Add",relief=RAISED, indicatoron=False,    command=selection2)        


        #Dropdown menu for imagesize
        optionsForImgSize = [
            50,80,110,140,170,200,230,260,290,320
        ]

        selectedImageSize=IntVar()
        selectedImageSize.set(optionsForImgSize[0])

        dropForImageSize= OptionMenu(frame,selectedImageSize,*optionsForImgSize)
        
        #To Submit the values
        submitImage= Button(frame,text="Submit...",font=("copperplate",20),width=10,command=submitImgCom).pack(side=BOTTOM,pady=120)

        ImageSizelabel=Label(master=frame,text="Image Size",font=("roman",16),fg="blue",bg="lightblue")



        option11.place(x=10,y=10)
        option12.place(y=110,x=10)
        option13.place(y=210,x=10)
        option14.place(y=310,x=10)
        option15.place(y=410,x=10)
        dropForImageSize.place(x=150,y=60)
        ImageSizelabel.place(x=150,y=20)

        

    elif TitleImagebool is False:
        option11.destroy()
        option12.destroy()
        option13.destroy()
        option14.destroy()
        option15.destroy()
        lable11.destroy()
        dropForImageSize.destroy()
        ImageSizelabel.destroy()
        
    else:
        pass

        
    if Bg_Imagebool is True:
        global option21, option22, option23, option24 ,var3 ,lable21
        print("Hi")
        lable21=Label(frame)
        lable21.place(x=250,y=610)

        var3=StringVar()

        option21=Radiobutton(master=frame,image=option11Img,variable=var3,value="Jaisalmer",relief=RAISED,  command=selection3,width=130,height=100)
        option22=Radiobutton(master=frame,image=option12Img,variable=var3,value="BackgroundImage3",relief=RAISED,   command=selection3,width=130,height=100)
        option23=Radiobutton(master=frame,image=option13Img,variable=var3,value="Goa",relief=RAISED,   command=selection3,width=130,height=100)
        option24=Radiobutton(master=frame,image=option14Img,variable=var3,value="Tajmahal",relief=RAISED,   command=selection3,width=130,height=100)

        option21.place(x=10,y=10)
        option22.place(y=130,x=10)
        option23.place(y=250,x=10)
        option24.place(y=370,x=10)
    elif Bg_Imagebool is False:
        option21.destroy()
        option22.destroy()
        option23.destroy()
        option24.destroy()
        lable21.destroy()    
    else:
        pass

    
    if WebTitle_Headingsbool is True:
        global Webtitletext, Webtitle, PageTitletext, PageTitle ,entryVar1 ,entryVar2, optionforTextSize, optionforTextFont, optionforTextColor,  OptionMenuInTextFontforTitleHeading, OptionMenuInTextSizeforTitleHeading, OptionMenuInTextColorforTitleHeading, selectedTextSizeVariable1, selectedTextFontVariable1, selectedTextColorVariable1, TextColorlabel, TextSizelabel, TextFontlabel ,selectedTextSizeVariable2, selectedTextFontVariable2, selectedTextColorVariable2
        print("3rd is selected")
        entryVar1=StringVar()
        entryVar2=StringVar()
        
        #widgets for inputs from the user
        Webtitletext=Label(master=frame,text="Web Title :")
        Webtitle=Entry(master=frame,width=20,font=("roman",12), textvariable=entryVar1)
        PageTitletext=Label(master=frame,text="Page Title :")
        PageTitle=Entry(master=frame,width=20,font=("roman",12),text="Hello", textvariable=entryVar2)


        #options for attributes in Text
        
        #size

        optionforTextSize = [
            10,20,30,50,80,110,140,170,200,230,260,290,320
        ]

        selectedTextSizeVariable1= IntVar()
        selectedTextSizeVariable1.set(optionforTextSize[3])
        
        selectedTextSizeVariable2= IntVar()
        selectedTextSizeVariable2.set(optionforTextSize[0])

        #OptionMenu for Test Size
        OptionMenuInTextSizeforTitleHeading= OptionMenu(frame,selectedTextSizeVariable1,*optionforTextSize)
        TextSizelabel=Label(master=frame,text="Text Size",font=("roman",10))
        
        
        #Font

        optionforTextFont = [
            "Arial","Verdana","Helvetica",
            "Tahoma","Trebuchet MS","Times New Roman",
            "Georgia","Garamond","Courier New","Monotype Corsiva",
            "Brush Script MT","Monaco","Copperplate"
        ]

        selectedTextFontVariable1= StringVar()
        selectedTextFontVariable1.set(optionforTextFont[0])

        selectedTextFontVariable2= StringVar()
        selectedTextFontVariable2.set(optionforTextFont[9])
        
        ##OptionMenu for Test Font
        OptionMenuInTextFontforTitleHeading= OptionMenu(frame,selectedTextFontVariable1,*optionforTextFont)
        TextFontlabel=Label(master=frame,text="Text Font",font=("roman",10))

        
        
        #Color

        optionforTextColor =[
            "Red","Cyan","Blue",
            "DarkBlue","Lightblue",
            "Purple","Yellow","Lime",
            "Magenta","Olive","Green",
            "Maroon","Brown","Orange",
            "Black","Silver","White"
        ]

        selectedTextColorVariable1= StringVar()
        selectedTextColorVariable1.set(optionforTextColor[14])

        selectedTextColorVariable2= StringVar()
        selectedTextColorVariable2.set(optionforTextColor[14])

        ##OptionMenu for Test Color
        OptionMenuInTextColorforTitleHeading= OptionMenu(frame,selectedTextColorVariable1,*optionforTextColor)
        TextColorlabel=Label(master=frame,text="Text Color",font=("roman",10))

        





        Webtitletext.place(x=20,y=50)
        Webtitle.place(x=80,y=50)
        PageTitletext.place(x=20,y=100)
        PageTitle.place(x=80,y=100)

        #Text attributes for page title
        OptionMenuInTextSizeforTitleHeading.place(x=50,y=175)
        TextSizelabel.place(x=50,y=150)
        OptionMenuInTextFontforTitleHeading.place(x=50,y=275)
        TextFontlabel.place(x=50,y=250) 
        OptionMenuInTextColorforTitleHeading.place(x=50,y=375)
        TextColorlabel.place(x=50,y=350)



        
    elif WebTitle_Headingsbool is False:
        Webtitletext.destroy()
        Webtitle.destroy()
        PageTitletext.destroy()
        PageTitle.destroy()
        OptionMenuInTextSizeforTitleHeading.destroy()   
        OptionMenuInTextFontforTitleHeading.destroy()
        OptionMenuInTextColorforTitleHeading.destroy()
        TextColorlabel.destroy()
        TextFontlabel.destroy()
        TextSizelabel.destroy()


    else:
        pass

    if Form_Optionsbool is True:
        global textforFormInput,  Option_UserName, Option_UserEmail, Option_UserQuery ,submit,formcheckVar_UserName ,formcheckVar_UserEmail,  formcheckVar_UserQuery ,entryFormVar1 ,Form_Ok ,SearchVar, FormTitle,FormTitleText, Option_Search ,FormOption, OptionMenuInTextColorforFormTitle, TextColorlabel01, OptionMenuInTextFontforFormTitle, TextFontlabel01, OptionMenuInTextSizeforFormTitle, TextSizelabel01, Option_UserProfileImage

        print("4Th selected")
        #For search tag
        SearchVar=StringVar()
        Option_Search=Checkbutton(master=frame,text="Add Search option",variable=SearchVar,offvalue="!",onvalue="",indicatoron=True ,state=ACTIVE)
        Option_Search.place(x=150,y=360)



        #form inputs
        entryFormVar1= StringVar()

        FormOption=Label(master=frame,text="Form :",font=("roman",16))
        FormTitleText=Label(master=frame,text="Form Title: ",font=("roman",16))
        FormTitle=Entry(master=frame,width=20,font=("roman",12), textvariable=entryFormVar1)
        

        #Additional Option/Attribute for 'Form Title'
        
        ##for Color
        selectedTextColorVariable2= StringVar()
        selectedTextColorVariable2.set(optionforTextColor[14])
        OptionMenuInTextColorforFormTitle= OptionMenu(frame,selectedTextColorVariable2,*optionforTextColor)
        TextColorlabel01=Label(master=frame,text="Text Color:",font=("roman",10))

        ##For Size
        selectedTextSizeVariable2= IntVar()
        selectedTextSizeVariable2.set(optionforTextSize[0])
        OptionMenuInTextSizeforFormTitle= OptionMenu(frame,selectedTextSizeVariable2,*optionforTextSize)
        TextSizelabel01=Label(master=frame,text="Text Size",font=("roman",10))
        
        ##For Font
        selectedTextFontVariable2= StringVar()
        selectedTextFontVariable2.set(optionforTextFont[9])
        OptionMenuInTextFontforFormTitle= OptionMenu(frame,selectedTextFontVariable2,*optionforTextFont)
        TextFontlabel01=Label(master=frame,text="Text Font",font=("roman",10))


        #Text for Form inputoption
        textforFormInput=Label(master=frame,text="Some FORM Options For Input :",font=(16))


        #Web Buttons For Forms

        formcheckVar_UserName= StringVar()
        formcheckVar_UserEmail= StringVar()
        formcheckVar_UserQuery= StringVar()
        formcheckVar_UserProfileImage= StringVar()

        Option_UserName=Checkbutton(master=frame,text="User_Name",variable=formcheckVar_UserName,onvalue="!",offvalue="",indicatoron=False ,state=ACTIVE)
        Option_UserEmail=Checkbutton(master=frame,text="User_Email",variable=formcheckVar_UserEmail,onvalue="!",offvalue="",indicatoron=False ,state=ACTIVE)
        Option_UserQuery=Checkbutton(master=frame,text="User_Query",variable=formcheckVar_UserQuery,onvalue="!",offvalue="",indicatoron=False ,state=ACTIVE)
        Option_UserProfileImage=Checkbutton(master=frame,text="User_UserProfileImage",variable=formcheckVar_UserProfileImage,onvalue="!",offvalue="",indicatoron=False ,state=ACTIVE)


        #rest main
        FormTitle.place(x=130,y=50)
        FormOption.place(x=10,y=10)
        FormTitleText.place(x=15,y=50)

        textforFormInput.place(x=15,y=320)
        Option_UserName.place(x=20,y=350)
        Option_UserEmail.place(x=20,y=380)
        Option_UserQuery.place(x=20,y=410)
        Option_UserProfileImage.place(x=20,y=440)


        #For text additional options
        OptionMenuInTextSizeforFormTitle.place(x=25, y=120)
        TextSizelabel01.place(x=25,y=100)
        OptionMenuInTextFontforFormTitle.place(x=25, y=190)
        TextFontlabel01.place(x=25,y=170)
        OptionMenuInTextColorforFormTitle.place(x=25, y=260)
        TextColorlabel01.place(x=25,y=240)
        
    

    elif Form_Optionsbool is False:
        textforFormInput.destroy()
        Option_UserName.destroy()
        Option_UserEmail.destroy()
        Option_UserQuery.destroy()
        Option_UserProfileImage.destroy()
        Option_Search.destroy()
        FormOption.destroy()
        FormTitle.destroy()
        FormTitleText.destroy()
        
        #addition option's
        OptionMenuInTextColorforFormTitle.destroy()
        TextColorlabel01.destroy()
        OptionMenuInTextFontforFormTitle.destroy()
        TextFontlabel01.destroy()
        OptionMenuInTextSizeforFormTitle.destroy()
        TextSizelabel01.destroy()



        
    else:
        pass

    
    

    if AddPageNavbool is True:
        global  AddPageNavLabel, selectedNavOption1, selectedNavOption2 ,selectedNavOption3 ,NavOptionSubmit ,NavOptionClear, Option1LinkLabel, Option1LinkEntry ,Option2LinkLabel ,Option2LinkEntry ,Option3LinkLabel ,Option3LinkEntry ,AddPagebaroptionLabel ,selectedNavBarOption1 ,selectedNavBarOption2 ,Option1NameValue,Option2NameValue,Option3NameValue,Page1Option,Page2Option,Page3Option
        
        def Navsubmit() :     
            global Option1NameValue,Page1Option
            a=True
            while a is True:
                global Page1Option,Page2Option,Page3Option,Option1LinkLabel
                    
                if selectedNavOption1Variable.get() =="Yes" and selectedNavOption1Variable.get() != "NO":
                    Page1Option=""
                    global Option1LinkLabel ,Option1LinkEntry,Option1LinkValue ,Option1NameLabel ,Option1NameEntry, Option1NameValue,Option2NameValue,Option3NameValue,AddPagebaroptionabe
                    print("option1 Yes")

                
                    Option1LinkLabel=Label(master=frame,text="Page1 Address :")
                    Option1LinkValue= StringVar()
                    Option1LinkEntry=Entry(master=frame,width=40,font=("roman",12),textvariable=Option1LinkValue)

                    Option1NameLabel=Label(master=frame,text="Name :")
                    Option1NameValue= StringVar()
                    Option1NameEntry=Entry(master=frame,width=10,font=("roman",12),textvariable=Option1NameValue)

                    Option1LinkLabel.place(x=20,y=350)
                    Option1LinkEntry.place(x=120,y=350)
                    Option1NameLabel.place(x=160,y=100)
                    Option1NameEntry.place(x=220,y=100)
                    a=False

                elif selectedNavOption1Variable.get() =="NO":
                    Page1Option="!"
                    Option1LinkLabel.destroy()
                    Option1LinkEntry.destroy()
                    Option1NameLabel.destroy()
                    Option1NameEntry.destroy()
                    a=False
                else:
                    pass

                if selectedNavOption2Variable.get() =="Yes" and selectedNavOption2Variable.get() != "NO":
                    Page2Option=""
                    global Option2LinkLabel ,Option2LinkEntry ,Option2NameLabel ,Option2NameEntry,Option2LinkValue
                    print("option2 Yes")

                
                    Option2LinkLabel=Label(master=frame,text="Page2 Address :")
                    Option2LinkValue= StringVar()
                    Option2LinkEntry=Entry(master=frame,width=40,font=("roman",12),textvariable=Option2LinkValue)
                    
                    Option2NameLabel=Label(master=frame,text="Name :")
                    Option2NameValue= StringVar()
                    Option2NameEntry=Entry(master=frame,width=10,font=("roman",12),textvariable=Option2NameValue)

                    Option2LinkLabel.place(x=20,y=400)
                    Option2LinkEntry.place(x=120,y=400)
                    Option2NameLabel.place(x=160,y=150)
                    Option2NameEntry.place(x=220,y=150)
                    a=False

                elif selectedNavOption2Variable.get() =="NO" :
                    Page2Option="!"
                    Option2LinkLabel.destroy()
                    Option2LinkEntry.destroy()
                    Option2NameLabel.destroy()
                    Option2NameEntry.destroy()
                    a=False
                else:
                    pass


                if selectedNavOption3Variable.get() =="Yes" and selectedNavOption3Variable.get() !="NO":
                    Page3Option=""
                    global Option3LinkLabel ,Option3LinkEntry ,Option3NameLabel ,Option3NameEntry,Option3LinkValue
                    print("option3 Yes")

                
                    Option3LinkLabel=Label(master=frame,text="Page3 Address :")
                    Option3LinkValue= StringVar()
                    Option3LinkEntry=Entry(master=frame,width=40,font=("roman",12),textvariable=Option3LinkValue)

                    Option3NameLabel=Label(master=frame,text="Name :")
                    Option3NameValue= StringVar()
                    Option3NameEntry=Entry(master=frame,width=10,font=("roman",12),textvariable=Option3NameValue)

                    Option3LinkLabel.place(x=20,y=450)
                    Option3LinkEntry.place(x=120,y=450)
                    Option3NameLabel.place(x=160,y=200)
                    Option3NameEntry.place(x=220,y=200)
                    a=False

                elif selectedNavOption3Variable.get() =="NO" :
                    Page3Option="!"
                    Option3LinkLabel.destroy()
                    Option3LinkEntry.destroy()
                    Option3NameLabel.destroy()
                    Option3NameEntry.destroy()
                    a=False
                else:
                    pass

        def NavClear():
            Option1LinkLabel.destroy()
            Option1LinkEntry.destroy()
            Option1NameLabel.destroy()
            Option1NameEntry.destroy()

            Option2LinkLabel.destroy()
            Option2LinkEntry.destroy()
            Option2NameLabel.destroy()
            Option2NameEntry.destroy()

            Option3LinkLabel.destroy()
            Option3LinkEntry.destroy()
            Option3NameLabel.destroy()
            Option3NameEntry.destroy()


        def NavBarOptions():
            global NavBarOptioncommentstart ,NavBarOptioncommentend
            if selectedNavBarOptionVariable.get() == "Yes":
                NavBarOptioncommentstart=""
                NavBarOptioncommentend=""
            elif selectedNavBarOptionVariable.get() == "NO":
                NavBarOptioncommentstart="<!--"
                NavBarOptioncommentend="-->"
        
        AddPagebaroptionLabel= Label(master=frame,text="ADD WEB NAVIGATION BAR :",font=("Times New Roman",16))
        AddPageNavLabel= Label(master=frame,text="Elements For website navigation Bar",font=(16))
        
        selectedNavBarOptionVariable= StringVar()
        selectedNavOption1Variable= StringVar()
        selectedNavOption3Variable= StringVar()
        selectedNavOption2Variable= StringVar()

        selectedNavBarOption1=Radiobutton(master=frame,text="YES",variable=selectedNavBarOptionVariable,value="Yes",command=NavBarOptions)
        selectedNavBarOption2=Radiobutton(master=frame,text="NO",variable=selectedNavBarOptionVariable,value="NO",command=NavBarOptions)
        selectedNavOption1=Checkbutton(master=frame,text="Add Page 1",variable=selectedNavOption1Variable,onvalue="Yes",offvalue="NO",indicatoron=False )
        selectedNavOption2=Checkbutton(master=frame,text="Add Page 2",variable=selectedNavOption2Variable,onvalue="Yes",offvalue="NO",indicatoron=False )        
        selectedNavOption3=Checkbutton(master=frame,text="Add Page 3",variable=selectedNavOption3Variable,onvalue="Yes",offvalue="NO",indicatoron=False )

        NavOptionSubmit=Button(master=frame,text="OK",command=Navsubmit)
        NavOptionClear=Button(master=frame,text="Clear",command=NavClear)

        selectedNavBarOptionVariable.set("NO")

        #placement
        AddPagebaroptionLabel.place(x=10,y=10)
        selectedNavBarOption1.place(x=340,y=10)
        selectedNavBarOption2.place(x=400,y=10)
        AddPageNavLabel.place(x=30,y=50)
        selectedNavOption1.place(x=30,y=100)
        selectedNavOption2.place(x=30,y=150)
        selectedNavOption3.place(x=30,y=200)
        NavOptionSubmit.place(x=150,y=230)
        NavOptionClear.place(x=200,y=230)


    elif AddPageNavbool is False:
        AddPagebaroptionLabel.destroy()
        AddPageNavLabel.destroy()
        selectedNavOption1.destroy()
        selectedNavOption2.destroy()
        selectedNavOption3.destroy()
        NavOptionSubmit.destroy()
        NavOptionClear.destroy()
        selectedNavBarOption1.destroy()
        selectedNavBarOption2.destroy()

        Option1LinkLabel.destroy()
        Option1LinkEntry.destroy()
        Option2LinkLabel.destroy()
        Option2LinkEntry.destroy()
        Option3LinkLabel.destroy()
        Option3LinkEntry.destroy() 
                   




        

    
def selection2():
    selection2 = "You selected the option in TitleImage ------> " + var2.get()  
    lable11.config(text = selection2)

def selection3():
    selection3 = "You selected the option in Bg_Image ------> " + var3.get()  
    lable21.config(text = selection3)

def submitImgCom():

    
    print(f"""
    Web Title is ----->{entryVar1.get()},

    background image is ---->{var3.get()},


    page title is ------> {entryVar2.get()}
    page title Size is -----> {selectedTextSizeVariable1.get()}
    page title Color is -----> {selectedTextColorVariable1.get()}
    page title Font is -----> {selectedTextFontVariable1.get()} 


    image is --->{var2.get()},   size is ----> {selectedImageSize.get()}

    search tag---->{SearchVar.get()}
    
    Selected from forms :
    Form Title: --->{entryFormVar1.get()}

    option 
    1---->{formcheckVar_UserName.get()}, 
    2---->{formcheckVar_UserEmail.get()}, 
    3---->{formcheckVar_UserQuery.get()}""")


    
    if formcheckVar_UserName.get()=="!" and formcheckVar_UserQuery.get()=="!" and formcheckVar_UserEmail.get()=="!":
        Form_Ok="!"
        print("\n<--form ok-->")
    else:
        Form_Ok=""


    #Html script past  

    Web_Title=entryVar1.get()
    Web_Bg_Image=var3.get()


    Page_Title=entryVar2.get()
    Redirect_page=""
    Attach_image=var2.get()
    image_Size=selectedImageSize.get()

    Form=open("Project Details Form","w+")
    Form.write("This is a simple test for A pre written form which I might use")
    Form.close()

    Form=open("Project Details Form","r+")
    print("                   ",Form.name)
    Readstr=Form.read(200)
    print(Readstr)
    Form.close()

    Form=open("Project Details Form","w+")
    print("Project Details: \n")







    Form=open("Project Details Form02.html","w+")
    Form.write(f"""
    <html>
    <head>
    <style>
    html {{
    scroll-behavior: smooth;
    }}

        #section1 {{
        height:100px;
    }}

        #section2 {{
        height:150px;
    }}
    </style>
    <div class="main" id="section1">
    <title>{Web_Title}</title> 
    <style>
    .right {{
    text-align: right;
    }}
    </style>

        
    <style>
    body {{
    font-family: Arial, Helvetica, sans-serif;
    }}

    .navbar {{
    overflow: hidden;
    background-color: #333;
    }}

    .navbar a {{
    float: left;
    font-size: 16px;
    color: white;
    text-align: center;
    padding: 14px 16px;
    text-decoration: none;
    }}

    .dropdown {{
    float: left;
    overflow: hidden;
    }}

    .dropdown .dropbtn {{
    font-size: 16px;  
    border: none;
    outline: none;
    color: white;
    padding: 14px 16px;
    background-color: inherit;
    font-family: inherit;
    margin: 0;
    }}

    .navbar a:hover, .dropdown:hover .dropbtn {{
    background-color: red;
    }}

    .dropdown-content {{
    display: none;
    position: absolute;
    background-color: #f9f9f9;
    min-width: 160px;
    box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
    z-index: 1;
    }}

    .dropdown-content a {{
    float: none;
    color: black;
    padding: 12px 16px;
    text-decoration: none;
    display: block;
    text-align: left;
    }}

    .dropdown-content a:hover {{
    background-color: #ddd;
    }}

    .dropdown:hover .dropdown-content {{
    display: block;
    }}
    </style>
    </style>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>


    </style>

    </head>

    <body background="images/{Web_Bg_Image}.png"
    background-repeat= no-repeat;
    background-size=cover; text="">
        <center>
        
        
        <style>
        p.b {{
            font-size : {2*selectedTextSizeVariable1.get()};
            font-weight:bold;
            font-family:{selectedTextFontVariable1.get()}; 
            color :{selectedTextColorVariable1.get()};
        }}
        </style>
        <p class="b">{Page_Title}</p>
        
        <style>
            img{{
                border-radius:70%;
                width:{selectedImageSize.get()}px;
                border-color: rgb(0, 0, 255);
                border-style:dashed;
            }}
        </style>
        <a href="https://www.youtube.com/results?search_query={Attach_image}">
        <img src="images/{Attach_image}.png" alt="Webpage logo" border="0" aling="right"width="100" height="100"></a>
        

        {NavBarOptioncommentstart}
        <div class="topnav">
        <div class="navbar">
        <{Page1Option}a href={Option1LinkValue.get()}>{Option1NameValue.get()}</a>
        <{Page1Option}a href={Option2LinkValue.get()}>{Option2NameValue.get()}</a>
        <{Page1Option}a href={Option3LinkValue.get()}>{Option3NameValue.get()}</a>
            <div class="dropdown">
    <button class="dropbtn">Features 
        <i class="fa fa-caret-down"></i>
    </button>
    <div class="dropdown-content">
    <a href="#">{Option3NameValue.get()}</a>
        <a href="#">Our Products</a>
        <a href="#">Membership</a>
        </div>
        </div>
        <a href="#section2">Contact US</a>
            <form action="/action_page.php">
    <input text= "Search our website" list="browsers" name="browser">
    <datalist id="browsers">
    <option value="Internet Explorer">
    <option value="Firefox">
    <option value="Chrome">
    <option value="Opera">
    <option value="Safari">
    </datalist>
    <input type="submit" value="Submit">
    {NavBarOptioncommentend}
    </form>

            
        
        
        </div>
        
        
            
        <br><br>
        
        <style>
        p.a {{
            font :italic small-caps bold 20px/20px Georgia, serif;
        }}
        </style>
        <p class="a">Add Website Description here</p>
        <br><br>
        
        <{SearchVar.get()}input type="text" placeholder="Search..">
        
        </div>

        
        <br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
        <style>
        img{{
                border-radius:70%;
                border-color: rgb(0, 0, 255);
                border-style:dashed;
            }}
        h1 {{
            font-size : {selectedTextSizeVariable2.get()};
            font-weight:bold;
            font-family:{selectedTextFontVariable2.get()}; 
            color :{selectedTextColorVariable2.get()};
        }}
        </style>	
        <img src="Attach_image.png" alt="Profile Image" border="2" aling="right" width="200" height=""></a>

        
        <form name="get">
        <h1> {entryFormVar1.get()} </h1>
            <{formcheckVar_UserName.get()}input type="Name" name="User_name"placeholder="Your name"><br><br>
            <{formcheckVar_UserEmail.get()}input type="email" name="User_email"placeholder="Your email address"><br><br>
            <{formcheckVar_UserQuery.get()}textarea input type="Ask your Queries" name="User_Query"placeholder="Ask us Query"></textarea><br>
            <{Form_Ok}input type="submit" value="OK">
        </form>
            

        
        <br><br>
        <address>
                <span><i class="fa fa-map-marker fa-lg"></i> Place your Institute address here  </span><br>
                <a href="tel:123-456-7890">123-456-7890</a><br>
                <span><i class="fa fa-envelope-o fa-lg"></i> <a href="mailto:contact@example.com">contact&#64;example.com</a></span><br>
                <span><i class="fa fa-globe fa-lg"></i> <a href="http://support.example.com">support.example.com</a></span>
        </address>
        <br><br>


        <style>
            img{{
                border-radius:50%;
                border-color: rgb(0, 0, 255);
                border-		style:dashed;
            }}
        </style>
        <a href="https://www.facebook.com/">
        <img src="logo/fb.png" alt="Gmail logo" border="0" aling="right" width="50" height="50"></a>

        <a href="https://www.instagram.com/">
        <img src="logo/insta.png" alt="Instagram logo" border="0" aling="right" width="50" height="50"></a>

        <a href="https://web.whatsapp.com/">
        <img src="logo/wt.png" alt="Whatsapp logo" border="0" aling="right" width="50" height="50"></a>

        <a href="https://accounts.google.com/signin/v2/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin">
        <img src="logo/gmail.png" alt="Youtube logo" border="0" aling="right" width="50" height="50"></a>
        
        <div class="main" id="section2">
        <div class="right">
        <a href="#section1">
        <img src="arrow.png" alt="up Arrow logo" href="#section1" border="0" aling="right" width="50" height="50"></a>
        
        </div>
        </div>

    </body> 



    </html>

    """)

    Form.close()


    Form=open("Project Details Form","r+")
    Readstr=Form.read(9999)
    print(Readstr)

    Form.close()
    print(Form.name)
 



#images in use
option1Img= PhotoImage(file="images/basketball.png",master=frame,width=90,height=70)
option11Img= PhotoImage(file="images/Jaisalmer.png",master=frame,width=140,height=120)

option2Img= PhotoImage(file="images/swimming.png",master=frame,width=90,height=70)
option12Img= PhotoImage(file="images/BackgroundImage3.png",master=frame,width=140,height=120)

option3Img= PhotoImage(file="images/football.png",master=frame,width=90,height=70)
option13Img= PhotoImage(file="images/Goa.png",master=frame,width=140,height=120)

option4Img= PhotoImage(file="images/Karata.png",master=frame,width=90,height=70)
option14Img= PhotoImage(file="images/Tajmahal.png",master=frame,width=140,height=120)

option5Img= PhotoImage(file="images/plusImg.png",master=frame,width=90,height=70)

#execution of first past of the radiobutton script

var1=StringVar()




option1=Radiobutton(master=frame,text="TitleImage",font=("roman",20),relief=RAISED,width=15,variable=var1,value="TitleImage",borderwidth=2,  command=selection1,     activebackground = "blue",activeforeground = "Turquoise",fg="blue",bg="Royalblue")
option2=Radiobutton(master=frame,text="Background Image",font=("roman",20),relief=RAISED,width=15,variable=var1,value="Bg_Image",borderwidth=2,command=selection1,   activebackground = "red",activeforeground = "Turquoise",fg="blue",bg="Royalblue")
option3=Radiobutton(master=frame,text="WebTitle_Headings",font=("roman",20),relief=RAISED,width=15,variable=var1,value="WebTitle_Headings",borderwidth=2,command=selection1,   activebackground = "purple",activeforeground = "Turquoise",fg="blue",bg="Royalblue")
option4=Radiobutton(master=frame,text="Form_Options",font=("roman",20),relief=RAISED,width=15,variable=var1,value="Form_Options",borderwidth=2,command=selection1,   activebackground = "green",activeforeground = "Turquoise",fg="blue",bg="Royalblue")
option5=Radiobutton(master=frame,text="Add PageNav",font=("roman",20),relief=RAISED,width=15,variable=var1,value="AddPageNav",borderwidth=2,command=selection1,   activebackground = "Grey",activeforeground = "Turquoise",fg="blue",bg="Royalblue")
option1.pack(anchor=NE)
option2.pack(anchor=NE,pady=20)
option3.pack(anchor=NE,pady=20)
option4.pack(anchor=NE,pady=20)
option5.pack(anchor=NE,pady=20)
















mainwindow.mainloop()