import tkinter as tk
from tkinter import ttk

from math import sqrt



class data(): 
    def __init__(self) -> None:
        self.history = []

    def write(self, list_expression = []):
        self.history.append(list_expression)

    def read(self):
        return self.history


class Calculator(data):
    def __init__(self) -> None:
        Gui()

    def calculate(self, input):
        try: 
            result = str(eval(input))
            #self.write([input, result])
            return result
        except:
            print('exeption')

class Gui(Calculator):
    def __init__(self):
        self.bgColor = '#262626'
        self.color = '#ffffff'

        self.root = tk.Tk()
        self.root.title('Calculator')
        self.root.geometry('650x450')

        self.style()

        self.build()
        

        self.root.mainloop()
    
    def build(self):

        self.calc_frame = ttk.Frame(self.root, height=450, width=350)
        self.calc_frame.pack_propagate(0)


        self.history_frame = ttk.Frame(self.root, height=450, width=300)
        self.history_frame.pack_propagate(0)


        

        self.history_table = ttk.Treeview(self.history_frame, show="tree")

        self.history_table['columns'] = ('Equation')

        self.history_table.column('#0', width = 0)
        self.history_table.column('Equation', width = 350)

        self.history_table.pack(fill = 'both', expand = True)


        
        # scrollbar
        scollbar_table = ttk.Scrollbar(self.history_frame, orient='vertical', command = self.history_table.yview, style='arrowless.Vertical.TScrollbar')
        self.history_table.configure(yscrollcommand = scollbar_table.set)
        scollbar_table.place(relx = 1, rely = 0, relheight = 1, anchor = 'ne')

        print(len(self.history_table.get_children()))




        self.history_frame.grid(row=0, column=0)
        self.calc_frame.grid(row=0, column=1)
        


        # DISPLAY
        self.display = ttk.Label(self.calc_frame, text = '0')
        self.display.pack()


        # Frame for numbers and operators
        self.numpad_frame = ttk.Frame(self.calc_frame)
        self.numpad_frame.pack()

        #Numpad
        list_buttons = [
            '(', ')', 'C', '\u2190',
            '\u221A', 'x^2', 'x^x', '/',
            '7', '8', '9', '*',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '+/-', '0', '.', '='
        ]

        self.buildButtons(list_buttons, self.numpad_frame, 4) 

    def displayHistoryList(self, list_history):
        pass
    
    def displayHistory(self, equation):
        
         self.history_table.insert(parent='', index = 0, values = [equation])




    def buildButtons(self, list_buttons, frame, maxCol = 1): #Create buttons for a frame 
        row = 0
        col = 0

        for button_text in list_buttons:
            button = ttk.Button(frame, text=button_text, takefocus = False)
            button.grid(row=row, column=col, padx = 2, pady = 2, ipadx = 1,ipady=14)
            
            button.bind('<Button-1>', self.events)
            col += 1
            if col == maxCol:
                col = 0
                row += 16
    
    def displayText(self, text):
    
        if len(self.display.cget('text')) == 0:
            newText = 0
        else:
                
            if self.display.cget('text') == '0':
                newText = text
            else:
                newText = self.display.cget('text') + text
                    
        self.display.config(text = newText)



    def events(self, event): #Button events
        newText = ''
        text = event.widget.cget('text')
        self.display.focus_set()

        match text:
            case '=':
                equation = self.display.cget('text')
                new = equation.replace('\u221A', 'sqrt')
                new = new.replace('^', '**')

                result = self.calculate(new)
                self.displayHistory(f'{equation} = {result}')
                
                self.display.config(text = result)
                
            case 'C':
                self.display.config(text = '0')
            

            case '\u2190': #Backspace

                newText = self.display.cget('text')[:-1]
                self.display.config(text = newText)
                if len(self.display.cget('text')) == 0:
                    self.display.config(text = '0')

            case '+/-':
                if self.display.cget('text')[0] != '-':
                    newText = '-' + self.display.cget('text')
                else:
                    newText = self.display.cget('text')[1:]

                self.display.config(text = newText)
                
            case '\u221A': #Squareroot
                newText = text + '('
                self.displayText(newText)
            
            case 'x^2': 
                newText = '^2'
                self.displayText(newText)

            case 'x^x':
                newText = '^'
                self.displayText(newText)
            
            case '\u2591':
                self.stateMachine('history')


            case _:
                newText = text
                self.displayText(newText)

    def style(self):

    
        style = ttk.Style()

        style.theme_use("default")

        style.configure('Treeview',
            background = self.bgColor, 
            foreground = self.color,
            fieldbackground = self.bgColor,
            rowheigt = 25,
            font = (None, 16),
            borderwidth = 0 
        )

        
        style.map('Treeview', background = [('selected' , self.bgColor)])

        style.configure('Vertical.TScrollbar', 
            background = '#4f4d4d',
            troughcolor = self.bgColor,
            borderwidth = 0
        )

        style.layout('arrowless.Vertical.TScrollbar', 
             [('Vertical.Scrollbar.trough',
               {'children': [('Vertical.Scrollbar.thumb', 
                              {'expand': '1', 'sticky': 'nswe'})],
                'sticky': 'ns'})])




        style.map('Vertical.TScrollbar', background = [('selected' , "blue")])



        style.configure('TButton', 
            background = '#3d3d3d',
            foreground = self.color,
            borderwidth = 0,
            width = 5,
            font = ('Arial', 16)
               
        )

        style.map('TButton', 
                background = [('active' , '#6e6e6e')],
                foreground = [('active', self.color)],      
        )



        style.configure('TFrame', 
            background = self.bgColor
               
        )

        style.configure('TLabel', 
            background = self.bgColor,
            foreground = self.color,
            font = ('Ariel', 32),
            anchor = 'e',
            justify = 'right',
            width = 12
               
        )








if __name__ == '__main__':
    Calculator()