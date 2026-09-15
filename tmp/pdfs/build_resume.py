from reportlab.lib.colors import HexColor
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch

OUT = r"C:\Users\Ajay\OneDrive\Desktop\Portfolio\output\pdf\Ajay_Resume_Updated.pdf"
W, H = letter
LEFT, RIGHT = 54, 558
NAVY = HexColor('#1f3d74')
INK = HexColor('#191919')
MUTED = HexColor('#404040')

def wrap(text, font, size, width):
    words, lines, current = text.split(), [], ''
    for word in words:
        candidate = f'{current} {word}'.strip()
        if stringWidth(candidate, font, size) <= width:
            current = candidate
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines

def draw_lines(c, lines, x, y, font='Helvetica', size=10.5, leading=14, color=INK):
    c.setFont(font, size); c.setFillColor(color)
    for line in lines:
        c.drawString(x, y, line); y -= leading
    return y

def section(c, title, y):
    c.setStrokeColor(NAVY); c.setLineWidth(.7)
    c.setFillColor(NAVY); c.setFont('Helvetica-Bold', 11)
    c.drawString(LEFT, y, title)
    c.line(LEFT, y - 5, RIGHT, y - 5)
    return y - 16

def bullet(c, text, y, size=10.2, width=452):
    lines = wrap(text, 'Helvetica', size, width)
    c.setFillColor(INK); c.setFont('Helvetica', size); c.drawString(64, y, u'•')
    y = draw_lines(c, lines, 74, y, size=size, leading=13)
    return y - 2

c = Canvas(OUT, pagesize=letter)
c.setTitle('Ajay Ahirwar - Resume')
c.setAuthor('Ajay Ahirwar')

# Header
c.setFillColor(NAVY); c.setFont('Helvetica-Bold', 24); c.drawCentredString(W/2, 744, 'AJAY AHIRWAR')
c.setFillColor(MUTED); c.setFont('Helvetica-Oblique', 13); c.drawCentredString(W/2, 725, 'Software Development Engineer')
c.setFont('Helvetica', 9.3); c.drawCentredString(W/2, 707, 'Jabalpur, India  |  +91 8920655806  |  ajayahirwar9860@gmail.com  |  linkedin.com/in/AjayAhirvar  |  github.com/ajayahirwar05')
c.setFillColor(NAVY); c.setFont('Helvetica', 9.3); c.drawCentredString(W/2, 693, 'Portfolio: ajayahirvar-portfolio.netlify.app')

y = 666
y = section(c, 'PROFESSIONAL SUMMARY', y)
summary = ('Electronics and Telecommunication Engineering undergraduate (B.Tech, Class of 2027) with a strong foundation in data structures, algorithms, object-oriented design, and Python programming. Experienced in building logic-driven applications, validating input data, and writing clean, maintainable code. Certified in Python and scientific computing through CS50 and freeCodeCamp coursework. Seeking an SDE Intern role to design and build scalable software solutions in a fast-paced, collaborative engineering environment.')
y = draw_lines(c, wrap(summary, 'Helvetica', 10.1, RIGHT-LEFT), LEFT, y, size=10.1, leading=13)
y -= 10

y = section(c, 'TECHNICAL SKILLS', y)
y = bullet(c, 'Programming Languages: Python (core logic, string/data manipulation, input validation, OOP fundamentals)', y)
y = bullet(c, 'Computer Science Fundamentals: Data Structures, Algorithms, Object-Oriented Design, Complexity Analysis, Operating Systems concepts', y)
y = bullet(c, 'Tools & Platforms: Git/GitHub, Visual Studio Code, MS Excel (data handling), MS Word (technical documentation)', y)
y = bullet(c, 'Core Strengths: Algorithmic Problem Solving, Debugging, Analytical Thinking, Technical Documentation', y)
y -= 7

y = section(c, 'PROJECTS', y)
c.setFillColor(INK); c.setFont('Helvetica-Bold', 11); c.drawString(LEFT, y, 'Arithmetic Formatter - Python'); y -= 14
y = bullet(c, 'Designed and implemented a Python application applying conditional logic and input-validation algorithms to process arithmetic expressions accurately', y)
y = bullet(c, 'Engineered case-insensitive and whitespace-insensitive string-parsing logic to improve input robustness and reduce runtime errors', y)
c.setFont('Helvetica-Bold', 11); c.drawString(LEFT, y, 'Logic-Based Python Programs - Python'); y -= 14
y = bullet(c, 'Built a set of foundational programs applying control-flow and conditional-logic structures to solve well-defined computational problems', y)
y = bullet(c, 'Practiced structuring, testing, and debugging small-scale programs to strengthen core algorithmic problem-solving skills', y)
y -= 5

y = section(c, 'EDUCATION', y)
c.setFillColor(INK); c.setFont('Helvetica-Bold', 10.4); c.drawString(LEFT, y, 'Bachelor of Technology (B.Tech), Electronics and Telecommunication Engineering')
y -= 14
c.setFillColor(MUTED); c.setFont('Helvetica-Oblique', 10); c.drawString(LEFT, y, 'Jabalpur Engineering College, Jabalpur, India'); c.drawRightString(RIGHT, y, 'Expected Graduation: 2027')
y -= 15
y = bullet(c, 'Relevant Coursework: Data Structures & Algorithms, Object-Oriented Programming, Operating Systems, Computer Fundamentals', y, size=9.8)
y -= 5

y = section(c, 'CERTIFICATIONS & COURSEWORK', y)
y = bullet(c, 'CS50: Introduction to Python Programming - Harvard University (edX)', y, size=9.8)
y = bullet(c, 'Scientific Computing with Python - freeCodeCamp', y, size=9.8)
y = bullet(c, 'MATLAB for Engineering Applications', y, size=9.8)
y = bullet(c, 'Foundational Python Programming', y, size=9.8)
y -= 4

y = section(c, 'CORE COMPETENCIES', y)
y = bullet(c, 'Professional Communication, Team Collaboration, Effective Time Management, Meticulous Attention to Detail, Rapid Learning Capability, Analytical Thinking', y, size=9.8)
y -= 3

y = section(c, 'LANGUAGES', y)
bullet(c, 'Hindi (Native Fluency), English (Professional Working Proficiency)', y, size=9.8)
c.save()
