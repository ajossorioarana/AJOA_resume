from fpdf import FPDF

def write_header(header_title: str, width: int, height: int):
        pdf.set_font("Ubuntu Bold", "", 14)
        pdf.set_text_color(0, 0, 0)
        pdf.set_draw_color(95, 130, 235)
        pdf.cell(w=width, h = height, txt=header_title, border='B', fill=False, ln=0)
        pdf.ln(8)

def write_exp(company: str, role: str, link: str, period: str, place: str, keypoints: list, width: int, height: int, x: float):
        pdf.set_font("Ubuntu Medium", "", 12)
        pdf.set_text_color(0, 25, 100)
        pdf.set_x(x)
        pdf.cell(w=width, h=height, txt="{0} @ {1}".format(role, company), link=link)
        pdf.ln(5)
        pdf.set_text_color(0, 0, 0)
        pdf.set_font("Ubuntu Medium", "", 9)
        pdf.set_x(x)
        pdf.cell(w=width, h=height, txt="{0} | {1}".format(period, place))
        pdf.ln(5)
        pdf.set_font("Ubuntu Light", "", 8)
        for keypoint in keypoints:
                pdf.set_x(x)
                pdf.multi_cell(w=width, h=height, txt="• {0}".format(keypoint))
        pdf.ln(4)

def write_education(title: str, university: str, grad_date: str, width: int, height: int):
        pdf.set_font("Ubuntu Medium", "", 10)
        pdf.set_text_color(0, 25, 100)
        pdf.cell(w=width, h=height, txt=title)
        pdf.ln(5)
        pdf.set_text_color(0, 0, 0)
        pdf.set_font("Ubuntu Light", "", 9)
        pdf.multi_cell(w=width, h=height, txt=university)
        pdf.multi_cell(w=width, h=height, txt=grad_date)
        pdf.ln(5)

def write_project(title: str, keypoints: list, link: str, width: int, height: int, x: float):
        pdf.set_font("Ubuntu Medium", "", 10)
        pdf.set_text_color(0, 25, 100)
        pdf.set_x(x)
        pdf.cell(w=width, h=height, txt=title, link=link)
        pdf.ln(5)
        pdf.set_text_color(0, 0, 0)
        pdf.set_font("Ubuntu Light", "", 8)
        for keypoint in keypoints:
                        pdf.set_x(x)
                        pdf.multi_cell(w=width, h=height, txt="• {0}".format(keypoint))
                        # pdf.ln(5)
        pdf.ln(3)

def write_skills(area: str, description: str, width: int, height: int):
        pdf.set_font(family="Ubuntu Medium", style="", size=9)
        pdf.set_text_color(0, 0, 0)
        pdf.cell(w=width, h=height, txt=area)
        pdf.ln(5)
        pdf.set_font(family="Ubuntu Light", style="I", size=8)
        pdf.multi_cell(w=width, h=height, txt=description, align='L')
        pdf.ln(1.5)

def write_activities(description: str, width: int, height: int):
        pdf.set_text_color(0, 0, 0)
        pdf.set_font(family="Ubuntu Light", style="I", size=8)
        pdf.multi_cell(w=width, h=height, txt=description, align='L')
        pdf.ln(1.5)


# TEXT VARIABLES

# Contact and general info

name = "Arturo J. Ossorio Arana"
role = "Data Scientist"
city = "San Martín de los Andes"
prov_country = "Neuquén, Argentina"
mail = "arturoa91@gmail.com"
cellphone = "+54 9 113 636 8323"
linkedin = "linkedin.com/in/ajossorioarana"
github = "github.com/ajossorioarana"
website = "ajossorioarana.github.io"

description = "Me gusta construir cosas, experimentar con nuevas herramientas y aprender nuevos conceptos. Encuentro el proceso de seccionar un problema, analizar sus distintos componentes y evaluar las posibles soluciones (con sus pros y contras) extremadamente estimulante, especialmente al encarar problemas complejos y multidisciplinarios con resultados tangibles.\nEn búsqueda de nuevos desafíos dentro de data analytics o data science. Estoy particularmente interesado en la intersección entre data science y ecohidrología o ecosistemas acuáticos."

# Experience info
exp_1_role = "Limnólogo | Data Analyst"
exp_1_company = "EcoAqua"
exp_1_company_link = "https://ecoaqua.com.ar/"
exp_1_period = "Mar. 2021 - Actualidad"
exp_1_place = "Argentina (Remoto)"
exp_1_keypoints = [
                "Elaboración periodica de informes a clientes sobre estado de espejos de agua, identificando tendencias negativas en parámetros clave y evaluando posibles soluciones.",
                "Modernicé proceso de informes, disminuyendo el tiempo de entrega en un 45% y disminuyendo substancialmente los errores cometidos.",
                "Realicé análisis con datos de calidad de agua, identificando diferencias regionales y estacionales en variables fundamentales, así como correlaciones potenciales entre parámetros limnológicos y características morfológica de los cuerpos de agua y sus cuencas."
                ]

