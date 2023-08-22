from fpdf import FPDF

def write_header(header_title: str, width: int, height: int):
        pdf.set_font("Ubuntu Bold", "", 13)
        pdf.set_text_color(0, 0, 0)
        pdf.set_draw_color(95, 130, 235)
        pdf.cell(w=width, h = height, txt=header_title, border='B', fill=False, ln=0)
        pdf.ln(7)

def write_company(company: str, link: str, place: str, width: int, height: int, x: float):
        pdf.set_font("Ubuntu Medium", "", 11)
        pdf.set_text_color(0, 25, 100)
        pdf.set_x(x)
        pdf.cell(w=width, h=height, txt=f"{company} ({place})", link=link)
        pdf.ln(5)

def write_exp(role: str, period: str, keypoints: list, width: int, height: int, x: float, indent: float):
        corrected_x = x + indent
        corrected_width = width - indent
        pdf.set_text_color(0, 0, 0)
        pdf.set_font("Ubuntu Medium", "", 9)
        pdf.set_x(corrected_x)
        pdf.cell(w=corrected_width, h=height, txt=f"{role} ({period})")
        pdf.ln(5)
        pdf.set_font("Ubuntu Light", "", 8)
        for keypoint in keypoints:
                pdf.set_x(corrected_x)
                pdf.multi_cell(w=corrected_width, h=height, txt=f"• {keypoint}")
        pdf.ln(2)

def write_education(title: str, university: str, location: str, grad_date: str, width: int, height: int):
        pdf.set_font("Ubuntu Medium", "", 10)
        pdf.set_text_color(0, 25, 100)
        pdf.cell(w=width, h=height, txt=university)
        pdf.ln(5)
        pdf.set_text_color(0, 0, 0)
        pdf.set_font("Ubuntu Medium", "", 9)
        pdf.multi_cell(w=width, h=height, txt=title)
        pdf.set_font(family="Ubuntu Light", style="", size=8)
        pdf.multi_cell(w=width, h=height, txt=location)
        pdf.multi_cell(w=width, h=height, txt=grad_date)
        pdf.ln(3)

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
role = "Data Scientist | Ecohydrologist"
location = "San Martín de los Andes, Patagonia, Argentina"
mail = "arturoa91@gmail.com"
linkedin = "linkedin.com/in/ajossorioarana"
github = "github.com/ajossorioarana"
website = "ajossorioarana.github.io"

description = "I am a hands-on professional who enjoys turning data into solutions. I take ownership of projects, driving them forward, and quickly learn new skills when needed.\nMy interest lies in the connection between data science and environmental concerns like freshwater ecosystems, soil moisture dynamics, sustainable drainage, and agriculture."

# Experience info
exp_1_role = "Python Programmer | Data Scientist"
exp_1_company = "HK Analytics"
exp_1_company_link = "https://hkanalytics.io/"
exp_1_period = "Jun-2022 - Aug-2023"
exp_1_place = "Remote, US Based"
exp_1_keypoints = [
                "Collaborated remotely with a two-member team to develop Python code for solar plant data analysis, contributing to feature enhancement, debugging, and documentation.",
                "Ensured high-quality codebase by adhering to documentation standards and producing clear, concise, and organized technical documentation.",
                "Contributed effectively in technical video meetings, presenting findings and solutions to obstacles, communicating complex concepts to both technical and non-technical stakeholders.",
                "Took initiative in structuring tasks and addressing challenges independently, with a high degree of autonomy and effective decision-making.",
                "Contract ended due to exhaustion of company funds designated for non-founder contributors."
                ]

exp_2_role = "Limnologist | Data Analyst"
exp_2_company = "EcoAqua"
exp_2_company_link = "https://ecoaqua.com.ar/"
exp_2_period = "Mar-2021 - Present"
exp_2_place = "Argentina (Remote) - Part-Time"
exp_2_keypoints = [
                "Consistently delivered limnological reports of client's water bodies, preventively identifying negative trends in key water quality parameters and evaluating possible solutions.",
                "Revamped reporting process, decreasing total delivery time by 45% while decreasing errors.",
                "Performed analysis on water data, identifying regional and seasonal differences in key variables as well as potential correlation between lake, watershed and limnological parameters."
                ]

