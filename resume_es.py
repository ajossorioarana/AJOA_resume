from fpdf import FPDF


def write_header(header_title: str, width: int, height: int):
        pdf.set_font("Ubuntu Bold", "", 11)
        pdf.set_text_color(0, 0, 0)
        pdf.set_draw_color(95, 130, 235)
        pdf.set_line_width(0.3)
        pdf.cell(w=width, h = height, txt=header_title, border="B", fill=False)
        pdf.ln(7)

def write_exp(company: str, role: str, link: str, period: str, place: str, keypoints: list, width: int, height: int):
        pdf.set_font("Ubuntu Medium", "", 10)
        pdf.set_text_color(0, 25, 100)
        pdf.cell(w=width, h=height, txt="{0} - {1}".format(role, company), link=link)
        pdf.ln(5)
        pdf.set_text_color(0, 0, 0)
        pdf.set_font("Ubuntu Medium", "", 8)
        pdf.cell(w=width, h=height, txt="{0} | {1}".format(period, place))
        pdf.ln(5)
        pdf.set_font("Ubuntu Light", "", 8)
        for keypoint in keypoints:
                pdf.write(h=height, txt="+ {0}".format(keypoint))
                pdf.ln(5)
        pdf.ln(3)

def write_education(title: str, university: str, grad_date: str, width: int, height: int):
        pdf.set_font("Ubuntu Medium", "", 10)
        pdf.set_text_color(0, 25, 100)
        pdf.cell(w=width, h=height, txt=title)
        pdf.ln(5)
        pdf.set_text_color(0, 0, 0)
        pdf.set_font("Ubuntu Light", "", 9)
        pdf.cell(w=width, h=height, txt=(university + " - " + grad_date))
        pdf.ln(8)

def write_project(title: str, keypoints: list, link: str, width: int, height: int):
        pdf.set_font("Ubuntu Medium", "", 10)
        pdf.set_text_color(0, 25, 100)
        pdf.cell(w=width, h=height, txt=title, link=link)
        pdf.ln(5)
        pdf.set_text_color(0, 0, 0)
        pdf.set_font("Ubuntu Light", "", 8)
        for keypoint in keypoints:
                        pdf.write(h=height, txt="+ {0}".format(keypoint))
                        pdf.ln(5)
        pdf.ln(3)


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

footnote  = ">>> Este CV se generó completamente en Python. Para ver el código, visite mi perfil de GitHub."
description = "Apasionado por aprovechar las soluciones de data science para abordar problemas complejos y multidisciplinarios, principalmente relacionados con los recursos hídricos y los ecosistemas acuáticos. Me destaco por ayudar a las organizaciones a comprender y aprovechar el potencial de su información. Reconocido por excelentes habilidades de comunicación combinadas con la capacidad de relacionarse con personas de orígenes diversos. Siempre abierto a nuevos desafíos, particularmente interesado en machine learning."


# Experience info

exp_1_role = "Biology Project Manager"
exp_1_company = "EcoAqua"
exp_1_company_link = "https://ecoaqua.com.ar/"
exp_1_period = "Feb. 2020 - Actualidad"
exp_1_place = "Buenos Aires, Argentina"
exp_1_keypoints = [
                "Diagnóstico y tratamiento de algas, malezas (sumergidas, flotantes y costeras), déficit de oxígeno disuelto y otros problemas de calidad de agua.",
                "Implementé nuevo sistema de elaboración de presupuestos basado en factores limnológicos y operativos asociados al lago del cliente, incrementando los ingresos un 27%.",
                "Desarrollé en conjunto con COO un nuevo flujo de trabajo para responder y solucionar reclamos de nuestros clientes, resultando en un aumento del 30% en la tasa de retención de clientes."
                ]

exp_2_role = "Aquatic Specialist"
exp_2_company = "EcoAqua"
exp_2_company_link = "https://ecoaqua.com.ar/"
exp_2_period = "Jun. 2017 - Ene. 2020"
exp_2_place = "Buenos Aires, Argentina"
exp_2_keypoints = [
                "Coordinador de cinco equipos de 2 personas, garantizando que los servicios y compromisos con los clientes se ejecuten a tiempo. Realicé planificaciones mensuales y semanales de tareas de campo, elaborando informes de gestión e instrucciones para operarios.",
                "Estuve a cargo del mantenimiento de 200+ hectáreas de lagos, lagunas y estanques, brindando un servicio de calidad superior que resultó en una reducción del 42% en la cantidad de reclamos.",
                "Formulé e implementé una rutina de mantenimiento de vehículos, herramientas y maquinaria, logrando disminuir interrupciones asociadas un 60%."
                ]

exp_3_role = 'Ayudante de Cátedra (Asignatura "Hidráulica Aplicada")'
exp_3_company = "UBA"
exp_3_company_link = "https://fi.uba.ar/"
exp_3_period = "Ago. 2017 - Actualidad"
exp_3_place = "Buenos Aires, Argentina"
exp_3_keypoints = [
                "Ayudante asignado a 100+ estudiantes, resolviendo consultas y corrigiendo trabajos prácticos. Reconocido como \"Excelente\" o \"Muy bueno\" por el 96% de los alumnos a cargo.",
                "Asistí a profesores en exámenes y en administración del curso. Dicté varias clases prácticas y desarrollé nuevas herramientas para que la mejor comprensión de temas difíciles de la asignatura.",
                "Programa de la materia: Cálculo de tuberías, máquinas hidráulicas, golpe de ariete, cálculo de canales, orificios y vertederos, curvas de remanso, resalto hidráulico y cálculo de alcantarillas."
                ]

