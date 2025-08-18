# Django-Based-Personal-Portfolio
📄 Description:
A modern, responsive personal portfolio built with Django and custom CSS — featuring a Netflix-inspired dark theme, animated sections, flip cards, certificate modals, GitHub integration, and a floating glassmorphism navbar.

📌 Features (for README or topics):
🎨 Netflix-style UI with glassmorphism effects

💡 Dynamic project and certificate sections using Django templates

🧠 GitHub API integration to fetch public repositories

🔄 Flip cards, scroll animations, and typing effects

🧩 Filterable certificate grid and skill bar animations

🔍 Smooth scroll, animated cursor, and scroll-to-top behavior

🧾 Contact form, volunteer section, and downloadable resume

💻 Fully responsive and mobile-optimized layout

## To run project
1. Copy `env.example` to `.env` and edit the `.env` file with your configuration (e.g., database settings, secret key).
2. Copy `user_setup.yaml.example` to `user_setup.yaml` and edit it with your personal details (e.g., name, GitHub username, social links).
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Apply migrations to set up the database:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Create a superuser for admin access:
   ```bash
   python manage.py createsuperuser
   ```
6. Initialize portfolio configuration (this command loads data from user_setup.yaml into the PortfolioConfig table):
   ```bash
   python manage.py init_portfolio_config
   ```
