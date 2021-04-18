
Web_Title=""
Web_Background_Image=""
Target_user=""
Image=""
Project_objective=""
Data_required=""

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

while True:

    a=input("Do you To regester Something ? (y/n) -> ")
    if a.upper()=="Y":
        Web_Title_bool=False
        Web_Background_Image_bool=False
        welcome_bool=False
        Image_bool=False
        Project_objective_bool=False
        Data_required_bool=False
        break
    elif a.upper()=="N":
        Web_Title_bool=True
        Web_Background_Image_bool=True
        welcome_bool=True
        Image_bool=True
        Project_objective_bool=True
        Data_required_bool=True
        break
    else:
        print("Please give a proper answer.")



Data_regesteration_bool = False
while Data_regesteration_bool is False:

    if Web_Title_bool is False:
        Web_Title=input("Enter Web Title-> ")
        Web_Title_bool=True
    elif Web_Background_Image_bool is False:
        Web_Background_Image=input("Enter Background Image Name-> ")
        Web_Background_Image_bool=True
    elif welcome_bool is False:
        Welcome=input("heading-> ")
        welcome_bool=True
    elif Image_bool is False:
        Image=input("insert an Image-> ")
        Image_bool=True
    elif Project_objective_bool is False:
        Project_objective=input("Project_objective-> ")
        Project_objective_bool=True
    elif Data_required_bool is False:
        Data_required=input("Data_required-> ")
        Data_required_bool=True
    else:
        Data_regesteration_bool= True
Form.close()






Form=open("Project Details Form.html","w+")
Form.write(f"""
<html>
    <head>
        <title>{Web_Title}</title>
        
    </head>
    <body background="Images/{Web_Background_Image}.png" text="Black">
        <center>
        <big><big><h1>{Welcome}</h1></big></big>
        </center> 
        <hr color="Blue" >
        <style>
            img{{
                border-radius:90%;
                width:150px;
                border-color: rgb(0, 0, 255);
                border-style:dashed;
            }}
        </style>
        <img src="Images/{Image}.png" alt="Just an Image" border="3" aling="left">
        <form name="get">
            Please enter your password: <input type="password" name="User_Password">
            your file<input type="file">
            <input type="submit" value="OK">
        </form>
        
        

    </body> 



</html>

""")

Form.close()


Form=open("Project Details Form","r+")
Readstr=Form.read(9999)
print(Readstr)

Form.close()
print(Form.name)




