# 🌐 URL Shortener Project

Welcome to the **URL Shortener** project! This Python script leverages the Cutt.ly API to convert long URLs into short, shareable links. The tool is simple, efficient, and perfect for anyone looking to manage or share links in a more concise format.

## 📋 Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Requirements](#requirements)
- [How to Use](#how-to-use)
- [API Status Codes](#api-status-codes)
- [Contributing](#contributing)

## ✨ Features

- Shorten any valid URL with a single click.
- Handles various error cases (e.g., invalid URLs, blocked domains, API key issues).
- Provides informative feedback for each request based on the Cutt.ly API status codes.
- Easy to set up and use with minimal dependencies.

## 📁 Project Structure

```
link_shortener/
├── link_shortener.py    # Main script to shorten URLs
├── README.md            # Project documentation
└── requirements.txt     # List of dependencies
```

## 🚀 Getting Started

Follow these instructions to set up and run the project on your local machine.

### Prerequisites

Ensure you have **Python 3.7+** installed on your system. You can download Python from [here](https://www.python.org/downloads/).

### Clone the Repository

```bash
git clone https://github.com/your-username/link_shortener.git
cd link_shortener
```

### Install Dependencies

Install the required packages using:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file includes:
```
requests
```

## 🛠️ How to Use

1. Run the `link_shortener.py` script:

    ```bash
    python link_shortener.py
    ```

2. Enter the URL you want to shorten when prompted:

    ```
    Enter a link to shorten: https://example.com
    ```

3. The script will interact with the Cutt.ly API and display the shortened link or an appropriate error message.

### Example Output

```
Enter a link to shorten: https://example.com
Success: Your shortened link is: https://cutt.ly/abcd123
```

### Handling Errors

The script gracefully handles various issues, providing meaningful messages such as:

- **Invalid URL**
- **API key issues**
- **Blocked domain warnings**
- **Monthly limit reached**

## 🛑 API Status Codes

Here are the status codes returned by the Cutt.ly API and their meanings:

| Status Code | Description                                                                 |
|-------------|-----------------------------------------------------------------------------|
| 1           | The link has already been shortened using this service                      |
| 2           | The entered text is not a valid URL                                         |
| 3           | The preferred link name is already taken                                    |
| 4           | Invalid API key                                                             |
| 5           | The link contains invalid characters or failed validation                   |
| 6           | The link is from a blocked domain                                           |
| 7           | OK - the link has been successfully shortened                               |
| 8           | Monthly link limit reached. Upgrade your plan to shorten more links         |

## 🤝 Contributing

We welcome contributions to improve this project! Here's how you can help:

1. **Fork the repository**
2. **Create a new branch** for your feature or bug fix:
    ```bash
    git checkout -b feature-branch
    ```
3. **Commit your changes**:
    ```bash
    git commit -m "Add your message"
    ```
4. **Push to your branch**:
    ```bash
    git push origin feature-branch
    ```
5. **Open a Pull Request** on GitHub.

