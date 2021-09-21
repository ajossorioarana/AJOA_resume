from fpdf import FPDF


def write_header(header_title: str, width: int, height: int):
        pdf.set_font("Ubuntu Bold", "", 12)
        pdf.set_text_color(0, 0, 0)
        #pdf.set_draw_color(232,212,148)
        pdf.set_draw_color(62, 171, 134)
        pdf.set_line_width(0.3)
        pdf.cell(w=width, h = height, txt=header_title, border="B", fill=False)
        pdf.ln(8)

def write_exp(company: str, role: str, link: str, period: str, place: str, keypoints: list, width: int, height: int):
        pdf.set_font("Ubuntu Medium", "", 10)
        pdf.set_text_color(0, 15, 75)
        pdf.cell(w=width, h=height, txt="{0} - {1}".format(company, role), link=link)
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
        pdf.set_text_color(0, 15, 75)
        pdf.cell(w=width, h=height, txt=title)
        pdf.ln(5)
        pdf.set_text_color(0, 0, 0)
        pdf.set_font("Ubuntu Light", "", 8)
        pdf.cell(w=width, h=height, txt=(university + " - " + grad_date))
        pdf.ln(8)

def write_project(title: str, keypoints: list, width: int, height: int):
        pdf.set_font("Ubuntu Medium", "", 10)
        pdf.set_text_color(0, 15, 75)
        pdf.cell(w=width, h=height, txt=title)
        pdf.ln(5)
        pdf.set_text_color(0, 0, 0)
        pdf.set_font("Ubuntu Light", "", 8)
        for keypoint in keypoints:
                        pdf.write(h=height, txt="+ {0}".format(keypoint))
                        pdf.ln(5)
        pdf.ln(3)


# TEXT VARIABLES

# Contact and general info
header  = ">>>This resume was generated entirely in Python. For full sourcecode, view my portfolio."
name = "Arturo J. Ossorio Arana"
role = "Ecohydrologist - Data Scientist"
city = "San Martín de los Andes"
prov_country = "Neuquén, Argentina"
mail = "arturoa91@gmail.com"
cellphone = "+54 9 113 636 8323"
linkedin = "linkedin.com/in/ajossorioarana"
github = "github.com/ajossorioarana"
website = "ajossorioarana.github.io"

desc = "Ecohydrologist geared towards data science, with an analytical background and experience working with stakeholders and managing teams. Currently increasing mastery in Machine Learning. I will be uploading related content through my GitHub account and website."


# Skills
skills = [
        "Python",     
        "Pandas",
        "NumPy",
        "Matplotlib",
        "Seaborn",
        "SQL",
        "BigQuery",
        "Git & GitHub",
        "MS Excel",
        "Power BI",
        "QGIS",
        "GRASS"
        ]

# Areas of interest
interests = [
        "Data Science",
        "Data Analytics",
        "Remote Sensing",
        "Hydrology",
        "Ecohydrology",
        "Limnology",
        "Hydraulics"
        ]

# Education info

edu_1_title = "M.SC. in Ecohydrology"
edu_1_place = "UNLP"
edu_1_grad_date = "ABT, Expected Graduation Date: 2022"

edu_2_title = "Engineer's degree, Civil Engineer"
edu_2_place = "UBA"
edu_2_grad_date = "Graduated 2018"

# Experience info

exp_1_role = "Chief of Technical Department"
exp_1_company = "EcoAqua"
exp_1_company_link = "https://ecoaqua.com.ar/"
exp_1_period = "Feb. 2020 - Present"
exp_1_place = "Buenos Aires, Argentina"
exp_1_keypoints = [
                "Diagnosed and treated customer's lakes for algae, weeds and water quality issues.",
                "Implemented new budgeting process, based on limnological factors, incresing revenue by > 30%.",
                "Worked together with COO, improving KPI performance, mainly client retention rate."
                ]

exp_2_role = "Aquatic Specialitst"
exp_2_company = "EcoAqua"
exp_2_company_link = "https://ecoaqua.com.ar/"
exp_2_period = "Jun. 2017 - Jan. 2020"
exp_2_place = "Buenos Aires, Argentina"
exp_2_keypoints = [
                "Managed five 2-people teams to ensure all services are completed on schedule.",
                "Serviced customer’s lakes to provide superior quality and service in the fulfillment of all customer needs.",
                "Deployed maintainance routine for vehicles and machinery, decreasing workflow interruptions by 40%."
                ]

exp_3_role = 'Graduate Teaching Assistant (Course "Applied Hydraulics")'
exp_3_company = "UBA"
exp_3_company_link = "https://fi.uba.ar/"
exp_3_period = "Aug. 2017 - Present"
exp_3_place = "Buenos Aires, Argentina"
exp_3_keypoints = [
                "Been asigned to > 100 students, answering queries and grading assignments.",
                "Aided professors in examinations and dictated several practical lectures.",
                "Syllabus: Pressurized pipe flow, pump selection, water hammer, open channel flow and weir design."
                ]

