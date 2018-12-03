import flask

from repocribro.extending import Extension
from repocribro.extending.helpers import ViewTab, Badge


from repocribro_file.models import FileDescriptor


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
    def provide_blueprints():
        from .controllers import all_blueprints
        return all_blueprints

    @staticmethod
    def provide_models():
        from repocribro_file.models import all_models
        return all_models

    @staticmethod
    def provide_template_loader():
        from jinja2 import PackageLoader
        return PackageLoader('repocribro_file', 'templates')

    # TODO: push webhook

    def view_core_repo_detail_tabs(self, repo, tabs_dict):
        tabs_dict['files'] = ViewTab(
            'files', 'Files', 10,
            flask.render_template('core/repo/files_tab.html', repo=repo),
            octicon='file'
        )

    def view_admin_index_tabs(self, tabs_dict):
        """Prepare tabs for index view of admin controller
        :param tabs_dict: Target dictionary for tabs
        :type tabs_dict: dict of str: ``repocribro.extending.helpers.ViewTab``
        """
        fds = self.db.session.query(FileDescriptor).all()

        tabs_dict['files'] = ViewTab(
            'files', 'Files', 0,
            self.app.jinja_env.get_template('admin/tabs/files.html').render(
                filedescriptors=fds
            ),
            octicon='file',
            badge=Badge(len(fds))
        )

    # TODO: search by content of file


def make_extension(*args, **kwargs):
    return FileExtension(*args, **kwargs)
