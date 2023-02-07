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
role = "Ecohydrologist | Data Scientist"
city = "San Martín de los Andes"
prov_country = "Neuquén, Argentina"
mail = "arturoa91@gmail.com"
cellphone = "+54 9 113 636 8323"
linkedin = "linkedin.com/in/ajossorioarana"
#github = "github.com/ajossorioarana"
website = "ajossorioarana.github.io"

description = "I love building things, tinkering with new tools, and learning new concepts. I find the process of dissecting a problem, analyzing the different components and evaluate possible solutions (with its trade-offs) extremely stimulating, especially when tackling complex, cross-functional problems with tangible outcomes.\nLooking for new challenges within the data spectrum. Particularly interested in the intersection between data science and ecohydrology or freshwater issues."

# Experience info
exp_1_role = "Python Programmer | Data Analyst"
exp_1_company = "HK Analytics"
exp_1_company_link = "https://hkanalytics.io/"
exp_1_period = "Jun. 2022 - Present"
exp_1_place = "Freelancer (through Upwork)"
exp_1_keypoints = [
                "Consistently delivered limnological reports of client's water bodies, preventively identifying negative trends in key water quality parameters and evaluating possible solutions",
                "Revamped reporting process, decreasing total delivery time by 45% while decreasing errors.",
                "Performed analysis on water data, identifying regional and seasonal differences in key variables as well as potential correlation between lake, watershed and limnological parameters."
                ]

exp_2_role = "Limnologist | Data Analyst"
exp_2_company = "EcoAqua"
exp_2_company_link = "https://ecoaqua.com.ar/"
exp_2_period = "Mar. 2021 - Present"
exp_2_place = "Argentina (Remote)"
exp_2_keypoints = [
                "Consistently delivered limnological reports of client's water bodies, preventively identifying negative trends in key water quality parameters and evaluating possible solutions",
                "Revamped reporting process, decreasing total delivery time by 45% while decreasing errors.",
                "Performed analysis on water data, identifying regional and seasonal differences in key variables as well as potential correlation between lake, watershed and limnological parameters."
                ]

exp_3_role = "Biology Project Manager"
exp_3_company = "EcoAqua"
exp_3_company_link = "https://ecoaqua.com.ar/"
exp_3_period = "Feb. 2020 - Feb. 2021"
exp_3_place = "Buenos Aires, Argentina"
exp_3_keypoints = [
                "Diagnosed and treated for algae, submersed, floating and shoreline weeds and any other unwanted vegetation and water quality issues.",
                "Implemented new budgeting process based on limnological and operational factors, increasing revenue by 27%.",
                "Developed new workflow for solving customer's complaints, improving client retention rate by 30%, ensuring response of every request on time."
                ]

exp_4_role = "Aquatic Specialist"
exp_4_company = "EcoAqua"
exp_4_company_link = "https://ecoaqua.com.ar/"
exp_4_period = "Jun. 2017 - Jan. 2020"
exp_4_place = "Buenos Aires, Argentina"
exp_4_keypoints = [
                "Managed five 2-people teams guaranteeing all services were completed on schedule. Devised and executed monthly and weekly schedules.",
                "Maintained 500+ acres of customer's lakes, providing superior quality service, fullfilling of all customer needs leading to 42% complaint reduction.",
                "Formulated and standardized maintenance routine for vehicles, machinery and tools, decreasing workflow interruptions by 60%."
                ]

exp_5_role = 'Graduate Teaching Assistant (Applied Hydraulics)'
exp_5_company = "UBA"
exp_5_company_link = "https://fi.uba.ar/"
exp_5_period = "Aug. 2017 - Aug. 2022"
exp_5_place = "Buenos Aires, Argentina"
exp_5_keypoints = [
                "Assigned to 100+ students, answering queries and grading assignments. Rated as \"Very helpful\" or \"Excellent\" by 96% of students.",
                "Aided professors in examinations and course administration. Gave several practical lectures, developing new material for grasping difficult concepts.",
                "Syllabus: Pressurized pipe flow, pump selection, water hammer, open channel flow, weir and culvert design."
                ]

# Education info
edu_1_title = "MSc., Ecohydrology (Part-time)"
edu_1_place = "Universidad Nacional de la Plata (UNLP)"
edu_1_grad_date = "Thesis pending\nExpected Graduation Date: 2023"

edu_2_title = "BEng. + MEng, Civil Engineer"
edu_2_place = "Universidad de Buenos Aires (UBA)"
edu_2_grad_date = "Graduated 2018"


# Projects info
proj_1_title = "Test Elaboration on Pandas to Evaluate Candidates for Different Roles"
proj_1_link = "https://www.testgorilla.com/test-library/programming-skills-tests/pandas-test/"
proj_1_keypoints = [
                "Created 50 scenario-based questions on Pandas, designed to test the situational judgement of the candidates. Reviewed and corrected 50+ previous questions made by another expert." 
                ]

proj_2_title = "EDA on Argentine Lakes and Reservoirs dataset"
proj_2_link = ""
proj_2_keypoints = [
                "Obtained Carlson's trophic state index (TSI) for waterbodies in dataset of Argentine lakes and reservoirs. Analyzed differences between natural and man-made waterbodies and the role of latitude and depth in eutrophication."
                ]

