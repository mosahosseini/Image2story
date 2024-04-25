# Image2story
Image2Story is an innovative application designed to transform your images into captivating audio narratives. By leveraging cutting-edge technology, it converts visual content into engaging stories, adding a new dimension to your media experience.
<p align="center">
  <img src="demo.png" width="350" title="Demo of the app"> </p>

## Getting Started 
To utilize Image2Story effectively, follow these simple steps:

1. **Clone the repository**: Begin by cloning the Image2Story repository to your local machine.
2. **Create a Conda Environment:** If you're not familiar with managing conda environments, refer to the [Conda documentation](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#activating-an-environment) for instructions on creating a new environment.

3. **Activate the Environment:** Activate the conda environment you just created using the following command:

```javascript
conda activate <your_env>
```

4. **Navigate to the Directory:** Change your working directory to where the Image2Story files are located:

```javascript
cd path/to/directory
```

5. **Install Required Modules:** Install the necessary Python modules specified in the `requirements.txt` file:

```javascript
pip install -r requirements.txt
```
6. **Download Mistral Model:** Download the `mistral-7b-instruct-v0.1.Q4_0.gguf` model file from  [the Hugging Face Model Hub](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF/tree/main) and place it in the same directory as your Image2Story files.
  
9. **Launch the Application:** In your Anaconda prompt or terminal, execute the following command:

```javascript
streamlit run app.py
```

This command will initiate the Streamlit application, opening it in your default web browser.

Experience the magic of Image2Story as it transforms your images into immersive audio narratives, enriching your multimedia experience like never before.


