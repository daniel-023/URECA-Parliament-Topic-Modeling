import streamlit as st
from sentence_transformers import SentenceTransformer
from topic_modeling import load_model


@st.cache_resource
def load_topic_model(model_name):
    model = load_model(model_name)
    model.set_topic_labels(custom_topic_names)
    return model

# Function to handle side bar text selection
def set_text(text):
    st.session_state['user_input'] = text

@st.cache_data
def get_embeddings(user_input):
    embeddings = embedding_model.encode([user_input], show_progress_bar=True)
    return embeddings

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
                16: 'Public Health',
                17: 'Fire and Emergency Services',
                18: 'Market and Hawker Licensing'
            }

# Load the model
model = load_topic_model("Parliament_Topic_Model")
 # Load the embedding model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Streamlit app title
st.title("Topic Modeling with BERTopic")

# Sidebar
page = st.sidebar.selectbox("Choose a page", ["Intertopic Distance Map", "Topic Keywords", "Topic Prediction",])

# Initialize session state for user input
if 'user_input' not in st.session_state:
    st.session_state['user_input'] = ""

sample_texts = {"Primary School in Simei Estate (11-12-1996)": """PRIMARY SCHOOL IN SIMEI ESTATE
Mr Teo Chong Tee asked the Minister for Education, following the overwhelming demand for primary one places in Changkat Primary School for 1997, whether his Ministry will now consider building another primary school in Simei Estate.
The Senior Minister of State for Education (Encik Sidek bin Saniff) (for the Minister for Education): Mr Speaker, Sir, Simei Estate falls within the Tampines Development Guide Plan (DGP) zone which has 11 primary schools. 
According to our projections, the 11 schools will have sufficient school places to serve the entire DGP up to the year 2000. Under the 5th Primary School Building Programme, the Ministry will build an additional primary school at Tampines Street 33 to cater to demand for primary school places beyond the year 2000. 
It will be ready by the year 2000. At this year's Primary 1 Registration Exercise, there were 189 Primary 1 vacancies in Qiaonan Primary School after completion of registration. The school is less than 1 km from Changkat Primary.
Mr Teo Chong Tee (Changi): Sir, may I ask the Senior Minister of State for Education whether he is aware that there is a growing population in Simei Estate, in particular, and there are a lot of young children who are now in our PCF kindergarten education centres? 
So we see a need for a primary school to be built within the Simei Housing Estate. May I request the Senior Minister of State to look further into this matter?
Encik Sidek bin Saniff: Sir, the Ministry is aware of the growing number of school-going children and that is why we are building an additional school at Tampines Street 33.
When the time comes, I am quite sure we will consider the request if there is a necessity. For instance, the Member has asked about Changkat Primary School which is nearest to his constituency. 
My officers have tried their best by increasing the number of places from 400 to 405 next year, though not many, to ensure convenience.
""", 
"Reclamation at Punggol (19-10-1984)": """RECLAMATION AT PUNGGOL
The Minister for Labour and Second Minister for Law and Home Affairs (Prof. S. Jayakumar): Mr Speaker, Sir, I beg to move the Motion* standing in the name of the Minister for Law as it appears on the Order Paper.
*The Motion reads as follows:
That this Parliament, in accordance with section 4 of the Foreshores Act (Chapter 270), approves the reclamation by the Government of that portion of the foreshore at Punggol containing an area of about 685 hectares as shown coloured pink on the plan marked "LAND OFFICE RECLAMATION PLAN NO. 2/84", which is deposited in the Land Office, Singapore.
Sir, to create additional land stock for public housing, the Housing and Development Board has studied the feasibility of reclaiming more land at Singapore's north-eastern coast. The study, carried out in consultation with the relevant authorities, such as the Port of Singapore Authority, Public Utilities Board, Jurong Town Corporation, Sewerage Department and the Primary Production Department, has shown that another 685 hectares of land at Punggol can be reclaimed. This is shown, coloured pink, on the plan marked "LAND OFFICE RECLAMATION PLAN NO. 2/84" a copy of which is displayed in the Library of this House for the information of Honourable Members. This reclamation will be in addition to the 277 hectares off Punggol, coloured yellow on the plan, approved for reclamation by this House at its sitting on 4th March, 1983.
The areas to be reclaimed are in the shallow waters off Pasir Ris, Punggol and Jalan Kayu. Areas 2, 3 and 4 in the plan will be used for public housing, while area 1, being adjacent to the Serangoon sludge treatment works, will be used for refuse tipping, and industrial and recreational purposes.
The proposed reclamation will not affect the navigational channel.
The reclamation works will be carried out in phases over a nine-year period from 1985 to 1993. Area 2 where the Punggol Fishing Port is located will be reclaimed last to give the fishing port a useful lifespan of almost 10 years. The fishing port will be relocated to a nearby location on the reclaimed land when reclamation works have been completed. Other consequential works required are the extension of the effluent out-fall pipes from the Seletar and Serangoon Sewerage Treatment Works and the preparation of new refuse tipping ground at Area 1.
The total cost of the project inclusive of the consequential works has been estimated at $874 million. About 76 million cubic metres of fill will be required for this project. Half of the fill can be taken from the HDB development sites in Woodlands, Tampines, Pasir Ris, Yishun, Seletar and Zhenghua and the overburden soil from the quarries at Bukit Timah areas. The other half will be imported from external sources.
Sir, I beg to move.
Question put, and agreed to.
Resolved,
That this Parliament, in accordance with section 4 of the Foreshores Act (Chapter 270), approves the reclamation by the Government of that portion of the foreshore at Punggol containing an area of about 685 heatares as shown coloured pink on the plan marked "LAND OFFICE RECLAMATION PLAN NO. 2/84", which is deposited in the Land Office, Singapore.
""",
"Punggol Pig Farmers (12-03-1984)": """PUNGGOL PIG FARMERS (Dispossession)
1. Mr J.B. Jeyaretnam asked the First Deputy Prime Minister and Minister of Education (a) what were the reasons for dispossessing the pig farmers in Punggol of their farms; (b) how many farmers have been dispossessed of their farms; (c) what has happened to the farmers who have been dispossessed; and (d) has any alternative livelihood been offered to them.
The First Deputy Prime Minister and Minister of Education (Dr Goh Keng Swee): Mr Speaker, Sir, no pig farmers in Punggol have been dispossessed of their farms. So the questions raised by the Member for Anson are irrelevant. Despite this, I shall take advantage of this occasion to explain Government's present thinking on pig farming.
Pig farming is a highly pollutive industry, the animal producing excrement five times as much as a human being. A major review of pig policy was undertaken in 1979 when a decision was taken, on the advice of the Primary Production Department (PPD) of the Ministry of National Development, to install waste treatment plants in all pig farms as a means of reducing environmental pollution.
Such plants are expensive to install and require a minimum size of farm. In effect, this means that small pig farms will have to close down. These farms are sited on Government land under Temporary Occupation Licences (TOL) with nominal annual rentals. In this way, they are thus subsidized.
PPD's policy was to convert these small farms to large-scale commercial enterprises, paying economic rents and eventually installing waste treatment plants. They will be concentrated mostly in the Punggol area, and farms elsewhere will be phased out. PPD envisaged that by the end of 1986, there will be 70 commercial farms with a pig population of 650,000. With the exception of eight commercial farms (with a pig population of about 150,000) whose leases expire in 2005, all leases will expire in 1995. This pig population of 650,000 can serve Singapore's consumers if it is supplemented by modest imports from Malaysia.
There are, however, three serious weaknesses in this policy. The first is a technical one - the reduction in the level of pollution. This is measured by the Biochemical Oxygen Demand (BOD) which is the demand for oxygen by organic pollutants in the water. Raw pig waste with a BOD level of 4000 mg per litre requires more then 400 times as much oxygen as clean stream water which has a BOD level of less than 10 mg per litre.
PPD aims to achieve a BOD level of 250 mg per litre as a preliminary target. This represents a considerable reduction in pollution level, from 4000 mg per litre. However, a BOD level of 250 mg per litre is not acceptable to the Ministry of the Environment, as it is the BOD level of raw human sewage.
The second and third weaknesses are economic. Pig farming requires scarce resources, notably land and water. The scarcity of land in Singapore means that the proximity of pig farms is much too close to densely populated areas. As for water, the Ministry of the Environment estimates that 30 to 40 litres of water per pig per day will be required just to wash pig waste into the cesspits and treatment plants. Assuming that about half of the water used is PUB water and that a pig population of 650,000 is maintained, the amount of PUB water required to wash pig waste into cesspits and treatment plants works out to two to three million gallons per day.
Finally, the high cost of constructing and maintaining the treatment plants. The capital cost of the treatment plant works out to about $120 per pig. PPD proposes to give a grant of $100 per pig to commercial farms. The operating cost could be $10 per pig, according to PPD, but the Ministry of the Environment believes it to be between $20 and $30 per pig. Both PPD and the Ministry of the Environment are agreed that the treatment of pig waste to a BOD level substantially below 250 mg per litre would make pig farming uneconomic.
What PPD is doing is to levy a cess of $10 per pig slaughtered at the abattoir with the intention of using this money to subsidize commercial farms' expenditure on waste treatment plant. The cess was introduced on 1st January 1980, and the amount accumulated at the end of 1983 is $33 million. In effect, what happens is that the Singapore consumer is being asked to subsidize commercial pig farms in two ways. First is the cess of $10 per pig slaughtered at the abattoir. Second is the restriction on import of pigs, ostensibly on health grounds but, in reality, to maintain pig prices high enough to make commercial farms viable.
The Government is making a review of this policy. Does it make sense to spend some $80 million on waste treatment plants to achieve poor environmental standards? If pig farms have eventually to go, why prolong the agony? Are we assured of reliable sources of live pigs from imports? Can we persuade the Singapore consumer to buy frozen imported pork at lower cost?
On 11th February, I visited Bangkok to discuss with the Thai authorities possibilities of imports of live pigs and frozen pork. The Thai counterparts of PPD assured me that they could easily supply our market and would set up the health standards we require. A technical mission will visit Bangkok next week for a study of quarantine facilities, the state of pig farms in Thailand and other matters. The Government has also received enquiries from Indonesian businessmen about possibilities of setting up commercial pig farms in the Rhio Islands.
The preliminary conclusion therefore is that it is possible to supply the whole of our pork requirements through imports, probably at a lower cost to the Singapore consumer. However, further studies have to be made before we can come to a firm conclusion.
If studies confirm that imported supplies are the best solution, we have to decide how quickly we can phase out our pig farms and in what manner, that is, by administrative controls or by allowing market forces to decide the outcome by free competition. The question of compensation, if any, can then be decided.
Returning to the Member's questions, 71 TOL pig farms in Punggol were informed on 8th April 1983, that they would have to be resettled. I have asked PPD to withhold action until the Government has reached a conclusion on the future of pig farms.
Mr Speaker, may I comment on the general tenor of the Member's questions. First, the word "dispossessed" carries strong emotive overtones. It suggests a heartless government depriving the poor of the little that they have. How can anyone in his right mind see the PAP Government in this light? Over the last 25 years, we have created a stable and prosperous society with full employment and raised the standard of living four or five-fold. When we started in 1959, Singapore was a riot-torn city with endemic high rates of unemployment and wretched overcrowding.
The last question betrays the Member's unstated major premise from which he addresses our economic problems. He asked: "Has any alternative livelihood been offered to them?" He believes that somebody owes the Singaporean a livelihood. This is a form of the welfare state syndrome which the Member has acquired because he believes that what the West does, Singapore must do likewise. We have repeatedly stated that nobody owes us a livelihood. We make our own livelihood by hard work, thrift and enterprise. The Government helps our citizens by its economic policy which ensures sustained and robust growth so that changes of occupation and employment, when these are necessary, can be made quickly and with minimum pain.
Mr J.B. Jeyaretnam (Anson): Mr Speaker, Sir, a supplementary question for the Minister. But before I ask him the supplementary question, may I say that I am indebted to him for his lengthy exposition on pig farming and how it could be economically carried out. But I am a little surprised that the Minister should take umbrage at my question. He says no one has been dispossessed. But now I understand that there were 71 farmers who held licences on a TOL basis. I am indebted to him to learn that now action will be withheld. So do I understand the Minister to say that the notices to quit addressed to the other 70 will be withdrawn, because one of them committed suicide, as we know, after receiving this notice to quit. [Laughter] It is no laughing matter, Members. One of them committed suicide because he was distressed by this notice to quit. Am I to understand that the notices to quit served on the other 70-odd farmers had been withdrawn and that no precipitate action will be taken against them?
Dr Goh Keng Swee: Sir, the Member for Anson is a lawyer by profession and he believes that, I assume correctly, from the legal point of view, that a notice to quit means action will be taken. I did say that the notices to the TOL pig farms were served on the farmers on 8th April 1983 which was nearly a year ago and up to now no action has been taken to ask them to quit. Even if the intention of Government to close down all these farms was carried out, time would be given to these farmers to adjust to the new situation.
He asked for an assurance whether these notices to quit will be withdrawn. Obviously, from the tenor of my reply, it does not make sense to withdraw these notices and then later on to tell them, "You have to phase out your farms." Because my assessment is that the now policy would mean that not only the small farmers have to cease operation but the big commercial farms also. I cannot see under what conditions they can compete with imported supplies of pigs, if they are asked to maintain a standard of anti-pollution treatment plants acceptable to the Ministry of Environment. In short, the future of the Singapore pig looks to me to be very bleak.
Mr Jeyaretnam: May I ask the Minister just one more question and, that is, has he considered bringing all these farmers into a son of cooperative so that they could farm more economically and meet the standards required?
Dr Goh Keng Swee: Sir, I have not considered it; it is a rather astonishing idea. When large-scale and efficient enterprises are not expected to survive com- petition from imported pigs by reason of the cost of waste treatment plant, I cannot see how cooperatives can perform better. I think it is more humane that we allow the pig farmers time to adjust and move on to other jobs.
May I draw the Member's attention to this fact. In 1975, there were 9,938 pig farms with 16,288 full-time workers. Last December, there were only 3,965 full-time workers. So in the meantime, we have more than 12,000 workers looking for other profitable ways of employment. I do not want to flog a dead horse, Mr Speaker, but when changes have to be made to let the economy grow, Singaporeans are enterprising; they do not need much help from the Government. There are opportunities and they will seize the opportunities. In this way, we make best use of our most scarce and valuable resources, that is, our human resources.
"""
}


