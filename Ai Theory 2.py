import tkinter as tk
from tkinter import messagebox
import random
class MissingNumberGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Missing Number Hunt - Decrease & Conquer")
        self.root.geometry("500x500")
        self.label = tk.Label(root, text="Select Difficulty", font=("Arial", 16))
        self.label.pack(pady=20)
        tk.Button(root, text="Easy (1-20)", command=lambda: self.start_game(20)).pack(pady=5)
        tk.Button(root, text="Medium (1-50)", command=lambda: self.start_game(50)).pack(pady=5)
        tk.Button(root, text="Hard (1-100)", command=lambda: self.start_game(100)).pack(pady=5)
    def start_game(self, N):
        self.N = N
        numbers = list(range(1, N+1))
        self.missing = random.choice(numbers)
        numbers.remove(self.missing)
        random.shuffle(numbers)

        # store for algorithm calculation
        self.numbers = numbers

        # Clear screen
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text=f"Numbers (1-{N}) — 1 Missing", font=("Arial", 14)).pack(pady=10)

        # Scrollable area to show numbers
        frame = tk.Frame(self.root)
        frame.pack()

        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.text_area = tk.Text(frame, height=10, width=40, yscrollcommand=scrollbar.set)
        self.text_area.pack()

        scrollbar.config(command=self.text_area.yview)

        # Display randomized list
        self.text_area.insert(tk.END, " ".join(map(str, numbers)))

        tk.Label(self.root, text="\nEnter the missing number:", font=("Arial", 12)).pack()

        self.answer_entry = tk.Entry(self.root, font=("Arial", 14))
        self.answer_entry.pack(pady=10)

        tk.Button(self.root, text="Submit Answer", command=self.check_answer).pack(pady=10)

    def check_answer(self):
        try:
            guess = int(self.answer_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number!")
            return

        # Decrease-and-conquer method to check
        total = self.N * (self.N + 1) // 2
        for num in self.numbers:
            total -= num

        if guess == total:
            messagebox.showinfo("Correct!", f"🎉 Correct! The missing number was {self.missing}")
        else:
            messagebox.showerror("Incorrect", f"❌ Wrong! The missing number was {self.missing}")
        
        # Ask to restart
        if messagebox.askyesno("Play Again?", "Do you want to play again?"):
            self.reset_game()
        else:
            self.root.quit()

    def reset_game(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.__init__(self.root)


# Run game
root = tk.Tk()
game = MissingNumberGame(root)
root.mainloop()