exp_2_role = "Biology Project Manager"
exp_2_company = "EcoAqua"
exp_2_company_link = "https://ecoaqua.com.ar/"
exp_2_period = "Feb. 2020 - Feb. 2021"
exp_2_place = "Buenos Aires, Argentina"
exp_2_keypoints = [
                "Diagnóstico y tratamiento de algas, malezas (sumergidas, flotantes y costeras), déficit de oxígeno disuelto y otros problemas de calidad de agua.",
                "Implementé nuevo sistema de elaboración de presupuestos basado en factores limnológicos y operativos asociados al lago del cliente, incrementando los ingresos un 27%.",
                "Desarrollé en conjunto con COO un nuevo flujo de trabajo para responder y solucionar reclamos de nuestros clientes, resultando en un aumento del 30% en la tasa de retención de clientes."
                ]

exp_3_role = "Aquatic Specialist"
exp_3_company = "EcoAqua"
exp_3_company_link = "https://ecoaqua.com.ar/"
exp_3_period = "Jun. 2017 - Ene. 2020"
exp_3_place = "Buenos Aires, Argentina"
exp_3_keypoints = [
                "Coordinador de cinco equipos de 2 personas, garantizando que los servicios y compromisos con los clientes se ejecuten a tiempo. Realicé planificaciones mensuales y semanales de tareas de campo, elaborando informes de gestión e instrucciones para operarios.",
                "Estuve a cargo del mantenimiento de 200+ hectáreas de lagos, lagunas y estanques, brindando un servicio de calidad superior que resultó en una reducción del 42% en la cantidad de reclamos.",
                "Formulé e implementé una rutina de mantenimiento de vehículos, herramientas y maquinaria, logrando disminuir interrupciones asociadas un 60%."
                ]

exp_4_role = 'Ayudante de Cátedra (Asignatura "Hidráulica Aplicada")'
exp_4_company = "UBA"
exp_4_company_link = "https://fi.uba.ar/"
exp_4_period = "Ago. 2017 - Actualidad"
exp_4_place = "Buenos Aires, Argentina"
exp_4_keypoints = [
                "Ayudante asignado a 100+ estudiantes, resolviendo consultas y corrigiendo trabajos prácticos. Reconocido como \"Excelente\" o \"Muy bueno\" por el 96% de los alumnos a cargo.",
                "Asistí a profesores en exámenes y en administración del curso. Dicté varias clases prácticas y desarrollé nuevas herramientas para que la mejor comprensión de temas difíciles de la asignatura.",
                "Programa de la materia: Cálculo de tuberías, máquinas hidráulicas, golpe de ariete, cálculo de canales, orificios y vertederos, curvas de remanso, resalto hidráulico y cálculo de alcantarillas."
                ]


# Education info
edu_1_title = "Maestría en Ecohidrología"
edu_1_place = "Universidad Nacional de la Plata (UNLP)"
edu_1_grad_date = "Tesis pendiente\nFecha estimada de graduación: 2023"

edu_2_title = "Ingeniero Civil"
edu_2_place = "Universidad de Buenos Aires (UBA)"
edu_2_grad_date = "Graduado 2018"


# Projects info
proj_1_title = "Desarrollo de exámen de Pandas para evaluación de candidatos de diversos roles"
proj_1_link = "https://www.testgorilla.com/test-library/programming-skills-tests/pandas-test/"
proj_1_keypoints = [
                "Creación de 50 preguntas sitauacionales acerca de Pandas, diseñadas para evaluar el análisis situacional de candidatos. Revisión de más de 50 preguntas elaboradas por otro experto en la materia." 
                ]


proj_2_title = "Análisis exploratorio sobre dataset de lagos y embalses de Argentina"
proj_2_link = "ajossorioarana.github.io"
proj_2_keypoints = [
                "Obtuve el índice de estado trófico (TSI) de Carlson para los cuerpos de agua del dataset mencionado. Analicé diferencias entre espejos de agua naturales y artificiales y el rol de la profundidad y latitud sobre la eutrofización. (Python + Seaborn)"
                ]


# Skills info
skills_1_title = "Python"
skills_1_description = "Pandas, scikit-learn, GeoPandas, NumPy, Request, Matplotlib, Seaborn"

skills_2_title = "Herramientas relacionadas"
skills_2_description = "Git, SQL, PostgreSQL"

skills_3_title = "GIS y Imágenes satelitales"
skills_3_description = "QGIS, Datos vectores y ráster, MDE, Delineación de cuencas"

skills_4_title = "Matemáticas"
skills_4_description = "Probabilidad, Estadística, Álgebra Lineal, Análisis Matemático"

skills_5_title = "Ecohidrología y Limnología"
skills_5_description = "Balance hídrico, Precipitaciones de diseño, Eutrofización, Manejo de lagos"

# Other activities
activities_description = "Fútbol, Pesca con mosca, Trekking, Esquí, Camping, Lectura, Guitarra, Radioafición."


# Creates an instance of FPDF class and sets its title and author
pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_title('Resumé AJOA')
pdf.set_author('Arturo J. Ossorio Arana')

