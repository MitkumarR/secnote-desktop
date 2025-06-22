
# secNOTE - Secure File Encryption Desktop App

**secNOTE** is a privacy-first, desktop application built with Python and PyQt5 to help you securely create, encrypt, decrypt, and manage your text files. It uses AES symmetric encryption via `cryptography.fernet` to protect your sensitive content, with a clean and simple user interface for a smooth experience.

---

## 📦 Features (Implemented)

### 🔐 Security
- AES-based encryption/decryption using `cryptography` (Fernet).
- Automatic extension change `.txt ➝ .enc` and vice versa.
- Secure file overwrite to prevent data recovery.
- File permission locking after encryption to prevent unauthorized modification or deletion.
- Decryption allowed only for `.enc` files.
- Clipboard-safe key generation and copy support.
- Error handling for incorrect keys or unsupported file types.

### 📁 File Handling
- Open `.txt` or `.enc` files directly.
- Text area for viewing and editing (with appropriate modes).
- Files are securely updated with the same name (extension changed).
- Key generation, key copy, and encryption done in dialog windows.

### 💻 GUI with PyQt5
- Minimal, user-friendly UI built using Qt.
- Menu bar for file and action management.
- Dialog windows for focused encryption and decryption flows.
- Modular UI code with proper layout and geometry.

---

## 🚀 Getting Started

### 🧰 Prerequisites
- Python 3.8+
- Install required libraries:
  ```bash
  pip install PyQt5 cryptography


### ▶️ Clone and Run

**Windows:**

```bash
git clone https://github.com/yourname/file-encryptor.git
cd file-encryptor
run.bat
```

**Linux/macOS:**

```bash
git clone https://github.com/yourname/file-encryptor.git
cd file-encryptor
./run.sh
```


<!--
## 🔮 Planned Features / Future Enhancements

### 🔐 Security-Oriented

* [ ] **Password-based Key Generation**
  Derive key from a password using PBKDF2. Users don’t need to store raw keys.

* [ ] **Auto-Lock After Inactivity**
  Auto-lock or encrypt files after a period of inactivity.

* [ ] **Master Password for App Access**
  App entry locked behind a secure master password (bcrypt).

* [ ] **Clipboard Timeout**
  Automatically clear keys from clipboard after N seconds.

---

### 📁 Workflow Improvements

* [ ] **History Panel**
  Log of encrypted/decrypted files with timestamps.

* [ ] **Drag-and-Drop Support**
  Users can drag `.txt` or `.enc` files into the app to open them.

* [ ] **Batch Encryption/Decryption**
  Multi-file selection and bulk processing.

* [ ] **Encrypted Notes Viewer**
  Read-only preview of encrypted (raw) data before decryption.

---

### 💻 UI/UX Enhancements

* [ ] **Dark Mode Support**
* [ ] **System Tray Integration**
* [ ] **Visual Loading Feedback**
* [ ] **Quick Actions from Tray**

---

### ☁️ Advanced Ideas (Optional)

* [ ] **Cloud Sync Integration** (Google Drive / Dropbox)
* [ ] **QR Code Key Sharing**
* [ ] **Digital Signature Verification**
* [ ] **Self-Destruct After Failed Attempts**

---

## 📁 Folder Structure

```
Secnote/
│
├── gui/                  # Main window, Encrypt/Decrypt dialogs
├── core/                 # Key utilities, file operations
├── scripts/              # .bat and .sh scripts for file locking
├── run.sh                # Linux/macOS runner
├── run.bat               # Windows runner
├── main.py               # App entry point
└── README.md
```

---

## 👨‍💻 Author

Developed by **Mit (aka Mice)**
Computer Science Student | Enthusiast in Security, Python & Systems

---

## 🛡️ License

MIT License. See the [LICENSE](LICENSE) file.


-->