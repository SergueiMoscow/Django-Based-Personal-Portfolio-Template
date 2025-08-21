import json
import random
from typing import List

import requests
from pathlib import Path
from django.conf import settings
from portfolio_site import settings as app_settings
from django.shortcuts import render, get_object_or_404
from .forms import ContactForm
from .models import PortfolioConfig, Project, Certificate


# Load static JSON
def load_json(filename):
    json_path = Path(settings.BASE_DIR) / 'portfolio' / 'static' / 'portfolio' / 'data' / filename
    with open(json_path, 'r', encoding='utf-8') as f:
        return json.load(f)

# Fetch GitHub Repositories
def fetch_github_repos(username):
    try:
        url = f"https://api.github.com/users/{username}/repos"
        headers = {
            "Accept": "application/vnd.github+json",
            "User-Agent": "Django-Portfolio"
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            repos = response.json()
            return [
                {
                    "title": repo["name"],
                    "description": repo.get("description", "No description available."),
                    "link": repo["html_url"],
                    "image": f"https://opengraph.githubassets.com/1/{username}/{repo['name']}",
                    "category": "GitHub"
                }
                for repo in repos if not repo.get("fork", False)
            ]
    except Exception as e:
        print(f"[GitHub Fetch Error] {e}")
    return []

def get_featured_projects() -> List[Project]:
    return list(Project.objects.filter(featured=True).order_by('order')[:3])


def get_all_projects() -> List[Project]:
    return list(Project.objects.filter(featured=True).order_by('order'))


# Deduplicate
def get_unique_projects(projects):
    seen = set()
    unique = []
    for p in projects:
        if p["title"] not in seen:
            seen.add(p["title"])
            unique.append(p)
    return unique

def get_all_certificates() -> List[Certificate]:
    return list(Certificate.objects.all().order_by('year'))

# Home Page – show 3 random projects
def index(request):
    github_username = PortfolioConfig.objects.filter(block='social_links', key='portfolio_github_user').first().value
    # Original version (only github)
    # github_projects = fetch_github_repos(github_username)
    # unique_projects = get_unique_projects(github_projects)
    # featured = random.sample(unique_projects, min(3, len(unique_projects)))

    # Changed version (projects from table)
    featured = get_featured_projects()

    return render(request, 'index.html', {
        'projects': featured,
        'certificates': get_all_certificates(), # load_json('certificates.json')[:3],
        'skills': load_json('skills.json'),
        'volunteers': load_json('volunteer.json'),
    })

# Projects Page – all GitHub repos
def projects(request):
    # Version with only github projects
    # github_username = PortfolioConfig.objects.filter(block='social_links', key='portfolio_github_user').first().value
    # github_projects = fetch_github_repos(github_username)
    # all_projects = get_unique_projects(github_projects)

    # Version with projects from table
    all_projects = get_all_projects()
    return render(request, 'projects.html', {
        'projects': all_projects
    })

# Certificates Page
def certificates(request):
    return render(request, 'certificates.html', {
        'certificates': load_json('certificates.json')
    })

# About Page
def about(request):
    return render(request, 'about.html')

# Contact Page
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send_email()
            return render(request, 'contact_success.html')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {
        'form': form
    })


def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'project_detail.html', {
        'project': project
    })


def csrf_failure(request, reason=""):
    ctx = {'message': app_settings.CORS_ALLOWED_ORIGINS}
    return render(request, 'csrf_view.html', ctx)