exp_4_role = "Analista de Adquisiciones"
exp_4_company = "Gobierno de la Ciudad de Buenos Aires"
exp_4_company_link = "https://www.buenosaires.gob.ar/desarrollourbano/desarrollo/planes/plan-hidraulico"
exp_4_period = "Jun. 2016 - May. 2017"
exp_4_place = "Buenos Aires, Argentina"
exp_4_keypoints = [
                "Control y auditoría de certificados de avance de obra \"Segundo Emisario Arroyo Vega\". Monto adjudicado de $145MM USD.",
                "Desarrollo de pliegos para la licitación de obras y consultorías de obras hidráulicas, de acuerdo a normativas y lineamientos del BIRF."
                ]

# Education info

edu_1_title = "Maestría en Ecohidrología (Part-time)"
edu_1_place = "Universidad Nacional de la Plata (UNLP)"
edu_1_grad_date = "Tesis pendiente, Fecha estimada de graduación: 2022"

edu_2_title = "Ingeniero Civil"
edu_2_place = "Universidad de Buenos Aires (UBA)"
edu_2_grad_date = "Graduado 2018"


# Projects info

proj_1_title = "Elaboración de exámen de Pandas para evaluación de candidatos de diversos roles"
proj_1_link = "https://www.testgorilla.com/test-library/programming-skills-tests/pandas-test/"
proj_1_keypoints = [
                "Creación de 50 preguntas sitauacionales acerca de Pandas, diseñadas para evaluar el análisis situacional de candidatos. Revisión de más de 50 preguntas elaboradas por otro experto en la materia." 
                ]


proj_2_title = "Análisis exploratorio de datos sobre dataset de lagos y embalses de Argentina"
proj_2_link = "ajossorioarana.github.io"
proj_2_keypoints = [
                "Obtuve el índice de estado trófico (TSI) de Carlson para los cuerpos de agua del dataset mencionado. Analicé diferencias entre espejos de agua naturales y artificiales y el rol de la profundidad y latitud sobre la eutrofización. (Python + Seaborn)"
                ]



# ARMADO DE PDF
pdf = FPDF()
pdf.add_font("Ubuntu Light", "", r"C:\Users\aoa91\AppData\Local\Microsoft\Windows\Fonts\Ubuntu-Light.ttf", uni=True)
pdf.add_font("Ubuntu Light", "I", r"C:\Users\aoa91\AppData\Local\Microsoft\Windows\Fonts\Ubuntu-Light.ttf", uni=True)
pdf.add_font("Ubuntu Medium", "", r"C:\Users\aoa91\AppData\Local\Microsoft\Windows\Fonts\Ubuntu-Medium.ttf", uni=True)
pdf.add_font("Ubuntu Bold", "", r"C:\Users\aoa91\AppData\Local\Microsoft\Windows\Fonts\Ubuntu-Bold.ttf", uni=True)
pdf.add_page()
pdf.set_auto_page_break(True, margin=1)

width = 189
h_cells = 5

# NAME AND ROLE

pdf.ln(3)
pdf.set_text_color(0, 0, 0)
pdf.set_font("Ubuntu Medium", "", 18)
pdf.cell(w=width, h=h_cells, txt=name)
pdf.ln(8)
pdf.set_font("Ubuntu Light", "", 14)
pdf.cell(w=width, h=h_cells, txt=role)

pdf.ln(8)

# CONTACT INFO 
pdf.set_font("Ubuntu Medium", "", 8)
pdf.set_text_color(0, 25, 100)
pdf.write(h_cells, mail, link=mail)
pdf.write(h_cells, txt=(" "*3 + "|" + " "*3))
pdf.write(h_cells, website, link=website)
pdf.write(h_cells, txt=(" "*3 + "|" + " "*3))
pdf.write(h_cells, linkedin, link=linkedin)
pdf.write(h_cells, txt=(" "*3 + "|" + " "*3))
pdf.write(h_cells, cellphone)
pdf.ln(8)

# DESCRIPTION

write_header("ACERCA DE MÍ", width, h_cells)
pdf.ln(1)
pdf.set_font("Ubuntu Light", "", 9)
pdf.write(h=h_cells, txt=description)
pdf.ln(8)


# EXPERIENCE

write_header("EXPERIENCIA LABORAL", width, h_cells)
write_exp(exp_1_company, exp_1_role, exp_1_company_link, exp_1_period, exp_1_place, exp_1_keypoints, width, h_cells)
write_exp(exp_2_company, exp_2_role, exp_2_company_link, exp_2_period, exp_2_place, exp_2_keypoints, width, h_cells)
write_exp(exp_3_company, exp_3_role, exp_3_company_link, exp_3_period, exp_3_place, exp_3_keypoints, width, h_cells)
write_exp(exp_4_company, exp_4_role, exp_4_company_link, exp_4_period, exp_4_place, exp_4_keypoints, width, h_cells)


# EDUCATION

write_header("EDUCACIÓN", width, h_cells)
write_education(edu_1_title, edu_1_place, edu_1_grad_date, width, h_cells)
write_education(edu_2_title, edu_2_place, edu_2_grad_date, width, h_cells)


# PROJECTS 

write_header("PROJECTOS/PUBLICACIONES", width, h_cells)
write_project(proj_1_title, proj_1_keypoints, proj_1_link, width, h_cells)
#write_project(proj_2_title, proj_2_keypoints, proj_2_link, width, h_cells)


# Footnote

pdf.set_text_color(100, 100, 100)
pdf.set_font("Ubuntu Light", "I", 7)
pdf.set_xy(x=10, y=285)
pdf.write(h=h_cells - 2, txt=footnote, link=github)


# Export as PDF

pdf.output("Ossorio_Arturo_Resume_ES.pdf", "F")