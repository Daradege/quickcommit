import tkinter as tk
from tkinter import ttk, messagebox
import pyperclip


class CommitMessageGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Git Commit Message Generator")
        self.root.geometry("800x800")
        self.root.configure(bg='#2d3748')

        self.commit_types = {
            "feat": {"emoji": "✨", "desc": "New feature"},
            "fix": {"emoji": "🐛", "desc": "Bug fix"},
            "docs": {"emoji": "📚", "desc": "Documentation"},
            "style": {"emoji": "💄", "desc": "Code style/formatting"},
            "refactor": {"emoji": "♻️", "desc": "Code refactoring"},
            "perf": {"emoji": "⚡", "desc": "Performance improvement"},
            "test": {"emoji": "🧪", "desc": "Tests"},
            "build": {"emoji": "🏗️", "desc": "Build system"},
            "ci": {"emoji": "👷", "desc": "CI/CD"},
            "chore": {"emoji": "🔧", "desc": "Maintenance"},
            "revert": {"emoji": "⏪", "desc": "Revert changes"},
            "merge": {"emoji": "🔀", "desc": "Merge branches"},
            "hotfix": {"emoji": "🚑", "desc": "Critical hotfix"},
            "init": {"emoji": "🎉", "desc": "Initial commit"},
            "config": {"emoji": "⚙️", "desc": "Configuration"},
            "security": {"emoji": "🔒", "desc": "Security fix"},
            "upgrade": {"emoji": "⬆️", "desc": "Upgrade dependencies"},
            "downgrade": {"emoji": "⬇️", "desc": "Downgrade dependencies"},
            "remove": {"emoji": "🗑️", "desc": "Remove code/files"},
            "add": {"emoji": "➕", "desc": "Add files/dependencies"}
        }

        self.scopes = [
            "api", "ui", "auth", "db", "core", "utils", "config",
            "routes", "models", "views", "components", "services",
            "middleware", "validation", "logging", "cache", "security",
            "tests", "docs", "build", "deploy", "migration"
        ]

        self.setup_ui()

    def setup_ui(self):
        main_frame = tk.Frame(self.root, bg='#2d3748')
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)

        title_label = tk.Label(main_frame, text="Git Commit Message Generator",
                               font=('Arial', 18, 'bold'), fg='#e2e8f0', bg='#2d3748')
        title_label.pack(pady=(0, 20))

        type_frame = tk.Frame(main_frame, bg='#2d3748')
        type_frame.pack(fill='x', pady=(0, 15))

        tk.Label(type_frame, text="Commit Type:", font=('Arial', 12, 'bold'),
                 fg='#e2e8f0', bg='#2d3748').pack(anchor='w')

        self.type_var = tk.StringVar()
        type_combo = ttk.Combobox(type_frame, textvariable=self.type_var,
                                  values=list(self.commit_types.keys()),
                                  state='readonly', width=50)
        type_combo.pack(fill='x', pady=(5, 0))
        type_combo.bind('<<ComboboxSelected>>', self.on_type_change)

        self.type_desc_label = tk.Label(type_frame, text="", font=('Arial', 10),
                                        fg='#a0aec0', bg='#2d3748')
        self.type_desc_label.pack(anchor='w', pady=(2, 0))

        scope_frame = tk.Frame(main_frame, bg='#2d3748')
        scope_frame.pack(fill='x', pady=(0, 15))

        tk.Label(scope_frame, text="Scope (optional):", font=('Arial', 12, 'bold'),
                 fg='#e2e8f0', bg='#2d3748').pack(anchor='w')

        self.scope_var = tk.StringVar()
        scope_combo = ttk.Combobox(scope_frame, textvariable=self.scope_var,
                                   values=self.scopes, width=50)
        scope_combo.pack(fill='x', pady=(5, 0))

        subject_frame = tk.Frame(main_frame, bg='#2d3748')
        subject_frame.pack(fill='x', pady=(0, 15))

        tk.Label(subject_frame, text="Subject:", font=('Arial', 12, 'bold'),
                 fg='#e2e8f0', bg='#2d3748').pack(anchor='w')

        self.subject_entry = tk.Entry(
            subject_frame, font=('Arial', 11), width=50)
        self.subject_entry.pack(fill='x', pady=(5, 0))

        body_frame = tk.Frame(main_frame, bg='#2d3748')
        body_frame.pack(fill='both', expand=True, pady=(0, 15))

        tk.Label(body_frame, text="Body (optional):", font=('Arial', 12, 'bold'),
                 fg='#e2e8f0', bg='#2d3748').pack(anchor='w')

        self.body_text = tk.Text(body_frame, font=(
            'Arial', 10), height=6, width=50)
        self.body_text.pack(fill='both', expand=True, pady=(5, 0))

        options_frame = tk.Frame(main_frame, bg='#2d3748')
        options_frame.pack(fill='x', pady=(0, 15))

        left_options = tk.Frame(options_frame, bg='#2d3748')
        left_options.pack(side='left', fill='x', expand=True)

        self.emoji_var = tk.BooleanVar(value=True)
        tk.Checkbutton(left_options, text="Include emoji", variable=self.emoji_var,
                       font=('Arial', 10), fg='#e2e8f0', bg='#2d3748',
                       selectcolor='#4a5568').pack(anchor='w')

        self.breaking_var = tk.BooleanVar()
        tk.Checkbutton(left_options, text="Breaking change", variable=self.breaking_var,
                       font=('Arial', 10), fg='#e2e8f0', bg='#2d3748',
                       selectcolor='#4a5568').pack(anchor='w')

        self.conventional_var = tk.BooleanVar(value=True)
        tk.Checkbutton(left_options, text="Conventional commits", variable=self.conventional_var,
                       font=('Arial', 10), fg='#e2e8f0', bg='#2d3748',
                       selectcolor='#4a5568').pack(anchor='w')

        right_options = tk.Frame(options_frame, bg='#2d3748')
        right_options.pack(side='right', fill='x', expand=True)

        self.capitalize_var = tk.BooleanVar(value=True)
        tk.Checkbutton(right_options, text="Capitalize subject", variable=self.capitalize_var,
                       font=('Arial', 10), fg='#e2e8f0', bg='#2d3748',
                       selectcolor='#4a5568').pack(anchor='w')

        self.period_var = tk.BooleanVar()
        tk.Checkbutton(right_options, text="End with period", variable=self.period_var,
                       font=('Arial', 10), fg='#e2e8f0', bg='#2d3748',
                       selectcolor='#4a5568').pack(anchor='w')

        self.limit_var = tk.BooleanVar(value=True)
        tk.Checkbutton(right_options, text="Limit to 50 chars", variable=self.limit_var,
                       font=('Arial', 10), fg='#e2e8f0', bg='#2d3748',
                       selectcolor='#4a5568').pack(anchor='w')

        buttons_frame = tk.Frame(main_frame, bg='#2d3748')
        buttons_frame.pack(fill='x', pady=(0, 15))

        generate_btn = tk.Button(buttons_frame, text="Generate Message",
                                 command=self.generate_message, font=(
                                     'Arial', 12, 'bold'),
                                 bg='#4299e1', fg='white', padx=20, pady=8)
        generate_btn.pack(side='left', padx=(0, 10))

        copy_btn = tk.Button(buttons_frame, text="Copy to Clipboard",
                             command=self.copy_to_clipboard, font=(
                                 'Arial', 12),
                             bg='#48bb78', fg='white', padx=20, pady=8)
        copy_btn.pack(side='left', padx=(0, 10))

        clear_btn = tk.Button(buttons_frame, text="Clear All",
                              command=self.clear_all, font=('Arial', 12),
                              bg='#f56565', fg='white', padx=20, pady=8)
        clear_btn.pack(side='left')

        quit_btn = tk.Button(buttons_frame, text="Quit", command=lambda: exit(),
                             font=('Arial', 12), bg='#f56565', fg='white', padx=20, pady=8)
        quit_btn.pack(side='right')

        result_frame = tk.Frame(main_frame, bg='#2d3748')
        result_frame.pack(fill='both', expand=True)

        tk.Label(result_frame, text="Generated Message:", font=('Arial', 12, 'bold'),
                 fg='#e2e8f0', bg='#2d3748').pack(anchor='w')

        self.result_text = tk.Text(result_frame, font=('Courier', 11), height=8, width=50,
                                   bg='#1a202c', fg='#e2e8f0', insertbackground='#e2e8f0')
        self.result_text.pack(fill='both', expand=True, pady=(5, 0))

    def on_type_change(self, event):
        selected_type = self.type_var.get()
        if selected_type in self.commit_types:
            emoji = self.commit_types[selected_type]["emoji"]
            desc = self.commit_types[selected_type]["desc"]
            self.type_desc_label.config(text=f"{emoji} {desc}")

    def generate_message(self):
        commit_type = self.type_var.get()
        scope = self.scope_var.get().strip()
        subject = self.subject_entry.get().strip()
        body = self.body_text.get("1.0", tk.END).strip()

        if not commit_type:
            messagebox.showerror("Error", "Please select a commit type")
            return

        if not subject:
            messagebox.showerror("Error", "Please enter a subject")
            return

        message_parts = []

        if self.conventional_var.get():
            type_part = commit_type
            if scope:
                type_part += f"({scope})"
            if self.breaking_var.get():
                type_part += "!"
            type_part += ": "

            if self.emoji_var.get() and commit_type in self.commit_types:
                type_part = self.commit_types[commit_type]["emoji"] + \
                    " " + type_part

            message_parts.append(type_part)
        elif self.emoji_var.get() and commit_type in self.commit_types:
            message_parts.append(self.commit_types[commit_type]["emoji"] + " ")

        if self.capitalize_var.get():
            subject = subject[0].upper() + subject[1:] if subject else ""

        if self.limit_var.get() and len(subject) > 50:
            subject = subject[:47] + "..."

        if self.period_var.get() and not subject.endswith('.'):
            subject += "."

        message_parts.append(subject)

        commit_message = "".join(message_parts)

        if body:
            commit_message += "\n\n" + body

        if self.breaking_var.get() and not self.conventional_var.get():
            commit_message += "\n\nBREAKING CHANGE: This commit contains breaking changes"

        self.result_text.delete("1.0", tk.END)
        self.result_text.insert("1.0", commit_message)

    def copy_to_clipboard(self):
        message = self.result_text.get("1.0", tk.END).strip()
        if message:
            pyperclip.copy(message)
            messagebox.showinfo("Success", "Message copied to clipboard!")
        else:
            messagebox.showwarning("Warning", "No message to copy")

    def clear_all(self):
        self.type_var.set("")
        self.scope_var.set("")
        self.subject_entry.delete(0, tk.END)
        self.body_text.delete("1.0", tk.END)
        self.result_text.delete("1.0", tk.END)
        self.type_desc_label.config(text="")
        self.emoji_var.set(True)
        self.breaking_var.set(False)
        self.conventional_var.set(True)
        self.capitalize_var.set(True)
        self.period_var.set(False)
        self.limit_var.set(True)


if __name__ == "__main__":
    root = tk.Tk()
    app = CommitMessageGenerator(root)
    root.mainloop()
