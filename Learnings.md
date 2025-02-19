# AWS AI Practitioner

## Cloud Computing 

    Deployment models of cloud: Public, Private and Hybrid

    Five Characteristics of Cloud Computing: On-demand self service,  Broad network access,  Multi-tenancy and resource pooling,  Rapid elasticity and scalability,  Measured service

    Six Advantages of Cloud Computing: Trade capital expense (CAPEX) for operational expense (OPEX), Benefit from massive economies of scale,  Stop guessing capacity, Increase speed and agility, Stop spending money running and maintaining data centers, Go global in minutes: leverage the AWS global infrastructur

    Types of Cloud Computing:
![alt text](image-20.png)
        Iaas: Amazon EC2
        PaaS: AWS Beanstalk (pre-configured EC2 server that can directly take up your application code and environment configurations and use it to automatically provision and deploy the required resources within AWS to run the web application.)
        SaaS: Google Apps, many of AWS services

    Pricing of the Cloud:
![alt text](image-21.png)

    AWS Global Cloud Infrastructure:

        AWS Regions -  It is a cluster of data centers (Most AWS services are region-scoped)

        AWS Availability Zones - It is one or more discrete data centers with redundant power, networking, and connectivity. Isolated from each other and also disasters occuring at individiual ones and AZs are connected with high bandwidth, ultra-low latency n/wing.

        AWS Data Centers - 

         AWS Edge Locations/Points of Presence: Edge Locations are strategically positioned data centers located around the world where there is a sufficient amount of population designed to the optimize the delivery of content and applications

    AWS Shared responsibility model and Acceptable Use Policy:
![alt text](image-22.png)

## Gen AI
    
    It is used to generate new data that is similar to the data it was trained on
        • Text
        • Image
        • Audio
        • Code
        • Video
    
    To generate data, we must rely on a Foundation Model.

    LLM is type of AI used to generate human-like Text.

## Amazon Bedrock

Foundation Model:

    Fine tuning:  Fine-tuning will change the weights of the base foundation model

        Instruction based fine tuning (improves perf. of model on domain specific tasks): Labeled examples of prompt-response pairs. [Cheaper] (also less data is required and less computations)
            Single turn msg
            Multi turn msg

        Continued Pre-training (also known as domain-adaption fine-tuning): Unlabeled data containing domain specific text to make model specific to that domain

    Transfer Learning:- Using pre trained model to adapt it to new related task. {fine tuning is a specific type of transfer learning}

    Evaluation of a Model: necessary for quality control of a model

        Automatic evaluation: 
            Programmatic: which just uses metrics to rate your model
            We have judge model for Automatic evaluation which evaluates actual model outputs with benchmark answers on Benchmark datasets.
![alt text](image-23.png)

        Human Evaluation: Thumbs up/down rating, ranking

        Metrics:
            For Text related tasks:
                ROUGE (Recall oriented understanding for gisting evaluation) - Evaluate automatic 'Summarizartion', machine translation system, ROUGE-N - measure number od matching n-grams, ROUGE-L - Matches longest common sub sequence b/w ref. and generated text.
                BLEU: Bilingual Evaluation Understudy - Evalute quality of gen. text, especially for 'translations'. Consider precision and panalizes too much brevity
                BERTScore - Semantic similarity b/w gen. text. Uses cosine similarity on embeddings to do the same.
                Perplexity: How well the model predicts next token correctly. (Lower is better here)
                Business metrics: User Satisfaction, Average revenue per user, cross domain perf., conversion rate, efficiency.

            For classification tasks:
                F1 Score, Accuracy, Precision, Recall
            
            For regression tasks:
                R2 score, MAE, MSE, MAPE
            
    RAG and Knowledge Base in Bedrock:
![alt text](image-24.png)
        Types of Vector DB for RAG in Amazon:
![alt text](image-25.png)   

    Gen AI Concepts:

        Tokenization: breaking raw text into sequence of tokens.

        Context Window:  number of tokens an LLM can consider when generating text.

        Embeddings: Vectors of numerical values out of text, image or audio.

    Amazon Bedrock Guardrails: To control interaction b/w users and FM, remove PII, filter undesirable content.

    Amazon Bedrock Agents: Manage and carry out various multi-step tasks related to infrastructure provisioning, application deployment, and operational activities. They are configured to perform specific pre-defined action groups. Can be integrated with other sys., DB and API to exchange data. Also can leverage RAG to retrieve info.
