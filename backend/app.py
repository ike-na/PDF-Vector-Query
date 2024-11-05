from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import os
from src.initialize import initialize
import shutil

app = Flask(__name__)
CORS(app)
global rag_chain

embeddings_dir = os.path.join(os.getcwd(), 'embeddings')
if not os.path.exists(embeddings_dir):
    os.makedirs(embeddings_dir)

@app.route('/upload', methods=['POST'])
@cross_origin(origins='http://localhost:3000') 
def upload_file():
    global rag_chain
    try:
        if 'pdf' not in request.files:
            return jsonify({'error': 'No file part'}), 400
        file = request.files['pdf']
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400
        file_path = os.path.join(embeddings_dir, file.filename) 
        file.save(file_path)
        rag_chain = initialize(file_path)
        return jsonify({'message': 'File uploaded and embedded successfully.'}), 200
    except Exception as e:
        print(f"Error during upload: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/ask', methods=['POST'])
def ask_question():
    global rag_chain
    data = request.json
    question = data.get('question', '')
    if not question:
        return jsonify({"error": "Question not provided"}), 400
    try:
        if rag_chain is None:
            raise ValueError("RAG chain is not initialized. Please upload a PDF first.")
        result = rag_chain.invoke({"question": question})
        return jsonify({"answer": result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/api/clear-databases', methods=['DELETE'])
def delete_databases():
    try:
        folders = ['chroma_vector_db', 'embeddings']
        for folder in folders:
            folder_path = os.path.join(os.getcwd(), folder)
            if os.path.exists(folder_path):
                for item in os.listdir(folder_path):
                    item_path = os.path.join(folder_path, item)
                    if os.path.isfile(item_path) or os.path.islink(item_path):
                        os.unlink(item_path)
                    elif os.path.isdir(item_path):
                        shutil.rmtree(item_path) 

        return jsonify({'message': 'Databases cleared successfully.'}), 200
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

if __name__ == '__main__':
    app.run(debug=True)