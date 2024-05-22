import tkinter as tk
from phonics import pro_generator



temp = [0]
test_obj = pro_generator(1, 1, 1, 1)
control_panel = tk.Tk()
control_panel.geometry("600x600")
control_panel.title("發音產生器")
word_number_label = tk.Label(control_panel, text="1. 輸入要產生的字數(>0)")
word_number_label.place(x = 10, y = 10)

result = tk.StringVar()

print(test_obj.Cis)
print("---------------------------")
print(test_obj.Vs)
print("---------------------------")
print(test_obj.Cs)
print("---------------------------")

def set_number():
    test_obj.word_number = word_number.get()
    # print(test_obj.generate_phonics())

def set_order(entry_x, entry_y, button_var, cust_bool):
   
    entry_x += 300
    print("test")
    part = int(button_var.get()[-1])
    group_type = {1:"頭子音", 2:"母音", 3:"尾子音"}
    groups = [test_obj.Cis, test_obj.Vs, test_obj.Cs]
    # orders = ['', '', '']
    print(test_obj.Ci_order)
    def save_order_cust():
        
         
        if part == 1:
            test_obj.Cis.append(list(map(lambda p: p.strip(), cust.get().split(','))))
            test_obj.Ci_order = len(test_obj.Cis)
        elif part == 2:
            test_obj.Vs.append(list(map(lambda p: p.strip(), cust.get().split(','))))
            test_obj.V_order = len(test_obj.Vs)
        else:
            test_obj.Cs.append(list(map(lambda p: p.strip(), cust.get().split(','))))
            test_obj.C_order = len(test_obj.Cs)

        print("final_orders", test_obj.Ci_order, test_obj.V_order, test_obj.C_order)
   

    if cust_bool.get().lower() == "yes":
        cust_label = tk.Label(control_panel, text=f"輸入自選{group_type[part]}並以','分隔(例:th, sh)")
        cust_label.place(x = entry_x, y = entry_y - 30)
        label_y = entry_y - 30
        cust = tk.StringVar()
        cust_entry = tk.Entry(control_panel, textvariable=cust, width=15)
        cust_entry.place(x = entry_x, y = (label_y + 15))
        # groups[part - 1].append(list(map(lambda p: p.strip(), cust.get().split(','))))
        
        # orders[part - 1] = len(groups[part - 1])
        cust_button = tk.Button(control_panel, text="確定", command=save_order_cust)
        cust_button.place(x = entry_x + 80, y = (label_y + 15))
       
    def save_order():
        print("called", order.get())
        
        
        if part == 1:
            test_obj.Ci_order = order.get()
        elif part == 2:
            test_obj.V_order = order.get()
        else:
            test_obj.C_order = order.get()

        print("final_orders", test_obj.Ci_order, test_obj.V_order, test_obj.C_order)
            
    #       Ci_order = len(Cis)
    if cust_bool.get().lower() == "no":
        
    
        default_label = tk.Label(control_panel, text=f"從第1~{len(groups[part - 1])}組中選一組頭子音(例:1)")
        default_label.place(x = entry_x, y = entry_y - 30)
        label_y = entry_y - 30
        order = tk.IntVar()
        order.set(0)
        order_entry = tk.Entry(control_panel, textvariable=order, width=5)
        order_entry.place(x = entry_x, y = (label_y + 15))
        # orders[part - 1] = order.get()
        order_button = tk.Button(control_panel, text="確定", command=save_order)
        order_button.place(x = entry_x + 40, y = (label_y + 15))
    
    
def generate_phonics():
   
    result = tk.StringVar()
    result.set(test_obj.generate_phonics().to_list())
    
    print(result.get())
    print(test_obj.generate_phonics())
    

    result_frame = tk.Frame(control_panel, width=200, height=200, bg = 'white')
    result_frame.place(x=5, y=300)
    scrollbar = tk.Scrollbar(result_frame)
    # scrollbar.place(x = 485, y=0, height=250)
    scrollbar.pack(side='right', fill='y')
    
    result_listbox = tk.Listbox(result_frame,  listvariable=result, height=200, width=200, yscrollcommand=scrollbar.set)
    result_listbox.pack(side='left', fill='y')  
    # result_listbox.place(x=5, y=0)
    scrollbar.config(command = result_listbox.yview)
    
word_number = tk.IntVar()
word_number.set('')
word_number_entry = tk.Entry(control_panel, textvariable=word_number, width=5)
word_number_entry.place(x = 10, y = 30)
word_number_button = tk.Button(control_panel, text="確定", command=set_number)
word_number_button.place(x = 50, y = 30)
cust_bool = tk.StringVar()
cust_bool.set('')
hint_texts = ["2. 頭子音是否客製化(yes/no)?", " 3. 母音是否客製化(yes/no)?", " 4. 尾子音是否客製化(yes/no)?"]
init_x, init_y = 10, 55

# for 0 in range(3):
#### Ci
label = tk.Label(control_panel, text=hint_texts[0])
label.place(x = init_x, y = init_y + 0 * 55)
cust_bool = tk.StringVar()

order_entry = tk.Entry(control_panel, textvariable=cust_bool, width=5)
entry_x1, entry_y1 = init_x, init_y + 0 * 55 + 30

order_entry.place(x = entry_x1, y = entry_y1)

button_var = tk.StringVar()
button_var.set(f"確定{0 + 1}")
order_button = tk.Button(control_panel, textvariable=button_var, command=lambda: set_order(entry_x1, entry_y1, button_var, cust_bool))
order_button.place(x = init_x + 40, y = entry_y1)

#### V
label2 = tk.Label(control_panel, text=hint_texts[1])
label2.place(x = init_x, y = init_y + 1 * 55)
cust_bool2 = tk.StringVar()
order_entry2 = tk.Entry(control_panel, textvariable=cust_bool2, width=5)
entry_x2, entry_y2 = init_x, init_y + 1 * 55 + 30

order_entry2.place(x = entry_x2, y = entry_y2)

button_var2 = tk.StringVar()
button_var2.set(f"確定{1 + 1}")
order_button2 = tk.Button(control_panel, textvariable=button_var2, command=lambda: set_order(entry_x2, entry_y2, button_var2, cust_bool2))
order_button2.place(x = init_x + 40, y = entry_y2)

#### C

label3 = tk.Label(control_panel, text=hint_texts[2])
label3.place(x = init_x, y = init_y + 2 * 55)
cust_bool3 = tk.StringVar()
order_entry3 = tk.Entry(control_panel, textvariable=cust_bool3, width=5)
entry_x3, entry_y3 = init_x, init_y + 2 * 55 + 30

order_entry3.place(x = entry_x3, y = entry_y3)

button_var3 = tk.StringVar()
button_var3.set(f"確定{1 + 2}")
order_button3 = tk.Button(control_panel, textvariable=button_var3, command=lambda: set_order(entry_x3, entry_y3, button_var3, cust_bool3))
order_button3.place(x = init_x + 40, y = entry_y3)

# print("temp1: ", temp)
generate_button = tk.Button(control_panel, text="產生結果", command=generate_phonics)
generate_button.place(x = init_x + 40, y = entry_y3 + 55)


control_panel.mainloop()
