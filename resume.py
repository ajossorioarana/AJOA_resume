from fpdf import FPDF

# TEXT VARIABLES

# Contact and general info
header  = ">>>This resume was generated entirely in Python. For full sourcecode, view my portfolio."
name = "Arturo J. Ossorio Arana"
role = "Ecohydrologist - Data Scientist"
city = "San Martín de los Andes"
prov_country = "Neuquén, Argentina"
mail = "arturoa91@gmail.com"
cellphone = "+54 9 11 3636823"
linkedin = "LinkedIn: /in/ajossorioarana"
github = "GitHub: /ajossorioarana"
website = "ajossorioarana.github.io"

desc_ln1 = "Ecohydrologist geared towards data science, with an analytical background and experience working with"
desc_ln2 = "stakeholders and managing teams. Currently increasing mastery in Machine Learning. I will be uploading"
desc_ln3 = "related content through my GitHub account and website."

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

# Education
edu_heading = "EDUCATION"

edu_1_title = "M.SC. in Ecohydrology"
edu_1_place = "UNLP"
edu_1_grad_date = "ABT, Expected Graduation Date: 2022"

edu_2_title = "Engineer's degree, Civil Engineer"
edu_2_place = "UBA"
edu_2_grad_date = "Graduated 2018"

# Experience
exp_heading = "EXPERIENCE"

exp_1_role = "Chief of Technical Department"
exp_1_company = "EcoAqua"
exp_1_company_link = "https://ecoaqua.com.ar/"
exp_1_period = "Feb. 2020 - Present"
exp_1_kp1 = "Diagnosed and treated customer's lakes for algae, weeds and water quality issues."
exp_1_kp2 = "Implemented new budgeting process, based on limnological factors, incresing revenue by > 30%."
exp_1_kp3 = "Worked together with COO, improving KPI performance, mainly client retention rate."

exp_2_role = "Aquatic Specialitst"
exp_2_company = "EcoAqua"
exp_2_company_link = "https://ecoaqua.com.ar/"
exp_2_period = "Jun. 2017 - Jan. 2020"
exp_2_kp1 = "Managed five 2-people teams to ensure all services are completed on schedule."
exp_2_kp2 = "Serviced customer’s lakes to provide superior quality and service in the fulfillment of all customer needs."
exp_2_kp3 = "Deployed maintainance routine for vehicles and machinery, decreasing workflow interruptions by 40%."

exp_3_role = 'Graduate Teaching Assistant (Course "Applied Hydraulics")'
exp_3_company = "UBA"
exp_3_period = "Aug. 2017 - Present"
exp_3_kp1 = "Been asigned to > 100 students, answering queries and grading assignments." 
exp_3_kp2 = "Aided professors in examinations and dictated several practical lectures."
exp_3_kp3 = "Syllabus: Pressurized pipe flow, pump selection, water hammer, open channel flow and weir design."

exp_4_role = "Bid/Tender Assistant"
exp_4_company = "Buenos Aires City Government"
exp_4_period = "Jun. 2016 - May. 2017"
exp_4_kp1 = "Cash-flow and finance audit of IBRD-loan WASH project (Arroyo Vega Drainage Tunnel > $145M)."
exp_4_kp2 = "Elaboration of bidding documentation in accordance to IBRD norms and recommendations."

# Projects
proj_heading = "PROJECTS/PUBLICATIONS"

proj_1_title = "EDA on Argentine lakes and reservoirs dataset"
proj_1_tech = "Python / Seaborn / EDA / CSV / DataViz"
proj_1_comment_1 = "Polished, visualized and interpreted resultes of Argentine lakes dataset."
proj_1_comment_2 = "Obtained Carlson's trophic state index (TSI) for waterboides and presented relevant analysis."

proj_2_title = "Watershed delineation of Chimehuín river, Patagonia, Argentina"
proj_2_tech = "QGIS / GRASS"
proj_2_comment_1 = "Developed map of Chimehuín river basin using processed DEM, with lakes and watercourses marked on it."
proj_2_comment_2 = "Created as part of dissertation about exotic willow (Salix fragilis) invasion of patagonian rivers."


# ARMADO DE PDF
pdf = FPDF()
pdf.add_font("Ubuntu Light", "", r"C:\Users\aoa91\AppData\Local\Microsoft\Windows\Fonts\Ubuntu-Light.ttf", uni=True)
pdf.add_font("Ubuntu Light", "I", r"C:\Users\aoa91\AppData\Local\Microsoft\Windows\Fonts\Ubuntu-Light.ttf", uni=True)
pdf.add_font("Ubuntu Medium", "", r"C:\Users\aoa91\AppData\Local\Microsoft\Windows\Fonts\Ubuntu-Medium.ttf", uni=True)
pdf.add_font("Ubuntu Bold", "", r"C:\Users\aoa91\AppData\Local\Microsoft\Windows\Fonts\Ubuntu-Bold.ttf", uni=True)
pdf.add_page()

