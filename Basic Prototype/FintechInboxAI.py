import tkinter as tk
from tkinter import ttk, messagebox
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import pandas as pd

# Load your dataset
data = pd.read_csv("data.csv")  # Adjust path as needed

# Function to classify email content
def classify_email(data, content):
    # Add the entered content to the dataset
    new_data = pd.DataFrame({'Email_Content': [content], 'Category': ['Unknown']})
    updated_data = pd.concat([data, new_data], ignore_index=True)
    
    # Perform feature extraction
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(updated_data['Email_Content'])
    y = updated_data['Category']
    
    # Train classifier
    clf = MultinomialNB(alpha=0.1)  # Adjust alpha parameter to prevent overfitting
    clf.fit(X, y)
    
    # Predict category for the entered content
    X_new = vectorizer.transform([content])
    predicted_category = clf.predict(X_new)
    
    return predicted_category[0]

# Function to handle button click event
def classify_email_click():
    email_content = text_entry.get("1.0",'end-1c')
    if email_content.strip() == '':
        messagebox.showwarning("Warning", "Please enter email content.")
    else:
        category = classify_email(data, email_content)
        messagebox.showinfo("Classification Result", f"The entered email content belongs to category: {category}")

#Function to change theme
def change_theme():
    theme = theme_var.get()
    if theme == "Light":
        root.tk_setPalette(background='#FFFFFF', foreground='#000000')
    elif theme == "Dark":
        root.tk_setPalette(background='#2E2E2E', foreground='#FFFFFF')
    else:  # System theme
        root.tk_setPalette("")

# Create GUI window
root = tk.Tk()
root.title("Email Classifier")

# Add theme selection option
theme_var = tk.StringVar()
theme_var.set("System")
theme_label = tk.Label(root, text="Select Theme:")
theme_label.pack()
theme_combobox = ttk.Combobox(root, textvariable=theme_var, values=["System", "Light", "Dark"], state="readonly")
theme_combobox.pack()
theme_combobox.bind("<<ComboboxSelected>>", lambda event: change_theme())

# Add a label for email content
email_label = tk.Label(root, text="Enter Email Content:")
email_label.pack()

# Create text entry field
text_entry = tk.Text(root, height=10, width=50)
text_entry.pack()

# Add a separator
separator = ttk.Separator(root, orient=tk.HORIZONTAL)
separator.pack(fill=tk.X, padx=5, pady=5)

# Create classify button
classify_button = tk.Button(root, text="Classify Email", command=classify_email_click, width=20)
classify_button.pack(pady=5)

# Run GUI main loop
root.mainloop()
