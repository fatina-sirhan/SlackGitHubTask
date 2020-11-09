from github import Github


# using an access token
g = Github("d8213a5457fffb9ea3bae5798c63eb8b5bb59732")

repos= g.get_user().get_repos()


# Then play with your Github objects:
for repo in repos:
    print(repo.name)