exp_3_role = "Biology Project Manager"
exp_3_company = "EcoAqua"
exp_3_company_link = "https://ecoaqua.com.ar/"
exp_3_period = "Feb-2020 - Feb-2021"
exp_3_place = "Buenos Aires, Argentina"
exp_3_keypoints = [
                "Diagnosed and treated for harmful algal blooms, submersed, floating and shoreline weeds and any other unwanted vegetation and water quality issues.",
                "Implemented a new budgeting process based on limnological and operational factors, increasing revenue by 27% and standardizing the procedure for future employees.",
                "Developed new workflow for managing and solving customer's complaints, improving client retention rate by 30%, ensuring response of every request on time."
                ]

exp_4_role = "Aquatic Specialist"
exp_4_company = "EcoAqua"
exp_4_company_link = "https://ecoaqua.com.ar/"
exp_4_period = "Jun-2017 - Jan-2020"
exp_4_place = "Buenos Aires, Argentina"
exp_4_keypoints = [
                "Managed five 2-person teams, guaranteeing all services were completed on schedule, creating and executing monthly and weekly schedules, and taking care of urgent tasks that came up.",
                "Maintained 500+ acres of customer's lakes, providing superior quality service, fullfilling of all customer needs leading to 42% complaint reduction.",
                "Formulated and standardized maintenance routine for vehicles, machinery and tools, decreasing workflow interruptions due to equipement break down by 60%."
                ]

exp_5_role = 'Graduate Teaching Assistant (Applied Hydraulics)'
exp_5_company = "UBA"
exp_5_company_link = "https://fi.uba.ar/"
exp_5_period = "Aug-2017 - Aug-2022"
exp_5_place = "Buenos Aires, Argentina"
exp_5_keypoints = [
                "Assigned to 100+ students, answering queries and grading assignments. Rated as \"Very helpful\" or \"Excellent\" by 96% of students.",
                "Aided professors in examinations and course administration. Gave several practical lectures, developing new material for grasping difficult concepts.",
                "Syllabus: Pressurized pipe flow, pump selection, water hammer, open channel flow, weir and culvert design."
                ]

# Education info
edu_1_title = "M.Sc. in Ecohydrology"
edu_1_university = "Universidad Nacional de la Plata"
edu_1_location = "La Plata, Argentina"
edu_1_grad_date = "2020 (Thesis pending)"

edu_2_title = "B.Eng. + M.Eng, Civil Engineering"
edu_2_university = "Universidad de Buenos Aires"
edu_2_location = "Buenos Aires, Argentina"
edu_2_grad_date = "2018"


# Projects info
proj_1_title = "Analysis of Trophic State of Argentinian Lakes and Reservoirs"
proj_1_link = "https://ajossorioarana.github.io/projects/arg_lakes/"
proj_1_keypoints = [
                "Analyzed trophic states in Argentine lakes and reservoirs using data analysis and visualizations, revealing eutrophication patterns with Carlson's Trophic State Index (TSI)."
                ]

proj_2_title = "EDA in Amateur Radio Licenses Numbers Across Argentina"
proj_2_link = "https://ajossorioarana.github.io/projects/ham_eda/"
proj_2_keypoints = [
                "Independently analyzed amateur radio license distribution in Argentina, utilizing data visualizations to reveal regional trends and potential contributing variables."
                ]

proj_3_title = "Test Elaboration on Pandas to Evaluate Candidates for Different Roles"
proj_3_link = "https://www.testgorilla.com/test-library/programming-skills-tests/pandas-test/"
proj_3_keypoints = [
                "Created 50 scenario-based questions for testing the situational judgement of candidates."
                ]

proj_4_title = "Python-Generated Resume"
proj_4_link = "github.com/ajossorioarana/AJOA_resume"
proj_4_keypoints = [
                "Using FPDF library, created the present resume entirely with Python."
                ]

# Skills info
skills_1_title = "Technical and Data"
skills_1_description = "Python (pandas, numpy, scipy, scikit-learn, polars, xarray, dask), Data Visualization (Plotly, Matplotlib, Seaborn), Virtual Environment, Version Control (Git, GitHub, GitLab), Data Cleaning, SQL, PostgreSQL, Linear Algebra, Calculus, Probability, Statistics"

