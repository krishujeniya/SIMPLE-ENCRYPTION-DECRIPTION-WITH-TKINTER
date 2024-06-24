
<a id="readme-top"></a>
![GitHub repo size](https://img.shields.io/github/repo-size/krishujeniya/SIMPLE-ENCRYPTION-DECRIPTION-WITH-TKINTER)
![GitHub contributors](https://img.shields.io/github/contributors/krishujeniya/SIMPLE-ENCRYPTION-DECRIPTION-WITH-TKINTER)
![GitHub stars](https://img.shields.io/github/stars/krishujeniya/SIMPLE-ENCRYPTION-DECRIPTION-WITH-TKINTER?style=social)
![GitHub forks](https://img.shields.io/github/forks/krishujeniya/SIMPLE-ENCRYPTION-DECRIPTION-WITH-TKINTER?style=social)

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <img src="logo.png" alt="Logo" width="80" height="80">

  <h1 align="center">Simple Encryption Decryption with Tkinter</h1>
</div>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#key-features">Key Features</a></li>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#license">License</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

## About The Project

This project is a graphical user interface (GUI) application developed using Python's Tkinter library. It allows users to perform simple encryption and decryption of text using a basic substitution cipher. The application provides an intuitive interface for inputting text and key, and displays the encrypted or decrypted result.

### Key Features

- **User-Friendly Interface:**
  - The application utilizes Tkinter to create a clean and visually appealing interface.
  - Large, readable fonts and intuitive layout enhance usability.

- **Encryption and Decryption:**
  - Supports simple substitution cipher for both encryption and decryption.
  - Users can input text and a key, and the encrypted or decrypted text is calculated and displayed with a single click.

- **Error Handling:**
  - Built-in error handling ensures that invalid inputs are detected and handled gracefully, preventing application crashes.
  - Displays an "Invalid input" message if non-alphabetic values are entered.

- **Responsive Design:**
  - Grid layout with padding (`padx` and `pady`) ensures that the elements are well-spaced and easy to interact with.

- **Clear Result Display:**
  - Results are displayed prominently in a label below the input fields and calculation button.
  - Ensures users can easily see the encrypted or decrypted text.

## Built With

- [![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
- [![Tkinter](https://img.shields.io/badge/Tkinter-2C2255?style=for-the-badge&logo=python&logoColor=white)](https://docs.python.org/3/library/tkinter.html)
- [![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)

## Getting Started

To get a local copy up and running, follow these steps.

### Prerequisites

- **Python**: Ensure you have the latest version of Python installed. [Python Installation Guide](https://www.python.org/downloads/)
- **Docker**: Ensure you have the latest version of Docker installed. [Docker Installation Guide](https://docs.docker.com/get-docker/)

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/krishujeniya/SIMPLE-ENCRYPTION-DECRIPTION-WITH-TKINTER.git
   cd SIMPLE-ENCRYPTION-DECRIPTION-WITH-TKINTER
   ```
2. Build the Docker image
   ```sh
   docker build -t encryption_decryption .
   ```

3. Step-by-Step Guide to Enable X11 Forwarding in Docker

   **Install XQuartz (macOS) or Xming (Windows)**:
   - **macOS**: Install XQuartz from [XQuartz.org](https://www.xquartz.org/).
   - **Windows**: Install Xming from [Xming.org](https://sourceforge.net/projects/xming/).

   **Allow Connections**:
   - **macOS**: Open XQuartz, go to **Preferences > Security**, and check "Allow connections from network clients".
   - **Windows**: Start Xming with default settings.

   **Run Docker Container with X11 Forwarding**:

   **On Linux**:
   ```sh
   xhost +local:docker
   docker run -it --rm -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix encryption_decryption
   ```

   **On macOS with XQuartz**:
   ```sh
   xhost + 127.0.0.1
   docker run -it --rm -e DISPLAY=host.docker.internal:0 encryption_decryption
   ```

   **On Windows with Xming**:
   ```sh
   docker run -it --rm -e DISPLAY=host.docker.internal:0 encryption_decryption
   ```

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

## Acknowledgments

* [Python](https://www.python.org/)
* [Tkinter](https://docs.python.org/3/library/tkinter.html)
* [Docker](https://www.docker.com/)
* [Open Source Community](https://opensource.org/)
* [Contributors](https://github.com/krishujeniya/SIMPLE-ENCRYPTION-DECRIPTION-WITH-TKINTER/graphs/contributors)