width_first = 150
h_cells = 10


# NAME AND ROLE
pdf.ln(5)
pdf.set_text_color(0, 0, 0)
pdf.set_font("Ubuntu Medium", "", 18)
pdf.cell(w=width_first, h = h_cells, txt=name)
pdf.ln(10)

pdf.set_font("Ubuntu Light", "", 16)
pdf.cell(w=width_first, h = h_cells, txt=role)
pdf.set_line_width(0.5)

pdf.ln(12)

pdf.set_fill_color(215, 215, 255)
pdf.line(10, 37, width_first + 10, 37)
pdf.set_font("Ubuntu Light", "", 9)
pdf.cell(w=width_first, h = h_cells, txt=desc_ln1)
pdf.ln(6)
pdf.cell(w=width_first, h = h_cells, txt=desc_ln2)
pdf.ln(6)
pdf.cell(w=width_first, h = h_cells, txt=desc_ln3)
pdf.ln(13)
pdf.line(10, 59, width_first + 10, 59)

pdf.set_line_width(43)
pdf.set_draw_color(30, 80, 125)
pdf.line((width_first + 35), 30, (width_first + 35), 270)

# Contact information
pdf.set_text_color(255, 255, 255)
pdf.set_font("Ubuntu Medium", "", 8)
pdf.text(width_first + 17.5, 20, txt=city)
pdf.text(width_first + 17.5, 25, txt=prov_country)
pdf.text(width_first + 17.5, 35, txt=mail)
pdf.text(width_first + 17.5, 40, txt=cellphone)
pdf.text(width_first + 17.5, 45, txt=linkedin)
pdf.text(width_first + 17.5, 50, txt=github)
pdf.text(width_first + 17.5, 60, txt=website)

# Skills
pdf.set_font("Ubuntu Medium", "", 10)
pdf.text(width_first + 17.5, 80, txt="Skills:")
pdf.set_font("Ubuntu Medium", "", 8)
for i in range(len(skills)):
        pdf.text(width_first + 20, (85 + i*5), txt=("+ " + skills[i]))

pdf.set_font("Ubuntu Medium", "", 10)
aux_depth = 85 + len(skills)*5 + 20
pdf.text(width_first + 17.5, aux_depth, txt="Areas of interest:")
pdf.set_font("Ubuntu Medium", "", 8)
for i in range(len(interests)):
        pdf.text(width_first + 20, (aux_depth + 5 + i*5), txt=("+ " + interests[i]))



# EXPERIENCE

pdf.set_font("Ubuntu Bold", "", 12)
pdf.set_text_color(30, 80, 125)
pdf.cell(w=width_first, h = (h_cells - 2), txt=exp_heading, fill=True)
pdf.ln(8)

pdf.set_text_color(0, 0, 0)

pdf.set_font("Ubuntu Medium", "", 10)
pdf.cell(w=width_first, h = h_cells, txt="{0} - {1}".format(exp_1_company, exp_1_role), link=exp_1_company_link)
pdf.ln(5)
pdf.set_font("Ubuntu Light", "", 10)
pdf.cell(w=width_first, h = h_cells, txt=exp_1_period)
pdf.ln(5)
pdf.set_font("Ubuntu Light", "", 8)
pdf.cell(w=width_first, h = h_cells, txt="+ {0}".format(exp_1_kp1))
pdf.ln(5)
pdf.cell(w=width_first, h = h_cells, txt="+ {0}".format(exp_1_kp2))
pdf.ln(5)
pdf.cell(w=width_first, h = h_cells, txt="+ {0}".format(exp_1_kp3))

pdf.ln(8)

pdf.set_font("Ubuntu Medium", "", 10)
pdf.cell(w=width_first, h = h_cells, txt="{0} - {1}".format(exp_2_company, exp_2_role), link=exp_2_company_link)
pdf.ln(5)
pdf.set_font("Ubuntu Light", "", 10)
pdf.cell(w=width_first, h = h_cells, txt=exp_2_period)
pdf.ln(5)
pdf.set_font("Ubuntu Light", "", 8)
pdf.cell(w=width_first, h = h_cells, txt="+ {0}".format(exp_2_kp1))
pdf.ln(5)
pdf.cell(w=width_first, h = h_cells, txt="+ {0}".format(exp_2_kp2))
pdf.ln(5)
pdf.cell(w=width_first, h = h_cells, txt="+ {0}".format(exp_2_kp3))

