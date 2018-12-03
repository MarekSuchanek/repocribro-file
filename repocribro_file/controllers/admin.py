import flask

from repocribro.security import permissions

from repocribro_file.models import FileDescriptor


#: Files admin controller blueprint
admin_files = flask.Blueprint('admin-files', __name__, url_prefix='/admin-files')


@admin_files.route('/create', methods=['GET'])
@permissions.roles.admin.require(404)
def create_file():
    ...


@admin_files.route('/create', methods=['POST'])
@permissions.roles.admin.require(404)
def create_file_post():
    ...


@admin_files.route('/<fd_id>/edit', methods=['GET'])
@permissions.roles.admin.require(404)
def edit_file(fd_id):
    db = flask.current_app.container.get('db')
    fd = db.session.query(FileDescriptor).filter_by(id=fd_id).first()
    if fd is None:
        flask.abort(404)
    ...


@admin_files.route('/<fd_id>/edit', methods=['PUT', 'POST'])
@permissions.roles.admin.require(404)
def edit_page_put(fd_id):
    db = flask.current_app.container.get('db')
    fd = db.session.query(FileDescriptor).filter_by(id=fd_id).first()
    if fd is None:
        flask.abort(404)
    ...
    return flask.redirect(
        flask.url_for('admin.index', tab='files')
    )


@admin_files.route('/<fd_id>/delete')
@permissions.roles.admin.require(404)
def delete_page(fd_id):
    db = flask.current_app.container.get('db')
    fd = db.session.query(FileDescriptor).filter_by(id=fd_id).first()
    if fd is None:
        flask.abort(404)

    db.session.delete(fd)
    db.session.commit()
    flask.flash(f'File descriptor {fd.filename} has been deleted', 'success')
    return flask.redirect(
        flask.url_for('admin.index', tab='files')
    )
