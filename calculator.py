import tkinter as tk

class CalcGUI:
    
    def __init__(self, master):
        self.num = 0
        self.hold = 0
        self.op = 0
        self.dot = False
        self.master = master
        master.title("Calculator")
        self._build_env(master)
    
    
    def _build_env(self, master):
        
        self.label = tk.Label(master, text=str(self.num))
        self.label.grid(row=0, columnspan=4, sticky=tk.W)
        
        self.add_button = tk.Button(master, text="+", command=self._add)
        self.add_button.grid(row=1, column=3)
        
        self.subtract_button = tk.Button(master, text="-", command=self._subtract)
        self.subtract_button.grid(row=2, column=3)
        
        self.multiply_button = tk.Button(master, text="x", command=self._multiply)
        self.multiply_button.grid(row=3, column=3)
        
        self.divide_button = tk.Button(master, text="/", command=self._divide)
        self.divide_button.grid(row=4, column=3)
        
        self.close_button = tk.Button(master, text="exit", command=master.quit)
        self.close_button.grid(row=5, column=3)
        
        self.clear_button = tk.Button(master, text="AC", command=self._clear)
        self.clear_button.grid(row=5, column=2)
        
        self.equal_button = tk.Button(master, text="=", command=self._equal)
        self.equal_button.grid(row=4, column=2)
        
        self.dot_button = tk.Button(master, text=".", command=self._dot)
        self.dot_button.grid(row=4,column=1)
        
        num_label = [[7,8,9],[4,5,6],[1,2,3]]
        bttn = []
        bn = 0
        for i in range(0,3):
            for j in range(0,3):
                n = num_label[i][j]
                bttn.append(tk.Button(master, text=str(n)))
                bttn[bn]["command"] = lambda x = n: self.num_press(x)
                bttn[bn].grid(row=i+1, column=j)
                bn += 1
        
        self.zero_button = tk.Button(master, text="0")
        self.zero_button["command"] = lambda x = 0: self.num_press(x)
        self.zero_button.grid(row=4, column=0)
        
        
    def _show(self, num):
        self.label.configure(text=str(num))
    
    def num_press(self, n):
        if self.dot:
            if "." not in str(self.hold):
                s_num = str(self.hold) + "."+ str(n)
            else:
                s_num = str(self.hold) + str(n)
            
            self.hold = float(s_num)
            
        else:
            self.hold = (10 * self.hold) + n
        
        self._show(self.hold)
    
    def _dot(self):
        self.dot = True
    
    def _clear(self):
        self.num = 0 
        self.hold = 0
        self.op = 0
        self.dot = False
        self._show(self.num)
    
    def _update(self):
        self.num = self.hold
        self.hold = 0
        
    ## Operators
    
    def _add(self):
        print("add")
        self.op = 1
        self._update()
        
        
    def _subtract(self):
        print("subtract")
        self.op = 2
        self._update()
        
    def _multiply(self):
        print("multiply")
        self.op = 3
        self._update()
        
    def _divide(self):
        print("divide")
        self.op = 4
        self._update()
        
    def _equal(self):
        print("equal")
        if self.op == 1:
            self.num += self.hold
        elif self.op == 2:
            self.num -= self.hold
        elif self.op == 3:
            self.num = self.num * self.hold
        elif self.op == 4:
            self.num = self.num / self.hold
        else:
            pass
        
        self._show(self.num)


root = tk.Tk()
my_gui = CalcGUI(root)
root.mainloop()