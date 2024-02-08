import time, random, datetime
import os, csv 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import url as site

url = site

max_quant = 50

date= datetime.date.today().strftime('%d-%m-%Y')

csv_file_name1 = 'totaljobsA - ' + date + '.csv'
csv_file_name2 = 'totaljobsB - ' + date + '.csv'
directory_path = 'data'
csv_file_path1 = os.path.join(directory_path, csv_file_name1)
csv_file_path2 = os.path.join(directory_path, csv_file_name2)

list_of_jobs = []

def pause(a, b):
    time.sleep(random.uniform(a, b))
    pass

def save_dict_to_csv(data):

    file_exists = os.path.exists(csv_file_path1)

    with open(csv_file_path1, 'a', newline='', encoding='utf-8') as csvfile:
        # Define CSV header
        fieldnames = list(data.keys())#  ['title', 'salary', 'recruiter', 'date', 'href', 'job desc', 'scrape date']
        
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter='|')

        if not file_exists:
            writer.writeheader()

        # Write header
        writer.writerow(data)


def scrape_jobs(driver):

    # set up while loop
    # find job card
    # check to see if the job is the last on the current page
    # move to next job
    pause(5,10)

    job_match_quant = (WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'span.res-vurnku.at-facet-header-total-results')))
    ).text

    job_match_quant = int(job_match_quant)

    if job_match_quant << max_quant:
        num = job_match_quant
    else:
        num = max_quant

    print(f'{num} jobs')

    while True:
        job_cards = driver.find_elements(By.CLASS_NAME, "res-vxbpca")

        if len(job_cards) >= num:
            break

        pause(5,11.4)

        try:
            next_page_button = driver.find_elements(By.CLASS_NAME, "res-1xvjmp2")
            next_page_button.click()
            pause(2,7)
            next_pg_job_cards = driver.find_elements(By.CLASS_NAME, "res-vxbpca")

            job_cards.append(next_pg_job_cards)
        except:
            break

    

    for job in job_cards:
        # find the web link element
        a_tag = job.find_element(By.CLASS_NAME, 'res-1taea5l')

        # Extract the href attribute
        href_value = a_tag.get_attribute('href')

        job_data = {'href': href_value}

        list_of_jobs.append(job_data)
        


        # 2 for loops
        # 1st loop to get all href tags which includes try and except for next page element and put in a list
        # 2nd loop loop through each href to perform scrape

    # for index, job in enumerate(list_of_jobs, start = 1):
    for job in list_of_jobs:   
            link = job['href']
            driver.get(link)
            pause(6,15)
        
            try:
                title = driver.find_element(By.ID, "job-title")
            except: 
                input('check IP')
                continue

            # Get the text within the element
            title = title.text

            try:    
                salary = driver.find_element(By.CLASS_NAME, "salary")
                salary = salary.text
            except Exception as error:
                print(f"An error occurred: {str(error)}")
                salary = None

            recruiter = driver.find_element(By.ID, "companyJobsLink")

            post_date = driver.find_element(By.CLASS_NAME, "date-posted")

            job_desc = driver.find_element(By.CLASS_NAME, "job-description")



            job = {
                'title': f'\n \n TITLE: {title}',
                'salary': f'\n \n SALARY: {salary}',
                'recruiter': f'\n \n RECRUITER: {recruiter.text}',
                'postdate': f'\n \n DATE: {post_date.text}',
                'href': f'\n \n LINK: {link}',
                'job desc': f'\n \n JOB DESC: {job_desc.text}',
                'scrape date': f'\n \n sSCRAPE DATE: {date}'
            }
            
            try:
                save_dict_to_csv(job)
            except Exception as e:
                print(f"An error occurred: {e}")


            print(title)   
            if salary:  
                print(salary)
            print(recruiter.text)
            print(post_date.text)
            print(job_desc.text)
            print('\n')
            pause(5,16)

    print('\nScript complete')
    pause(1,4)

def final_save_to_csv():

    file_exists = os.path.exists(csv_file_path2)

    with open(csv_file_path1, 'a', newline='', encoding='utf-8') as csvfile:
        
        writer = csv.DictWriter(csvfile, delimiter='|')

        if not file_exists:
            writer.writeheader()

        # Write header
        writer.writerow(list_of_jobs)
 
if __name__ == "__main__":
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    driver = webdriver.Chrome(options=chrome_options)
   
    driver.get(url)

    input('remove pop ups')

    scrape_jobs(driver)
    # set up loop for when the next page needs to be clicked onto

    driver.quit()

    final_save_to_csv()