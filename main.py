import requests
# import openai
import os
from tkinter import *

api_endpoint = "https://api.openai.com/v1/completions"
api_key = "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"

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + api_key
}


def delete_files():
    folder = "solutions"
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(e)


def generate():
    input_task = user_input.get()
    file_name = entry_file_name.get()
    count_solution = int(entry_num_version.get())

    for n in range(0, count_solution):

        request_data = {
            "model": "text-davinci-003",
            "prompt": f"Write python script to {input_task}. Provide only code, no text",
            "max_tokens": 500,
            "temperature": 0.5,
        }

        response = requests.post(api_endpoint, headers=headers, json=request_data)

        if response.status_code == 200:
            response_text = response.json()["choices"][0]["text"]
            with open(f"solutions/ver_{n}_{file_name}", mode="w") as file:
                file.write(response_text)
        else:
            print(f"Request failed with status code: {str(response.status_code)}")


# -------------------------------
window = Tk()
window.title("Automation with ChatGPT")
window.minsize(800, 300)
window.config(bg="#4C2A85")

main_frame = Frame(window, bg="#4C2A85")
main_frame.pack()

label_input_description = Label(main_frame, text="Write python script to:", bg="#4C2A85", fg="#FFF",
                                font=("Helvetica", "12", "bold"))
label_input_description.pack(pady=10)

user_input = Entry(main_frame, width=80, font=("Helvetica", "12"))
user_input.focus_set()
user_input.pack(pady=(0, 10))

count_button = Button(main_frame, text="generate", font=("Helvetica", "12", "bold"), command=generate)
count_button.pack(pady=(0, 10))

button_delete_solution = Button(main_frame, text="delete solutions folder", font=("Helvetica", "12", "bold"),
                                command=delete_files)
button_delete_solution.pack(pady=(30, 0), side="bottom")

label_file_name = Label(main_frame, text="file name:", bg="#4C2A85", fg="#FFF", font=("Helvetica", "12", "bold"))
label_file_name.pack(side="left", padx=(20, 0))

entry_file_name = Entry(main_frame, width=20, font=("Helvetica", "12"))
entry_file_name.insert(0, "output.py")
entry_file_name.pack(side="left", padx=(0, 20), pady=20)

entry_num_version = Entry(main_frame, width=20, font=("Helvetica", "12"))
entry_num_version.insert(0, "3")
entry_num_version.pack(side="right", padx=(0, 20))

label_file_name = Label(main_frame, text="count solutions:", bg="#4C2A85", fg="#FFF", font=("Helvetica", "12", "bold"))
label_file_name.pack(side="right")

window.mainloop()
