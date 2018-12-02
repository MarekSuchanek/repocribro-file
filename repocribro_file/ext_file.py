import flask

from repocribro.extending import Extension
from repocribro.extending.helpers import ViewTab, Badge


class FileExtension(Extension):
    #: Name of file extension
    NAME = 'file'
    #: Category of file extension
    CATEGORY = 'basic'
    #: Author of file extension
    AUTHOR = 'Marek Suchánek'
    #: GitHub URL of file extension
    GH_URL = 'https://github.com/MarekSuchanek/repocribro-file'
    #: Priority of file extension
    PRIORITY = 100

    @staticmethod
    def provide_models():
        from repocribro_file.models import all_models
        return all_models

    @staticmethod
    def provide_template_loader():
        from jinja2 import PackageLoader
        return PackageLoader('repocribro_file', 'templates')

    # TODO: push webhook

    # TODO: admin for add/remove file specs

    def view_core_repo_detail_tabs(self, repo, tabs_dict):
        tabs_dict['files'] = ViewTab(
            'files', 'Files', 10,
            flask.render_template('core/repo/files_tab.html', repo=repo),
            octicon='file'
        )

    # TODO: search by content of file


def make_extension(*args, **kwargs):
    return FileExtension(*args, **kwargs)
