---
layout: page
title: Schedule
subtitle: "All times are Eastern."
---

The schedule below is preliminary and will be updated as speakers are
confirmed. Talk titles link to the [Talks]({{ '/talks/' | relative_url }})
page; workshop sessions link to the
[Macaulay2 mini-workshop]({{ '/workshop/' | relative_url }}) page.

{% for day in site.data.schedule %}{% include schedule-day.html day=day %}{% endfor %}
