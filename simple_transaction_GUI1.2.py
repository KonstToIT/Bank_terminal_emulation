import random as rd
from tkinter import *
from PIL import ImageTk, Image

#Creating class "Client"
#Atributes:
#1) id-verification id for client
#2) soaa-state of an account
#3) priority-priority status for client
class client():
  def __init__(s,user_id,soaa,priority):
    s.user_id=user_id
    s.soaa=soaa
    s.priority=priority

# Method that tries  do transaction from client to another client
# Parameters:
# 0) s-current client,sender
# 1) sum-sum of transaction
# 2) recipient - recipient of transaction
  def try_tr(s,summ, recipient):
    if s.soaa<summ:
      return False
    else:
      s.soaa-=summ
      recipient.soaa+=summ
      return True
  # Method that returns current client's state of an account
  def get_soaa(s):
    return s.soaa

#=============================================================

#Creating list of possible priority status
priorities=["low","high"]

#Creating clients database
clients_database=[client(i,rd.randint(100,100000),rd.choice(priorities)) for i in range(100)]

#Function to searching client in our database by id
def search_by_id(user_id):
  for i in clients_database:
    if i.user_id==user_id:
      return i
  return False


#Printing our database
for i in clients_database:
  print(i.user_id,i.soaa,i.priority)

inputted_inf={"user_id":None,"rec_id":None,"sum":None}

#=============================================================
#Creating interface, which helps use our service
root=Tk()
root.geometry("500x400")
root.resizable(0,0)
logo_img=ImageTk.PhotoImage(Image.open("logo.jpg"))
#Functions, that creates our windows 
def create_enter_id_window():
	e_id=enter_id_window(root,"Enter your id!")
	e_id.packing_widgets()
	e_id.remove_go_back_button()
#Creating our window to chose one option
def create_chose_option_window():
	ch_opt=chose_option_window(root)
	ch_opt.packing_widgets()
def create_after_1_chosen_window():
	after_1=after_1_chosen_window(root)
	after_1.packing_widgets()
def create_after_2_chosen_enter_id_window():
	after_2=after_2_chosen_enter_id_window(root,"Enter rec id!")
	after_2.packing_widgets()
def create_enter_sum_of_transaction_window():
	sum_of_tr_window=enter_sum_of_transaction_window(root,"Enter sum of transaction")
	sum_of_tr_window.packing_widgets()
def create_after_entering_sum_of_transaction_window():
	after_sum_of_tr=after_entering_sum_of_transaction_window(root)
	after_sum_of_tr.packing_widgets()
#==============================================

#Classes for creating different windows

class window:
	def __init__(s,master):
		pass
#Placing widgets on screen
	def packing_widgets(s):
		for k in s.__dict__.keys():
			try:
				s.__dict__[k].grid()
			except AttributeError:
				pass
#Hiding widgets
	def hide_widgets(s):
		for k in s.__dict__.keys():
			try:
				s.__dict__[k].grid_remove()
			except AttributeError:
				pass

#Entry, Label, Button window.
class elb_window(window):
	def __init__(s,master):
		s.e=Entry(master,width=20,font="Consolas 16")
		s.l=Label(master,bg="black",fg="white",width=20,font="Consolas 16")
		s.b=Button(master,text="Next")
		s.back=Button(master,text="go_back")
	def enter_some_data():
		pass


class enter_id_window(elb_window):
	def __init__(s,master,l_text):
		super(enter_id_window,s).__init__(master)					
		s.l["text"]=l_text
		s.l.configure(fg="red")
		s.func_to_go_next_window=create_chose_option_window	
		s.b["command"]=s.enter_some_data
	def enter_some_data(s):
		try:
			user_input=int(s.e.get())
			inputted_inf["user_id"]=user_input
			if (not search_by_id(user_input)) is True:
				pass
			else:
				s.hide_widgets()
				s.func_to_go_next_window()
		except (TypeError,ValueError):
			s.l["text"]="Please use only digits"
	def packing_widgets(s):
		s.e.grid(row=1,column=0)
		s.l.grid(row=2,column=0)
		s.b.grid(row=3,column=1)
		s.back.grid(row=4,column=0)
	def remove_go_back_button(s):
		s.back.grid_remove()

