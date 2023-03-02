from bottle import route, run, template

timeline_tmpl = """
<h2>Clap back now {{user}}!!!</h2>

<p>Make a Post</p>

<textarea>Enter post test here</textarea>
<form action="???"><submit /></form>

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

@route('/<user>/timeline')
def timeline(user):
    return template(timeline_tmpl, user=user)

run(host='localhost', port=7581)


# @route('/<user>/account')
# @route('/<user>/profile')
