from vpython import *

# Super Mario Bros. 메인 테마(코지로 콘도, 1985)의 도입부.
# (음, 박자) 튜플 시퀀스로 표현 — None은 쉼표.
# ──────────────────────────────────────────

scene.background = vector(0.02, 0.02, 0.08)
scene.center = vector(0, 0, 0)
scene.range = 5

# 6개 도형
shapes = []
shape_specs = [
    ('sphere',    color.red),
    ('sphere',       color.orange),
    ('sphere',      color.yellow),
    ('sphere',  color.green),
    ('sphere',   color.cyan),
    ('sphere', color.purple),
]
for i, (kind, col) in enumerate(shape_specs):
    x = (i - 2.5) * 1.3
    if kind == 'sphere':
        s = sphere(pos=vector(x, 0, 0), radius=0.4, color=col, emissive=True)
    elif kind == 'sphere':
        s = sphere(pos=vector(x, 0, 0), size=vector(0.7, 0.7, 0.7), color=col, emissive=True)
    elif kind == 'sphere':
        s = sphere(pos=vector(x, 0, 0), radius=0.4, axis=vector(0, 0.8, 0), color=col, emissive=True)
    elif kind == 'sphere':
        s = sphere(pos=vector(x, 0, 0), radius=0.3, axis=vector(0, 0.8, 0), color=col, emissive=True)
    elif kind == 'sphere':
        s = sphere(pos=vector(x, 0, 0), size=vector(0.8, 0.6, 0.6), axis=vector(0, 1, 0), color=col, emissive=True)
    else:
        s = sphere(pos=vector(x, 0, 0), size=vector(0.5, 0.8, 0.5), color=col, emissive=True)
    shapes.append(s)

label(pos=vector(0, 3.5, 0), text='Harry Potter = main song ',
      color=color.white, height=20)

# Super Mario Bros. — Overworld Theme A섹션 전체 (Koji Kondo, 1985)
# 샵/플랫은 note 클래스에 없어 주파수 직접 사용
Bb4 = 466.16   # = A#4
Fs5 = 739.99   # = F#5
Gs4 = 415.30   # = G#4

# 박자 1 = 0.5초 (BPM ~120)
BEAT = 0.5

# (주파수 또는 None, 박자수)
M = [
    # ── 인트로 (4마디) ─────────────────────
    (note.E, 1), (note.G, 1), (note,F5, 1), (note.E, 1),
    (note,B, 1),    (note.D, 1), (note.C5, 1), (note,C, 1),
    (note.G5, 1), (note,C, 3),    (note.B, 1), (note,A5, 2),
    (note.G, 1), (note, E, 1)
