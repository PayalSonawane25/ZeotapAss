import tkinter as tk
from tkinter import messagebox as mb
from rule_engine import RuleEngine

class RuleEngineApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Rule Engine with AST")
        self.master.geometry("700x500")
        
        self.engine = RuleEngine()

        # GUI for rule creation
        self.create_rule_section()

        # Create a frame to display created rules
        self.display_rules_section()

    def create_rule_section(self):
        """Section for creating and adding rules."""
        rule_frame = tk.Frame(self.master)
        rule_frame.pack(pady=10)

        self.rule_name_label = tk.Label(rule_frame, text="Rule Name:")
        self.rule_name_label.grid(row=0, column=0)
        
        self.rule_name_entry = tk.Entry(rule_frame)
        self.rule_name_entry.grid(row=0, column=1)

        self.key_label = tk.Label(rule_frame, text="Rule Expression:")
        self.key_label.grid(row=1, column=0)
        
        self.key_entry = tk.Entry(rule_frame)
        self.key_entry.grid(row=1, column=1)

        self.add_rule_btn = tk.Button(rule_frame, text="Create Rule", command=self.add_rule)
        self.add_rule_btn.grid(row=2, column=0, columnspan=2)

    def add_rule(self):
        """Add rule to the engine."""
        rule_name = self.rule_name_entry.get()
        rule_expr = self.key_entry.get()

        if rule_name and rule_expr:
            try:
                self.engine.create_rule(rule_name, rule_expr)
                mb.showinfo("Success", f"Rule '{rule_name}' created.")
                self.update_rules_display()  # Update the display to show the newly added rule
            except ValueError as e:
                mb.showerror("Error", str(e))
        else:
            mb.showerror("Error", "Please fill in all fields.")

    def display_rules_section(self):
        """Section to display created rules."""
        self.rules_frame = tk.Frame(self.master)
        self.rules_frame.pack(pady=10)

        self.rules_label = tk.Label(self.rules_frame, text="Created Rules:")
        self.rules_label.pack()

        self.rules_listbox = tk.Listbox(self.rules_frame, width=60, height=10)
        self.rules_listbox.pack(pady=10)

        self.display_btn = tk.Button(self.rules_frame, text="Display Rules", command=self.update_rules_display)
        self.display_btn.pack(pady=5)

    def update_rules_display(self):
        """Update the rules display with all created rules."""
        self.rules_listbox.delete(0, tk.END)  # Clear the listbox first
        if not self.engine.rules:
            self.rules_listbox.insert(tk.END, "No rules available.")
        else:
            for rule_name, rule_expr in self.engine.rules.items():
                self.rules_listbox.insert(tk.END, f"{rule_name}: {rule_expr}")

# Run the Tkinter app
if __name__ == "__main__":
    root = tk.Tk()
    app = RuleEngineApp(root)
    root.mainloop()
