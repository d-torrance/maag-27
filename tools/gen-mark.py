#!/usr/bin/env python3
"""Generate the MAAG mark: the tropical curve dual to a unimodular
triangulation of the degree-d triangle.

This is the motif from the 2018 MAAG logo, redrawn as vector art. The output
is the body of _includes/mark.svg -- regenerate it with:

    python3 tools/gen-mark.py 5 1.6 0.055 0.11 0.12

  args: d  ray-length  grid-stroke  curve-stroke  padding

Grey polygons are the triangulation of the Newton polygon; the heavy path is
the dual curve, with unbounded rays in the three primitive directions. Every
vertex is trivalent and balanced, as a tropical curve must be.

The favicon is hand-written (assets/img/favicon.svg) rather than generated --
it is a single vertex, which stays legible at 16px where the full curve does
not.
"""

import math

SQ3 = math.sqrt(3)

def pt(i, j):
    """Lattice point (i,j) drawn in equilateral coordinates."""
    return (i + j * 0.5, j * SQ3 / 2)

def build(d):
    ups   = [(i, j) for j in range(d)   for i in range(d - j)]        # {(i,j),(i+1,j),(i,j+1)}
    downs = [(i, j) for j in range(d-1) for i in range(d - 1 - j)]    # {(i+1,j),(i,j+1),(i+1,j+1)}

    def up_v(i, j):   return [pt(i, j), pt(i+1, j), pt(i, j+1)]
    def down_v(i, j): return [pt(i+1, j), pt(i, j+1), pt(i+1, j+1)]
    def cen(vs):      return (sum(x for x, _ in vs)/3, sum(y for _, y in vs)/3)

    upc   = {(i, j): cen(up_v(i, j))   for (i, j) in ups}
    downc = {(i, j): cen(down_v(i, j)) for (i, j) in downs}

    # Dual edges: every down-triangle borders exactly three up-triangles.
    edges = []
    for (i, j) in downs:
        for nb in ((i, j), (i, j+1), (i+1, j)):
            if nb in upc:
                edges.append((downc[(i, j)], upc[nb]))

    # Unbounded rays: one per boundary edge of the big triangle, drawn from the
    # adjacent up-triangle's centroid through that edge's midpoint.
    def mid(a, b): return ((a[0]+b[0])/2, (a[1]+b[1])/2)
    rays = []
    for i in range(d):                      # bottom edge, j = 0
        rays.append((upc[(i, 0)], mid(pt(i, 0), pt(i+1, 0))))
    for j in range(d):                      # left edge, i = 0
        rays.append((upc[(0, j)], mid(pt(0, j), pt(0, j+1))))
    for i in range(d):                      # hypotenuse, i + j = d
        j = d - 1 - i
        rays.append((upc[(i, j)], mid(pt(i+1, j), pt(i, j+1))))
    return ups, downs, up_v, down_v, edges, rays

def svg(d, extend, stroke_grid, stroke_curve, pad):
    ups, downs, up_v, down_v, edges, rays = build(d)

    # Extend each ray well past the polygon so it reads as unbounded.
    long_rays = []
    for c, m in rays:
        dx, dy = m[0]-c[0], m[1]-c[1]
        n = math.hypot(dx, dy)
        long_rays.append((c, (c[0] + dx/n*extend, c[1] + dy/n*extend)))

    xs = [p[0] for seg in long_rays for p in seg]
    ys = [p[1] for seg in long_rays for p in seg]
    x0, x1, y0, y1 = min(xs)-pad, max(xs)+pad, min(ys)-pad, max(ys)+pad
    w, h = x1-x0, y1-y0

    def P(p): return f"{p[0]-x0:.3f},{(y1-p[1]):.3f}"   # flip y for SVG

    out = []
    out.append('<g class="mark__grid" fill="none" stroke="currentColor" '
               f'stroke-width="{stroke_grid}" stroke-linejoin="round" opacity="0.45">')
    for (i, j) in ups:
        out.append('<polygon points="' + " ".join(P(v) for v in up_v(i, j)) + '"/>')
    for (i, j) in downs:
        out.append('<polygon points="' + " ".join(P(v) for v in down_v(i, j)) + '"/>')
    out.append('</g>')

    out.append('<g class="mark__curve" fill="none" stroke="currentColor" '
               f'stroke-width="{stroke_curve}" stroke-linecap="round" stroke-linejoin="round">')
    for a, b in edges + long_rays:
        out.append(f'<line x1="{P(a).split(",")[0]}" y1="{P(a).split(",")[1]}" '
                   f'x2="{P(b).split(",")[0]}" y2="{P(b).split(",")[1]}"/>')
    out.append('</g>')
    return w, h, "\n  ".join(out)

if __name__ == "__main__":
    import sys
    d = int(sys.argv[1]); extend = float(sys.argv[2])
    sg = sys.argv[3]; sc = sys.argv[4]; pad = float(sys.argv[5])
    w, h, body = svg(d, extend, sg, sc, pad)
    print(f'VIEWBOX 0 0 {w:.3f} {h:.3f}')
    print(body)