if page == "Intertopic Distance Map":
    st.header("Intertopic Distance Map")
    st.write("""
This intertopic distance map visualises the relationships between different topics identified by the model.
Each circle represents a topic, and the size of the circle indicates the prevalence of the topic in the corpus.
The distance between circles represents how semantically similar or different the topics are from each other.
You can hover over each circle to see the top words associated with that topic.
""")
    
    fig = model.visualize_topics()
    st.plotly_chart(fig, use_container_width=True)

elif page == "Topic Keywords":
    st.header("Topic Keywords")
    st.write("""
This barchart visualises the top keywords for each topic identified by the model. 
Each bar represents a keyword, and the length of the bar indicates the importance or relevance of that keyword to the topic.
You can hover over each bar to see the exact score of the keyword.
""")
    chart = model.visualize_barchart(custom_labels=False, top_n_topics=20)
    st.plotly_chart(chart)

elif page == "Topic Prediction":
    st.sidebar.header("Sample Texts")
    st.write("""
This page allows you to enter text and analyse it using the BERTopic model. 
You can either type your own text or use one of the provided sample texts. 
When you click the "Analyse" button, the model will predict the most relevant topic for the input text and display the topic name along with the confidence score.
""")
    for label, text in sample_texts.items():
        st.sidebar.button(label, on_click=set_text, args=(text, ))
    # Input text area
    user_input = st.text_area("Enter text for topic modeling:", st.session_state['user_input'], height=300)

    if st.button("Analyse"):
        if user_input:
            # Generate embeddings
            embeddings = get_embeddings(user_input)

            # Perform topic modeling
            new_topics, new_probs = model.transform([user_input], embeddings)

            # Display results
            for topic, prob in zip(new_topics, new_probs):
                topic_name = custom_topic_names.get(topic, "Unknown Topic")
                st.write(f"Predicted Topic: {topic_name}, Topic Number: {topic}, Confidence: {prob:.2f}")
        else:
            st.write("Please enter some text for analysis.")


    
    
    