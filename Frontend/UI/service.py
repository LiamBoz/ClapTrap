from bottle import route, run, template

timeline_tmpl = """
<h2>Clap back now {{user}}!!!</h2>

<p>Make a Post</p>

<form action="http://localhost:7591/" method="post">
  <p><textarea name="clap">Enter post test here</textarea></p>
  <input type="submit" value="Clap Back!" />
</form>

<hr />

<div>
Date: <b>DATE</b>
<p>Latest post here</p>
</div>
<div>
Date: <b>DATE</b>
<p>Previous post here</p>
</div>
<div>
Date: <b>DATE</b>
<p>Previous Previous post here</p>
</div>
"""

# @post("???/???/???")

@route('/<user>/timeline')
def timeline(user):
    return template(timeline_tmpl, user=user)

run(host='localhost', port=7581)


# @route('/<user>/account')
# @route('/<user>/profile')
