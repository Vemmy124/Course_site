""" main file of handling the site """
import flask
import get_course
import views
from __init__ import app


@app.route('/', methods=['GET', 'POST'])
def index():
    """ represents the form for getting courses """
    form = views.CourseForm()
    if form.validate_on_submit():
        try:
            tmpresult = get_course.get_result(form.charcode.data,
                                              form.day.data,
                                              form.month.data,
                                              form.year.data)
            result = '{1} {2} ~ {0} RUB'.format(*tmpresult)
        except ValueError:
            result = 'No data found'
    else:
        result = 'Not submitted'
    return flask.render_template('index.html', form=form, result=result)


@app.route('/mycss.css', methods=['GET'])
def get_css():
    """ css getter """
    return flask.render_template('mycss.css')


if __name__ == '__main__':
    app.run()
