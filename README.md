# 🚀 SMS Management System

<div align="center">
  <h1 style="color: #00D4FF; text-shadow: 0 0 15px #00D4FF;">Making AI accessible to everyone </h1>
  <p style="color: #E0E7FF;">Using sms... <span style="animation: typing 3s steps(40, end) infinite;">|</span></p>
  <p>
    <img src="https://img.shields.io/badge/Status-Active-green?style=for-the-badge" alt="Status">
    <img src="https://img.shields.io/badge/Version-1.0-blue?style=for-the-badge" alt="Version">
    <img src="https://img.shields.io/badge/License-MIT-blueviolet?style=for-the-badge" alt="License">
  </p>
</div>

---

## 🌌 Overview

Step into the future with the **SMS Management System**! This sleek Flask-powered app redefines SMS management with a stunning blue "future tech" theme. Featuring a responsive dashboard, real-time graphs, and support for HSDPA USB modems, it’s your gateway to monitoring and controlling SMS operations.✨


## 🎮 Features

- 📊 **Real-Time Monitoring** of SMS logs and interactive graphs.
- 📡 **HSDPA Modem Support** for sending/receiving SMS.
- 🎛️ **Dynamic Dashboard** with start/stop controls.
- 🌐 **Cross-Platform** design for desktop, tablet, and mobile.

## 🛠 Prerequisites

- 🐍 **Python 3.8+** ([Download](https://www.python.org/))
- 📦 **pip** (included with Python)
- 🌐 **USB GSM Modem** (optional, e.g., Huawei E220 with SIM)
- ✍️ **Text Editor** (VS Code, PyCharm, etc.)

## 📦 Installation

1. Clone the repo:
git clone https://github.com/Trevorcohen16/sms-management-system.git cd sms-management-system
2. Install dependencies:
pip install -r requirements.txt
- Includes: `flask==3.0.3`, `pyserial==3.5`, `requests==2.31.0`

3. Setup modem (optional):
- Connect via USB and install drivers.
- Identify port (e.g., `COM3` or `/dev/ttyUSB0`).

4. Run the app:
- Access at `http://localhost:8050`

## 🚀 Usage

1. Launch: Open `http://localhost:8050` in your browser.
2. Configure: Enter modem port (e.g., `COM3`) and baud rate (e.g., `9600`).
3. Start: Click "Start" to begin processing... *Pulsing*: `. . .`
4. Monitor: Watch logs and graphs update live.
5. Stop: Click "Stop" to halt.

## 🎨 Customization

- 🔧 Adjust theme colors in `static/style.css` (e.g., `#00D4FF`).
- 🌟 Modify the modem logo SVG in `index.html`.
- ⚙️ Update port defaults in `templates/index.html`.

## ⚙ Troubleshooting

- 🔴 **Modem not connecting?** Check port with `python -m serial.tools.list_ports`.
- 📵 **No SMS?** Verify SIM service and test `AT+CMGL` manually.
- 📉 **Graph issues?** Ensure `chart.js` is loaded; check console (F12).

## 🤝 Contributing

1. Fork the repo.
2. Create a branch: `git checkout -b feature/cool-feature`
3. Commit changes: `git commit -m 'Add cool feature'`
4. Push: `git push origin feature/cool-feature`
5. Open a PR!

## 📜 License

Licensed under the [MIT License](LICENSE). Use, modify, and share freely! 🚀

---




