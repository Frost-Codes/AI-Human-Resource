import os
from dotenv import load_dotenv
from groq import Groq
from pypdf import PdfReader
from .models import Job


load_dotenv()


def get_text(pdf):
    pdf_reader = PdfReader(pdf)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text


def get_data(job, cv_path):
    resume = get_text(cv_path)
    responsibilities = ''.join(job.responsibilities.split('\n'))
    qualifications = ''.join(job.qualifications.split('\n'))

    data = {'resume': resume, 'responsibilities': responsibilities, 'qualifications': qualifications}

    return data


def consult_ai(job, cv_path):
    data = get_data(job=job, cv_path=cv_path)
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

    data = ''

    for chunk in completion:
        try:
            data += chunk.choices[0].delta.content
        except Exception as e:
            pass

    return data