class chose_option_window(window):
	def __init__(s,master):
		s.t=Text(root,bg="black",fg="white",width=50,height=3,state="normal",font="Consolas 14",wrap=WORD)
		s.t.insert(1.0,"Chose one option from folowing:\n Click '1' button to know current state of your account\n Click '2' button to make transaction")
		s.t.configure(state="disabled")
		s.b1=Button(root,text="1")
		s.b2=Button(root,text="2")
		s.back=Button(root,text="go_back")
		s.b1["command"]=s.first_option_is_chosen
		s.b2["command"]=s.second_option_is_chosen
		s.back["command"]=s.go_back
	def first_option_is_chosen(s):
		s.hide_widgets()
		create_after_1_chosen_window()
	def second_option_is_chosen(s):
		s.hide_widgets()
		create_after_2_chosen_enter_id_window()
	def go_back(s):
		s.hide_widgets()
		create_enter_id_window()

class after_1_chosen_window(window):
	def __init__(s,master):
		s.l=Label(master,bg="black",fg="white",width=50,text="current state of your account:{0}".format(search_by_id(inputted_inf["user_id"]).get_soaa()))
		s.b=Button(master,bg="green",fg="white",text="На главную!)")
		s.b["command"]=s.go_to_enter_id_window
	def go_to_enter_id_window(s):
		s.hide_widgets()
		create_enter_id_window()


class after_2_chosen_enter_id_window(enter_id_window):
	def __init__(s,master,l_text):
		super(after_2_chosen_enter_id_window,s).__init__(master,l_text)	
		s.func_to_go_next_window=create_enter_sum_of_transaction_window
		s.back=Button(master,text="go back")
		s.back["command"]=s.go_back
#Method that validates entered data and call function to create next window if entered data is correct
#Validates if user with entered id exist in data baze
	def enter_some_data(s):
		try:
			user_input=int(s.e.get())
			inputted_inf["rec_id"]=user_input
			#Validating process
			if ((not search_by_id(user_input)) is True) or (inputted_inf["user_id"]==inputted_inf["rec_id"]):
				pass
			else:
				s.hide_widgets()
				s.func_to_go_next_window()
		except (TypeError,ValueError):
			s.l["text"]="Please use only digits"
	def go_back(s):
		s.hide_widgets()
		create_chose_option_window()

class enter_sum_of_transaction_window(enter_id_window):
	def __init__(s,master,l_text):
		super(enter_sum_of_transaction_window,s).__init__(master,l_text)	
		s.func_to_go_next_window=create_after_entering_sum_of_transaction_window
		s.b["command"]=s.enter_some_data
		s.back["command"]=s.go_back
#Method that validates entered data and call function to create next window if entered data is correct
#Validates if user with entered id has enough money to make transaction
	def enter_some_data(s):
		try:
			global summ
			summ=int(s.e.get())
			inputted_inf["sum"]=summ
			#Validating process
			if not search_by_id(inputted_inf["user_id"]).try_tr(inputted_inf["sum"],search_by_id(inputted_inf["rec_id"])):
				s.l["text"]="Sorry.You have not enough money to make this transaction"
			else:
				s.hide_widgets()
				s.func_to_go_next_window()
		except (TypeError,ValueError):
			s.l["text"]="Enter sum of transaction please(use only digits)"
	def go_back(s):
		s.hide_widgets()
		create_after_2_chosen_enter_id_window()	
class after_entering_sum_of_transaction_window(window):
	def __init__(s,master):
		s.t=Text(master,bg="black",fg="white",width=50,height=3,state="normal",wrap=WORD)
		s.t.insert(1.0,"Transaction successfully completed {0}$ debited the account client with id {1} to client with id {2} account".format(inputted_inf["sum"],inputted_inf["user_id"],inputted_inf["rec_id"]))
		s.t.configure(state="disabled")
		s.b=Button(master,bg="green",fg="white",text="На главную!)")
		s.b["command"]=s.go_to_enter_id_window
	def go_to_enter_id_window(s):
		s.hide_widgets()
		create_enter_id_window()
	
create_enter_id_window()
root.mainloop()


