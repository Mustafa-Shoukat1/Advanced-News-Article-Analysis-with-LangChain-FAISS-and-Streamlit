
# NewsBot: News Research Tool 📈📰🌐📊🔍

![NewsBot](https://corover.ai/wp-content/uploads/2021/10/news_bot-1280x1005.png) 



<div style="position: relative; text-align: center; background-image: url('https://th.bing.com/th/id/OIP.FhY2jL9E3OtyWAmmT_fFaAHaDt?w=341&h=175&c=7&r=0&o=5&dpr=1.5&pid=1.7'); background-size: cover; background-position: center; border-radius: 20px; border: 2px solid #64B5F6; padding: 15px; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.4), 0px 6px 20px rgba(0, 0, 0, 0.19); transform: perspective(1000px) rotateX(5deg) rotateY(-5deg); transition: transform 0.5s ease-in-out;">
    <div style="position: relative; z-index: 1; background-color: rgba(255, 255, 255, 0.9); backdrop-filter: blur(10px); border-radius: 20px; padding: 20px;">
        <h1 style="color: red; text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.4); font-weight: bold; margin-bottom: 10px; font-size: 32px;">Welcome!</h1>
        <p style="color: #1976D2; font-size: 18px; margin: 10px 0;">
            I'm Mustafa Shoukat, a Generative Expert. I'm exploring various concepts of LangChain and techniques to enhance my skills. 
        </p>
        <p style="color: #000000; font-size: 16px; font-style: italic; margin: 10px 0;">
            "I am just a humble data practitioner. I make mistakes and I have blind spots. If you notice things I can improve or if you just want to chat, please feel free to DM me or connect :)"
        </p>
        <p style="color: #2980B9; font-size: 16px; font-style: italic; margin: 10px 0;">
            <strong>About Notebook:</strong> 🧠 Integrating LangChain with HuggingFace and FAISS for Advanced NLP Applications
        </p>
        <p style="color: #27AE60; font-size: 16px; font-style: italic; margin: 10px 0;">
            This notebook explores building a Newsbot with LangChain. It covers data preprocessing, chat model creation, document retrieval with FAISS, and question answering. Through practical examples, you'll learn to integrate these components into a context-aware chatbot system, providing a streamlined guide to developing advanced NLP applications.
        </p>
        <h2 style="color: red; margin-top: 15px; font-size: 28px;">Contact Information</h2>
        <table style="width: 100%; margin-top: 15px; border-collapse: collapse;">
            <tr style="background-color: #64B5F6; color: #ffffff;">
                <th style="padding: 8px; border-bottom: 2px solid #000000;">Name</th>
                <th style="padding: 8px; border-bottom: 2px solid #000000;">Email</th>
                <th style="padding: 8px; border-bottom: 2px solid #000000;">LinkedIn</th>
                <th style="padding: 8px; border-bottom: 2px solid #000000;">GitHub</th>
                <th style="padding: 8px; border-bottom: 2px solid #000000;">Kaggle</th>
            </tr>
            <tr style="background-color: #FFFFFF; color: #000000;">
                <td style="padding: 8px;">Mustafa Shoukat</td>
                <td style="padding: 8px;">mustafashoukat.ai@gmail.com</td>
                <td style="padding: 8px;">
                    <a href="https://www.linkedin.com/in/mustafashoukat/" target="_blank">
                        <img src="https://img.shields.io/badge/LinkedIn-0e76a8.svg?style=for-the-badge&logo=LinkedIn&logoColor=white" alt="LinkedIn Badge" style="border-radius: 5px; width: 100px;">
                    </a>
                </td>
                <td style="padding: 8px;">
                    <a href="https://github.com/Mustafa-Shoukat1" target="_blank">
                        <img src="https://img.shields.io/badge/GitHub-171515.svg?style=for-the-badge&logo=GitHub&logoColor=white" alt="GitHub Badge" style="border-radius: 5px; width: 100px;">
                    </a>
                </td>
                <td style="padding: 8px;">
                    <a href="https://www.kaggle.com/mustafashoukat" target="_blank">
                        <img src="https://img.shields.io/badge/Kaggle-20beff.svg?style=for-the-badge&logo=Kaggle&logoColor=white" alt="Kaggle Badge" style="border-radius: 5px; width: 100px;">
                    </a>
                </td>
            </tr>
        </table>
    </div>
</div>

<div style="position: relative; text-align: center; background-image: url('https://th.bing.com/th/id/OIP.FhY2jL9E3OtyWAmmT_fFaAHaDt?w=341&h=175&c=7&r=0&o=5&dpr=1.5&pid=1.7'); background-size: cover; background-position: center; border-radius: 20px; border: 2px solid #64B5F6; padding: 15px; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.4), 0px 6px 20px rgba(0, 0, 0, 0.19); transform: perspective(1000px) rotateX(5deg) rotateY(-5deg); transition: transform 0.5s ease-in-out;">
    <div style="position: relative; z-index: 1; background-color: rgba(255, 255, 255, 0.9); backdrop-filter: blur(10px); border-radius: 20px; padding: 20px;">
        <p style="font-size: 16px; color: #000000;">
            Note: Include your API key in the sections where it is required. For instance, you might include your OpenAI API key or LangChain Hugging Face API key in the necessary code cells.
        </p>
    </div>
</div>





**NewsBot** is a web-based tool designed to analyze news articles and provide insights based on the content. Built with Streamlit and LangChain, it allows users to input URLs of news articles, process the content, and retrieve answers to queries along with the sources.

![Analytics](https://images.squarespace-cdn.com/content/v1/55ed989ee4b0c7f115ddc924/1541600620919-VEI2IOYGNT2WJXA2W4A0/analytics.gif)

## Features

- **Process News Articles**: Enter up to 3 URLs of news articles for analysis.
- **Chunk Text and Create Embeddings**: The tool splits the article text into manageable chunks and creates embeddings for effective retrieval.
- **Query-Based Insights**: Ask questions based on the processed articles and receive answers along with the sources.

## Prerequisites

- Python 3.12.0
- Streamlit
- LangChain
- FAISS
- OpenAI (requires an API key)
- Python-dotenv

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-username/newsbot.git
    cd newsbot
    ```

2. **Set Up a Virtual Environment** (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up Environment Variables**:
    Create a `.env` file in the root directory and add your OpenAI API key:
    ```plaintext
    OPENAI_API_KEY=your_openai_api_key
    ```

## Usage

1. **Run the Streamlit App**:
    ```bash
    streamlit run app.py
    ```

2. **Interact with the App**:
    - Open the app in your browser (the URL will be provided in the terminal).
    - Enter up to 3 news article URLs in the sidebar.
    - Click the "Process URLs" button to analyze the articles.
    - Enter your query in the text input field to get insights based on the processed content.

## Files

- `app.py`: The main Streamlit application script.
- `faiss_store_openai.pkl`: The FAISS index file used for storing embeddings (generated after processing URLs).
- `.env`: Environment variables file (do not forget to add your OpenAI API key here).
- `requirements.txt`: Python package dependencies.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes. Make sure to follow the coding standards and write tests for your changes.


## Contact

For any questions or support, please reach out to [Mustafa Shoukat](mailto:mustafashoukat.ai@gmail.com).

---

Feel free to replace `Mustafa-Shoukat1` in the clone URL with your GitHub username and add any additional information relevant to your project.

---

**Note:** Include your API key in the sections where it is required. For instance, you might include your OpenAI API key or LangChain Hugging Face API key in the necessary code cells.

<div style="position: relative; text-align: center; background-color: #f9f9f9; border-radius: 20px; border: 2px solid #64B5F6; padding: 20px; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2), 0px 6px 20px rgba(0, 0, 0, 0.1); margin-top: 20px;">
    <h2 style="color: #27AE60; margin-bottom: 10px; font-size: 24px;">Thank You!</h2>
    <p style="font-size: 16px; color: #000000; margin: 10px 0;">
        Thank you for taking the time to explore this notebook. I hope you find the information and examples useful in your journey to mastering advanced NLP techniques with LangChain, HuggingFace, and FAISS. If you have any questions, feedback, or suggestions, please feel free to reach out.
    </p>
    <p style="font-size: 16px; color: #1976D2; margin: 10px 0;">
        Your support and interest in this project are greatly appreciated. Stay curious and keep learning!
    </p>
    <p style="font-size: 16px; color: #000000;">
        Happy coding!
    </p>
</div>


