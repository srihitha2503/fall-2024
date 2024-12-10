import tkinter as tk
from tkinter import colorchooser
import random

# Function to map custom color names to hex codes
def map_color_name_to_hex(color_name):
    color_map = {
        "peach": "#FFDAB9",  # Peach color in hex
        "lightbrown": "#D2B48C",  # Light brown color in hex
        "pink": "#FFC0CB",  # Pink color in hex
        "lightblue": "#ADD8E6",  # Light blue color in hex
        "green": "#008000",  # Green color in hex
        "black": "#000000",  # Black color in hex
        "brown": "#A52A2A",  # Brown color in hex
        "blue": "#0000FF",  # Blue color in hex
        "blonde": "#FAF0BE",  # Blonde color in hex
        "yellow": "#FFFF00",  # Yellow color in hex
    }
    return color_map.get(color_name.strip().lower(), color_name.strip())

# Function to open color picker dialog and update the entry field with the selected color
def choose_color(entry_field):
    color_code = colorchooser.askcolor()[1]  # Returns tuple (RGB, hex)
    if color_code:
        entry_field.delete(0, tk.END)  # Clear the current entry
        entry_field.insert(0, color_code)  # Insert the selected color code

# Function to draw a more realistic person based on the user's input
def draw_person(hair_color, eye_color, clothing_color, skin_color, gender, hairstyle, expression):
    # Create a new window for the drawing
    draw_window = tk.Toplevel()  # This creates a new window (tab)
    draw_window.title("Your Police Sketch")
    
    # Create a Canvas widget for drawing
    canvas = tk.Canvas(draw_window, width=300, height=500)
    canvas.pack()

    # Map the skin color if it matches a custom name
    skin_color = map_color_name_to_hex(skin_color)
    hair_color = map_color_name_to_hex(hair_color)
    eye_color = map_color_name_to_hex(eye_color)
    clothing_color = map_color_name_to_hex(clothing_color)
    
    # Draw the person's head (human-like oval with slight chin)
    canvas.create_oval(100, 50, 200, 150, fill=skin_color, outline="black")  # Head
    
    # Draw the hair based on the selected hairstyle
    if hairstyle == "short":
        canvas.create_rectangle(100, 50, 200, 80, fill=hair_color, outline="black")  # Short hair
    elif hairstyle == "long":
        canvas.create_rectangle(100, 50, 200, 120, fill=hair_color, outline="black")  # Long hair
    elif hairstyle == "curly":
        canvas.create_oval(100, 40, 200, 100, fill=hair_color, outline="black")  # Curly hair
    
    # Draw the eyes (two small circles with pupils)
    canvas.create_oval(130, 80, 150, 100, fill=eye_color, outline="black")  # Left eye
    canvas.create_oval(170, 80, 190, 100, fill=eye_color, outline="black")  # Right eye
    canvas.create_oval(140, 90, 145, 95, fill="black")  # Left pupil
    canvas.create_oval(180, 90, 185, 95, fill="black")  # Right pupil
    
    # Draw the nose (simple line for now)
    canvas.create_line(160, 110, 160, 125, width=2)  # Nose
    
    # Draw the mouth based on the selected expression
    if expression == "happy":
        canvas.create_arc(130, 120, 170, 150, start=0, extent=-180, style=tk.ARC, width=2)  # Happy mouth
    elif expression == "sad":
        canvas.create_arc(130, 120, 170, 150, start=180, extent=180, style=tk.ARC, width=2)  # Sad mouth
    elif expression == "surprised":
        canvas.create_oval(130, 130, 170, 160, outline="black", width=2)  # Surprised mouth
    
    # Draw the ears (simple ovals)
    canvas.create_oval(100, 100, 120, 130, fill=skin_color, outline="black")  # Left ear
    canvas.create_oval(180, 100, 200, 130, fill=skin_color, outline="black")  # Right ear
    
    # Draw the body (simple rectangle with more realistic proportions)
    canvas.create_rectangle(125, 150, 175, 250, fill=clothing_color, outline="black")  # Torso
    
    # Draw the arms (more realistic proportions)
    canvas.create_line(100, 175, 125, 200, width=2)  # Left arm
    canvas.create_line(200, 175, 175, 200, width=2)  # Right arm
    
    # Draw the legs (realistic proportions)
    canvas.create_line(125, 250, 125, 300, width=2)  # Left leg
    canvas.create_line(175, 250, 175, 300, width=2)  # Right leg
    
    # Gender-specific details
    if gender.lower() == "female":
        # Add a simple skirt for females
        canvas.create_rectangle(125, 250, 175, 280, fill="pink", outline="black")
    elif gender.lower() == "male":
        # Add pants for males
        canvas.create_rectangle(125, 250, 175, 280, fill="blue", outline="black")
    
    # Display the drawing
    draw_window.mainloop()

