# author: yuling shi
# date: 2023-2-19
# description: a demo for word by word plagiarism detection

import streamlit as st

st.title('Word by Word Plagiarism Detection')

# provide an input box
input1 = st.text_input('Input sentence 1')

# st.markdown(input1)

input2 = st.text_input('Input sentence 2')

# st.markdown(input2)

input1 = input1.split()
input2 = input2.split()


def ngram_overlap(sentence1, sentence2, n):
    s1_ngrams = [' '.join(sentence1[i:i+n]) for i in range(len(sentence1)-n+1)]
    s2_ngrams = [' '.join(sentence2[i:i+n]) for i in range(len(sentence2)-n+1)]
    overlap = set(s1_ngrams) & set(s2_ngrams)
    return overlap


n = 3
overlap = ngram_overlap(input1, input2, n)
# print("N-gram overlap (n={}): {}".format(n, overlap))

# attach html background color to the overlaps


def highlight_overlap(sentence1, sentence2, overlap):
    s1_highlighted = []
    s2_highlighted = []
    
    sentence1_flag = 0
    sentence2_flag = 0

    for i, word in enumerate(sentence1):
        if ' '.join(sentence1[i:i+n]) in overlap:
            s1_highlighted.append('<span style="background-color: #FFFF00">{}</span>'.format(word))
            sentence1_flag = n
        elif sentence1_flag > 0:
            s1_highlighted.append('<span style="background-color: #FFFF00">{}</span>'.format(word))
            sentence1_flag -= 1
        else:
            s1_highlighted.append(word)
            sentence1_flag -= 1
            
    for i, word in enumerate(sentence2):
        if ' '.join(sentence2[i:i+n]) in overlap:
            s2_highlighted.append('<span style="background-color: #FFFF00">{}</span>'.format(word))
            sentence2_flag = n
        elif sentence2_flag > 0:
            s2_highlighted.append('<span style="background-color: #FFFF00">{}</span>'.format(word))
            sentence2_flag -= 1
        else:
            s2_highlighted.append(word)
            sentence2_flag -= 1

    s1_highlighted = ' '.join(s1_highlighted)
    s2_highlighted = ' '.join(s2_highlighted)
    return s1_highlighted, s2_highlighted


s1_highlighted, s2_highlighted = highlight_overlap(input1, input2, overlap)

st.markdown('**Sentence 1:**')
st.markdown(s1_highlighted, unsafe_allow_html=True)
st.markdown('**Sentence 2:**')
st.markdown(s2_highlighted, unsafe_allow_html=True)