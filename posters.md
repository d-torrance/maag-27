---
layout: page
title: Poster Session
subtitle: "Saturday afternoon, preceded by a poster blitz."
math: true
---

MAAG 2027 includes a **poster session** on Saturday afternoon, preceded by a
short **poster blitz** in which each presenter gives a one-slide, one-minute
advertisement for their poster.

Graduate students, postdocs, and undergraduates are especially encouraged to
present. A poster is a low-pressure way to get feedback and to meet people
working on related problems.

## Submitting a poster

Indicate your interest in presenting a poster when you
[register]({% if site.registration.open %}{{ site.registration.url }}{% else %}{{ '/funding/' | relative_url }}{% endif %}),
including a tentative title and abstract. There is no separate application.

Posters should be no larger than **48 inches wide by 36 inches tall**
(landscape). Boards and clips are provided.

## Accepted posters

{% assign posters = site.posters | sort: "last_name" %}
{% if posters.size == 0 %}

Accepted posters will be listed here once the registration deadline has passed.

{% else %}
{% for p in posters %}{% include poster-card.html poster=p %}{% endfor %}
{% endif %}