# Adds fonts relevant to the document
pdf.add_font("Ubuntu Light", "", r"C:\Users\aoa91\AppData\Local\Microsoft\Windows\Fonts\Ubuntu-Light.ttf", uni=True)
pdf.add_font("Ubuntu Light", "I", r"C:\Users\aoa91\AppData\Local\Microsoft\Windows\Fonts\Ubuntu-Light.ttf", uni=True)
pdf.add_font("Ubuntu Medium", "", r"C:\Users\aoa91\AppData\Local\Microsoft\Windows\Fonts\Ubuntu-Medium.ttf", uni=True)
pdf.add_font("Ubuntu Bold", "", r"C:\Users\aoa91\AppData\Local\Microsoft\Windows\Fonts\Ubuntu-Bold.ttf", uni=True)

# Adds page and sets auto page break
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=10)

# Declares useful width measurements for later use
ef_page_width = pdf.w - pdf.l_margin - pdf.r_margin
col1_width = 60 # mm
col_sep = 5 # mm
col2_width = ef_page_width - col1_width - col_sep
col2_start = pdf.l_margin + col1_width + col_sep

h_cells = 5

# NAME AND ROLE
pdf.ln(h=5)
pdf.set_text_color(0, 0, 0)
pdf.set_font(family="Ubuntu Medium", style="", size=18)
pdf.cell(w=ef_page_width, txt=name)
pdf.ln(h=8)
pdf.set_font(family="Ubuntu Light", style="", size=16)
pdf.cell(w=ef_page_width, txt=role)

pdf.ln(h=5)

# CONTACT INFO 
pdf.set_font("Ubuntu Medium", "", 8)
pdf.set_text_color(0, 25, 100)
pdf.write(h=h_cells, txt=mail, link=mail)
pdf.write(h=h_cells, txt=(" "*3 + "|" + " "*3))
pdf.write(h=h_cells, txt=website, link=website)
pdf.write(h=h_cells, txt=(" "*3 + "|" + " "*3))
pdf.write(h=h_cells, txt=linkedin, link=linkedin)
pdf.write(h=h_cells, txt=(" "*3 + "|" + " "*3))
pdf.write(h=h_cells, txt=cellphone)
pdf.ln(10)

ybefore = pdf.get_y() # Save the top coordinate of the columns

# DESCRIPTION
write_header("ACERCA DE MI", col1_width, h_cells)
pdf.ln(1)
pdf.set_font("Ubuntu Light", "", 9)
pdf.multi_cell(w=col1_width, h=h_cells, txt=description, align='L')
pdf.ln(5)

# EDUCATION
write_header("EDUCACIÓN", col1_width, h_cells)
write_education(edu_1_title, edu_1_place, edu_1_grad_date, col1_width, h_cells)
write_education(edu_2_title, edu_2_place, edu_2_grad_date, col1_width, h_cells)

# SKILLS
write_header("HABILIDADES", col1_width, h_cells)
write_skills(skills_1_title, skills_1_description, col1_width, h_cells)
write_skills(skills_2_title, skills_2_description, col1_width, h_cells)
write_skills(skills_3_title, skills_3_description, col1_width, h_cells)
write_skills(skills_4_title, skills_4_description, col1_width, h_cells)
write_skills(skills_5_title, skills_5_description, col1_width, h_cells)
pdf.ln(3)

# ACTIVITIES
write_header("OTRAS ACTIVIDADES", col1_width, h_cells)
write_activities(activities_description, col1_width, h_cells)

pdf.set_xy(x=col2_start, y=ybefore)

# EXPERIENCE
write_header("EXPERIENCIA", col2_width, h_cells)
write_exp(exp_1_company, exp_1_role, exp_1_company_link, exp_1_period, exp_1_place, exp_1_keypoints, col2_width, h_cells, col2_start)
write_exp(exp_2_company, exp_2_role, exp_2_company_link, exp_2_period, exp_2_place, exp_2_keypoints, col2_width, h_cells, col2_start)
write_exp(exp_3_company, exp_3_role, exp_3_company_link, exp_3_period, exp_3_place, exp_3_keypoints, col2_width, h_cells, col2_start)
write_exp(exp_4_company, exp_4_role, exp_4_company_link, exp_4_period, exp_4_place, exp_4_keypoints, col2_width, h_cells, col2_start)
pdf.ln(1)
# PROJECTS 
pdf.set_x(col2_start)
write_header("PROJECTOS/PUBLICACIONES", col2_width, h_cells)
write_project(proj_1_title, proj_1_keypoints, proj_1_link, col2_width, h_cells, col2_start)
write_project(proj_2_title, proj_2_keypoints, proj_2_link, col2_width, h_cells, col2_start)


# Write line that separates columns
pdf.set_draw_color(95, 130, 235)
x_line = col2_start - 0.5 * col_sep
y_line = ybefore - h_cells*0.5
pdf.line(x1=pdf.l_margin, y1=y_line, x2=(ef_page_width + pdf.r_margin), y2=y_line)
pdf.line(x1=x_line, y1=y_line, x2=x_line, y2=(pdf.h - pdf.b_margin))

# Export as PDF
pdf.output("Ossorio-Arturo_Resume_ES.pdf", "F")