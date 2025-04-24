BlogSphere 🚀
BlogSphere is a modern, multi-user blogging platform built with Django and PostgreSQL. It allows users to create, share, and engage with posts, comments, and likes in a vibrant community. Whether you're a blogger or a reader, BlogSphere offers a seamless and interactive experience.
Features ✨

Multi-user Blogging: Every registered user can create, edit, and delete their own posts.
Rich Interactions: Like posts, comment with nested replies, and share content on social media.
Categories and Search: Organize posts by categories and find content easily with a powerful search.
User Profiles: Customize your profile with a bio and avatar.
Admin Dashboard: Manage posts, comments, and users with a robust admin panel.
Responsive Design: Built with Tailwind CSS for a beautiful, mobile-friendly experience.

Tech Stack 🛠️

Backend: Django (Python), PostgreSQL
Frontend: HTML, Tailwind CSS, JavaScript
Other: Django Crispy Forms, Pillow

Installation 📦
Follow these steps to set up BlogSphere locally:

Clone the repository:
git clone https://github.com/YourUsername/BlogSphere.git
cd BlogSphere


Create a virtual environment:
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate


Install dependencies:
pip install -r requirements.txt


Set up PostgreSQL:

Install PostgreSQL and create a database named blog_db.
Update blog/settings.py with your database credentials:DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'blog_db',
        'USER': 'your_postgres_user',
        'PASSWORD': 'your_postgres_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}




Run migrations:
python manage.py makemigrations
python manage.py migrate


Create a superuser:
python manage.py createsuperuser


Run the development server:
python manage.py runserver

Open http://127.0.0.1:8000 in your browser.


Usage 📝

Create a Post: Log in, navigate to "New Post," and publish your content.
Engage: Like and comment on posts to interact with the community.
Admin Panel: Access /admin/ to manage content and users.

Contributing 🤝
We welcome contributions! To contribute:

Fork the repository.
Create a new branch (git checkout -b feature/your-feature).
Commit your changes (git commit -m 'Add your feature').
Push to the branch (git push origin feature/your-feature).
Open a Pull Request.

License 📜
This project is licensed under the MIT License - see the LICENSE file for details.
Contact 📬
Have questions or suggestions? Reach out via email or open an issue on GitHub.

Built with ❤️ by Bunyod  
