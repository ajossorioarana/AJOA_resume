from fpdf import FPDF

# TEXT VARIABLES

# Contact and general info
header  = ">>>This resume was generated entirely in Python. For full sourcecode, view my portfolio."
name = "Arturo J. Ossorio Arana"
role = "Data Science and Analytics - Ecohidrologist"
city = "San Martín de los Andes"
prov_country = "Neuquén, Argentina"
mail = "arturoa91@gmail.com"
cellphone = "+54 9 11 3636823"
linkedin = "linkedin.com/in/ajossorioarana"
github = "github.com/ajossorioarana"
website = "ajossorioarana.github.io"

# Skills
skills = [
        "Python",     
        "Pandas",
        "NumPy",
        "Matplotlib",
        "Seaborn",
        "SQL",
        "Bigquery",
        "Git & GitHub",
        "MS Excel",
        "Power BI",
        "QGIS",
        "GRASS"
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
exp_1_kp2 = "Implemented new budgeting process, based on technical demans of client's waterbody, incresing revenue by > 30%."
exp_1_kp3 = "Worked together with COO, improving KPI performance, mainly refearing to "

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
exp_4_kp1 = "Assigned to  IBRD-loan (> $145M)"
exp_4_kp2 = "Second keypoint and comment."
exp_4_kp3 = "Third keypoint and comment."

# Projects
proj_heading = "PROJECTS/PUBLICATIONS"

proj_1_title = "EDA on Argentine lakes dataset"
proj_1_tech = "Python / Seaborn / EDA / CSV / DataViz"
proj_1_comment = "Polished, visualized and interpreted resultes of Argentine lakes dataset."

proj_2_title = "EDA on Argentine lakes dataset"
proj_2_tech = "Python / Seaborn / EDA / CSV / DataViz"
proj_2_comment = "Polished, visualized and interpreted resultes of Argentine lakes dataset."


# ARMADO DE PDF
pdf = FPDF()
pdf.add_font("Ubuntu Light", "", r"C:\Users\aoa91\AppData\Local\Microsoft\Windows\Fonts\Ubuntu-Light.ttf", uni=True)
pdf.add_font("Ubuntu Light", "I", r"C:\Users\aoa91\AppData\Local\Microsoft\Windows\Fonts\Ubuntu-Light.ttf", uni=True)
pdf.add_font("Ubuntu Medium", "", r"C:\Users\aoa91\AppData\Local\Microsoft\Windows\Fonts\Ubuntu-Medium.ttf", uni=True)
pdf.add_font("Ubuntu Bold", "", r"C:\Users\aoa91\AppData\Local\Microsoft\Windows\Fonts\Ubuntu-Bold.ttf", uni=True)
pdf.add_page()

width_first = 130
h_cells = 10


# HEADER, NAME AND ROLE
pdf.ln(5)
pdf.set_text_color(0, 0, 0)
pdf.set_font("Ubuntu Medium", "", 18)
pdf.cell(w=width_first, h = h_cells, txt=name)
pdf.ln(10)

pdf.set_font("Ubuntu Light", "", 16)
pdf.cell(w=width_first, h = h_cells, txt=role)
pdf.set_line_width(0.5)

pdf.ln(17)

pdf.set_fill_color(215, 215, 255)
pdf.line(10, 37, width_first + 10, 37)

pdf.set_line_width(60)
pdf.set_draw_color(30, 80, 125)
pdf.line((width_first + 45), 40, (width_first + 45), 260)

pdf.set_text_color(255, 255, 255)
pdf.set_font("Ubuntu Medium", "", 10)
pdf.text(width_first + 19, 20, txt=city)
pdf.text(width_first + 19, 25, txt=prov_country)
pdf.text(width_first + 19, 35, txt=mail)
pdf.text(width_first + 19, 40, txt=cellphone)
pdf.text(width_first + 19, 45, txt=linkedin)
pdf.text(width_first + 19, 50, txt=github)
pdf.text(width_first + 19, 60, txt=website)



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
pdf.cell(w=width_first, h = h_cells, txt="+ {0}".format(proj_1_comment))

pdf.ln(8)

pdf.set_font("Ubuntu Medium", "", 10)
pdf.cell(w=width_first, h = h_cells, txt=proj_2_title)
pdf.ln(5)
pdf.set_font("Ubuntu Light", "", 8)
pdf.cell(w=width_first, h = h_cells, txt="+ {0}".format(proj_2_tech))
pdf.ln(5)
pdf.cell(w=width_first, h = h_cells, txt="+ {0}".format(proj_2_comment))

pdf.ln(15)

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
pdf.ln(5)
pdf.cell(w=width_first, h = h_cells, txt="+ {0}".format(exp_4_kp3))

pdf.ln(15)

# EDUCATION

pdf.set_font("Ubuntu Bold", "", 12)
pdf.set_text_color(30, 80, 125)
pdf.cell(w=width_first, h=(h_cells - 2), txt=edu_heading, fill=True)
pdf.ln(8)

pdf.set_text_color(0, 0, 0)

pdf.set_font("Ubuntu Medium", "", 10)
pdf.cell(w=width_first, h = h_cells, txt=edu_1_title)
pdf.ln(5)
pdf.set_font("Ubuntu Light", "", 10)
pdf.cell(w=width_first, h = h_cells, txt=edu_1_place)
pdf.ln(5)
pdf.cell(w=width_first, h = h_cells, txt=edu_1_grad_date)

pdf.ln(8)

pdf.set_font("Ubuntu Medium", "", 10)
pdf.cell(w=width_first, h = h_cells, txt=edu_2_title)
pdf.ln(5)
pdf.set_font("Ubuntu Light", "", 10)
pdf.cell(w=width_first, h = h_cells, txt=edu_2_place)
pdf.ln(5)
pdf.cell(w=width_first, h = h_cells, txt=edu_2_grad_date)

pdf.ln(10)

pdf.set_text_color(100, 100, 100)
pdf.set_font("Ubuntu Light", "I", 9)
pdf.text(10, 285, txt=header)


pdf.output("Resume.pdf", "F")