exp_4_role = "Bid/Tender Assistant"
exp_4_company = "Buenos Aires City Government"
exp_4_company_link = "https://www.buenosaires.gob.ar/desarrollourbano/desarrollo/planes/plan-hidraulico"
exp_4_period = "Jun. 2016 - May. 2017"
exp_4_place = "Buenos Aires, Argentina"
exp_4_keypoints = [
                "Cash-flow and finance audit of IBRD-loan WASH project (Arroyo Vega Drainage Tunnel > $145M).",
                "Elaboration of bidding documentation in accordance to IBRD norms and recommendations."
                ]

# Projects info

proj_1_title = "EDA on Argentine lakes and reservoirs dataset"
proj_1_keypoints = [
                "Python / Seaborn / EDA / CSV / DataViz",
                "Polished, visualized and interpreted resultes of Argentine lakes dataset.",
                "Obtained Carlson's trophic state index (TSI) for waterboides and presented relevant analysis."
                ]

proj_2_title = "Watershed delineation of Chimehuín river, Patagonia, Argentina"
proj_2_keypoints = [
                "QGIS / GRASS",
                "Developed map of Chimehuín river basin using processed DEM, with lakes and watercourses marked on it.",
                "Created as part of dissertation about exotic willow (Salix fragilis) invasion of patagonian rivers."
                ]


# ARMADO DE PDF
pdf = FPDF()
pdf.add_font("Ubuntu Light", "", r"C:\Users\aoa91\AppData\Local\Microsoft\Windows\Fonts\Ubuntu-Light.ttf", uni=True)
pdf.add_font("Ubuntu Light", "I", r"C:\Users\aoa91\AppData\Local\Microsoft\Windows\Fonts\Ubuntu-Light.ttf", uni=True)
pdf.add_font("Ubuntu Medium", "", r"C:\Users\aoa91\AppData\Local\Microsoft\Windows\Fonts\Ubuntu-Medium.ttf", uni=True)
pdf.add_font("Ubuntu Bold", "", r"C:\Users\aoa91\AppData\Local\Microsoft\Windows\Fonts\Ubuntu-Bold.ttf", uni=True)
pdf.add_page()

width = 189
h_cells = 6

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
pdf.set_text_color(0, 15, 75)
pdf.write(h_cells, mail, link=mail)
pdf.write(h_cells, txt=(" "*3 + "|" + " "*3))
pdf.write(h_cells, cellphone)
pdf.write(h_cells, txt=(" "*3 + "|" + " "*3))
pdf.write(h_cells, linkedin, link=linkedin)
pdf.write(h_cells, txt=(" "*3 + "|" + " "*3))
pdf.write(h_cells, github, link=github)
pdf.write(h_cells, txt=(" "*3 + "|" + " "*3))
pdf.write(h_cells, website, link=website)
pdf.ln(8)

# DESCRIPTION

write_header("ABOUT ME", width, h_cells)
pdf.ln(1)
pdf.set_font("Ubuntu Light", "", 9)
pdf.write(h=h_cells - 1, txt=desc)
pdf.ln(8)


# EXPERIENCE

write_header("EXPERIENCE", width, h_cells)
write_exp(exp_1_company, exp_1_role, exp_1_company_link, exp_1_period, exp_1_place, exp_1_keypoints, width, h_cells)
write_exp(exp_2_company, exp_2_role, exp_2_company_link, exp_2_period, exp_2_place, exp_2_keypoints, width, h_cells)
write_exp(exp_3_company, exp_3_role, exp_3_company_link, exp_3_period, exp_3_place, exp_3_keypoints, width, h_cells)
write_exp(exp_4_company, exp_4_role, exp_4_company_link, exp_4_period, exp_4_place, exp_4_keypoints, width, h_cells)


# EDUCATION

write_header("EDUCATION", width, h_cells)
write_education(edu_1_title, edu_1_place, edu_1_grad_date, width, h_cells)
write_education(edu_2_title, edu_2_place, edu_2_grad_date, width, h_cells)


# PROJECTS 

write_header("PROJECTS/PUBLICATIONS", width, h_cells)
write_project(proj_1_title, proj_1_keypoints, width, h_cells)
write_project(proj_2_title, proj_2_keypoints, width, h_cells)


# Footer

pdf.ln(3)
pdf.set_text_color(100, 100, 100)
pdf.set_font("Ubuntu Light", "I", 7)
pdf.cell(w=width, h=h_cells-4, txt=header)


# Export as PDF

pdf.output("Ossorio_Arturo_Resume.pdf", "F")