![alt text](image-26.png)

    Amazon Bedrock & CloudWatch:
![alt text](image-27.png)
    Other features:
        Bedrock Studio: give access of bedrock to your team.

        Watermark detection: check if image was generated by Amazon Titan Generator
    
    Amazon Bedrock Pricing:
![alt text](image-28.png)

## Prompt Engineering
    Prompts are just like guidances to model to perform tasks. 
    And Prompt Engineering means developing, designing and optimizing prompts to enhance output of FMs.

    Enhanced/Ideal Prompt should contain:
        Instructions
        Context
        Input data
        Output Indicator
        Expected Output
    
    Negative prompting improves performance by telling model what to avoid while generating output. OR A technique where you explicitly instruct the model on what not to include or do in its response

    Prompt Performance Optimization:
![alt text](image-29.png)
    Also includes Latency which is impacted by:
        Model size, model type. number of tokens in i/p and o/p.
        And not impacted by TopP, TopK, Temp.

    Prompt Engineering Techniques:
        - Few-show prompting
        - Chain of thought prompting
        - RAG
    
    Prompt Templates: It is used to simplify and standardize the process of generating prompts
![alt text](image-30.png)
    There is a risk of prompt template injection where a user might inject some malicious statements/instructions/code bcz of which model can generate prohibited or harmful response.

## Amazon Q


