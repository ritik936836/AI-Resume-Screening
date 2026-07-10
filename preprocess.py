import re

def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9 ]', '', text)
    text = " ".join(text.split())
    return text


if __name__ == "__main__":
    sample = """
    Name: John Doe
    Skills: Python, AI, Machine Learning!!!
    """
    
    print(preprocess(sample))