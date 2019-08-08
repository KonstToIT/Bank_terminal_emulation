import random as rd
from tkinter import *

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
      print("Error. Not Enough money to do this transaction")
      return False
    else:
      s.soaa-=summ
      recipient.soaa+=summ
      print("Transaction successfully completed")
      print("{0}$ debited the account client with id {1} to client with id {2} account".format(summ,s.user_id,recipient.user_id))
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



#=============================================================
#Creating interface, which helps use our service
def interface():
	root=Tk()
	
#Function to creating id entering window 
	def create_enter_id_window():
		e_id=enter_id_window(root,"Enter your id!")
		e_id.packing_widgets()
	#Creating our window to chose one option
	def create_choosing_option_window():
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
#

	class window:
		def __init__(s,master):
			pass
		def packing_widgets(s):
			for k in s.__dict__.keys():
				s.__dict__[k].grid()
		def hide_widgets(s):
			for k in s.__dict__.keys():
				try:
					s.__dict__[k].grid_remove()
				except AttributeError:
					pass
		def go_back(s,num_of_current_window):
			all_windows[num_of_current_window-1]()

	class elb_window(window):
		def __init__(s,master):
			s.e=Entry(master,width=20)
			s.l=Label(master,bg="black",fg="white",width=20)
			s.b=Button(master,text="Enter")
			s.back=Button(master,text="go_back")
			s.master=master
			s.master.resizable(width=False, height=False)
		def enter_some_data():
			pass

	class enter_id_window(elb_window):
		def __init__(s,master,l_text):
			super(enter_id_window,s).__init__(master)					
			s.l["text"]=l_text
			s.l.configure(fg="red")
			s.func_to_go_next_window=create_choosing_option_window	
			s.b["command"]=s.enter_some_data
		def enter_some_data(s):
			try:
				user_input=int(s.e.get())
				global user_id
				user_id=user_input
				if (not search_by_id(user_input)) is True:
					pass
				else:
					s.hide_widgets()
					s.func_to_go_next_window()
			except (TypeError,ValueError):
				s.l["text"]+="!"
			
		def packing_widgets(s):
			s.e.grid()
			s.l.grid()
			s.b.grid()
	

	class chose_option_window(window):
		def __init__(s,master):
			s.l=Label(root,bg="black",fg="white",width=50,font="arial")
			s.l["text"]="Chose one option from folowing:\n Click '1' button to know current state of your account\n Click '2' button to make transaction"
			s.b1=Button(root,text="1")
			s.b2=Button(root,text="2")
			s.back=Button(root,text="go_back")
			s.b1["command"]=s.first_option_is_chosen
			s.b2["command"]=s.second_option_is_chosen
		def first_option_is_chosen(s):
			s.hide_widgets()
			create_after_1_chosen_window()
		def second_option_is_chosen(s):
			s.hide_widgets()
			create_after_2_chosen_enter_id_window()
	class after_1_chosen_window(window):
		def __init__(s,master):
			s.l=Label(master,bg="black",fg="white",width=50,text="current state of your account:{0}".format(search_by_id(user_id).get_soaa()))
			s.b=Button(master,bg="green",fg="white",text="На главную!)")
			s.b["command"]=s.go_to_enter_id_window
		def go_to_enter_id_window(s):
			s.hide_widgets()
			create_enter_id_window()
	class after_2_chosen_enter_id_window(enter_id_window):
		def __init__(s,master,l_text):
			super(after_2_chosen_enter_id_window,s).__init__(master,l_text)	
			s.func_to_go_next_window=create_enter_sum_of_transaction_window
		def enter_some_data(s):
			try:
				user_input=int(s.e.get())
				global rec_id
				rec_id=user_input
				if (not search_by_id(user_input)) is True:
					pass
				else:
					s.hide_widgets()
					s.func_to_go_next_window()
			except (TypeError,ValueError):
				s.l["text"]+="!"

	class enter_sum_of_transaction_window(enter_id_window):
		def __init__(s,master,l_text):
			super(enter_sum_of_transaction_window,s).__init__(master,l_text)	
			s.func_to_go_next_window=create_enter_id_window
			s.b["command"]=s.enter_some_data
		def enter_some_data(s):
			try:
				summ=int(s.e.get())
				if not search_by_id(user_id).try_tr(summ,search_by_id(rec_id)):
					pass
				else:
					s.hide_widgets()
					s.func_to_go_next_window()
			
			except (TypeError,ValueError):
				s.l["text"]+="!"
	create_enter_id_window()
	root.mainloop()

interface()



"""#Function that listening clicking on "id_b" Button



  print("Chose one option:")
  print("Click '1' to check the balance of your account")
  choice=0
  while choice!=1 and choice!=2:
    print("Enter 1 or 2 please")
    choice=int(input())
  # Setting id to not exsisting in our database value of id
  id=len(clients_database) + 1

  # Asking user to enter id, while his input is invalid(input is invalid if we haven't a client with inputed id in our database)
  while (not search_by_id(id)) is True:
    print("Enter your id please")
    id=int(input())

  #Realization of checking the balance 
  if choice==1:
    print("current state of your account:{0}".format(search_by_id(id).get_soaa()))

  #Realization of doing transaction
  else:
  #Setting recipient id to not exsisting in our database value of id
    rec_id=len(clients_database) + 1
    while (not search_by_id(rec_id)) is True:
      print("Enter recipient id please")
      rec_id=int(input())

    #Define our sender and recipient to use try_tr Method
    sender=search_by_id(id)
    recipient=search_by_id(rec_id)
    print("Enter sum of transaction")
    sum=int(input())
    while not sender.try_tr(sum,recipient):
      print("Enter sum of transaction")
      sum=int(input())
  #Starting our interface:"""





