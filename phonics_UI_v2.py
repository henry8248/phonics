import tkinter as tk
from tkinter import ttk, messagebox
import random

# Define the syllable groups and subgroups
syllables = {
    'Ci': {
        'Ci1': ['b', 'p', 'm', 'f', 'd', 't', 'n', 'l'],
        'Ci2': ['g', 'k', 'h', 'm', 'n', 's', 'r'],
        'Ci3': ['v', 'w', 'z'],
        'Ci4': ['dr', 'tr', 'br', 'pr'],
        'Ci5': ['bl', 'pl', 'kl', 'sl'],
        'Ci6': ['sm', 'sn', 'sp', 'st', 'sk', 'str']
    },
    'V': {
        'V1': ['a', 'e', 'i', 'o', 'u'],
        'V2': ['_a_e', '_e_e', '_i_e', '_o_e', '_u_e'],
        'V3': ['ay', 'ai', 'ea', 'ee', 'oa'],
        'V4': ['ar', 'er', 'ir', 'or', 'ur'],
        'V5': ['ou', 'ow', 'oi']
    },
    'C': {
        'C1': ['s', 'ss'],
        'C2': ['b', 'p'],
        'C3': ['d', 't'],
        'C4': ['g', 'k'],
        'C5': ['st', 'sp', 'sk'],
        'C6': ['m', 'n'],
        'C7': ['m', 'mb', 'mp'],
        'C8': ['n', 'nd', 'nt'],
        'C9': ['ph', 'ch', 'sh', 'ths']
    }
}

# Function to generate words
def generate_words(ci_groups, v_groups, c_groups, num_words, custom_syllables):
    words = []
    v_flag = False
    ci_choices = sum([syllables["Ci"].get(group, []) for group in ci_groups], []) + custom_syllables['Ci']
    v_choices = sum([syllables["V"].get(group, []) for group in v_groups], []) + custom_syllables['V']
    c_choices = sum([syllables["C"].get(group, []) for group in c_groups], []) + custom_syllables['C']
    
    for _ in range(num_words):
        ci = random.choice(ci_choices)
        v = random.choice(v_choices)
        if v[-1] in ['a', 'e', 'i', 'o', 'u', 'r']:
            c = random.choice(c_choices)
        else:
            c = ''
        
        if '_' in v:
            v_flag = True
            v = v.replace('_', ci, 1).replace('_', c, 1)
        else:
            v_flag = False
        
        word = ci + v + c if not v_flag else v
        words.append(word)
    return words

# Function to add custom subgroups
def add_custom_syllable(custom_syllables, group, entry, listbox):
    elements = entry.get().split(',')
    custom_syllables[group].extend(elements)
    entry.delete(0, tk.END)
    listbox.insert(tk.END, *elements)
    messagebox.showinfo("Info", f"Added custom {group} syllables: {elements}")

# Function to clear custom subgroups
def clear_custom_syllables(custom_syllables, group, listbox):
    custom_syllables[group].clear()
    listbox.delete(0, tk.END)
    messagebox.showinfo("Info", f"Cleared custom {group} syllables.")

# GUI Code
def generate():
    ci_groups = [ci_var.get() for ci_var in ci_vars if ci_var.get()]
    v_groups = [v_var.get() for v_var in v_vars if v_var.get()]
    c_groups = [c_var.get() for c_var in c_vars if c_var.get()]
    num_words = int(num_words_entry.get())
    
    if not ci_groups and not custom_syllables['Ci']:
        messagebox.showerror("Error", "Please select or define at least one subgroup from Ci.")
        return
    if not v_groups and not custom_syllables['V']:
        messagebox.showerror("Error", "Please select or define at least one subgroup from V.")
        return
    if not c_groups and not custom_syllables['C']:
        messagebox.showerror("Error", "Please select or define at least one subgroup from C.")
        return
    
    generated_words = generate_words(ci_groups, v_groups, c_groups, num_words, custom_syllables)
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, "\n".join(generated_words))

# Create the main window
root = tk.Tk()
root.title("Pronunciation Practice")

custom_syllables = {'Ci': [], 'V': [], 'C': []}

# Ci Group
ci_frame = ttk.LabelFrame(root, text="Ci Groups")
ci_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

