import sys
import graphviz


# ----
# read
# ----

def read(string):
    """
    get a device and the devices it outputs to
    """
    device, outputs = (parts := string.split(':'))[0], parts[1].split()
    return device, outputs

if __name__ == "__main__":
    flows = dict(map(read, sys.stdin))
    dot = graphviz.Digraph()
    for key in flows:
        color = 'orange' if key == 'fft' or key == 'dac' else 'white'
        dot.node(key, fillcolor=color, style='filled')

    for key, val in flows.items():
        for out in val:
            dot.edge(key, out)

    print(dot.source)
    dot.render(view=True)
