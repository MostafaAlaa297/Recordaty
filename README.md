# Recordaty

![Recordaty Logo](path_to_logo_image)

## Introduction

**Recordaty** is a medical records-keeping application designed to streamline the management and accessibility of medical records. This project is part of a portfolio showcasing various web technologies including HTML, CSS, JavaScript, Python Flask, Flask WTForms, MySQL, and SQLAlchemy.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- User registration and authentication
- Profile management
- Secure storage of medical records
- Search functionality to easily find records
- Responsive design

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python Flask, Flask WTForms
- **Database**: MySQL, SQLAlchemy

## Setup and Installation

### Prerequisites

- Python 3.x
- MySQL
- Pip (Python package installer)

### Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/recordaty.git
    cd recordaty
    ```

2. Create a virtual environment:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

4. Configure the database:

    - Ensure MySQL is running and create a database for the project.
    - Update the database configuration in `app.py`:

    ```python
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost/database_name'
    ```

5. Initialize the database:

    ```sh
    flask shell
    >>> from app import db
    >>> db.create_all()
    >>> exit()
    ```

6. Run the application:

    ```sh
    flask run
    ```

## Usage

1. Navigate to `http://127.0.0.1:5000/` in your web browser.
2. Register a new user or log in with existing credentials.
3. Manage your profile and medical records.

## Screenshots

### Home Page
![Home Page](path_to_home_page_image)

### Registration Page
![Registration Page](path_to_registration_page_image)

### Profile Page
![Profile Page](path_to_profile_page_image)

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature-name`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries or feedback, please reach out to:

- **Your Name**
- **Email**: your.email@example.com
- **GitHub**: [yourusername](https://github.com/yourusername)

---

Thank you for visiting Recordaty!
