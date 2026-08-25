---
layout: page
title: Talks
subtitle: "Invited talks at MAAG 2027."
math: true
---

{% assign speakers = site.speakers | sort: "last_name" %}
{% assign plenary = speakers | where: "kind", "plenary" %}
{% assign invited = speakers | where: "kind", "invited" %}
{% assign contributed = speakers | where: "kind", "contributed" %}

{% if speakers.size == 0 %}

Speakers for MAAG 2027 have not yet been announced. Check back in fall 2026, or
see the [schedule]({{ '/schedule/' | relative_url }}) for the shape of the
program.

{% else %}

{% if plenary.size > 0 %}
## Plenary talks
{% for sp in plenary %}{% include speaker-card.html speaker=sp %}{% endfor %}
{% endif %}

{% if invited.size > 0 %}
## Invited talks
{% for sp in invited %}{% include speaker-card.html speaker=sp %}{% endfor %}
{% endif %}

{% if contributed.size > 0 %}
## Contributed talks
{% for sp in contributed %}{% include speaker-card.html speaker=sp %}{% endfor %}
{% endif %}

{% endif %}
