---
layout: page
title: Macaulay2 Mini-Workshop
subtitle: "Hands-on sessions running alongside MAAG 2027."
---

MAAG 2027 includes a **Macaulay2 mini-workshop**: a set of hands-on sessions
introducing [Macaulay2](https://macaulay2.com), the open-source computer
algebra system for research in commutative algebra and algebraic geometry. All
sessions run back to back on Friday afternoon, before the talks begin.

The workshop is open to all registered participants at no additional cost, and
assumes no prior Macaulay2 experience for the introductory session.

## What to bring

The sessions are in a lecture room rather than a computer lab, so **please
bring your own laptop** with
[Macaulay2 installed](https://github.com/Macaulay2/M2/wiki) — there are no
machines provided.

If installing locally is inconvenient, Macaulay2 also runs in a web browser at
[macaulay2.com/TryItOut](https://macaulay2.com/TryItOut/), which needs nothing
but a network connection. A local install is more comfortable for a working
session.

## Sessions

{% assign sessions = site.workshop | sort: "order" %}
{% if sessions.size == 0 %}

Session details will be posted here.

{% else %}
{% for s in sessions %}
<article class="talk" id="{{ s.ref }}">
  <h3 class="talk__name">{{ s.title }}</h3>
  <p class="talk__affiliation">
    {{ s.leader }}{% if s.leader_affiliation and s.leader_affiliation != "" %}, {{ s.leader_affiliation }}{% endif %}
    &middot; {{ s.duration }} &middot; {{ s.level }}
  </p>
  <div class="talk__abstract">{{ s.content | markdownify }}</div>
  {% if s.requirements and s.requirements != "" %}
  <p class="cta-note"><strong>You will need:</strong> {{ s.requirements }}</p>
  {% endif %}
</article>
{% endfor %}
{% endif %}
