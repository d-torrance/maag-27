---
layout: page
title: Code of Conduct
subtitle: "MAAG 2027 is committed to a welcoming, harassment-free meeting for everyone."
---

## Our expectations

MAAG 2027 is a professional scientific meeting. We expect all participants —
speakers, poster presenters, organizers, and attendees — to treat one another
with respect, in the lecture rooms, at meals and receptions, and in any
meeting-related online space.

**Harassment and discrimination will not be tolerated.** This includes, but is
not limited to:

- Offensive or unwelcome comments related to sex, gender, gender identity or
  expression, sexual orientation, disability, physical appearance, race,
  ethnicity, national origin, age, religion, or veteran status
- Unwelcome sexual attention, advances, or physical contact
- Deliberate intimidation, stalking, or following
- Sustained disruption of talks or other events
- Photographing or recording a participant against their wishes

Participants asked to stop any harassing behavior are expected to comply
immediately. Organizers may take any action they deem appropriate, including
warning the individual or expelling them from the meeting without refund of
travel support.

## Reporting

If you experience or witness harassment, or have any other concern, please
contact an organizer. You can speak to any of us in person during the meeting,
or write to
[{{ site.event.contact_email }}](mailto:{{ site.event.contact_email }}).

The organizing committee is:

{% assign organizers = site.data.organizers | sort: "last_name" %}{% for o in organizers %}- {% if o.website and o.website != "" %}[{{ o.name }}]({{ o.website }}){% else %}{{ o.name }}{% endif %}
{% endfor %}

Reports will be handled discreetly. We will listen, take your concern
seriously, and discuss what you would like to happen next before taking action,
except where we are legally obligated to report.

### Georgia Tech reporting channels

Because MAAG 2027 is hosted on the Georgia Tech campus, incidents may also be
reported directly to the Institute:

- [Georgia Tech Title IX reporting](https://titleix.gatech.edu/) — for sexual
  harassment, sexual misconduct, and sex or gender discrimination
- [Georgia Tech EthicsPoint hotline](https://ethics.gatech.edu/) — anonymous
  reporting of ethics and compliance concerns
- **Georgia Tech Police Department** — 404-894-2500, or 911 in an emergency

Note that Georgia Tech employees who are Responsible Employees under Title IX
are required to report disclosures of sexual misconduct to the Institute.

## NSF policy

MAAG 2027 is funded by the National Science Foundation. NSF requires that
organizations receiving conference awards have a policy addressing sexual
harassment, other forms of harassment, and sexual assault, and that the policy
be disseminated to conference participants. This page is that policy for MAAG
2027.

NSF's own policy is available at
[nsf.gov/harassment](https://www.nsf.gov/harassment). Harassment involving
NSF-funded activity may be reported to NSF's Office of Equity and Civil Rights.

## Attribution

This code of conduct draws on the practices of previous MAAG meetings and on
the [AMS Policy on a Welcoming Environment](https://www.ams.org/about-us/governance/policy-statements/anti-harassment-policy).
