
> Clone and run with:
>
> **Windows:**
>
> ```bash
> git clone https://github.com/yourname/file-encryptor.git
> cd file-encryptor
> run.bat
> ```
>
> **Linux/macOS:**
>
> ```bash
> git clone https://github.com/yourname/file-encryptor.git
> cd file-encryptor
> ./run.sh
> ```

Sure, here's a complete guide to using **Qt Designer** with **PyQt5** in a drag-and-drop fashion, along with how to convert `.ui` files to Python `.py` files using `pyuic5`.

---

## 🛠 What is Qt Designer?

**Qt Designer** is a GUI design tool that comes with PyQt5. It allows you to **visually design GUIs** and save them as `.ui` files (XML format). You then convert that `.ui` file into a `.py` file using `pyuic5`.

---

## ✅ Step-by-Step Guide

### 1. 📦 Install Required Tools

If you haven't already:

```bash
pip install PyQt5 pyqt5-tools
```

---

### 2. 🧱 Open Qt Designer

#### Method 1: Using `pyqt5-tools`

```bash
python -m pyqt5_tools.designer
```

#### Method 2: Direct Path (if installed globally)

If installed in environment:

```bash
path/to/your/env/Lib/site-packages/qt5_applications/Qt/bin/designer.exe
```

Just double-click `designer.exe`.

---

### 3. 🎨 Design Your UI

* Drag components like `QPushButton`, `QLabel`, `QTextEdit`, etc.
* Save the file as `my_ui.ui` (or any name).

---

### 4. 🔁 Convert `.ui` to `.py` using `pyuic5`

Run this command in your terminal:

```bash
pyuic5 -x my_ui.ui -o my_ui.py
```

**Explanation:**

* `-x`: Makes the output Python file runnable directly (adds main check).
* `my_ui.ui`: Input file.
* `-o my_ui.py`: Output file.

---

### 5. 👨‍💻 Use the Converted File in Your Python Code

After conversion, `my_ui.py` will contain a class (usually `Ui_MainWindow` or similar).

#### Example:

If the `.ui` file had a `QMainWindow`, you’d use:

```python
from PyQt5.QtWidgets import QApplication, QMainWindow
from my_ui import Ui_MainWindow  # This was generated

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Now you can access elements like
        self.ui.pushButton.clicked.connect(self.say_hello)

    def say_hello(self):
        print("Hello clicked")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())
```

---

## 🧪 Bonus Tips

* You can edit `.ui` again and re-convert it.
* Use consistent naming in Designer (e.g., `pushButton`, `lineEdit`).
* Keep `.ui` in a separate `ui/` folder to organize large projects.

---

Let me know if you want a **sample UI file** or help integrating it into your existing project like `Secnote`.


