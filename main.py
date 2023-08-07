from tkinter import *
from tkinter import messagebox
import pickle
import os.path

def add_task():
    task = entrytask.get()
    if task != "":
        listbox.insert(END, task)
        entrytask.delete(0, END)
    else:
        messagebox.showwarning(title="Warning!", message="no task is entered")
def delete_task():
    try:
        task_index = listbox.curselection()[0]
        listbox.delete(task_index)
    except:
        messagebox.showwarning(title="Warning!", message="No task is selected")
def load_task():
    listbox.delete(0, END)
    file_exists = os.path.exists("tasks.dat")
    if file_exists:
        tasks = pickle.load(open("tasks.dat", "rb"))
        if tasks != ():
            for t in tasks:
                listbox.insert(END, t)
        else:
            listbox.insert(END, "NO TASKS IN YOUR TO-DO LIST \U0001F600")
            messagebox._show(title="No Tasks!", message="YOUR TO DO LIST IS EMPTY \U0001F600")
            listbox.delete(0, END)
    else:
        messagebox.showwarning(title="Warning!", message="No file exists")
def save_task():
    tasks = listbox.get(0, listbox.size())
    pickle.dump(tasks, open("tasks.dat", "wb"))
    messagebox._show(title="Successfull",message="\U0001F600")
def edit_task():
    try:
        task_index=listbox.curselection()[0]
        previous_task_name=listbox.get(task_index)
        task=entrytask.get()
        if task!="" and previous_task_name!=task:
            listbox.delete(task_index)
            listbox.insert(task_index,task)
            entrytask.delete(0, END)
            messagebox._show(title="Successfully edited", message="\U0001F600")
        elif previous_task_name==task:
            entrytask.delete(0, END)
            messagebox.showwarning(title="Same Name" , message="Previous and present names are same")
        else:
            messagebox.showwarning(title="Warning!",message="The Task name can't be an Empty")
    except:
        messagebox.showwarning(title="Warning!",message="Nothing is selected to edit")
def priority_task():
    try:
        task_index=listbox.curselection()[0]
        if task_index==0:
            messagebox.showwarning(title="Already at top",message="It has high priority")
        else:
            task_name=listbox.get(task_index)
            listbox.delete(task_index)
            listbox.insert(0,task_name)
    except:
        messagebox.showwarning(title="Warning!",message="Nothing is selected")
#creating GUI
m = Tk()
m.title("TO-Do list by Vinay")
frames_tasks = Frame(m)
frames_tasks.pack()
listbox = Listbox(frames_tasks, height=15, width=50,selectbackground="red")
listbox.pack(side=LEFT,ipady=12)
scrollbar = Scrollbar(frames_tasks)
scrollbar.pack(side=RIGHT, fill=Y,expand=2)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)
entrytask = Entry(m, width=50)
entrytask.pack()
add_task = Button(m, text="Add task", width=48, command=add_task,bg="red",fg="white")
add_task.pack()
delete_task = Button(m, text="Delete task", width=48, command=delete_task,bg="green",fg="white")
delete_task.pack()
load_task = Button(m, text="Load tasks", width=48, command=load_task,bg="blue",fg="white")
load_task.pack()
save_task = Button(m, text="Save tasks", width=48, command=save_task,bg="yellow",fg="black")
save_task.pack()
edit_task = Button(m, text="Edit task", width=48, command=edit_task,bg="brown",fg="white")
edit_task.pack()
priority_task = Button(m, text="priority task", width=48, command=priority_task,bg="white",fg="black")
priority_task.pack()
m.mainloop()