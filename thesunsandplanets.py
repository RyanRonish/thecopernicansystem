import numpy as np
import math
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def spheres(size, clr, dist=0, frame=None): 
    theta = np.linspace(0, 2*np.pi, 100)
    phi = np.linspace(0, np.pi, 100)
    x0 = dist + size * np.outer(np.cos(theta), np.sin(phi))
    y0 = size * np.outer(np.sin(theta), np.sin(phi))
    z0 = size * np.outer(np.ones(100), np.cos(phi))
    
    trace = go.Surface(x=x0, y=y0, z=z0, colorscale=[[0, clr], [1, clr]], cmin=-1, cmax=1, surfacecolor=z0)
    trace.update(showscale=False)
    
    return trace

def orbits(dist, offset=0, clr='white', wdth=2): 
    xcrd, ycrd, zcrd = [], [], []
    for i in range(0, 361):
        xcrd = xcrd + [(round(np.cos(math.radians(i)), 5)) * dist + offset]
        ycrd = ycrd + [(round(np.sin(math.radians(i)), 5)) * dist]
        zcrd = zcrd + [0]
    
    trace = go.Scatter3d(x=xcrd, y=ycrd, z=zcrd, marker=dict(size=0.1), line=dict(color=clr, width=wdth))
    
    return trace

def annot(xcrd, zcrd, txt, xancr='center'):
    strng = dict(showarrow=False, x=xcrd, y=0, z=zcrd, text=txt, xanchor=xancr, font=dict(color='white', size=12))
    return strng

diameter_km = [200000, 4878, 12104, 12756, 6787, 142796, 120660, 51118, 48600]
diameter = [((i / 12756) * 2) for i in diameter_km]
distance_from_sun = [0, 57.9, 108.2, 149.6, 227.9, 778.6, 1433.5, 2872.5, 4495.1]

# Create spheres for the Sun and planets
trace0 = spheres(diameter[0], '#ffff00', distance_from_sun[0])
trace1 = spheres(diameter[1], '#87877d', distance_from_sun[1])
trace2 = spheres(diameter[2], '#d23100', distance_from_sun[2])
trace3 = spheres(diameter[3], '#325bff', distance_from_sun[3])
trace4 = spheres(diameter[4], '#b20000', distance_from_sun[4])
trace5 = spheres(diameter[5], '#ebebd2', distance_from_sun[5])
trace6 = spheres(diameter[6], '#ebcd82', distance_from_sun[6])
trace7 = spheres(diameter[7], '#37ffda', distance_from_sun[7])
trace8 = spheres(diameter[8], '#2500ab', distance_from_sun[8])

# Set up orbit traces
trace11 = orbits(distance_from_sun[1])
trace12 = orbits(distance_from_sun[2])
trace13 = orbits(distance_from_sun[3])
trace14 = orbits(distance_from_sun[4])
trace15 = orbits(distance_from_sun[5])
trace16 = orbits(distance_from_sun[6])
trace17 = orbits(distance_from_sun[7])
trace18 = orbits(distance_from_sun[8])

# Use the same to draw a few rings for Saturn
trace21 = orbits(23, distance_from_sun[6], '#827962', 3) 
trace22 = orbits(24, distance_from_sun[6], '#827962', 3) 
trace23 = orbits(25, distance_from_sun[6], '#827962', 3)
trace24 = orbits(26, distance_from_sun[6], '#827962', 3) 
trace25 = orbits(27, distance_from_sun[6], '#827962', 3) 
trace26 = orbits(28, distance_from_sun[6], '#827962', 3)

# Set up layout
layout = go.Layout(
    title='Solar System Animation',
    showlegend=False,
    margin=dict(l=0, r=0, t=0, b=0),
    scene=dict(
        xaxis=dict(title='Distance from the Sun', titlefont_color='black', range=[-7000, 7000], backgroundcolor='black', color='black', gridcolor='black'),
        yaxis=dict(title='Distance from the Sun', titlefont_color='black', range=[-7000, 7000], backgroundcolor='black', color='black', gridcolor='black'),
        zaxis=dict(title='', range=[-7000, 7000], backgroundcolor='black', color='white', gridcolor='black'),
        annotations=[
            annot(distance_from_sun[0], 40, 'Sun', xancr='left'),
            annot(distance_from_sun[1], 5, 'Mercury'),
            annot(distance_from_sun[2], 9, 'Venus'),
            annot(distance_from_sun[3], 9, 'Earth'),
            annot(distance_from_sun[4], 7, 'Mars'),
            annot(distance_from_sun[5], 30, 'Jupiter'),
            annot(distance_from_sun[6], 28, 'Saturn'),
            annot(distance_from_sun[7], 20, 'Uranus'),
            annot(distance_from_sun[8], 20, 'Neptune'),
        ]
    ),
)

# Create frames for animation
frames = [go.Frame(data=[trace0, trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8,
                         trace11, trace12, trace13, trace14, trace15, trace16, trace17, trace18,
                         trace21, trace22, trace23, trace24, trace25, trace26])]
for i in range(1, 361, 10):
    frame_data = [
        spheres(diameter[0], '#ffff00', distance_from_sun[0]),
        spheres(diameter[1], '#87877d', distance_from_sun[1] * np.cos(np.radians(i * 10))),
        spheres(diameter[2], '#d23100', distance_from_sun[2] * np.cos(np.radians(i * 8))),
        spheres(diameter[3], '#325bff', distance_from_sun[3] * np.cos(np.radians(i * 6))),
        spheres(diameter[4], '#b20000', distance_from_sun[4] * np.cos(np.radians(i * 5))),
        spheres(diameter[5], '#ebebd2', distance_from_sun[5] * np.cos(np.radians(i * 3))),
        spheres(diameter[6], '#ebcd82', distance_from_sun[6] * np.cos(np.radians(i * 2))),
        spheres(diameter[7], '#37ffda', distance_from_sun[7] * np.cos(np.radians(i))),
        spheres(diameter[8], '#2500ab', distance_from_sun[8] * np.cos(np.radians(i))),
        orbits(distance_from_sun[1]),
        orbits(distance_from_sun[2]),
        orbits(distance_from_sun[3]),
        orbits(distance_from_sun[4]),
        orbits(distance_from_sun[5]),
        orbits(distance_from_sun[6]),
        orbits(distance_from_sun[7]),
        orbits(distance_from_sun[8]),
        orbits(23, distance_from_sun[6], '#827962', 3),
        orbits(24, distance_from_sun[6], '#827962', 3),
        orbits(25, distance_from_sun[6], '#827962', 3),
        orbits(26, distance_from_sun[6], '#827962', 3),
        orbits(27, distance_from_sun[6], '#827962', 3),
        orbits(28, distance_from_sun[6], '#827962', 3),
    ]
    frames.append(go.Frame(data=frame_data))

# Update layout with frames
layout.update(updatemenus=[dict(type='buttons', showactive=False, buttons=[dict(label='Play',
                            method='animate', args=[None, dict(frame=dict(duration=200, redraw=True), fromcurrent=True)])])])

# Create figure with initial data and layout
fig = go.Figure(data=[trace0, trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8,
                      trace11, trace12, trace13, trace14, trace15, trace16, trace17, trace18,
                      trace21, trace22, trace23, trace24, trace25, trace26],
                layout=layout,
                frames=frames)

# Show the figure
fig.show()