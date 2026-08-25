---
layout: page
title: Funding
subtitle: "MAAG 2027 is supported by the National Science Foundation."
---

{% assign nsf = site.data.support.nsf %}

## NSF support

MAAG 2027 is supported by the National Science Foundation,
{{ nsf.program }}, under award **{{ nsf.award_number }}**.

{{ nsf.disclaimer }}

We are also grateful for support from:

{% for s in site.data.support.other %}
- [{{ s.name }}]({{ s.url }})
{% endfor %}

## Travel support

NSF funding allows us to reimburse travel and lodging expenses for a number of
participants. **Priority is given to graduate students, postdocs, and
early-career researchers** who do not have other sources of travel funding, and
to participants from institutions in the Southeast.

To apply, complete the travel-support section of the registration form by
**{{ site.registration.travel_support_deadline_display }}**. Applications
received after that date will be considered only if funds remain.

<div class="hero__actions">
  {% include register-button.html variant="btn--solid-navy" %}
</div>

### What is reimbursable

- Coach airfare on a U.S. flag carrier, or mileage for driving
- Lodging at the conference rate for the nights of the meeting
- Ground transportation to and from the airport

Reimbursement is made **after** the meeting, against original receipts. Federal
rules require us to collect receipts for lodging and for any single expense over
$25. Alcohol is not reimbursable.

### If you are awarded support

You will hear from the organizers by email with your award amount and
instructions for submitting receipts. Please do not book non-refundable travel
before you receive that notice.

## Questions

Email the organizers at
[{{ site.event.contact_email }}](mailto:{{ site.event.contact_email }}).
