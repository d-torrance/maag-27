---
layout: page
title: Past Meetings
subtitle: "Previous Meetings on Applied Algebraic Geometry."
---

MAAG is a regional gathering that attracts participants primarily from the
Southeastern United States, and has been hosted by a rotating set of
institutions in the region.

<div class="table-scroll" markdown="0">
<table>
  <thead>
    <tr>
      <th scope="col">Year</th>
      <th scope="col">Host</th>
      <th scope="col">Location</th>
    </tr>
  </thead>
  <tbody>
    {% for m in site.data.past_meetings %}
    <tr>
      <th scope="row">
        {%- if m.url and m.url != "" -%}
          <a href="{{ m.url }}">{{ m.year }}</a>
          {%- if m.archived %} <span class="meeting-archived">(archived)</span>{% endif -%}
        {%- else -%}
          {{ m.year }}
        {%- endif -%}
      </th>
      <td>{{ m.host }}</td>
      <td>{{ m.location }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>
</div>
