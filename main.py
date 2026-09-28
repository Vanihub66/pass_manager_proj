import pyperclip
import os

File_Name="pass.txt"

def set_pass():
    Website=input("Enter website url: ")
    passw= input("enter password: ")
    with open(File_Name,"a")as f:
         f.write(f"{Website}<||>{passw}\n")

def get_pass():
     website=input("Enter website url: ")
     found = False
     with open(File_Name,"r")as f:
          for line in f:
               if website in line:
                    passw=line.strip().split("<||>")[1]
                    pyperclip.copy(passw)
                    print("password copied to clipboard")
                    found=True
                    break
     if not found:
          print("password not found")          

def main():
     while True:
          print("1. set password")
          print("2. get password")
          print("3. exit")
          choice= input("choose an option:")
          if choice=="1":
               set_pass()
          elif choice=="2":
               get_pass()
          elif choice=="3":
               print("exiting")
               break          
          else:
                print("invalid choice")

main()