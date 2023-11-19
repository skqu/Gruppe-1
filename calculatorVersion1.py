import tkinter as tk
from tkinter import ttk

from math import sqrt
import re





class Calculator():
    def __init__(self) -> None:
        Gui()
    
    def calculate(self, input):
        try: 
            return str(eval(input))
        except:
            print("exeption")

class Gui(Calculator):
    def __init__(self):
        self.root = tk.Tk()
        self.root.title = ("Calculator")
        self.handler = Handler()
        self.buildLayout()
        self.style()


        self.root.mainloop()

    def DisplayFrame(self):
     #__init__(self, master=None):
     #   super().__init__(master)
        self.pack()
        self.result_list = []

        # Create a label to display the results
        self.result_label = tk.Label(self, text="Results:")
        self.result_label.pack()

        # Create a button to trigger the display_text method
        self.display_button = tk.Button(self, text="Display Text", command=self.display_text)
        self.display_button.pack()   

    def buildLayout(self):

        # DISPLAY

        self.display = tk.Label(self.root, text = "0", font=("Arial", 32), anchor="e", justify="right", width=12)
        self.display.pack()


        self.display.pack(padx=10, pady=10)
        self.display.focus_set()

        # Frame for numbers and operators
        self.numpad_frame = tk.Frame(self.root)
        self.numpad_frame.pack()
        
        # Frame for result-historic
        #################################
        
        #Numpad
        self.list_buttons = [
            "(", ")", "C", "\u2190",
            "\u221A", "x^2", "x^x", "/",
            "7", "8", "9", "*",
            "4", "5", "6", "-",
            "1", "2", "3", "+",
            "+/-", "0", ".", "="
        ]

        self.buildButtons(self.list_buttons, self.numpad_frame, 4) 


    def buildButtons(self, list_buttons, frame, maxCol = 1): #Create buttons for a frame 
        row = 0
        col = 0

        for button_text in list_buttons:
            button = tk.Button(frame, text=button_text, font=("Arial", 16), width=6, height=2, borderwidth=0)
            button.grid(row=row, column=col, padx=2, pady=2)
            button.bind("<Button-1>", self.events)
            col += 1
            if col == maxCol:
                col = 0
                row += 1
    
    def displayText(self, text):
        

        if len(self.display.cget("text")) == 0:
            newText = 0
        
        else:
                
            if self.display.cget("text") == "0":
                newText = text
             
            else:
                newText = self.display.cget("text") + text
             
                    
        self.display.config(text = newText)
     
    

    def events(self, event): #Button events
        newText = ""
        text = event.widget.cget("text")
        self.display.focus_set()
        
        

        match text:
            case "=":
                new = self.display.cget("text").replace('\u221A', 'sqrt')
                new = new.replace('^', '**')

                newText = self.calculate(new)
                self.display.config(text = newText)
                #print("testA",newText, new)
                self.handler.save_result(newText, new)
                self.handler.display_results()

            case "C":
                self.display.config(text = "0")
                

            case "\u2190": #Backspace

                newText = self.display.cget("text")[:-1]
                self.display.config(text = newText)
                if len(self.display.cget("text")) == 0:
                    self.display.config(text = "0")
                   
            case "+/-":
                if self.display.cget("text")[0] != "-":
                    newText = "-" + self.display.cget("text")
                    
                else:
                    newText = self.display.cget("text")[1:]
                    

                self.display.config(text = newText)
                
            case "\u221A": #Squareroot
                newText = text + "("
                self.displayText(newText)
               
            
            case "x^2": 
                newText = "^2"
                self.displayText(newText)
                

            case "x^x":
                print("SAdasdsdsd")
                newText = "^"
                self.displayText(newText)
                
            
            case _:
                newText = text
                self.displayText(newText)
               

    def styleChildren(self, widget, bg_color, text_color):
        widget.configure(bg=bg_color)
        if isinstance(widget, (tk.Label, tk.Button)):
            widget.configure(fg=text_color)
        if isinstance(widget, tk.Frame):
            for child in widget.winfo_children():
                self.styleChildren(child, bg_color, text_color)
                    

    def style(self):

        backgroundColor = "#262626"
        fontColor = "#ffffff"

        self.styleChildren(self.numpad_frame, "#3d3d3d", fontColor)

        self.root.config(background = backgroundColor)
        self.display.config(background = backgroundColor)
        self.numpad_frame.config(background = backgroundColor)
        self.display.config(fg = fontColor)
        
class Handler():
       
    def __init__(self):
       
        # Initialize an empty list to store results
        self.result_list = []
      
    def save_result(self, newText, new):
        # l=self.result_list()
        # Save the result in the list
        self.result_list.append((newText, new))
        
        # Keep only the last 10 results
        if len(self.result_list) > 20:  # Assuming each result is a pair
            self.result_list = self.result_list[-20:]
    def display_results(self):
        print("Results:")
        # Display up to the last 10 results
        for i, result_pair in enumerate(reversed(self.result_list)):
            # Display results in reverse order (latest calculation first)
            print(f"{i + 1}. {result_pair[0]} = {result_pair[1]}")
      
            
  


       
if __name__ == "__main__":
    Calculator()
