import tkinter as tk
from tkinter import *
from tkinter import messagebox

import mysql.connector

# connect to database
con = mysql.connector.connect(user='root', port=3306, host='127.0.0.1', database='voters_details')
cur = con.cursor()
cur.execute("select * from voter_info")  # retrieving the details from the database
info = cur.fetchall()  # fetching the details
res = list(zip(*info))  # unzip the tuple from the list
voter_id = list(res[0])  # conversation of tuple into list
num_of_voters = len(voter_id)

# declaring variable globally
no_of_vote1 = 0
no_of_vote2 = 0
nominee = ''
nominee2 = ''


# Result to be display
def result():
    global no_of_vote1, no_of_vote2, voter_id, num_of_voters
    if voter_id == []:  # checks the voter id list is empty or not
        messagebox.showinfo("showinfo", "Voting Session is Over")  # if empty then they show msg

        if no_of_vote1 > no_of_vote2:  # compare the votes
            per = (no_of_vote1 / num_of_voters) * 100  # percentages of votes
            messagebox.showinfo("Nominee 1 has won by", per)

        elif no_of_vote2 > no_of_vote1:  # compare the votes
            per = (no_of_vote2 / num_of_voters) * 100 # percentages of votes
            messagebox.showinfo("Nominee 2 has won", per)
    else:
        messagebox.showinfo("showinfo", "Voting Session is Not Over")  # if non empty then they show msg


class Voting:

    def __init__(self, root):
        self.root = root
        self.root.title("KDRs Voting System")
        self.root.geometry("800x600")

        title = Label(root, text="KDR's Voting System", font=("times new roman", 40, "bold"), bg="Yellow", fg="RED")
        title.pack(side=TOP, fill=X)

        self.Nominee_name = StringVar()
        self.Nominee_name2 = StringVar()
        self.Vote_id = IntVar()
        self.i = IntVar()

        Manage_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        Manage_Frame.place(x=20, y=100, width=760, height=470)

        lbl_name = Label(Manage_Frame, text="Nominee Name 1", bg="crimson", fg="white",
                         font=("times new roman", 20, "bold"))
        lbl_name.grid(row=1, column=0, pady=10, padx=20)

        lbl_name2 = Label(Manage_Frame, text="Nominee Name 2", bg="crimson", fg="white",
                          font=("times new roman", 20, "bold"))
        lbl_name2.grid(row=2, column=0, pady=10, padx=20)

        voteid = Label(Manage_Frame, text="Enter Voting ID", bg="crimson", fg="white",
                       font=("times new roman", 20, "bold"))
        voteid.grid(row=3, column=0, pady=10, padx=20)

        Vote_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="Orange")
        Vote_Frame.place(x=80, y=300, width=630, height=200)

        txt_nomi = Entry(Manage_Frame, textvariable=self.Nominee_name, font=("times new roman", 15, "bold"), bd=5,
                         relief=GROOVE)
        txt_nomi.grid(row=1, column=2, pady=10, padx=20)

        txt_nomi2 = Entry(Manage_Frame, textvariable=self.Nominee_name2, font=("times new roman", 15, "bold"), bd=5,
                          relief=GROOVE)
        txt_nomi2.grid(row=2, column=2, pady=10, padx=20)

        txt_voteid = Entry(Manage_Frame, textvariable=self.Vote_id, font=("times new roman", 15, "bold"), bd=5,
                           relief=GROOVE)
        txt_voteid.grid(row=3, column=2, pady=10, padx=20)

        val_btn = Button(Vote_Frame, text="Validate", width=20, command=self.validate).grid(row=0, column=0, padx=220,
                                                                                            pady=30)
        add_btn = Button(Vote_Frame, text="Result", width=20, command=result).grid(row=1, column=0, padx=220, pady=30)

    def validate(self):
        vid = self.Vote_id.get()
        if vid in voter_id:
            voter_id.remove(vid)
            window(self)
        else:
            messagebox.showerror("error", "Sorry !!! You Are Not a Voter or You Have already Voted")


def window(self):
    global no_of_vote1, no_of_vote2
    win = Toplevel(self.root)
    win.title("Choose the Vote")
    win.geometry("500x300")
    title = Label(win, text="Cast The Vote", font=("times new roman", 40, "bold"), bg="Yellow", fg="RED")
    title.pack(side=TOP, fill=X)
    win_frame = Frame(win, bd=4, relief=RIDGE, bg="Orange")
    win_frame.place(x=10, y=80, width=480, height=200)
    nominee = self.Nominee_name.get()
    nominee2 = self.Nominee_name2.get()
    first_btn = Radiobutton(win_frame, text="%s" % nominee, width=20, value=1, variable=self.i,
                            command=win.destroy).grid(
        row=0,
        column=0,
        padx=120,
        pady=30)
    second_btn = Radiobutton(win_frame, text="%s" % nominee2, width=20, value=2, variable=self.i,
                             command=win.destroy).grid(
        row=1,
        column=0,
        padx=220,
        pady=30)
    if self.i.get() == 1:
        no_of_vote1 += 1
        return print(no_of_vote1)

    elif self.i.get() == 2:
        no_of_vote2 += 1
        return print(no_of_vote2)


root = Tk()
ob = Voting(root)
root.mainloop()
