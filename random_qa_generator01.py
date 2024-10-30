

from crewai import Agent, Task, Crew, Process
from langchain_community.tools import tool
import time
from langchain_community.llms import Ollama
from crewlib import show_time

llm = Ollama(model = "gemma2:latest")
# llm = Ollama(model = "mistral:latest")
# llm = Ollama(model='mixtral')   # bellek yetmediği için oldukça yavaş

# Agents
question_generator = Agent(
    role='Question Generator',
    goal='''Belleğinde yer alan bilgileri kullanarak anlamlı Türkçe sorular çıkar. 
    Bu soruların doğru yanıtlarını da üret. 
    Gerektiğinde soruların çeşitliliğini ve zorluğunu artır.
    Kendine dair soru ve yanıt üretme.    
    Her aşamada Türkçe kullan''',
    backstory='''Bilgilendirici ve zihin açıcı sorular oluşturmada uzmansın. 
    Türkçe dilinde soru oluşturma konusunda deneyimli ve yaratıcısın. 
    Sorularının anlamlı ve yararlı olmasına özen gösterirsin. 
    Sorularının doğru yanıtlarının bulunmasını sağlar ve soruların çeşitliliğini ve zorluğunu artırmak için çabalarsın.''',
    verbose=True,
    allow_delegation=False,
    llm=llm    
)

# Tasks

question_generation_task = Task(
    description='''Senin eğitimin için kullanılan bilgilarden Türkçe sorular oluştur. 
    Soruları yalın metin halinde yayınlanacak hale getir.
    Her aşamada Türkçe kullan. İngilizceye çevirme.''',
    agent=question_generator,
    expected_output='''En az 20 Türkçe soru ve cevabı. 
    Her sorunun doğru yanıtını da sağla. 
    Soruların çeşitliliğini ve zorluğunu artır. 
    Soruları düz metin olarak raporlanacak hale getir.
    Sadece soru ve cevapları yaz. Başka bir şey ekleme. Satır numarası ekleme.
    Çıktıları formatlamak için #, * {, } gibi özel işaretler kullanma.
    Sadece soru ve cevap arasına : işareti koy.
    Elde ettiğin sonuçların her satırının aşağıdaki biçime sahip olmasını sağla ve satırları boş satır bırakmadan alt alta yaz:

    {soru}: {cevap}
    {soru}: {cevap}
    {soru}: {cevap}
    {soru}: {cevap}
    '''
)


# Instantiate and run the crew
crew = Crew(
    agents=[question_generator],
    tasks=[question_generation_task],
    verbose=2
)

def main():
    # Execute the crew
    result = crew.kickoff()

    # Combine results
    final_article = f"""
    {question_generation_task.output.exported_output}
    """
    print("--------------------------")

    print(result)

    with open(f"random_qa_generator01_turkce.txt","a") as f:
        print(final_article, file=f)

if __name__ == "__main__":
    t1 = t0 = time.time()
    while True:
        try:
            main()
            time.sleep(5)
        except Exception as e:
            print(e)
            break
        t1 = show_time("main", t1, t0)
    t1 = show_time("main", t1, t0)