#!/usr/bin/env python3
"""One-line office joke entry for make.fun's "Make the AI Judge Laugh:
Office Jokes" bounty.

Writes a single one-line joke about office life to /output/entry.txt
(or to the path in ENTRY_OUTPUT when set, for local testing). Pure
standard library only.

The joke was chosen after brainstorming several candidates against the
judge's five criteria (real one-line office joke first, then a real
turn/surprise at the end, recognition that makes the laugh come with a
wince, tight wording, and freshness against the obvious Monday-morning
or photocopier lines):

- Performance review: "My performance review said I exceed expectations
  in meetings but need improvement at actual work, so I booked more
  meetings." THE WINNER. A genuine joke, not an observation: the setup
  is a recognisable review verdict, and the punchline turns it inside
  out -- instead of fixing the weakness, the speaker doubles down on
  the thing they are already good at. Every tired office worker knows
  both the review ritual and the meeting trap, and the line is tight
  (124 characters) with no wasted word.
- Open-plan office: "Our open-plan office really encourages
  collaboration -- I now know everything about Dave's divorce and
  nothing about my job." Funny and true, but the punchline is a
  one-note overshare gag and "Dave" carries the joke rather than the
  office truth; weaker turn than the winner.
- Out-of-office loop: "My out-of-office reply says I'm on holiday, but
  my boss replied to it asking if I could just quickly check one
  thing." Strong recognition, but the ending is predictable -- the
  reader sees the boss's reply coming from the first clause, so the
  surprise lands soft.
- IT ticket: "I filed an IT ticket about my slow laptop; IT closed it
  as resolved, and now my laptop is still slow but so is my faith in
  humanity." The "faith in humanity" closer is a generic internet
  punchline, not an office-specific turn, and the line runs long.

Set aside without drafting: reply-all chains, the office plant,
standups, printers, "per my last email", focus-time meetings, calendar
double-booking and "we're a family here" -- all flooding the live feed
and all failing the freshness criterion before the first word.
"""

import os
from pathlib import Path

ENTRY = (
    "My performance review said I exceed expectations in meetings but "
    "need improvement at actual work, so I booked more meetings."
)


def validate(entry: str) -> None:
    """Raise ValueError unless entry is 1-199 non-blank characters."""
    if not (1 <= len(entry) <= 199) or not entry.strip():
        raise ValueError("entry must be 1-199 non-blank characters")


def main() -> None:
    entry = ENTRY.rstrip("\n")
    validate(entry)
    output_path = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(entry, encoding="utf-8")


if __name__ == "__main__":
    main()
