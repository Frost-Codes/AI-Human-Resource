from django.test import TestCase
import os
from dotenv import load_dotenv
from groq import Groq
from pypdf import PdfReader
# from .models import Job

load_dotenv()

# Create your tests here.

r = """
Automated AI Modelling:Ability to creatively solve business problems by building AI systems.Ability to Constructively disrupt current business practices using Generative AI (GenAI).Designing and developing scaled (Gen)AI solutions.Show a propensity to collaboratively work with the larger team in the AI tribe to productionize AI algorithms.Being able & willing to stretch yourself to work on other multiple data science projects.Ability to test hypotheses from raw data sets, draw meaningful conclusions, and effectively communicate results verbally, in writing, and through effective visualization Quantify improvements in business areas resulting from the use of algorithms and modelling through A/B testingStatistical & ML Modelling:Demonstrate competency in utilizing advanced statistical and machine learning methods and technologies to deliver best-in-class models to support risk decision making.Developing code and automated processes to manipulate high volume, high dimensional data sources, including alternative data, to extract informative patterns, perform exploratory analyses and engineer useful features.Ability to develop machine learning & deployment of models and algorithms from large volumes of structured and/or unstructured data in a commercial /consumer environment in order solve real business problems, taking account of user needs and technology and operational landscapeIdentifying new analytics trends and opportunities to drive the innovation agenda across business functions Programming Languages and Big Data Technologies: Along with a strong knowledge of Big Data Technologies, the candidate should have:Practical skills in GIT version control.Strong hands-on programming skills in Python. Knowledge of SQL, Hadoop/Hive, Spark, and/or Scala.Proficient in AI libraries in Python (e.g. H2O, SciPy and NLTK, PyTorch etc.) Familiar with leading visualisation tools (e.g. Tableau, Qliksense, QuickSight)Cloud computing, especially AWS Behavioural Competencies:Ability to work cross functional teams to translate business issues into potential analytics solutions Excellent communication skills with the ability to document solutions effectively.An analytical mindset to identify patterns and insights from data and business processes.The ability to collaborate with cross-functional teams to assess business needs and develop AI solutions.A self-driven and creative mindset to apply AI methods to solve real issues.Ability to provide effective leadership and guidance to junior data scientistsA problem-solving aptitude.
"""

q = """
A degree in Statistics, Mathematics, Data Science, Computer Science, or a related field.An MSc in a data science related discipline like Mathematics, Statistics, Computer Scientist or Engineering will be an added advantage.5+ years of experience relevant to this role Proven work experience in advanced Gen (AI) techniques, including prompt engineering, LLM implementation, and agent development, with a fundamental knowledge of inner workings.Experience in cloud technologies, generative AI techniques, will be an added advantage.Significant experience in machine learning & deployment of models and algorithms from large volumes of structured and/or unstructured data in a commercial /consumer environment
"""


def get_text(pdf):
    pdf_reader = PdfReader(pdf)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text


def get_data(cv_path):
    resume = get_text(cv_path)
    responsibilities = ''.join(r.split('\n'))
    qualifications = ''.join(q.split('\n'))

    data = {'resume': resume, 'responsibilities': responsibilities, 'qualifications': qualifications}

    return data


data = get_data(cv_path='../cvs/Ian_CV_DS.pdf')


client = Groq(api_key=os.environ.get('GROQ_API_KEY'))

completion = client.chat.completions.create(
    model="llama3-70b-8192",
    messages=[
        {
            "role": "user",
            "content": f"""Your are an experienced HR assistant. We are shortlisting candidates for job
            in the company. Given a resume, job responsibilities and required qualifications you are supposed to
            rate that resume in a scale of 0 to 100 percent where 0 is lowest score and 100 is highest score.
            This is the resume:  {data['resume']}
            This are the responsibilities: {data['responsibilities']}
            This are the qualifications: {data['qualifications']}
            
            return your response in a python dictionary of format with score and summary as keys
            NOTE: I only need dictionary output i.e respond like an API
            """

        },
        {
            "role": "assistant",
            "content": "Please provide the job posting, and I'll help you build a custom resume tailored to the "
                       "specific requirements and keywords mentioned in the posting.\n\nAlso, please let me know what "
                       "type of resume format you prefer:\n\n1. Chronological ( highlighting work experience in "
                       "reverse chronological order)\n2. Functional (emphasizing skills and qualifications rather "
                       "than work history)\n3. Combination (a mix of chronological and functional formats)\n4. "
                       "Targeted (tailored to a specific job or industry)\n\nAdditionally, please provide me with the "
                       "following information:\n\n* Your current resume (if you have one)\n* Your relevant work "
                       "experience, education, and skills\n* Any specific achievements, certifications, "
                       "or awards you'd like to highlight\n* Your preferred tone for the resume (e.g., formal, "
                       "conversational, humorous)\n\nOnce I have this information, I'll create a custom resume that "
                       "showcases your strengths and increases your chances of getting noticed by the hiring manager."
        }
    ],
    temperature=1,
    max_tokens=1024,
    top_p=1,
    stream=True,
    stop=None,
)

for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")

