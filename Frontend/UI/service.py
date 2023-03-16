from bottle import route, run, template
from requests import get

timeline_tmpl = """
<h2>Clap back now {user}!!!</h2>

<p>Make a Post</p>

<form action="http://localhost:7591/{user}/timeline" method="post">
  <p><textarea name="clap">Enter post test here</textarea></p>
  <input type="submit" value="Clap Back!" />
</form>

<hr />

{claps}
"""

# @post("???/???/???")

@route('/<user>/timeline')
def timeline(user):
    claps = get("http://localhost:7591/{user}/timeline".format(**{"user":user}))
    return template(timeline_tmpl.format(**{"user":user, "claps":claps}), user=user)

run(host='localhost', port=7581)


# @route('/<user>/account')
# @route('/<user>/profile')
