from interface import TerminalInterface
from confidentials import ConfidentialData


if __name__ == "__main__":
    terminal = TerminalInterface()
    terminal.run()
    u = "test"
    p = "pass"
    first = ConfidentialData(u,p)
