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
                pdf.write(h=height, txt="• {0}".format(keypoint))
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
                        pdf.write(h=height, txt="• {0}".format(keypoint))
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

footnote  = ">>> This resume was generated entirely in Python. For full source code, view my portfolio."
description = "Passionate about harnessing data science solutions to tackle complex, cross-functional problems, mainly related to water resources and freshwater ecosystems. I excel in helping organizations to understand and leverage the full potential of their data. Recognized for excellent communication skills combined with the ability to relate to people from diverse backgrounds. Always open for new challenges, particularly interested in machine learning."


# Experience info

exp_1_role = "Biology Project Manager"
exp_1_company = "EcoAqua"
exp_1_company_link = "https://ecoaqua.com.ar/"
exp_1_period = "Feb. 2020 - Present"
exp_1_place = "Buenos Aires, Argentina"
exp_1_keypoints = [
                "Diagnosed and treated for algae, submersed, floating and shoreline weeds, non-desirable buffer vegetation and any other unwanted vegetation and water quality issues.",
                "Implemented new budgeting process based on limnological and operational factors, increasing revenue by 27%.",
                "Devised and developed alongside COO new workflow for dealing with customer's complaints, improving client retention rate by 30% and ensuring response of every request on time."
                ]

exp_2_role = "Aquatic Specialist"
exp_2_company = "EcoAqua"
exp_2_company_link = "https://ecoaqua.com.ar/"
exp_2_period = "Jun. 2017 - Jan. 2020"
exp_2_place = "Buenos Aires, Argentina"
exp_2_keypoints = [
                "Managed five 2-people teams guaranteeing all services were completed on schedule. Planned monthly and weekly field and client related work, providing detailed notes and service instructions.",
                "In charge of maintaining 500+ acres of customer’s lakes, providing superior quality service in the fulfillment of all customer needs, leading to 42% complaint reduction.",
                "Formulated and standardized maintenance routine for vehicles, machinery and tools, decreasing workflow interruptions by 60%."
                ]

exp_3_role = 'Graduate Teaching Assistant (Course "Applied Hydraulics")'
exp_3_company = "UBA"
exp_3_company_link = "https://fi.uba.ar/"
exp_3_period = "Aug. 2017 - Present"
exp_3_place = "Buenos Aires, Argentina"
exp_3_keypoints = [
                "Assigned to 100+ students, answering queries and grading assignments. Rated as \"Very helpful\" or \"Excellent\" by 96% of students.",
                "Aided professors in examinations and course administration. Gave several practical lectures, developing new material for grasping difficult concepts.",
                "Syllabus: Pressurized pipe flow, pump selection, water hammer, open channel flow and weir and culvert design."
                ]

exp_4_role = "Bid/Tender Analyst"
exp_4_company = "Buenos Aires City Government"
exp_4_company_link = "https://www.buenosaires.gob.ar/desarrollourbano/desarrollo/planes/plan-hidraulico"
exp_4_period = "Jun. 2016 - May. 2017"
exp_4_place = "Buenos Aires, Argentina"
exp_4_keypoints = [
                "Cash-flow and finance audit of IBRD-loan WASH project (Arroyo Vega Drainage Tunnel, $145MM USD).",
                "Elaboration of bidding documentation in accordance to IBRD norms and recommendations."
                ]

# Education info

edu_1_title = "Master of Science MSc., Ecohydrology (Part-time)"
edu_1_place = "Universidad Nacional de la Plata (UNLP)"
edu_1_grad_date = "Thesis pending, Expected Graduation Date: 2022"

edu_2_title = "Master of Engineering - MEng, Civil Engineer"
edu_2_place = "Universidad de Buenos Aires (UBA)"
edu_2_grad_date = "Graduated 2018"


# Projects info

proj_1_title = "Test elaboration on Pandas to evaluate candidates for different roles"
proj_1_link = "https://www.testgorilla.com/test-library/programming-skills-tests/pandas-test/"
proj_1_keypoints = [
                "Created 50 scenario-based questions on Pandas, designed to test the situational judgement of the candidates. Reviewed and corrected 50+ previous questions made by another expert." 
                ]

proj_2_title = "EDA on Argentine lakes and reservoirs dataset"
proj_2_link = "ajossorioarana.github.io"
proj_2_keypoints = [
                "Obtained Carlson's trophic state index (TSI) for waterbodies in dataset of Argentine lakes and reservoirs. Analyzed differences between natural and man-made waterbodies and the role of latitude and depth in eutrophication. Used Python and Seaborn library to analyze and present the results."
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

write_header("ABOUT ME", width, h_cells)
pdf.ln(1)
pdf.set_font("Ubuntu Light", "", 9)
pdf.write(h=h_cells, txt=description)
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
write_project(proj_1_title, proj_1_keypoints, proj_1_link, width, h_cells)
write_project(proj_2_title, proj_2_keypoints, proj_2_link, width, h_cells)


# Footnote

pdf.set_text_color(100, 100, 100)
pdf.set_font("Ubuntu Light", "I", 7)
pdf.set_xy(x=10, y=285)
pdf.write(h=h_cells - 2, txt=footnote, link=github)


# Export as PDF

pdf.output("Ossorio_Arturo_Resume.pdf", "F")