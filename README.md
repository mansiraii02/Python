# ☕ Coffee Bot – Interactive Python Quiz App

**Coffee Bot** is a fun, GUI-based Python app built with **Tkinter** that lets you place a virtual coffee order interactively.  
Choose between **Black**, **Regular**, or **Both** coffees — and customize everything from size, sweetener, milk type, and ice!

---

## 🚀 Features

- Simple, clean **Tkinter GUI**
- Interactive coffee selection flow  
- Options for coffee type, size, milk, sweetener, and ice  
- “Start Over” button to restart anytime  
- Works both **locally on macOS** and **in GitHub Codespaces**

---

## 🧩 Requirements

- **Python 3.10+**
- **Tkinter**
- **xvfb** (for virtual display inside Codespaces)

---

## ⚙️ Setup Instructions (for GitHub Codespaces on Mac)

> By default, GitHub Codespaces has no GUI display.  
> Follow these steps to make your Tkinter app run smoothly.

### 1️⃣ Update and install dependencies
Open the **Codespaces Terminal** and run:

```bash
sudo apt-get update
sudo apt-get install -y python3-tk xvfb
# Python