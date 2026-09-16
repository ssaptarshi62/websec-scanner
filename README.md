# 🛡️ WebSec-Scanner

> A lightweight, modular web security scanner designed to analyze web applications for common vulnerabilities, misconfigurations, and security header flaws.

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Maintenance](https://img.shields.io/badge/Maintained%3D-yes-green.svg)](https://github.com/ssaptarshi62/websec-scanner/graphs/commit-activity)

---

## 📋 Overview

**WebSec-Scanner** is a Python-based utility crafted for web application security auditing, reconnaissance, and vulnerability identification. It scans target URLs for security-sensitive headers, exposed endpoints, form security flaws, and common client-side weaknesses.

---

## ⚙️ Key Features

- **Header Security Analysis:** Validates the presence and posture of defensive headers (`Content-Security-Policy`, `X-Frame-Options`, `Strict-Transport-Security`, `X-Content-Type-Options`, etc.).
- **Endpoint & Form Auditing:** Discovers input entry points and checks for missing security tokens or insecure transmission attributes.
- **Reconnaissance & Fingerprinting:** Identifies server signatures and exposed framework metadata.
- **Structured Reporting:** Exports findings cleanly to console output and structured report files (JSON/text).

---

## 📁 Repository Layout

```text
websec-scanner/
├── core/               # Core audit and scanning logic
├── payloads/           # Payloads and test dictionaries
├── reports/            # Scan output directory
├── scanner.py          # CLI entry point
├── requirements.txt    # Project dependencies
└── README.md           # Documentation
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- `git`
- `pip`

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ssaptarshi62/websec-scanner.git
   cd websec-scanner
   ```

2. **Set up a virtual environment (recommended):**
   ```bash
   python -m venv venv
   # On Linux/macOS:
   source venv/bin/activate
   # On Windows:
   venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 📖 Usage

Run an assessment against a target URL:

```bash
python scanner.py -u https://example.com
```

### CLI Arguments

| Flag | Argument | Description | Default |
| :--- | :--- | :--- | :--- |
| `-u`, `--url` | `<URL>` | Target URL to scan (*required*) | — |
| `-t`, `--threads` | `<INT>` | Number of concurrent request threads | `5` |
| `-o`, `--output` | `<FILE>` | Output file path for scan results | `None` |
| `-v`, `--verbose` | | Enable detailed output logging | `False` |
| `-h`, `--help` | | Show help options and exit | — |

*Example:*
```bash
python scanner.py -u https://target.local -t 8 -o reports/scan_target.json -v
```

---

## ⚠️ Legal Disclaimer

> **Notice:** This software is designed strictly for authorized security assessments, defensive hardening, and educational purposes. 

Unauthorized access, probing, or scanning of computer networks or targets without explicit, documented authorization is illegal. The author (`ssaptarshi62`) assumes no liability for any unauthorized usage, damages, or unintended consequences resulting from the use of this tool.

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/NewFeature`)
3. Commit your changes (`git commit -m 'Add NewFeature'`)
4. Push to the branch (`git push origin feature/NewFeature`)
5. Open a Pull Request

---

## 📄 License

Distributed under the [MIT License](LICENSE).
