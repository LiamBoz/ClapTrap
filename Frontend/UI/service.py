from bottle import route, run, template
from requests import get

timeline_tmpl = """
<h2>Clap back now {user}!!!</h2>

<p>Make a Post</p>

<form action="http://127.0.0.1:7591/{user}/timeline" method="post">
  <p><textarea name="clap">Enter post test here</textarea></p>
  <input type="submit" value="Clap Back!" />
</form>

<hr />

{claps}
"""

table_tmpl = """

  <table border="5">
    <tr>
        <td>{user}</td>
        <td>❤️:{likes}</td>
        <td>{date}</td>
    </tr>
    <tr>
        <td colspan="3">{text}</td>
    </tr>
  </table>
  """


@route('/<user>/timeline')
def timeline(user):
    response_object = get("http://127.0.0.1:7591/{user}/timeline".format(**{"user":user}))

    print(response_object.text)

    if response_object.status_code == 500:
        claps_as_html = "{user} has no claps yet!!".format(**{"user":user})
    else:
      claps_from_db = response_object.json()

      claps_as_html = ""
      for clap in claps_from_db:
          claps_as_html += table_tmpl.format(
              **{"user": user, "likes": clap[2], "date": clap[1], "text": clap[0]}
            )

    return template(timeline_tmpl.format(**{"user":user, "claps":claps_as_html}), user=user)

run(host='127.0.0.1', port=7581)




# @route('/<user>/account')
# @route('/<user>/profile')
