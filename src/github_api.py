
from datetime import datetime
from github import Github, GithubException
import json
import logging



logger = logging.getLogger(__name__)


def get_starred_repos():
    user = 'andyr'
    starred = Github().get_user(user).get_starred()

    # format response
    return [{
        'name': repo.name,
        'description':repo.description,
        'url':repo.git_url
    } for repo in starred]

