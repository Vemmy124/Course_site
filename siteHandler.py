import flask
import getCourse
import views
from __init__ import app

@app.route('/', methods=['GET', 'POST'])
def index():
    form = views.CourseForm()
    if form.validate_on_submit():
        try:
            tmpresult = getCourse.get_result(form.charcode.data, form.day.data, form.month.data, form.year.data)
            result = '1 RUB ~ {} {}'.format(str(tmpresult[0]), str(tmpresult[1]))
        except:
            result = 'No data found'
    else:
        result = 'not submitted'
    return flask.render_template('index.html', form=form, result=result)

if __name__ == '__main__':
    app.run()