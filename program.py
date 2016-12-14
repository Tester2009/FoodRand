import tkinter as tk
from tkinter import messagebox
import pymysql.cursors
import random


# December 14, 2016
# coded while listening to Viktor Tsoi

class mainProgram:
    def __init__(self, master):
        self.master = master
        self.master.geometry("300x300")
        self.master.title("FoodRand")
        self.master.resizable(width=False, height=False)
        self.frame = tk.Frame(self.master)

        self.label = tk.Label(self.master, text="Hello. This is random food chooser")
        self.label.pack()

        # self.button1 = tk.Button(self.frame, text = 'New Window', width = 25, command = self.new_window)
        # self.button1.pack()

        self.button2 = tk.Button(self.frame, text = "Add New Menu", width = 25, command = self.AddMenu)
        self.button2.pack()

        self.button3 = tk.Button(self.frame, text = "Choose Food Restaurant", width = 25, command = self.FoodRand)
        self.button3.pack()
        connection = pymysql.connect(host='localhost',
							 user='root',
							 password='toor',
							 db='foodrand')

        with connection.cursor() as cursor:
        	# read a single record
        	sql = "SELECT `restaurantname`, `restaurantlocation` FROM `foodrestaurant`"
        	cursor.execute(sql)
        	# result = cursor.fetchone()
        	result = cursor.fetchall()
        	selected = random.choice(result)
        	print(selected)
        	# print(dict(result)) #store in dictionary
        	
        	# r_name = dict(result)
        	# print(r_name)
        	
        	# #print(result)
        	# for data in result:
        	# 	print(data)

        	# senarai = list(cursor.fetchall())
        	# print(senarai)


        connection.close()
        
        self.frame.pack()
    # def new_window(self):
    #     self.newWindow = tk.Toplevel(self.master)
    #     self.app = Demo2(self.newWindow)

    def AddMenu(self):
     	self.newWindow = tk.Toplevel(self.master)
     	self.app = AddMenu(self.newWindow)

    def FoodRand(self):
    	connection = pymysql.connect(host='localhost',
							 user='root',
							 password='toor',
							 db='foodrand')
    	with connection.cursor() as cursor:
        	# read a single record
        	sql = "SELECT `restaurantname`, `restaurantlocation` FROM `foodrestaurant`"
        	cursor.execute(sql)
        	result = cursor.fetchall()
        	selected = random.choice(result)
        	# print(result)
        	messagebox.showinfo("Selected restaurant", selected)
     	# self.newWindow = tk.Toplevel(self.master)
     	# self.app = FoodRand(self.newWindow)

# class Demo2:
#     def __init__(self, master):
#         self.master = master
#         self.master.geometry("300x300")
#         self.master.title("Demo2")
#         self.master.resizable(width=False, height=False)
#         self.frame = tk.Frame(self.master)
#         self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
#         self.quitButton.pack()
#         self.frame.pack()
#     def close_windows(self):
#         self.master.destroy()

class AddMenu:
    def __init__(self, master):
        self.master = master
        self.master.geometry("400x400")
        self.master.title("FoodRand Add New Menu")
        self.master.resizable(width=False, height=False)
        self.frame = tk.Frame(self.master)

        #label 1: Restaurant Name
        self.label = tk.Label(self.master, text="Hello. Please enter your restaurant name and location")
        self.label.pack()

        self.label1 = tk.Label(self.master, text="Restaurant Name")
        self.label1.place(x=25, y=50)
        self.label1.pack()

        self.myEntryBox = tk.Entry(self.master)
        self.myEntryBox.focus_set()
        self.myEntryBox.pack()
        # self.frame = tk.Frame(self.master)

        #label 2: Restaurant Location
        self.label2 = tk.Label(self.master, text="Restaurant Location")
        self.label2.place(x=25, y=75)
        self.label2.pack()

        self.myEntryBox2 = tk.Entry(self.master)
        # self.myEntryBox2.focus_set()
        self.myEntryBox2.pack()
        # self

        self.mySubmitButton = tk.Button(self.master, text='OK', width = 25, command = self.Submit)
        # self.mySubmitButton = tk.Button(self.master, text='OK', width = 25, command = lambda: valueGET(myEntryBox.get(), myEntryBox2.get()))        
        self.mySubmitButton.pack()

        # self.frame = tk.Frame(self.master)
        # self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        # self.quitButton.pack()
        
        
        self.frame.pack()
    def close_windows(self):
        self.master.destroy()

    def Submit(self):
    	restaurant_name = self.myEntryBox.get()
    	restaurant_location = self.myEntryBox2.get()

    	if restaurant_name == '': # empty
    		messagebox.showinfo("Warning", "Please no leave empty space !")
    	elif restaurant_location == '':
    		messagebox.showinfo("Warning", "Please no leave empty space !")
    	else:
    		# get value then save to db. then close window
    		messagebox.showinfo("Result", "Thank you !")
    		# store to db
    		connection = pymysql.connect(host='localhost',
							 user='root',
							 password='toor',
							 db='foodrand')
    		with connection.cursor() as cursor:
    			sql = "INSERT INTO `foodrestaurant` (restaurantname, restaurantlocation) VALUES (%s, %s)"
    			cursor.execute(sql, (restaurant_name, restaurant_location))
    		connection.commit()

    		connection.close()

    		# destroy window
    		self.master.destroy()
    	# print(self.myEntryBox.get())
    	# print(self.myEntryBox2.get())
    	# messagebox.showinfo("Alert", "Added !")
    	# self.master.destroy()

    # def Submit(self):
    # 	self.master.callback(self.myEntryBox.get())
    #     lel = self.myEntryBox.get()
    #     print(lel)
    	# aa = self.callback(self.myEntryBox.get())
    	# bb = self.callback(self.myEntryBox2.get())
    	# print(aa)
    	# print(bb)





def main(): 
    root = tk.Tk()
    app = mainProgram(root)
    root.mainloop()

if __name__ == '__main__':
    main()