# Function to generate a random character
def generate_random_character():
    hair_colors = ["black", "brown", "blonde", "red"]
    eye_colors = ["blue", "green", "brown", "gray"]
    clothing_colors = ["red", "blue", "green", "yellow"]
    skin_colors = ["peach", "lightbrown", "pink"]
    hairstyles = ["short", "long", "curly"]
    expressions = ["happy", "sad", "surprised"]
    genders = ["male", "female"]
    
    # Generate random characteristics
    hair_color = random.choice(hair_colors)
    eye_color = random.choice(eye_colors)
    clothing_color = random.choice(clothing_colors)
    skin_color = random.choice(skin_colors)
    gender = random.choice(genders)
    hairstyle = random.choice(hairstyles)
    expression = random.choice(expressions)
    
    # Call the drawing function with random characteristics
    draw_person(hair_color, eye_color, clothing_color, skin_color, gender, hairstyle, expression)

# Main application window
def main_window():
    root = tk.Tk()
    root.title("Person Drawing Game")
    
    # Instructions
    instructions = tk.Label(root, text="Enter characteristics to create your person:")
    instructions.pack(pady=10)
    
    # Hair Color Input
    hair_label = tk.Label(root, text="Choose Hair Color:")
    hair_label.pack()
    hair_entry = tk.Entry(root)
    hair_entry.pack()
    hair_color_button = tk.Button(root, text="Choose Color", command=lambda: choose_color(hair_entry))
    hair_color_button.pack()

    # Eye Color Input
    eye_label = tk.Label(root, text="Choose Eye Color:")
    eye_label.pack()
    eye_entry = tk.Entry(root)
    eye_entry.pack()
    eye_color_button = tk.Button(root, text="Choose Color", command=lambda: choose_color(eye_entry))
    eye_color_button.pack()

    # Clothing Color Input
    clothing_label = tk.Label(root, text="Choose Clothing Color:")
    clothing_label.pack()
    clothing_entry = tk.Entry(root)
    clothing_entry.pack()
    clothing_color_button = tk.Button(root, text="Choose Color", command=lambda: choose_color(clothing_entry))
    clothing_color_button.pack()

    # Skin Color Input
    skin_label = tk.Label(root, text="Choose Skin Color:")
    skin_label.pack()
    skin_entry = tk.Entry(root)
    skin_entry.pack()
    skin_color_button = tk.Button(root, text="Choose Color", command=lambda: choose_color(skin_entry))
    skin_color_button.pack()

    # Gender Input (Male or Female)
    gender_label = tk.Label(root, text="Enter Gender (Male/Female):")
    gender_label.pack()
    gender_entry = tk.Entry(root)
    gender_entry.pack()
    
    # Expression Input (Happy, Sad, Surprised)
    expression_label = tk.Label(root, text="Enter Expression (Happy/Sad/Surprised):")
    expression_label.pack()
    expression_entry = tk.Entry(root)
    expression_entry.pack()
    
    # Hairstyle Input (Short, Long, Curly)
    hairstyle_label = tk.Label(root, text="Enter Hairstyle (Short/Long/Curly):")
    hairstyle_label.pack()
    hairstyle_entry = tk.Entry(root)
    hairstyle_entry.pack()
    
    # Submit Button to create the drawing
    def submit():
        hair_color = hair_entry.get()
        eye_color = eye_entry.get()
        clothing_color = clothing_entry.get()
        skin_color = skin_entry.get()
        gender = gender_entry.get()
        expression = expression_entry.get()
        hairstyle = hairstyle_entry.get()
        
        # Call the draw_person function with inputs
        draw_person(hair_color, eye_color, clothing_color, skin_color, gender, hairstyle, expression)
    
    submit_button = tk.Button(root, text="Create Person", command=submit)
    submit_button.pack(pady=10)
    
    # Generate Random Character Button
    random_button = tk.Button(root, text="Generate Random Character", command=generate_random_character)
    random_button.pack(pady=10)
    
    # Start the GUI loop
    root.mainloop()

# Start the main window
if __name__ == "__main__":
    main_window()













    