proj_3_title = "Python-Generated Resume"
proj_3_link = "github.com/ajossorioarana/AJOA_resume"
proj_3_keypoints = [
                "Using FPDF library, created the present resume entirely with Python."
                ]

# Skills info
skills_1_title = "Python"
skills_1_description = "pandas, numpy, scikit-learn, geopandas, request, matplotlib, seaborn"

skills_2_title = "Data-related tools"
skills_2_description = "Git, SQL, PostgreSQL"

skills_3_title = "GIS and Remote Sensing"
skills_3_description = "QGIS, Vector & Raster Data, DEM, Watershed Delineation"

skills_4_title = "Maths"
skills_4_description = "Probability, Statistics, Combinatorics, Linear Algebra, Calculus"

skills_5_title = "Ecohydrology & Freshwater Ecosystems"
skills_5_description = "Water Balance, Hydrograms, Eutrophication, Nutrient Budgeting, Lake Management"

# Other activities
activities_description = "Fly Fishing, Amateur Radio, Reading, Cooking, Traditional Folk Music, Guitar, Soccer, Skiing"
        
# Creates an instance of FPDF class and sets its title and author
pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_title('Resume AJOA')
pdf.set_author('Arturo J. Ossorio Arana')

# Adds fonts relevant to the document
pdf.add_font("Ubuntu Light", "", r"C:\Windows\Fonts\Ubuntu-L.ttf", uni=True)
pdf.add_font("Ubuntu Light", "I", r"C:\Windows\Fonts\Ubuntu-LI.ttf", uni=True)
pdf.add_font("Ubuntu Medium", "", r"C:\Windows\Fonts\Ubuntu-M.ttf", uni=True)
pdf.add_font("Ubuntu Bold", "", r"C:\Windows\Fonts\Ubuntu-B.ttf", uni=True)

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
#pdf.write(h=h_cells, txt=website, link=website)
#pdf.write(h=h_cells, txt=(" "*3 + "|" + " "*3))
pdf.write(h=h_cells, txt=linkedin, link=linkedin)
pdf.write(h=h_cells, txt=(" "*3 + "|" + " "*3))
pdf.write(h=h_cells, txt=cellphone)
pdf.ln(10)

ybefore = pdf.get_y() # Save the top coordinate of the columns

# DESCRIPTION
write_header("ABOUT ME", col1_width, h_cells)
pdf.ln(1)
pdf.set_font("Ubuntu Light", "", 9)
pdf.multi_cell(w=col1_width, h=h_cells, txt=description, align='L')
pdf.ln(5)

# EDUCATION
write_header("EDUCATION", col1_width, h_cells)
write_education(edu_1_title, edu_1_place, edu_1_grad_date, col1_width, h_cells)
write_education(edu_2_title, edu_2_place, edu_2_grad_date, col1_width, h_cells)

# SKILLS
write_header("SKILLS", col1_width, h_cells)
write_skills(skills_1_title, skills_1_description, col1_width, h_cells)
write_skills(skills_2_title, skills_2_description, col1_width, h_cells)
write_skills(skills_3_title, skills_3_description, col1_width, h_cells)
write_skills(skills_4_title, skills_4_description, col1_width, h_cells)
write_skills(skills_5_title, skills_5_description, col1_width, h_cells)
pdf.ln(3)

# ACTIVITIES
write_header("OTHER ACTIVITIES", col1_width, h_cells)
write_activities(activities_description, col1_width, h_cells)

pdf.set_xy(x=col2_start, y=ybefore)

# EXPERIENCE
write_header("EXPERIENCE", col2_width, h_cells)
write_exp(exp_1_company, exp_1_role, exp_1_company_link, exp_1_period, exp_1_place, exp_1_keypoints, col2_width, h_cells, col2_start)
write_exp(exp_2_company, exp_2_role, exp_2_company_link, exp_2_period, exp_2_place, exp_2_keypoints, col2_width, h_cells, col2_start)
write_exp(exp_3_company, exp_3_role, exp_3_company_link, exp_3_period, exp_3_place, exp_3_keypoints, col2_width, h_cells, col2_start)
write_exp(exp_4_company, exp_4_role, exp_4_company_link, exp_4_period, exp_4_place, exp_4_keypoints, col2_width, h_cells, col2_start)
pdf.ln(1)
# PROJECTS 
pdf.set_x(col2_start)
write_header("PROJECTS/PUBLICATIONS", col2_width, h_cells)
write_project(proj_1_title, proj_1_keypoints, proj_1_link, col2_width, h_cells, col2_start)
write_project(proj_2_title, proj_2_keypoints, proj_2_link, col2_width, h_cells, col2_start)
write_project(proj_3_title, proj_3_keypoints, proj_3_link, col2_width, h_cells, col2_start)


# Write line that separates columns
pdf.set_draw_color(95, 130, 235)
x_line = col2_start - 0.5 * col_sep
y_line = ybefore - h_cells*0.5
pdf.line(x1=pdf.l_margin, y1=y_line, x2=(ef_page_width + pdf.r_margin), y2=y_line)
pdf.line(x1=x_line, y1=y_line, x2=x_line, y2=(pdf.h - pdf.b_margin))

# Export as PDF
pdf.output("Ossorio-Arturo_Resume.pdf", "F")