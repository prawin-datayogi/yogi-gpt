#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 20:26:15 2023

@author: prawinraja
"""

import streamlit as st


import base64
import openai

#from dotenv import load_dotenv, find_dotenv
#_ = load_dotenv(find_dotenv())


openai.api_key = st.secrets["pass"]





st.title(" Yogi GPT ")


text = st.text_area('Enter your concern child :')


#text = "My girl friend just broke up with me, I am feeling worthless and afraid of being single for life"

prompt_2 = f"""
    Your task is to perform the following actions:
    1 - Understand the users negative feelings with empathy and Generate three short sentence positive affirmations in first person tense not more than 15 words.
    2 - classify the input based on below information on the chakras, find which chakra is affect based on the user feeling. Tell the chakra name only
    
    Root Chakra (Muladhara): Stability, Security, Grounding, Safety, Survival, Fear, Trust, Belonging
    Sacral Chakra (Svadhisthana): Creativity, Passion, Pleasure, Sensuality, Desire, Passion, Intimacy, Joy
    Solar Plexus Chakra (Manipura): Personal Power, Confidence, Confidence, Willpower, Ambition, Courage, Self-Esteem
    Heart Chakra (Anahata): Love, Compassion, Relationships, Love, Compassion, Empathy, Forgiveness, Gratitude
    Throat Chakra (Vishuddha): Communication, Expression, Authenticity, Communication, Expression, Truth, Confidence, Clarity
    Third Eye Chakra (Ajna): Intuition, Insight, Awareness, Intuition, Insight, Wisdom, Imagination, Introspection
    Crown Chakra (Sahasrara): Consciousness, Spiritual Connection, Spiritual Connection, Divine Awareness, Transcendence, Bliss, Unity
    
    3 - based on the affected chakra suggest the meditation from the below information
    
    Root Chakra Seed Mantra – LAM Chanting Meditation
    Sacral Chakra Seed Mantra – VAM Chanting Meditation
    Solar Plexus Chakra Seed Mantra – RAMM Chanting Meditation
    Heart Chakra Seed Mantra – YAM Chanting Meditation
    Throat Chakra Seed Mantra – HAM Chanting Meditation
    Third Eye Chakra Seed Mantra – OM Chanting Meditation
    Crown Chakra Seed Mantra – AH Chanting Meditation
    
    4 - suggest 3 (easy, moderate and difficult) yoga poses for strengthening the affected chakra
    
    Text: <{text}> """







def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]
    #return response



if st.button('Affirm'):
    st.write(get_completion(prompt_2))
else:
    st.write('Your Resolutions will appear here')





    
