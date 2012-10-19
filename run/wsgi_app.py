
import logging
import os
import sys
import web


project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
src = os.path.join(project_root, 'src')
templates = os.path.join(project_root, 'templates')
static = os.path.join(project_root, 'static')

# do this first on application start
def set_path():
    if not src in sys.path:
        sys.path.insert(0, src)



# == Response Rendering ==
def render(template, **kwargs):
    """Render a template as html (or change the request header to something else)
    @see: http://docs.makotemplates.org/en/latest/usage.html#using-templatelookup
    @param template: C{str} path to template, relative to the template root
    """
    web.header('Content-Type', web.ctx.environ.get('Content-Type') or 'text/html')

    template = os.path.split(template)
    template_lookup = TemplateLookup(directories=[template_root, os.path.join(template_root, template[0])])
    return template_lookup.get_template(template[1]).render(**kwargs)


# == Controllers ==
class IndexController(object):

    def GET(self):
        # render a template object
        return 'hi'



# == web.py Session Pre/Post Actions ==
class DBSession(object):

    @classmethod
    def open(self):
        return

    @classmethod
    def close(self):
        return



# web.py Application Init
# @todo: run this on GAE
# @see: http://stackoverflow.com/questions/3665292/web-py-on-google-app-engine
def app():
    """@see http://webpy.org/cookbook/url_handling"""
    urls = (
        '/?', IndexController, # main page
    )

    github_viewer = web.application(urls, globals())
    github_viewer.add_processor(web.loadhook(DBSession.open))
    github_viewer.add_processor(web.unloadhook(DBSession.close))
    return github_viewer


if __name__ == '__main__':
    set_path()
    app().run()

