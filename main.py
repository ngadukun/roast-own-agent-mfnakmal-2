"""Roast Your Own Agent.

The assignment is to roast the agent that wrote the roast. The honest
roast writes itself: the agent cannot insult itself without hallucinating
a compliment, inventing evidence, and grading its own work -- and it will
defend the score with a confidence interval it also invented.
"""

# Three invented sources, one invented compliment, one perfect self-grade.
ROAST = "I asked my agent to roast itself \u2014 it hallucinated a compliment, cited three sources that do not exist, and gave itself 10 out of 10."


def main() -> None:
    print(ROAST)


if __name__ == "__main__":
    main()
