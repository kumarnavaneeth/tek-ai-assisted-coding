import random
import torch
from transformers import BertTokenizer, BertModel
from sklearn.metrics.pairwise import cosine_similarity

random_seed = 42

random.seed(random_seed)
torch.manual_seed(random_seed)

if torch.cuda.is_available():
    torch.cuda.manual_seed_all(random_seed)

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

text = 'colab is a computer science and research portal'

encoding = tokenizer(
    [text],
    padding=True,
    truncation=True,
    return_tensors='pt'
)

input_ids = encoding['input_ids']
print(f'Input IDs: {input_ids}')

attention_mask = encoding['attention_mask']
print(f'Attention mask: {attention_mask}')
with torch.no_grad():
    outputs=model(input_ids,attention_mask=attention_mask)
    word_embeddings=outputs.last_hidden_state
print(f'shape of the word Embeddings:{word_embeddings.shape}')
decoded_text=tokenizer.decode(input_ids[0],skip_specia_tockens=True)
print(f'Decoded Text:{decoded_text}')
tokenized_text=tokenizer.tokenize(decoded_text)
print(f'tokenized Text:{tokenized_text}')
encoded_text=tokenizer.encode(text,return_tensrs='pt')
print(f'Encoded Text:{encoded_text}')
for token,embedding in zip(tokenized_text,word_embeddings[0]):
    print(f'Embedding:{embedding}')
    print()
sentence_embedding=word_embeddings.mean(dim=1)
print('Sentence Embedding:')
print(sentence_embedding)
print(f'Shape of Sentence Embedding:{sentence_embedding.shape}')
example_sentence='Colab is also a technology website'
example_encoding=tokenizer(
    [example_sentence],
    padding=True,
    truncation=True,
    return_tensors='pt',
    add_special_tokens=True
)
example_input_ids=example_encoding['input_ids']
example_attention_mask=example_encoding['attention_mask']
with torch.no_grad():
    example_outputs=model(example_input_ids,attention_mask=example_attention_mask)
    example_sentence_embedding=example_outputs.last_hidden_state.mean(dim=1)
similarity_score=cosine_similarity(sentence_embedding,example_sentence_embedding)
print('Cosine Similarity Score:',similarity_score[0][0])
text1='Colab ia a computer Science and research portal.Google Colab(short for Colaboratory) is a free, '\
'cloud based platform provided by Google that allows you to writ and execute pyhton code entirely in your web browser. '
text2='It is built on Project Jupyter and provides a "notebook" environment where you can combine executable code. '\
'rich text (using Markdown),images,and visualizations in a single document.'
encoding=tokenizer([text1,text2],
padding=True,
truncation=True,
return_tensors='pt',
add_special_tokens=True
)