pdf.ln(8)

pdf.set_font("Ubuntu Medium", "", 10)
pdf.cell(w=width_first, h = h_cells, txt="{0} - {1}".format(exp_3_company, exp_3_role))
pdf.ln(5)
pdf.set_font("Ubuntu Light", "", 10)
pdf.cell(w=width_first, h = h_cells, txt=exp_3_period)
pdf.ln(5)
pdf.set_font("Ubuntu Light", "", 8)
pdf.cell(w=width_first, h = h_cells, txt="+ {0}".format(exp_3_kp1))
pdf.ln(5)
pdf.cell(w=width_first, h = h_cells, txt="+ {0}".format(exp_3_kp2))
pdf.ln(5)
pdf.cell(w=width_first, h = h_cells, txt="+ {0}".format(exp_3_kp3))

pdf.ln(8)

pdf.set_font("Ubuntu Medium", "", 10)
pdf.cell(w=width_first, h = h_cells, txt="{0} - {1}".format(exp_4_company, exp_4_role))
pdf.ln(5)
pdf.set_font("Ubuntu Light", "", 10)
pdf.cell(w=width_first, h = h_cells, txt=exp_4_period)
pdf.ln(5)
pdf.set_font("Ubuntu Light", "", 8)
pdf.cell(w=width_first, h = h_cells, txt="+ {0}".format(exp_4_kp1))
pdf.ln(5)
pdf.cell(w=width_first, h = h_cells, txt="+ {0}".format(exp_4_kp2))

pdf.ln(10)

# EDUCATION

pdf.set_font("Ubuntu Bold", "", 12)
pdf.set_text_color(30, 80, 125)
pdf.cell(w=width_first, h=(h_cells - 2), txt=edu_heading, fill=True)
pdf.ln(8)

pdf.set_text_color(0, 0, 0)

pdf.set_font("Ubuntu Medium", "", 10)
pdf.cell(w=width_first, h = h_cells, txt=edu_1_title)
pdf.ln(5)
pdf.set_font("Ubuntu Light", "", 9)
pdf.cell(w=width_first, h = h_cells, txt=(edu_1_place + " - " + edu_1_grad_date))

pdf.ln(8)

pdf.set_font("Ubuntu Medium", "", 10)
pdf.cell(w=width_first, h = h_cells, txt=edu_2_title)
pdf.ln(5)
pdf.set_font("Ubuntu Light", "", 9)
pdf.cell(w=width_first, h = h_cells, txt=(edu_2_place + " - " + edu_2_grad_date))

pdf.ln(10)


# PROJECTS 

pdf.set_font("Ubuntu Bold", "", 12)
pdf.set_text_color(30, 80, 125)
pdf.cell(w=width_first, h = (h_cells - 2), txt=proj_heading, fill=True)
pdf.ln(8)

pdf.set_text_color(0, 0, 0)

pdf.set_font("Ubuntu Medium", "", 10)
pdf.cell(w=width_first, h = h_cells, txt=proj_1_title)
pdf.ln(5)
pdf.set_font("Ubuntu Light", "", 8)
pdf.cell(w=width_first, h = h_cells, txt="+ {0}".format(proj_1_tech))
pdf.ln(5)
pdf.cell(w=width_first, h = h_cells, txt="+ {0}".format(proj_1_comment_1))
pdf.ln(5)
pdf.cell(w=width_first, h = h_cells, txt="+ {0}".format(proj_1_comment_2))

pdf.ln(8)

pdf.set_font("Ubuntu Medium", "", 10)
pdf.cell(w=width_first, h = h_cells, txt=proj_2_title)
pdf.ln(5)
pdf.set_font("Ubuntu Light", "", 8)
pdf.cell(w=width_first, h = h_cells, txt="+ {0}".format(proj_2_tech))
pdf.ln(5)
pdf.cell(w=width_first, h = h_cells, txt="+ {0}".format(proj_2_comment_1))
pdf.ln(5)
pdf.cell(w=width_first, h = h_cells, txt="+ {0}".format(proj_2_comment_2))

pdf.ln(9)

pdf.set_text_color(100, 100, 100)
pdf.set_font("Ubuntu Light", "I", 7)
pdf.cell(w=width_first, h = h_cells-4, txt=header)

pdf.output("AJOA_Resume.pdf", "F")