ci_vars = [tk.StringVar() for _ in range(6)]
for i, ci_group in enumerate(syllables["Ci"].keys()):
    chk = ttk.Checkbutton(ci_frame, text=ci_group, variable=ci_vars[i], onvalue=ci_group, offvalue="")
    chk.grid(row=i, column=0, sticky="w")

ci_custom_label = ttk.Label(ci_frame, text="Custom Ci:")
ci_custom_label.grid(row=6, column=0, sticky="w")
ci_custom_entry = ttk.Entry(ci_frame)
ci_custom_entry.grid(row=7, column=0, sticky="w")
ci_custom_button = ttk.Button(ci_frame, text="Add", command=lambda: add_custom_syllable(custom_syllables, 'Ci', ci_custom_entry, ci_custom_listbox))
ci_custom_button.grid(row=7, column=1, sticky="w")

ci_custom_listbox = tk.Listbox(ci_frame, height=5)
ci_custom_listbox.grid(row=8, column=0, columnspan=2, sticky="w")

ci_clear_button = ttk.Button(ci_frame, text="Clear", command=lambda: clear_custom_syllables(custom_syllables, 'Ci', ci_custom_listbox))
ci_clear_button.grid(row=9, column=0, sticky="w")


# V Group
v_frame = ttk.LabelFrame(root, text="V Groups")
v_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

v_vars = [tk.StringVar() for _ in range(5)]
for i, v_group in enumerate(syllables["V"].keys()):
    chk = ttk.Checkbutton(v_frame, text=v_group, variable=v_vars[i], onvalue=v_group, offvalue="")
    chk.grid(row=i, column=0, sticky="w")

v_custom_label = ttk.Label(v_frame, text="Custom V:")
v_custom_label.grid(row=5, column=0, sticky="w")
v_custom_entry = ttk.Entry(v_frame)
v_custom_entry.grid(row=6, column=0, sticky="w")
v_custom_button = ttk.Button(v_frame, text="Add", command=lambda: add_custom_syllable(custom_syllables, 'V', v_custom_entry, v_custom_listbox))
v_custom_button.grid(row=6, column=1, sticky="w")

v_custom_listbox = tk.Listbox(v_frame, height=5)
v_custom_listbox.grid(row=7, column=0, columnspan=2, sticky="w")

v_clear_button = ttk.Button(v_frame, text="Clear", command=lambda: clear_custom_syllables(custom_syllables, 'V', v_custom_listbox))
v_clear_button.grid(row=8, column=0, sticky="w")


# C Group
c_frame = ttk.LabelFrame(root, text="C Groups")
c_frame.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")

c_vars = [tk.StringVar() for _ in range(9)]
for i, c_group in enumerate(syllables["C"].keys()):
    chk = ttk.Checkbutton(c_frame, text=c_group, variable=c_vars[i], onvalue=c_group, offvalue="")
    chk.grid(row=i, column=0, sticky="w")

c_custom_label = ttk.Label(c_frame, text="Custom C:")
c_custom_label.grid(row=9, column=0, sticky="w")
c_custom_entry = ttk.Entry(c_frame)
c_custom_entry.grid(row=10, column=0, sticky="w")
c_custom_button = ttk.Button(c_frame, text="Add", command=lambda: add_custom_syllable(custom_syllables, 'C', c_custom_entry, c_custom_listbox))
c_custom_button.grid(row=10, column=1, sticky="w")

c_custom_listbox = tk.Listbox(c_frame, height=5)
c_custom_listbox.grid(row=11, column=0, columnspan=2, sticky="w")

c_clear_button = ttk.Button(c_frame, text="Clear", command=lambda: clear_custom_syllables(custom_syllables, 'C', c_custom_listbox))
c_clear_button.grid(row=12, column=0, sticky="w")


# Number of Words
num_words_label = ttk.Label(root, text="Number of Words:")
num_words_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
num_words_entry = ttk.Entry(root)
num_words_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")
num_words_entry.insert(0, "10")

# Generate Button
generate_button = ttk.Button(root, text="Generate", command=generate)
generate_button.grid(row=1, column=2, padx=10, pady=10, sticky="e")

# Result Text Box with Scrollbar
result_frame = ttk.Frame(root)
result_frame.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

result_text = tk.Text(result_frame, height=15, width=50)
result_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = ttk.Scrollbar(result_frame, orient=tk.VERTICAL, command=result_text.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

result_text.config(yscrollcommand=scrollbar.set)

# Run the application
root.mainloop()
