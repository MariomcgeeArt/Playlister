{% extends 'base.html' %}

{% block content %}
<a href='/'>Back to Home</a>

<h1>{{ playlist.title }}</h1>
<h2>{{ playlist.description }}</h2>

{% for video in playlist.videos %}
    <iframe width='420' height='315' src='{{ video }}'></iframe>
{% endfor %}

<p><a href='/playlists/{{ playlist._id }}/edit'>Edit</a></p>

<!-- Delete button -->
<p>
    <form method='POST' action='/playlists/{{ playlist._id }}/delete'>
    <button type='submit'>Delete</button>
    </form>
</p>

{% endblock %}