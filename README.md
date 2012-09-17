github-stargazer
================

Keep track of github starred repos


#### Goals

App/tools for querying github starred repos.  I often find myself interested in
so many github projects, I star ones I want to come back to or have value --
so far purely academic.  I want to be able to have a concise view of all my
starred repos with descriptions.  Possible extensions would be to group by
language or something else (like "web" or "device drivers").

(TODO - still TBD) Components:
- authenticating a github account (oauth)
- fetching remote content (libcurl)
- server process that either polls for OR gets notified about changes
- parser and writer (?)
- topic sets by repo (python, oauth) - similar to tag clouds