skills_2_title = "GIS and Ecohydrology"
skills_2_description = "QGIS, Vector and raster data, DEM, Watershed delineation, Water cycle, Water balance, Hydrograms, Eutrophication, Lake management"

skills_3_title = "Soft skills"
skills_3_description = "Problem-solving, Project Ownership, Work Autonomy, Communication, Collaboration"

skills_4_title = "Languages"
skills_4_description = "Spanish (Native), English (Fluent)"

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
pdf.write(h=h_cells, txt=location)
pdf.write(h=h_cells, txt=(" "*3 + "|" + " "*3))
pdf.write(h=h_cells, txt=mail, link=mail)
pdf.write(h=h_cells, txt=(" "*3 + "|" + " "*3))
pdf.write(h=h_cells, txt=website, link=website)
pdf.write(h=h_cells, txt=(" "*3 + "|" + " "*3))
pdf.write(h=h_cells, txt=linkedin, link=linkedin)
pdf.ln(10)

ybefore = pdf.get_y() # Save the top coordinate of the columns

# DESCRIPTION
write_header("ABOUT ME", col1_width, h_cells)
pdf.ln(1)
pdf.set_font("Ubuntu Light", "", 9)
pdf.multi_cell(w=col1_width, h=h_cells, txt=description, align='L')
pdf.ln(4)

# EDUCATION
write_header("EDUCATION", col1_width, h_cells)
write_education(edu_1_title, edu_1_university, edu_1_location, edu_1_grad_date, col1_width, h_cells)
write_education(edu_2_title, edu_2_university, edu_2_location, edu_2_grad_date, col1_width, h_cells)

# SKILLS
write_header("SKILLS & TOOLS", col1_width, h_cells)
write_skills(skills_1_title, skills_1_description, col1_width, h_cells)
write_skills(skills_2_title, skills_2_description, col1_width, h_cells)
write_skills(skills_3_title, skills_3_description, col1_width, h_cells)
write_skills(skills_4_title, skills_4_description, col1_width, h_cells)
#write_skills(skills_5_title, skills_5_description, col1_width, h_cells)
pdf.ln(3)

# ACTIVITIES
write_header("PERSONAL INTERESTS", col1_width, h_cells)
write_activities(activities_description, col1_width, h_cells)

pdf.set_xy(x=col2_start, y=ybefore)

# EXPERIENCE
write_header("EXPERIENCE", col2_width, h_cells)
pdf.ln(1)
write_company(exp_1_company, exp_1_company_link, exp_1_place, col2_width, h_cells, col2_start)
write_exp(exp_1_role, exp_1_period, exp_1_keypoints, col2_width, h_cells, col2_start, indent=3)
write_company(exp_3_company, exp_3_company_link, exp_3_place, col2_width, h_cells, col2_start)
write_exp(exp_2_role, exp_2_period, exp_2_keypoints, col2_width, h_cells, col2_start, indent=3)
write_exp(exp_3_role, exp_3_period, exp_3_keypoints, col2_width, h_cells, col2_start, indent=3)
write_exp(exp_4_role, exp_4_period, exp_4_keypoints, col2_width, h_cells, col2_start, indent=3)
pdf.ln(1)
# PROJECTS 
pdf.set_x(col2_start)
write_header("PROJECTS", col2_width, h_cells)
pdf.ln(1)
write_project(proj_1_title, proj_1_keypoints, proj_1_link, col2_width, h_cells, col2_start)
write_project(proj_2_title, proj_2_keypoints, proj_2_link, col2_width, h_cells, col2_start)
write_project(proj_3_title, proj_3_keypoints, proj_3_link, col2_width, h_cells, col2_start)
#write_project(proj_4_title, proj_4_keypoints, proj_4_link, col2_width, h_cells, col2_start)


# Write line that separates columns
pdf.set_draw_color(95, 130, 235)
x_line = col2_start - 0.5 * col_sep
y_line = ybefore - h_cells*0.5
pdf.line(x1=pdf.l_margin, y1=y_line, x2=(ef_page_width + pdf.r_margin), y2=y_line)
pdf.line(x1=x_line, y1=y_line, x2=x_line, y2=(pdf.h - pdf.b_margin))

# Export as PDF
pdf.output("Ossorio-Arturo_Resume.pdf", "F")