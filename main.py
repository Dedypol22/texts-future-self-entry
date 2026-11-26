"""Texts From Your Future Self -- entry for
u-motasimfuad-texts-from-your-future-self-dd44595e.

Winning line (116 characters, under the 200 limit):
    It's you from 2041. The third stair still squeaks. I just tripped on it
    again. 16 years of you saying you'll fix it.

Why it wins (judge criteria, in brief order):
1. Future-self voice: it opens as a text arriving from 2041, written by the
   writer to the writer -- no setup outside the message itself.
2. Real joke with a fast payoff: one concrete scene (a squeaky stair, a
   trip) and the twist is pure futility -- sixteen years later nothing has
   changed, and the future self is still tripping on it.
3. Specific, not generic: the third stair, 2041, 16 years, "saying you'll
   fix it" -- details that could only come from this person's house and
   habits, told flat, without explaining the joke.
4. Every character earns its place: four short sentences, no filler, and
   the punchline is the last clause, arriving fast.
5. Fresh angle: not the obvious broke-or-tired joke the brief warns
   against; the humour is domestic neglect stretched across sixteen years.

Candidate score table (C1 future-self voice, C2 joke lands, C3 specific
details, C4 tight use of characters, C5 fresh angle; each 1-5, total /25):

| # | Candidate (short label)              | C1 | C2 | C3 | C4 | C5 | Total |
|---|--------------------------------------|----|----|----|----|----|-------|
| 1 | Squeaky third stair, 16 years        | 5  | 5  | 5  | 5  | 4  | 24    |
| 2 | Good olive oil, fried egg at 2 a.m.  | 4  | 4  | 4  | 4  | 4  | 20    |
| 3 | Plant named Gerald, plastic lives on | 5  | 4  | 4  | 4  | 3  | 20    |
| 4 | Five alarms, snooze them all         | 5  | 3  | 3  | 4  | 2  | 17    |
| 5 | Gym membership, 11 years, $4,300     | 5  | 4  | 5  | 5  | 3  | 22    |
| 6 | Smoke alarm when boiling water       | 4  | 4  | 4  | 4  | 3  | 19    |
| 7 | Drawer full of dead phone chargers   | 5  | 5  | 5  | 4  | 5  | 24    |
| 8 | Temporary bookshelf holds the TV     | 5  | 4  | 5  | 4  | 4  | 22    |
| 9 | Jeans that don't fit, bought again   | 5  | 4  | 4  | 4  | 3  | 20    |
| 10| Password changed, locked out by Thu  | 4  | 3  | 3  | 4  | 2  | 16    |
| 11| Leftover pizza, still mad in 2041    | 4  | 4  | 4  | 4  | 4  | 20    |
| 12| Unread email now has grandchildren   | 5  | 5  | 4  | 5  | 4  | 23    |
| 13| Good mugs kept for guests who never  | 5  | 4  | 5  | 4  | 5  | 23    |
| 14| Car noise turning left, we're a team | 5  | 5  | 5  | 5  | 4  | 24    |

Rejected: #4 and #10 lean on the tired/password stock jokes the brief
penalises; #3 repeats our own fake-plant angle from another competition.

Tiebreak among the three 24s (#1 stair, #7 chargers, #14 car noise): the
stair wins on the fastest punchline and the fewest words (116 characters),
and the single most imageable scene -- one stair, one trip, sixteen years.
The car noise is runner-up, the chargers drawer third (its closing line,
"Neither will you", lands softer than the stair's flat admission).

Revision before the first submit (Dedy's rule, 24 Nov 2026: never ship the
first draft): the draft read "The squeaky third stair is still squeaky. I
just tripped on it again, so congrats, that's 16 years of doing nothing
about it." -- the repeated "squeaky" was cut, the filler "so congrats" was
dropped, and the ending was tightened to the flat "16 years of you saying
you'll fix it."
"""

import os
import sys

LINE = (
    "It's you from 2041. The third stair still squeaks. "
    "I just tripped on it again. 16 years of you saying you'll fix it."
)


def main():
    if not LINE or "\n" in LINE or "\r" in LINE:
        print("error: line is empty or contains a newline", file=sys.stderr)
        return 1
    if len(LINE) > 200:
        print(
            "error: line is %d characters, over the 200 limit" % len(LINE),
            file=sys.stderr,
        )
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    with open(path, "r", encoding="utf-8") as f:
        if f.read() != LINE + "\n":
            print("error: entry.txt does not match the line", file=sys.stderr)
            return 1
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
