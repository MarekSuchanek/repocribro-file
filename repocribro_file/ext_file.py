from repocribro.extending import Extension


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

    # TODO: templates

    # TODO: push webhook

    # TODO: admin for add/remove file specs

    # TODO: tab for repository with files

    # TODO: search by content of file


def make_extension(*args, **kwargs):
    return FileExtension(*args, **kwargs)
