# 🧠 AI Psychologist Chatbot

A simple, non-therapeutic **psychological chatbot** built in Python.  
This lightweight console-based application simulates a supportive conversation with users, offering empathetic responses to emotions such as sadness, happiness, or anger.  

> ⚠️ *This chatbot is not a replacement for professional therapy. It is designed solely for educational and supportive interaction purposes.*

---

## 🧩 Features

- 💬 Engages users in friendly, non-judgmental conversations  
- 🧠 Detects basic emotions from user input (e.g., *sad, happy, angry*)  
- 🔁 Maintains a continuous chat loop until the user types `bye`, `quit`, or `exit`  
- ⚙️ Uses Python’s built-in `random` module for varied responses  
- 🗂️ Rule-based system using dictionaries — no external dependencies  

---

## 🛠️ Technologies Used

- **Language:** Python 3.11  
- **Libraries:**  
  - `random` (built-in)  
- **Interface:** Command Line Interface (CLI)

---

## 📋 How It Works

The chatbot uses **keyword matching** to determine the user’s emotional state and selects a predefined response from a dictionary.  

For example:
- Input: “I feel sad today.”  
  → Output: “I'm sorry you're feeling sad. Want to talk about what's bothering you?”  
- Input: “I’m happy today!”  
  → Output: “That’s great! What made you feel happy today?”

---

## 🚀 How to Run

1. **Clone or download** the project files.  
2. Open a terminal or command prompt in the project folder.  
3. Run the Python file:  
   ```bash
   python ai_pysch.py
   ```
4. Start chatting with your AI psychologist!  
   Type `bye`, `exit`, or `quit` to end the conversation.

---

## 📁 Project Structure

```
ai_pysch.py        # Main Python script containing chatbot logic
README.md          # Project documentation
```

---

## 🧠 Example Interaction

```
AI Psychologist: Hi! I'm your AI psychologist. How are you feeling today?
You: I'm feeling a bit sad.
AI Psychologist: It’s okay to feel sad sometimes. What do you think caused it?
You: I just had a rough day.
AI Psychologist: That sounds tough. What usually helps you feel better?
You: bye
AI Psychologist: Take care of yourself. Goodbye!
```

---

## 🧾 Future Enhancements

- Add a GUI using **Tkinter** or **PyQt**  
- Integrate more advanced NLP with **NLTK** or **spaCy**  
- Enable response logging and mood tracking  
- Include multilingual support  

---

## 👨‍💻 Author

**Name:** ""  
**Department:** ""  
**Institution:** ""  
**Semester:** ""  

---

## 📚 References

- Python 3.11 Documentation  
- Command Line Interface Programming in Python  
- Research on Woebot, Wysa, and Youper Chatbots  
