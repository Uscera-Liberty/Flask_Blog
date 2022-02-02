from flask import render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort

from app.forms import User_registration_form
from app.repositories import get_all_posts, get_post, add_post, update_post, delete_post, add_user, get_likes

from app import app


@app.route('/')
def draw_main_page():
    posts = get_all_posts()
    return render_template('index.html', posts=posts)

@app.route('/<int:id>/like', methods=('POST',))
def like(id):
    post = get_post(id)
    likes = post['likes'] + 1
    get_likes(id, likes)
    return redirect(url_for('get_blog_post', id=id))


@app.route('/<int:id>')
def get_blog_post(id):
    post = get_post(id)

    if post is None:
        abort(404)

    return render_template('post.html', post=post)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Введите заголовок!')
        else:
            add_post(title, content)
            return redirect(url_for('draw_main_page'))

    return render_template('create.html')

@app.route('/<int:id>/comment', methods=('GET', 'POST'))
def create_comment(id):
    post = get_post(id)

    if request.method == 'POST':
        comment = post['comment']
        create_comment(comment)
        return redirect(url_for('get_blog_post'))

    return render_template('comment.html',post=post)

@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            update_post(title, content, id)
            return redirect(url_for('draw_main_page'))

    return render_template('edit.html', post=post)


@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    post = get_post(id)
    delete_post(id)
    flash('"{}" was successfully deleted!'.format(post['title']))
    return redirect(url_for('draw_main_page'))


@app.route('/register/', methods=['get', 'post'])
def register_user():
    form = User_registration_form()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        password_again = form.passwordRepeatFieled.data

        if password != password_again:
            flash('Enter equal passwords!')
        else:
            print(f'{name} {email}')
            add_user(name, email, password)
            return redirect(url_for('draw_main_page'))

    return render_template('registration.html', form=form)


