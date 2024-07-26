from sentence_transformers import SentenceTransformer
from topic_modeling import load_model


model = load_model("Parliament_Topic_Model")

user_input = ["""
 RECLAMATION AT PUNGGOL
3.47 pm
    The Minister for Labour and Second Minister for Law and Home Affairs (Prof. S. Jayakumar): Mr Speaker, Sir, I beg to move the Motion* standing in the name of the Minister for Law as it appears on the Order Paper.
*The Motion reads as follows:
    That this Parliament, in accordance with section 4 of the Foreshores Act (Chapter 270), approves the reclamation by the Government of that portion of the foreshore at Punggol containing an area of about 685 hectares as shown coloured pink on the plan marked "LAND OFFICE RECLAMATION PLAN NO. 2/84", which is deposited in the Land Office, Singapore.
    Sir, to create additional land stock for public housing, the Housing and Development Board has studied the feasibility of reclaiming more land at Singapore's north-eastern coast. The study, carried out in consultation with the relevant authorities, such as the Port of Singapore Authority, Public Utilities Board, Jurong Town Corporation, Sewerage Department and the Primary Production Department, has shown that another 685 hectares of land at Punggol can be reclaimed. This is shown, coloured pink, on the plan marked "LAND OFFICE RECLAMATION PLAN NO. 2/84" a copy of which is displayed in the Library of this House for the information of Honourable Members. This reclamation will be in addition to the 277 hectares off Punggol, coloured yellow on the plan, approved for reclamation by this House at its sitting on 4th March, 1983.
    The areas to be reclaimed are in the shallow waters off Pasir Ris, Punggol and Jalan Kayu. Areas 2, 3 and 4 in the plan will be used for public housing, while area 1, being adjacent to the Serangoon sludge
Column: 2096
treatment works, will be used for refuse tipping, and industrial and recreational purposes.
    The proposed reclamation will not affect the navigational channel.
    The reclamation works will be carried out in phases over a nine-year period from 1985 to 1993. Area 2 where the Punggol Fishing Port is located will be reclaimed last to give the fishing port a useful lifespan of almost 10 years. The fishing port will be relocated to a nearby location on the reclaimed land when reclamation works have been completed. Other consequential works required are the extension of the effluent out-fall pipes from the Seletar and Serangoon Sewerage Treatment Works and the preparation of new refuse tipping ground at Area 1.
    The total cost of the project inclusive of the consequential works has been estimated at $874 million. About 76 million cubic metres of fill will be required for this project. Half of the fill can be taken from the HDB development sites in Woodlands, Tampines, Pasir Ris, Yishun, Seletar and Zhenghua and the overburden soil from the quarries at Bukit Timah areas. The other half will be imported from external sources.
    Sir, I beg to move.
    Question put, and agreed to.
    Resolved,
    That this Parliament, in accordance with section 4 of the Foreshores Act (Chapter 270), approves the reclamation by the Government of that portion of the foreshore at Punggol containing an area of about 685 heatares as shown coloured pink on the plan marked "LAND OFFICE RECLAMATION PLAN NO. 2/84", which is deposited in the Land Office, Singapore."""]

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = embedding_model.encode(user_input, show_progress_bar=True)

print(embeddings)
new_topics, new_probs = model.transform(user_input, embeddings)

custom_topic_names = {
    0: 'Education',
    1: 'Land Development and Reclamation',
    2: 'Economy and Trade',
    3: 'Public Service',
    4: 'Law and Legislation',
    5: 'Citizenship and Immigration',
    6: 'Public Transport and Infrastructure',
    7: 'Property and Housing',
    8: 'Agriculture and Production',
    9: 'Diplomacy and Foreign Relations',
    10: 'Cultural Programmes and Media',
    11: 'Reproductive Rights and Family Planning',
    12: 'Retirement Fund',
    13: 'International Travel',
    14: 'Sports and National Events',
    15: 'Drug Control and Regulation',
    16: 'Public Helth',
    17: 'Fire and Emergency Services',
    18: 'Market and Hawker Licensing'
}

for topic, prob in zip(new_topics, new_probs):
    topic_name = custom_topic_names.get(topic)
    print(f"Predicted Topic: {topic_name}, Confidence: {prob}")