## Machine Learning

    - Bias (Underfitting as model can't understand data) = Difference or error b/w predicted and actual
        To reduce bias: i. Use more complex model, ii. Increase number of features
    - Variance (Overfitting as model is highly sensitive)= Change in model's perf. when there is slight change in training data although it would be with same distribution as previously.
        reduce variance: i. Feature selection of more important ones, ii. split training and test data multiple times
    
    - Evaluation Metrics:

        i. Confustion Matrix: Comparison of predicted and true values with TP, FN, FP, TN. It has metrics such as Precision [Best when FP are costly] = TP/(TP+FP), Recall [Best when FN are costly]= TP/(TP+FN), F1 Score [Balance b/w pre. and recall] = 2*prec.*recall/(Pre. + Recall)

        ii. Area Under Curve- receiver operator curve (AUC - ROC) {0 to 1(being prefect)}: Shows what the curve for TP and FP look like under various thresholds with multiple C-M

        iii. Regression Metrics:
            a. MAE b/w predicted and actual values.
            b. MAPE
            c. RMSE
            d. R-squared: Explains variance in your model (0 to 1 (being best)) {Similar to accuracy as it is for whole dataset}

    - Inferencing:

        i. Real-Time = data has to be processed as it is generated. i.e Chatbot

        ii. Batch = a certain amount data is analyzed together at once.

        Inferencing at Edge:
            
            i. SLM on edge devices
            ii. LLM on remote servers

    - Phases of ML Project:
        
        i.   Business Problem
        ii.  ML Prob. framing (Also check if ML should be applied)
        iii. Data collection
        iv.  Feature Engineering
        v.   Model development
        vi.  Model Testing  
             EDA
             Retrain
        vii. Deployment
        Monitoring
        Itrations
![alt text](image-19.png)
    
    - Hyperparameter Tuning: HP are the settings that define model structure and learning algorithm and process (eg. Learning Rate (steps used for updating weight during training), Batch size(Number of observations taken parallely OR no. of training examples taken to update model's weights in one iteration), Epoch, Regularization (To adjust balance between simple and complex model -> To reduce overfitting, increase regularization))
        How to do: Grid search, Random search, or service like Sagemaker Automatic Model Tuning

    - ML is Not Appropriate when there is deterministic problems OR for well defined problem


    - AWS AI Managed Services:

        High level services:-

            Amazon Sagemaker Jumpstart

            Amazon Bedrock

            Amazon Q Business

            Amazon Q Developer
        
        Services (Domain):

        Amazon Comprehend (Text & Document) - Fully managed and serverless NLP service for analysis and all of stuff.
            - Custom classification by providing own training dataset (Text labelled with classification tag)
            - Named Entity Recognition = Extract pre-defined, general purpose entities like people, places, org., dates, etc. from text.
                Also custom entity recognition 
        Amazon Comprehend also exists which can create a visual relationship for patient demographics, medicine, dosage, etc.

        Amazon Translate (Text & Document) - Natural and accurate Language translation service

        Amazon Textract (Text & Document) - Extract text, handwriting, data from any scanned documents using AI and ML. Read and process any type of data such as tables, forms, pdf, images. etc. 

        Amazon Rekognition (Vision) - Service that allows you to search object, people, text, scenes in images/videos using ML
            You can have custom labels to identify your product/logo, have content moderation(auto. detect inappropriate unwanted and offensive content)

        Amazon Kendra (Search) - Fully managed document search service powered by ML. Extract answers from documents

        Amazon Lex (Chatbots): Build chatbots quickly for your application which uses voice and text (integration with lambda, kendra, connect, comprehend)

        Amazon Polly (Speech, Text to speech): using DL, it has features like Lexicons (define how to read certain piece of text, i.e WWW = World wide web), SSML{Speech Synthesis Markup Language} (Markup your text to let model know how to pronounce it. like Hello, <break> How are you?), voice engine, speech mark (helpful for lip-syncing/ highlight words as they are spoken)

        Amazon Transcribe (Speech, Speech to text) -  Speech to text, uses DL techniques for ASR, autom. removes PII (you can add custom vocab., also create custom model (for custom context)), also has toxicity detection.
        Amazon Transcribe Medical: (HIPAA compliant) converts medical related speech to text 

        Amazon Personalize (For recommendations): Fully managed service to build apps with real-time personalized recommendations (same tech. is used by amazon.com), can take a long to be implemented as large data is requird

        Amazon Mechanical Turk: Crowdsourcing marketplace for simple human tasks (use: image classification, data collection, ...)

        Amazon A2I (Augmented AI): Human oversight of ML predictions in production, Here, High confidence predictions are automatically being sent to client But if there is a low confidence prediction then it is sent for human review and then only necessary action is taken. It can be built anywhere on AWS like SageSmaker, etc. 

        Amazon Hardware for AI (EC2 {Elastic Compute Cloud - IaaS}): They are basically servers of diff. type.
            
            EC2 instances that have GPU are P-family (P3, P4,...) and G-family (G3-G6)
            Amazon provides further h/w for AI such as: (Tnf and Inf instances have the lowest env. footprint)

                Amazon Trainium: ML chip for performing DL on models with 100B+ parameter. Trn1 instances has 16 Trainium accelerators. Offering 50% cost reduction when training a model

                Amazon Inferentia: ML chip to deliver inference at high perf. and low cost. Inf1, Inf2 instances are powered by inferentia which offers upto 4x throughput and 70% cost reduction


        Whole ML (Customization as well):

## Amazon Sagemaker: Fully managed service for dev./scientist to build ML models

![Sagemaker built-in algorithms](image.png)

            AMT (Auto. model tuning): AMT auto. chooses hyperparameter ranges, search strategy, max. runtime of job and early stop condition

            Model deployment and inference: you can deploy models with one click and with no servers to manage . Managed solution. 
                Deployment types: 
                    i. Real-time (Here we select server speci. like CPU, GPU, etc.), 
                    ii. Serverless (Here we just have to choose RAM capacity, app. should be able to tolerate cold start.)
                    iii. Asynchronous(used for large payload sizes upto 1 GB, it will have long processing time so we put the payload in S3 staging bucket), 
                    iv. Batch (Prediction for entire dataset in batches concurrently)
                    ![alt text](image-1.png)
            
            Sagemaker Studio: It is the unified interface for end-to-end ML dev. which supports team collaboration, testing, debugging , deployment of ML models and automated workflows. It has many applications inside it like JupyterLab, RStudio, Canvas, etc. and tools for Data processing, training, testing, pipelines, models, jumpstart, etc. 

            Sagemaker Data Wrangler: It helps to prepare tabular and image data for ML. Single interface for Data preparation, transformation and feature eng., data selection, cleansing, exploration, visualization and processing. It also supports SQL. 
            Also has Data Quality tool.

            Sagemaker Feature Store: Store features metadata in central place AND ingest features from a variety of sources, we have ability to define transformation of data into feature from within only. also can be published from data wrangler to it. Features are discoverable within studio too.

            Sagemaker Clarify: Evaluate FM. Explain mmodel's o/p. We provide task on which it  evaluates/compares 2 models. It can also detect bias in data (also in individual column)

            Sagemaker Ground Truth: It is based on RLHF (Reinforcement Learning from Human Feedback) where his feedback is included in 'reward' function
            Ground Truth Plus: Labels data using taskforce (your emp. or mechanical turk)

            Sagemaker ML Governance: 

                Sagemaker Model Cards - To gather essential model information

                Sagemaker Model Dashboard - centralized repo. for all of your ML models. also provides info and insights for all models.

                Sagemaker Role Manager -  define roles for personas

                Sagemaker Model Monitor - It helps in tracking models for alerts in deviations for bias, quality either continuosly or on-schedule.

                Sagemaker Model Registry: Allows you to track, manage and version ML models.
                " Role manager: For access control

                Sagemaker Pipelines - A workflow that automates the process of building, training and deploying a ML model. It is Continuous Integration/Continuous Delivery service for ML.

![alt text](image-2.png)

                Sagemaker Jumpstart: ML hub to find pre-trained FM and use them directly. models can be fully customized for your data and use case. 
                It has 2 options: 
                    ML Hub: Browse -> Exp. -> Customize -> Deploy

                    ML Solutions: Access & Browse->  Select & Customize -> Deploy
                
                Sagemaker Canvas: Build ML modesl using a visual interface. Here, you can have access to ready-to-use models from bedrock and jumpstart. You can also make your own customized model using AutoML powered by Sagemaker autopilot

                MLFlow: It is an open source too which helps teams build entire ML lifecycle.
                MLFlow on Amazon Sagemaker can be utilized using MLflow tracking servers in sagemaker
            
            Sagmaker Extra Features:

                N/W isolation mode: run sagemaker job containers without any outbound internet access. After it, model containers can't access anything outside that trained data, not even S3.

                Sagemaker DeepAR forecasting algorithm: used to forecast time series data.

## Responsible AI, Security, Governance, Compliance:

![alt text](image-3.png)
![alt text](image-4.png)
![alt text](image-5.png)
![alt text](image-6.png)
![alt text](image-7.png)
![alt text](image-8.png)
![alt text](image-9.png)

        Compliance:
![alt text](image-10.png)

        Governance:
![alt text](image-11.png)
![alt text](image-12.png)
![alt text](image-13.png)

        Security and Privacy for AI systems:
![alt text](image-14.png)
![alt text](image-17.png)
![alt text](image-16.png)
![alt text](image-15.png)

>
![alt text](image-18.png)


## AWS Security Services:

        Identity and Access Management Users: A physical user is mapped with an IAM to a root user

        IAM Groups: Group of users

        IAM Policies: JSON document that outlines the permission for users or groups.

        IAM Roles: It is role for a service such as Bedrock Agent, etc. to access another service like EC2/S3 or AWS services.

        EC2 Instance: Has OS (AMI(Amazon machine image)), Instance size (CPU + RAM) + Storage + Security groups + EC2 User data

        AWS Lambda: Serverless, FaaS to run code in cloud, seamless scaling, used for automation

        VPC: Each Availibility Zone has private and public subnets. Public subnets use Internet gateway and private subnets use N/w Add. translation Protocol (NAT) gateway to stay completely private from internet. (It enables to have multiple local machines be connected with only 1 public IP)
        VPC Endpoint powered by AWS PrivateLink: It is used to connect one AWS service to another within VPC seamlessly without using internet with the help of PrivateLink.
        There also exists S3 Gateway Endpoint similar to PrivateLink to access S3 privately.

        AWS Macie: It is helpful in finding private data such as PII in Amazon S3 buckets (before training GenAI models).

        Config: Track configuration changes and compliance against rules

        Inspector: Find softwate vulnerabilities in EC2, ECR (Elastic Container Registry) and Lambda functions continuously.

        CloudTrail: Provides Governance, Compliance and audit for your AWS account. Track API calls/events made by users within account.

        Artifact: On-demand access to compliance reports such as ISO, HIPAA, PCI, etc. 

        Audit Manager: Assess risk and compliance of your AWS workloads. continuosly audit AWS services usage and prepare audits and also generate reports with evidence for compliance reports that are to be submitted to get certified in particular certifications. 

        Trusted Advisor: To get insights, support plans adapted for your needs

        Scenarios For Security:

            - Bedrock must access an encrypted S3 bucket with using AWS KMS which directly means that bedrock must have access to S3 and KMS with decrypt permission

            - Deploy sagemaker in VPC which accesses S3 with a VPC Endpoint (vpc Endpoint would have a Security group and would have Endpoint Policies) and IAM Roles

            - Privately deployed app should also access bedrock with above mentioned way only. 

            - We can analyze the usage of bedrock api calls by using CloudTrail which states if a user was replied successfully or not 


