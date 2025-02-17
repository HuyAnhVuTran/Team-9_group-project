# Retweet, Repeat, Deceit: How Content Amplifiers Created Fake News Loops on Twitter During the COVID-19 Pandemic

**Github URL:** [Team-9 Group Project](https://github.com/HuyAnhVuTran/Team-9_group-project/tree/main)

## Team Members
- Kyle CHANDRASENA
- Yuri MATIENZO
- Huy Anh Vu TRAN

---

## Section 1: Phenomena of Interest  

The COVID-19 Pandemic was one of the largest outbreaks recorded recently. It prompted widespread misinformation regarding the origin of the virus, potential treatments or protections, and the severity and prevalence of the disease. This misinformation was largely propagated through content amplification bots, also known as super-spreaders. These bots engage in automated activities such as liking, sharing, retweeting, commenting, and reposting content to artificially boost the visibility of misinformation. A key feature of this process is the interaction between bots themselves. Misinformation-spreading bots engage with each other to reinforce and sustain false narratives. 

In one sample of tweets related to COVID-19, **24.8% of tweets included misinformation, and 17.4% included unverifiable information**. The authors found no difference in engagement patterns with misinformation and verified information, suggesting that myths about the virus reach as many people on Twitter as truths (Himelein-Wachowiak et al., 2021). This AI-to-AI interaction creates self-reinforcing misinformation cycles, known as **fake news loops**, where falsehoods repeatedly resurface and gain credibility through repetition. During the pandemic, these loops ensured that misinformation remained persistent on Twitter, reaching many users as verified information. 

Understanding the role of bot-driven amplification and false news loops is critical for analyzing the spread of misinformation in digital media ecosystems.

---

## Section 2: Relevant Works (References)  

### **Bots and Misinformation Spread on Social Media: Implications for COVID-19**  
During the COVID-19 pandemic, social media bots played a critical role in spreading misinformation and swaying public opinion. These automated accounts amplified false information and narratives, including unverified medical advice and conspiracy theories, which undermined public health aid and advice. The research focuses on bots strategically engaging with human users, which increases the credibility and visibility of the false content. 

The dissemination of misinformation on mainstream platforms like Twitter and Facebook contributed to public confusion and hesitation towards the vaccine. Mitigating and identifying bot activities poses an obstacle to social media companies and policies. Addressing this issue would need improved bot detection algorithms and public awareness to combat misinformation.

- **Reference:** Himelein-Wachowiak, M., Giorgi, S., Devoto, A., Rahman, M., Ungar, L., Schwartz, H. A., Epstein, D. H., Leggio, L., & Curtis, B. (2021, May 20). *Bots and misinformation spread on social media: Implications for COVID-19*. Journal of Medical Internet Research. [Link](https://pmc.ncbi.nlm.nih.gov/articles/PMC8139392/)

### **Lies Kill, Facts Save: Detecting COVID-19 Misinformation on Twitter**  
This paper explains how misinformation on COVID-19 spreads through Twitter and proposes machine learning as a foundation to detect it. The authors utilized an ensemble-learning model by combining multiple machine-learning algorithms to identify tweets as non-credible or credible. Their dataset has 400,000 tweets that are labeled based on credibility. The model leverages user and tweet features to achieve high accuracy in misinformation detection. The study highlights the dangers of misinformation, creating the need for better detection tools and emphasizing the role of fact-checking organizations in combating false information online.

- **Reference:** Al-Rakhami, M. S., & Al-Amri, A. M. (2020). *Lies Kill, Facts Save: Detecting COVID-19 Misinformation in Twitter*. IEEE Access, 8, 1–1. [DOI](https://doi.org/10.1109/access.2020.3019600)

---

## Section 3: The Core Components of the Simulation  

The closest **Mesa model** for simulating our phenomenon is the **Virus on a Network** model. This model effectively captures how misinformation spreads across social media, similar to how a virus propagates through a network. In our adaptation:

- **Misinformation bots** act as infectious agents.
- **Susceptible users** function as potential hosts.
- **Fact-checkers** serve as intervention mechanisms that reduce the spread.

### **Entities**  

- **Human Users**: General Twitter users engaging with COVID-19 discussions.
- **Fact-Checkers**: Users in the Birdwatch Program (Community Notes) who verify claims.
- **Susceptible Users**: Neutral users who can be influenced by misinformation.
- **Misinformed Users**: Users who believe and spread false content.
- **Resistant Users**: Users resistant to misinformation.
- **Misinformation Bots**: Automated accounts spreading misleading content.

### **Affordances**  

- **Metric Boosting**: Likes, upvotes, hashtags influencing ranking algorithms.
- **Comments**: Reinforce misinformation narratives.
- **Sharing (Retweets, Tagging)**: Ensures rapid exposure across the platform.

### **Algorithms**  

- **Community Notes Ranking Algorithm**: Detects misinformation and neutralizes spread through credibility scoring.
- **Recommendation Algorithm**: Suggests content based on engagement but can be exploited by misinformation bots.
- **Trending Algorithm**: Promotes viral topics, sometimes amplifying misinformation.

---

## Section 4: Simulation Anticipated Outcomes  

The goal of this simulation is to visualize how misinformation spread by content amplification bots can create and sustain fake news loops on Twitter. The simulation will demonstrate:

- **Propagation Patterns**: How misinformation moves through connections over time.
- **Echo Chambers**: Clusters of users engaging primarily with misinformation.
- **Fact-Check Interventions**: How fact-checking disrupts misinformation spread.

### **Metrics**  

- **Misinformation Reach** – Percentage of users exposed to misinformation over time.
- **User State Transitions** – Time series of user behavior shifts (susceptible, misinformed, resistant, etc.).
- **Engagement Metrics** – Impact of likes, shares, retweets on visibility.
- **User-Based Misinformation Reproduction Rate (R₀,m)** – Efficiency of misinformation spread by human users.
- **Bot-Based Misinformation Reproduction Rate (R₀,b)** – Efficiency of misinformation spread by bots.
- **Echo Chamber Density** – Percentage of users engaging primarily with misinformation, rarely encountering fact-checks.

A successful simulation will reveal **self-reinforcing misinformation cycles**, where engagement affordances drive further amplification. However, if fact-checkers are effective, the model should demonstrate a **disruption in these cycles**, reducing the spread and visibility of misinformation over time.

---
