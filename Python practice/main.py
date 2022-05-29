from tkinter import *
from tkinter import messagebox
from customtkinter import *
import qrcode
from PIL import ImageTk
from resizeimage import resizeimage

class QRCodeGenrator(object):
    def __init__(self,root) -> None:
        self.root = root
        self.root.title("QR Genrator")
        self.root.geometry("800x600+200+20")
        self.root.resizable(False,False)
        
        #frames....
        self.left_partation = CTkFrame(self.root,corner_radius=0,fg_color=("#ffffff","#262626"))
        self.left_partation.place(x=0,y=0,width=450,height=600)
        self.right_partation = CTkFrame(self.root,corner_radius=0,fg_color="#0179d0")
        self.right_partation.place(x=450,y=0,width=350,height=600)
        self.right_subframe = Label(self.right_partation,text="QR Not \nAvailable",border=2,font=("arial",20),fg="#ff0000")
        self.right_subframe.place(x=50,y=100,width=250,height=250)
        
        #Welcome Label....
        self.user_dialog=CTkInputDialog(root,title="Welcome User",text="Please Enter Your Name")
        self.username = self.user_dialog.get_input()
        self.username = self.checkusername()
        self.user_welcome = CTkLabel(self.root,corner_radius=0,text="Welcome, "+self.username,text_font=("arial",25),fg_color=("#ffffff","#262626"))
        self.user_welcome.place(x=0,y=50,width=450,height=80)
        

        #Labels....
        self.student_id = CTkLabel(self.left_partation,corner_radius=0,text="STUDENT ID :",text_font=("arial",9),text_color=("#000000","#ffffff"))
        self.student_id.place(x=0,y=200,width=90)
        self.student_name = CTkLabel(self.left_partation,corner_radius=0,text="FULL NAME :",text_font=("arial",9),text_color=("#000000","#ffffff"))
        self.student_name.place(x=225,y=200,width=100)
        self.student_course = CTkLabel(self.left_partation,corner_radius=0,text="COURSE :",text_font=("arial",9),text_color=("#000000","#ffffff"))
        self.student_course.place(x=10,y=250,width=90)
        self.student_branch = CTkLabel(self.left_partation,corner_radius=0,text="BRANCH :",text_font=("arial",9),text_color=("#000000","#ffffff"))
        self.student_branch.place(x=235,y=250,width=100)
        self.student_session = CTkLabel(self.left_partation,corner_radius=0,text="SESSION :",text_font=("arial",9),text_color=("#000000","#ffffff"))
        self.student_session.place(x=5,y=300,width=90)
        self.student_father_name = CTkLabel(self.left_partation,corner_radius=0,text="FATHER NAME :",text_font=("arial",9),text_color=("#000000","#ffffff"))
        self.student_father_name.place(x=215,y=300,width=100)
        self.student_contact = CTkLabel(self.left_partation,corner_radius=0,text="PHONE :",text_font=("arial",9),text_color=("#000000","#ffffff"))
        self.student_contact.place(x=10,y=350,width=90)
        self.student_blood = CTkLabel(self.left_partation,corner_radius=0,text="BLOOD GROUP :",text_font=("arial",9),text_color=("#000000","#ffffff"))
        self.student_blood.place(x=215,y=350,width=100)
        self.student_address = CTkLabel(self.left_partation,corner_radius=0,text="ADDRESS :",text_font=("arial",9),text_color=("#000000","#ffffff"))
        self.student_address.place(x=0,y=400,width=100)

        #Right Partation Label....
        self.qr_label = CTkLabel(self.right_partation,text="QR CODE\nGenrator",text_color=("#ff751a","#ff3399"),text_font=("arial",20))
        self.qr_label.place(x=100,y=400,width=150)

        #Contributor Label....
        self.contributor_label = CTkLabel(self.right_partation,text="By Kapil Dagur",text_color=("#ffffff","#000000"),text_font=("arial",9))
        self.contributor_label.place(x=250,y=550,width=100)
        
        #Input Variables....
        self.student_id_var = StringVar()
        self.student_name_var = StringVar()
        self.student_course_var = StringVar()
        self.student_branch_var = StringVar()
        self.student_session_var = StringVar()
        self.student_father_name_var = StringVar()
        self.student_contact_var = StringVar()
        self.student_blood_var = StringVar()
        self.student_address_var = StringVar()

        #Entry.....
        self.student_id_entry = CTkEntry(self.left_partation,textvariable=self.student_id_var)
        self.student_id_entry.place(x=90,y=200,width=120)
        self.student_name_entry = CTkEntry(self.left_partation,textvariable=self.student_name_var)
        self.student_name_entry.place(x=320,y=200,width=120)
        self.student_course_entry = CTkEntry(self.left_partation,textvariable=self.student_course_var)
        self.student_course_entry.place(x=90,y=250,width=120)
        self.student_branch_entry = CTkEntry(self.left_partation,textvariable=self.student_branch_var)
        self.student_branch_entry.place(x=320,y=250,width=120)
        self.student_session_entry = CTkEntry(self.left_partation,textvariable=self.student_session_var)
        self.student_session_entry.place(x=90,y=300,width=120)
        self.student_father_name_entry = CTkEntry(self.left_partation,textvariable=self.student_father_name_var)
        self.student_father_name_entry.place(x=320,y=300,width=120)
        self.student_contact_entry = CTkEntry(self.left_partation,textvariable=self.student_contact_var)
        self.student_contact_entry.place(x=90,y=350,width=120)
        self.student_blood_entry = CTkEntry(self.left_partation,textvariable=self.student_blood_var)
        self.student_blood_entry.place(x=320,y=350,width=120)
        self.student_address_entry = CTkEntry(self.left_partation,textvariable=self.student_address_var)
        self.student_address_entry.place(x=90,y=400,width=320)

        #Buttons.....
        self.submit_btn = CTkButton(self.left_partation,text=" Submit ",corner_radius=35,text_color=("#000000","#ffffff"),command=self.submit)
        self.submit_btn.place(x=80,y=480,width=120,height=35)
        self.reset_btn = CTkButton(self.left_partation,text=" Reset ",corner_radius=35,text_color=("#000000","#ffffff"),command=self.reset)
        self.reset_btn.place(x=250,y=480,width=120,height=35)
    
    #Constructor for Conatain/Arrange all Data of student....
    def data(self)->str:
        return f"Student I'd : {self.student_id_var.get()} \nStudent Name : {self.student_name_var.get()} \nCourse : {self.student_course_var.get()} \nBranch : {self.student_branch_var.get()} \nSession : {self.student_session_var.get()} \nFather's Name : {self.student_father_name_var.get()} \nPhone : {self.student_contact_var.get()} \nBlood Group : {self.student_blood_var.get()}\nAddress : {self.student_address_var.get()}"

    #Constructor for Validate Input Data
    def isValidStudentName(self)->bool:
        name = self.student_name_var.get()
        if len(name) > 2:
            if name[0].isupper():
                return True
            else:
                messagebox.showerror("Invalid Student Name :","You Entered Invalid Name \nPlease Start with Capital latter")
        else:
            messagebox.showerror("Invalid Student Name :","Name Too Short (Note:- Mininmun Words required in name is 3)")
        return False

    def isValidFatherName(self)->bool:
        name = self.student_father_name_var.get()
        if len(name) > 2:
            if name[0].isupper():
                return True
            else:
                messagebox.showerror("Invalid Father Name :","You Entered Invalid Name \nPlease Start with Capital latter")
        else:
            messagebox.showerror("Invalid Father Name :","Name Too Short (Note:- Mininmun Words required in name is 3)")
        return False
    
    def isValidPhone(self)->bool:
        phone = self.student_contact_var.get()
        if(len(phone) == 10):
            if phone.isnumeric() :
                return True
        messagebox.showerror("Invalid Phone Number :","You Entered Invalid Phone Number,\nPlease Enter A Valid Phone Number")
        return False

    def isValidBlood(self)->bool:
        BGS = ["A+","A-","B+","B-","AB+","AB-","O+","O-"]
        blood_group = self.student_blood_var.get()
        if blood_group in BGS :
            return True
        else:
            messagebox.showinfo("Invalid Blood Group :","Plaese Enter Valid Blood Group \ni.e ['A+','A-','B+','B-','AB+','AB-','O+','O-']")
            return False

    #Constructor For Create QR Code....
    def submit(self)->None:
        if self.student_id_var.get() == "" or self.student_name_var.get() == "" or self.student_course_var.get() == "" or self.student_branch_var.get() == "" or self.student_session_var.get() == "" or self.student_father_name_var.get() == "" or self.student_contact_var.get() == "" or self.student_address_var.get() == "" :
            messagebox.showwarning("Fill All Requrired Entries :","Please Enter All Data !!!")
        elif(self.isValidStudentName() and self.isValidFatherName() and self.isValidPhone() and self.isValidBlood()):
            student_data = self.data()
            qr = qrcode.make(student_data)
            resizeqr = resizeimage.resize_cover(qr,size=[240,240])
            CTk_label_qr = ImageTk.PhotoImage(resizeqr)
            self.right_subframe.config(image=CTk_label_qr)
            resizeqr.save(f"Student ID {self.student_id_var.get()}.png",format="png")
            messagebox.showinfo("QR Created Successfully :","Hurry !!! \nYour Qr Code Genrated Successfully")
    
    #Constructor For Reset All Input Data....
    def reset(self)->None:
        self.student_id_var.set("")
        self.student_name_var.set("")
        self.student_course_var.set("")
        self.student_branch_var.set("")
        self.student_session_var.set("")
        self.student_father_name_var.set("")
        self.student_contact_var.set("")    
        self.student_blood_var.set("")
        self.student_address_var.set("")
        self.right_subframe.destroy()
        self.right_subframe = Label(self.right_partation,text="QR Not \nAvailable",font=("arial",20),fg="#ff0000")
        self.right_subframe.place(x=50,y=100,width=250,height=250)
    def checkusername(self):
        if self.username == None or self.username == "" :
            return "Guest"
        else:
            return self.username

    #Constructor for Start Application.....
    def start(self):
        self.root.mainloop()

if __name__ == '__main__':
    widget = CTk()
    app = QRCodeGenrator(widget)
    app.start()