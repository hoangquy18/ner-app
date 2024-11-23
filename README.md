# Exercise 1 - Named Entity Recognition
I have provided the URL to view the live demo results: http://44.202.255.40:8080/

https://github.com/user-attachments/assets/a53556b9-1fbc-4c3a-bbe4-b08535664dc4


## Project Structure

```
├── output
│   ├── model-best    # model weights
├── train
│   ├── annotate.ipynb         # convert pdf to text file and create train_data
│   ├── train_model.ipynb      # train model
├── inference.ipynb            # for inference
├── app.py            # ui for demo
├── Exercise 1-Named Entity Recognition.pdf  # report
```
## How to run

Create virtual environment
```
conda create -n ner-app python=3.10.13 anaconda
conda activate ner-app
```
Install requirements
```
pip install -r requirements.txt
```
Run demo
```
streamlit run app.py --server.port 8080
```
