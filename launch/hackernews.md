# Hacker News "Show HN" Post

> HN will test the claim, not the product. Lead with the craft and the localisation story,
> state the epistemic position plainly in the first paragraph, and be present in the comments.
> Do not get defensive — the most upvoted comment will be the sceptical one.

```
Show HN: Aura144 – an Android app that reads the aura from a full-body photo

I built Aura144. You take a full-body photo the way the in-app guide shows you
(standing, arms open, palms forward, plain light background), and the app renders
the energy field around your body as a colour image, plus a written reading
covering emotional, mental and spiritual layers. Results save to the device and
can be annotated with private notes.

Straight up front: this is an energy-based interpretation, not a measurement. I'm
not claiming it's science, and the app says so on the page and in the terms. What
I built is a well-engineered delivery mechanism for a reading that people were
previously travelling to practitioners and paying for — and it was developed with
Judith Collins, an Australian aura teacher who has worked with the human aura for
decades.

The parts HN might actually find interesting:
- A server-side generation step behind a native app, with photo validation before
  payment so a rejected photo doesn't cost the user a reading.
- 15 locales. Installs grew from a handful/day to ~240/day in six months, and
  roughly half the users are outside my four largest markets — which is what
  forced localisation from "nice to have" to a launch requirement.
- Getting an app through review when the category itself is contentious.

Happy to answer questions about the pipeline, the localisation process, or the
positioning problem of shipping something people either love or consider
pseudoscience. Store listing: [LINK]. Site: https://www.aura144.com/
```

Rules to respect:
- Title starts with "Show HN" exactly.
- Be present in the comments and answer the sceptical questions directly.
- Do not ask for upvotes.
- Do not post repeatedly (HN guideline: don't use HN primarily for promotion).

Prepared answers for the predictable comments:
- *"This is pseudoscience."* — Agreed that it isn't science, and I'm not presenting it as such. The claim is that
  the reading follows a specific tradition, and that tradition is where the value is for the people who use it.
  The app states it's an energy-based interpretation in the terms, the privacy page and the footer.
- *"How does it actually work?"* — A server-side image processing step reads the photo and generates the aura
  image and reading; the app validates the photo first to ensure the subject is fully framed. I'm not going to
  overstate the mechanism.
- *"Isn't this exploitative?"* — The fee is shown before payment, nothing is charged automatically, there is no
  subscription, and the reading is framed as self-reflection rather than diagnosis or advice.
