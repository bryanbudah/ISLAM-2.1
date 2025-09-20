s# IlmHub

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/)

**IlmHub** is an Islamic educational platform providing online courses, articles, and events to help learners deepen their knowledge of Islam. Designed to be responsive and engaging, IlmHub offers curated educational content for beginners and advanced learners alike.

---

## 🚀 Features

* **Home Page**

  * Hero section introducing the platform
  * Featured learning paths (courses)
  * Knowledge base with insightful articles
  * Upcoming events

* **Courses**

  * Quranic Arabic, Fiqh of Worship, Seerah of the Prophet
  * Easy navigation to course details

* **Articles**

  * Educational content on Tawheed, Salah, and more
  * Curated from trusted Islamic sources

* **Events**

  * Webinars, workshops, and study sessions
  * Details include date, time, and description

* **Responsive Design**

  * Mobile-friendly interface
  * Built with Tailwind CSS

* **User Authentication**

  * Admin access for managing content
  * Conditional display of admin features

* **Footer**

  * Quick links to courses, company pages, and social media

---

## 💻 Tech Stack

* **Backend:** Django 5.2
* **Frontend:** Tailwind CSS, HTML5, CSS3
* **Database:** SQLite (default, can use PostgreSQL/MySQL)
* **Deployment:** Compatible with Heroku, PythonAnywhere, AWS, etc.

---

## 🛠️ Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/ilmhub.git
   cd ilmhub
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**

   ```bash
   python manage.py runserver
   ```

7. Open your browser and visit `http://127.0.0.1:8000/`.

---

## 💾 Directory Structure

```
ilmhub/
├── core/                  # Django app with views, models, templates
│   ├── templates/core/
│   │   ├── home.html
│   │   ├── article_detail.html
│   │   └── course_detail.html
│   ├── views.py
│   ├── models.py
│   └── urls.py
├── static/                # CSS, JS, images
├── config/                # Django project settings
│   ├── settings.py
│   └── urls.py
├── manage.py
└── README.md
```

---

## 🖼 Screenshots

*Home Page*
![Home Page](screenshots/home.png)

*Course Page*
![Course Detail](screenshots/course_detail.png)

*Article Page*
![Article Detail](screenshots/article_detail.png)

---

## ⚙️ Usage

* Browse featured courses and upcoming events on the **Home Page**.
* Access the **Articles** section for Islamic educational content.
* Admin users can log in to manage courses, articles, and events.
* Use the footer links to quickly navigate courses, company info, or social media.

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch

   ```bash
   git checkout -b feature/YourFeature
   ```
3. Commit your changes

   ```bash
   git commit -m "Add your feature"
   ```
4. Push to the branch

   ```bash
   git push origin feature/YourFeature
   ```
5. Open a Pull Request

---

## 📧 Contact

* **Website:** [IlmHub](http://yourwebsite.com)
* **Email:** [contact@ilmhub.com](mailto:illhubacademy@gmail.com)
* **Social Media:**

  * Facebook: [link](https://www.facebook.com/r.php?entry_point=login)
  * Twitter: [link](https://x.com/home)
  * Instagram: [link](https://www.instagram.com/)

---

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

illhubacademy@gmail.com
password:Islam@2025

admin
password:Islam@2025
