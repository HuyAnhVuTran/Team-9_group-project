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

The closest Mesa model for simulating our phenomenon is the Virus on a Network model. This model effectively captures how misinformation spreads across social media, similar to how a virus propagates through a network. In our adaptation, misinformation bots act as infectious agents, susceptible users function as potential hosts, and fact-checkers serve as intervention mechanisms that reduce the spread. Our simulation will incorporate 5 different entities that each represent various types of users on Twitter. By modifying the model, we can incorporate key entities that both amplify and counteract misinformation on Twitter, simulating the dynamics of misinformation outbreaks and the role of AI-to-AI interactions in sustaining fake news loops 

### **Entities**  

- **Human Users**: These are people who used the Twitter social media platform during the COVID-19 Pandemic. Human users may interact with COVID-19 discussions on Twitter. These users are split into four specific entities that have different behaviors, roles, and goals on the platform
- **Fact-Checkers**: These are Twitter users who participated in the Birdwatch Program (now Community Notes). They are given the authority to verify claims and provide context to misleading posts by submitting explanatory notes. If a note reaches a high approval rating, it appears with the misinformation content. This encourages public accountability by challenging misinformation and it increases transparency in fact-checking. Their role is to counter misinformation and educate users regarding false narratives.

- **Susceptible Users**: These are Twitter users who can be influenced, manipulated, or deceived by information from external sources like misinformation, propaganda, or scams. Lacking the awareness or tools to critically assess credibility, they are the most vulnerable to misinformation. They can either become misinformed users (if influenced by bot-amplified content) or resistant users (if exposed to fact-checking). Their role is to act as neutral users on Twitter who have not yet formed strong opinions about COVID-19-related information.

- **Misinformed Users**: These are Twitter users who believe, share, or engage with misleading content posted by misinformation bots or other misinformed users. Their actions (liking, commenting, sharing, etc.) contribute to the amplification of falsehoods. However, exposure to fact-checking may reverse their misinformation stance, making them resistant over time. Their role is to consume misinformation and possibly influence susceptible users.
- **Resistant Users**: These are Twitter users who are reluctant to believe information posted on the platform without sufficient evidence. These users are not influenced by misinformation content shared by misinformation bots or misinformed users. They remain immune to bot-driven misinformation. Their role is to prevent misinformation spread by being reluctant to engage in false content
- **Misinformation Bots**: For the purpose of this study, we will refer to this type of content amplification bot as Misinformation bots. These bots aim to spread misleading content about COVID-19, including false treatments. They amplify the visibility of misinformation by liking, sharing, retweeting, commenting, and reposting content on Twitter. These artificial visibility-boosting activities can manipulate the platform’s trending algorithms. Some of them are even programmed to interact with each other to simulate an organic human discourse to avoid detection by Twitter. These bots can act like viruses on a network, sending infectious misinformation that exploits user attention to spread content and mimic human behavior to avoid detection algorithms 
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
