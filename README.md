# **Project Objective**

To summarize Cookie Policy in public website (for example Financial website).

Due to Cookie Policy that appear on websites are too long and some users have difficulty to understand.

### Prerequisites

You have to install the python 3.10 or higher version on your machine and run the below command to make sure that your python is installed on your machine.

* check your python version
  ```sh
  python --version
  ```

  or 

  ```sh
  python3 --version
  ```

### Installation

If python is installed on your machine. You are ready to do a following instruction

1. Clone the repo
   ```sh
   git clone https://github.com/nuttapol-kor/Summarize_CookiePolicy.git
   ```

2. Create `.env` in root of the project and enter your open api key. If you not have it yet, your can get the api key in this link -> https://platform.openai.com/
   ```env
   OPENAI_API_KEY='Enter your Open API Key';
   ```

3. Download summarize model -> https://drive.google.com/file/d/1EJJ1Rme8D_ia7efNTr00Nqr41MsTSVvL/view?usp=sharing

4. Make new folder in the root of the project. Folder name `models` and move the downloaded summarize model to new folder.
    ```
    your model will be struct like this -> ./models/e5_1
    ```

5. install the necessary library from `requirements.txt`
    ```bash
    pip install -r requirements.txt
    ```

6. Run the project
    ```bash
    uvicorn main:app --reload
    ```

# **References**

## Finaicial Websites which we use as examples

* https://www.set.or.th/th/cookies-policy

* https://www.tisco.co.th/th/cookies-policy.html

* https://www.scb.co.th/th/personal-banking/cookies-policy.html

* https://www.kgieworld.co.th/corporate/cookies

* https://www.kkpfg.com/th/cookies-policy



## Websites which provide information about Cookie policy

* https://cookieinformation.com/compliance-check/


* https://pdpa.pro/blogs/what-is-cookie-consent-and-why-we-must-have-it
