import random as rd

#Creating class "Client"
#Atributes:
#1) id-verification id for client
#2) soaa-state of an account
#3) priority-priority status for client
class client():
  def __init__(s,id,soaa,priority):
    s.id=id
    s.soaa=soaa
    s.priority=priority

# Method that tries  do transaction from client to another client
# Parameters:
# 0) s-current client,sender
# 1) sum-sum of transaction
# 2) recipient - recipient of transaction
  def try_tr(s,sum, recipient):
    if s.soaa<sum:
      print("Error. Not Enough money to do this transaction")
      return False
    else:
      s.soaa-=sum
      recipient.soaa+=sum
      print("Transaction successfully completed")
      print("{0}$ debited the account client with id {1} to client with id {2} account".format(sum,s.id,recipient.id))
      return True
  # Method that return current client's state of an account
  def get_soaa(s):
    return s.soaa

#=============================================================

#Creating list of possible priority status
priorities=["low","high"]

#Creating clients database
clients_database=[client(i,rd.randint(100,100000),rd.choice(priorities)) for i in range(10)]

#Printing our database
for i in clients_database:
  print(i.id,i.soaa,i.priority)

#Function to searching client in our database by id
def search_by_id(id):
  for i in clients_database:
    if i.id==id:
      return i
  return False
#=============================================================
#Creating interface, which helps use our service
def interface():
  print("Chose one option:")
  print("Click '1' to check the balance of your account")
	print("Click '2' to make a transaction")
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
		print(rec_id)
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
  #Starting our interface:
interface()







