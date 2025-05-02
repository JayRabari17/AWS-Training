# AWS DEA-C01 Certification

## Services

### ANALYTICS
    Amazon EMR
    AWS Lake Formation
    Amazon Redshift
    Amazon Kinesis
    AWS Glue
    Amazon Managed Streaming for Apache Kafka
    Amazon OpenSearch Service
    Amazon QuickSight
    Amazon Athena

### APP INTEGRATION
    Amazon EventBridge
    AWS Step Functions
    Amazon AppFlow
    Amazon Simple Notification Service (Amazon SNS)
    Amazon Simple Queue Service (Amazon SQS)
    Amazon Managed Workflows for Apache Airflow

### CLOUD FINANCIAL MANAGEMENT
    AWS Budgets
    AWS Cost Explorer

### COMPUTE
    AWS Batch
    AWS Lambda
    Amazon Elastic Compute Cloud (Amazon EC2)
    AWS Serverless Application Repository

### CONTAINERS
    Amazon Elastic Container Registry (Amazon ECR)
    Amazon Elastic Container Service (Amazon ECS)
    Amazon Elastic Kubernetes Service (Amazon EKS)

### DATABASE
    Amazon DocumentDB (with MongoDB compatibility)
    Amazon DynamoDB
    Amazon Keyspaces (for Apache Cassandra)
    Amazon MemoryDB for Redis
    Amazon Neptune
    Amazon Relational Database Service (Amazon RDS)

### DEVELOPER TOOLS
    AWS Command Line Interface (AWS CLI)
    AWS Cloud9
    AWS Cloud Development Kit (AWS CDK)
    AWS CodeBuild
    AWS CodeCommit
    AWS CodeDeploy
    AWS CodePipeline

### FRONTEND WEB
    Amazon API Gateway

### MACHINE LEARNING
    Amazon SageMaker

### MANAGEMENT AND GOVERNANCE
    AWS CloudFormation
    AWS CloudTrail
    Amazon CloudWatch
    AWS Config
    Amazon Managed Grafana
    AWS Systems Manager
    AWS Well-Architected Tool

### MIGRATION AND TRANSFER
    AWS Application Discovery Service
    AWS Application Migration Service
    AWS Database Migration Service (AWS DMS)
    AWS DataSync
    AWS Transfer Family
    AWS Snow Family

### NETWORKING AND CONTENT DELIVERY
    Amazon CloudFront
    AWS PrivateLink
    Amazon Route 53
    Amazon Virtual Private Cloud (Amazon VPC)

### SECURITY, IDENTITY, AND COMPLIANCE
    AWS Identity and Access Management (IAM)
    AWS Key Management Service (AWS KMS)
    Amazon Macie
    AWS Secrets Manager
    AWS Shield
    AWS WAF

### STORAGE
    AWS Backup
    Amazon Elastic Block Store (Amazon EBS)
    Amazon Elastic File System (Amazon EFS)
    Amazon Simple Storage Service (Amazon S3)


## Data Engineering Fundamental concepts:

- Types of Data: 
    1. Structured (defin. in particular manner or schema) -> Characteristics - Easily queryable, Org. in rows and cols. and has consis. struct.
    2. Semi-structured (not org. as struct. data but has some level of struture in form of tags, hierarchies or other patterns) -> Char.: ele. are tagged or categori., more flexible than struct. data but not chaotic as unstruct. data - Eg. XML or JSON files, Email Headers, Log files
    3. Unstructured (doesn't really has any predefined schema) -> Char.: Not easily queryable, comes in var. formats - Eg. Raw Text files, Video, Audio files, Emails and Word processing documents

- Properties of Data: (Only 3 V's (Veracity not included))
    1. Volume (refers to size of data)
    2. Velocity (refers to the speed at which new data is genera., collec. and processed)
    3. Variety (refers to diff. types of data and sources)

- **Data Warehouse (Amazon Redshift)**: A centralized repo. optimiz. for analysis where data from diff. sources is stored in diff. format.
    Charac.: 
        Designed for complex queries and analysis
        Data is cleaned, trans. and loaded (ETL)
        Typically uses star or snowflake schema
        Optimized for read-heavy operations
        Schema-on-write
        Primarily data is in structured format
        Less agile due to pre-defin. schema.
        More expensive as it also needs optimizations for complex queries
        Use when you need:
            to perform fast and complex queries
            Data integration from diff. sources is essential
            BI and analytics are primary use cases

- **Data Lake (Amazon S3, HDFS on hadoop ecosys. is also an eg. of it)**: A storage repo. that holds vast amount of raw data in its native format (i.e any type of data).
    Charac.:
        Can store large amount of raw data without predefined schema
        Data is loaded as-is, no need for prepreoces.
        Supports real-time, batch and stream processing
        Can be queried for data transf. or exploration purpose
        ELT is performed meaning schema-on-read.
        More agile as it accepts raw data without any pre-defined structure
        Cost-effective but cost can rise when processing large amounts of data
        Use when you need:
            when you have mix data of diff. types.
            need scalable and cost effective solu.
            future needs are uncertain
            Adv. analytics, ML and Data discovery are key goals.

- **Data Lakehouse (AWS Lake Formation, also Apache Delta Lake (not on AWS))**: A hybrid data archi. that combines best features of data lakes and data warehouses aiming to prov. perf., reliab., capab. of warehouse with cost effec., flex., scale and low cost storage of lake
    Charac.:
        Supports both struct. and unstruct.
        Allows for schema on-write and on-read
        ...
        Benefits from tech. like Delta lake which brings ACID prop. to big data

- **Data Mesh (Data as a product) [Domain-based Data Management]**: Individual teams own data products within a given domain within larger org.
    These data products can be used by other teams BUT maintainence of data prod. is done by its domain team only while also following central standards.
    Federated Governance with central standards.
    Data mesh is about a higher order data management paradigm (like who maintains data, who owns it, how will it be accessed, how is it distrib. among larger org.) where lakes and warehouses are used but Data mesh is not a specific tech. or archi.

- **ETL** (Extract Transform and Load) - Process used to move data from sources to data warehouse
    Managed ETL pipelines:
        Through AWS Glue or orchestration services like Eventbridge, MWAA, Step functions, Lambda, Glue workflows

- **Data Sources:**

    1. JDBC Connection(Java Database Connectivity): Platform independent, Language dependent
    2. ODBC Connection (Open DB connectivity): Platform dependent (certain drivers are needed), Language independent
    3. Raw Log files
    4. API's
    5. Streams

- **Data Formats:**

    1. CSVs (should be used for small to med. datasets, human readability and editability, import or exporting data from dbs)
    2. JSON (used when web exchanges are done, config. and settings for soft. app., use cases need flexible schema)
    3. Avro: Binary format that stores both the data and its schema, ig making processing platform independent (i.e diff. sys can do it without needing ori. sys. context.) [should be used when working in big data and real time processing sys., when schema evolution is needed, efficient serialization for data transport between sys] - Apache sys. (be it any from kafka, hadoop, spark, flink, etc.) can use it easily.
    4. Parquet: Columnar storage optimized for analytics. Allows for efficient compression and encoding schemas [should be used when analyzing large data with analy. engines, when need to read specific columns instead of rows, storing data on distrib. sys where I/O op. and storage needs optimization] - Hadoop eco., Spark, Hive, Apache impala, Redshift spectrum can use parquet.

- **Data Modeling**

    Star Schema
![alt text](image.png)

- **Data Lineage:** Visual representation that traces the flow and transf. of data throgh its lifecycle from source to final destination.
![alt text](image-1.png)

- **Schema Evolution:** Ability to adapt and change schema of dataset over time without disrupting existing processes or systems. - Eg. Glue Schema Registry (it is schema discovery, compatibility, validation, registration tool)

- **Database Performance Optimization:**
    Indexing: Avoid full table scans. Enforce data uniqueness and integrity
    Partitioning: (You can partition your data according to the needs like partitioning by month if you know you need data from last month mostly.) Reduces amount of data scanned. Helps with data lifecycle management, enables parallel processing
    Compression: Speed up data tranfers, reduce storage and disk reads. Eg. GZIP, LZOP, BZIP2, ZSTD (eg. used in Redshift), There also exists columnar compression techniques for parquet, etc.

- **Sampling Techniques (When you want a sample representative of your whole database for analysis purposes)**
    1. Random Sampling: Everything has equal chance.
    2. Stratified Sampling: Divide population into homogeneous subgroups (strata), Random sample within each strata. This ensures representation of each subgroup (strata)
    Other techniques are: Systemic (instead of random sampling, we define a rule where we take items after fixed interval or something like that), Cluster, Convenience, Judgemental, etc.

- **Data Skew Mechanisms**: Data Skew refers to the unqual distribution or imbalance of data across various nodes or partitions in distrib. computing sys. (Causes can be non-uniform distrib. of data, temporal skew, etc.) Eg. IMDB celeb. partitioning where more read traffic comes on a particular part.. Monitoring must be done which can done through cloudwatch.
    - Addressing Data Skew:
        1. Adaptive Partitioning: Dynamically adjust data based on data char. to enusre more balanced distrib.
        2. Salting: Introduce a random factor (salt) to data to distrib. it more uniformly.
        3. Repartitioning: Regularly redistribute data based on its current distrib.
        4. Sampling: Use a sample of data to determine distrib. and adjust processing strategy.
        5. Custom partitioning: Define custom rules for partitioning based on domain knowledge (like for eg., giving a celeb. its own partition)

- **Data Validation and Profiling:**
    Data can be validated through many aspects and they are:
        1. Completeness: ensure all req. data is present
            Checks that can be done are - missing values, null counts, percentage of populated fields
        2. Consistency: ensures data values are consist across datasets even after perf. some oper. like importing,  etc.
            Checks are - cross-field validation, comparing data from diff. sources
        3. Accuracy - ensures data is correct, reliable and represents what it is supposed to
            Checks are - Comparing with trusted sources, validation against known standards
        4. Integrity - Ensures data maintains its correctness and consistency over its lifecycle and across systems.
            Checks are - Referential Integrity, Relationship validations

- **SQL Review:**
    - Aggregations - COUNT(*), SUM(col), AVG(), MAX/MIN(), With CASE (helps you apply filters on more than one condition inside single query instead of just a single filter if WHERE is used.)
![alt text](image-2.png)
    - Grouping
    - Sorting
    - Pivoting - Act of turning row level data into columnar data. (Sometimes it can be done through CASE clause)
![alt text](image-3.png)
    - SQL Joins - INNER, LEFT, RIGHT, FULL OUTER, CROSS OUTER
    - SQL Regular Expression ( ~ is the regex operator and ~* for case insensitive matching)- Way of searching a pattern in string (Similar to LIKE but more powerful)
![alt text](image-4.png)

SQL Coding test:

Task 1

` select     * from    titanic limit     10;`

`select     count(*)/100.0 as overall_rate from     titanic where     Survived == 1;`

`select    (( SUM(CASE WHEN Survived = 1 THEN 1 ELSE 0 END) ) * 1.0) / count(*) as women_children_rate  from    titanic where     (        Sex = 'female'        OR         Age <= 12    );`

`select    (( SUM(CASE WHEN Survived = 1 THEN 1 ELSE 0 END) ) * 1.0) / count(*) as others_rate from    titanic where    (        Sex = 'male'        AND         Age > 12    )`

Task 2:

`select     Pclass, SUM(CASE when Survived = 1 THEN 1 ELSE 0 END) * 1.0/count(*) as survival_rate from     titanic group by     Pclass`

Task 3:

`select     p.ProductName, s.CompanyName from     Products p LEFT OUTER JOIN Suppliers s ON p.SupplierID = s.SupplierID order by     p.ProductName ASC;`

- Git Review:
![alt text](image-5.png)

## Storage 

### Amazon S3 

- Building block of AWS, advertised as 'infinitely scaling' storage, many websites use s3 as their backbone, many aws services use s3 as an integration. S3 does not have hierarchy like File sytems. 
- Use cases: Backup, storage, Disaster recov. purpose, Archive, Hybrid cloud storage, app. hosting, media hosting, data lakes and analytics, soft. delivery, hosting static sites

    - **Buckets:** S3 allows us to store files known as 'objects' in directories known as 'buckets'. They must have globally unique name. Still Buckets are defined at the Region level only.
        Naming Conventions: 
        - No uppercase or underscore, ONLY lowercase or numbers or hyphen. 
        - Should not be an IP, not start with prefix xn--, not end with suffix -s3alias. 
        - Can be 3 to 63 char. long.
    
    - **Objects:** Objects are located at Full Path also known as 'Key' (i.e s3//bucket/key). Key is composed of "prefix + obj._name". Object values are the content of the body. Max. Object size is 5TB. If uploading file >5GB then you must use "multi-part upload".
        Objects have Metadata (list of text key-value pairs either by system or user) associated with it.
        Tags (Unicode key-value pair) - useful for security and lifecycle
        Objects might have version_id associated with it if 'Versioning' enabled.
    
- Security:

    - **User based Policies:** IAM Policies - which API calls should be allowed for specific IAM user

    - **Resource based Policies:** 
        - **Bucket Policies:**- Bucket wide rules from S3 console - allows cross account. - Object ACLs for finer control (although it can be disabled) - At Bucket level, we can also have Bucket ACLs which are less common though.
![alt text](image-6.png)
        - There are also bucket setting for ***Block Public Access*** which prohibits all access of bucket overwriting any bucket policy for public access. If you want all of your buckets to blocked for public access, you can use it at account level.

        - An IAM Principal can access an S3 object if user IAM permissions ALLOW it or Resouce policy ALLOWS it AND there are no explicit DENY.

        - For public access like on Internet, Use **Bucket Policy**.

    - Encryption: Objects encryp. using encryption keys.

- **Versioning**: Enabled at bucket level
    - If enabled, same key overwrite will change the versions (i.e from 1 to 2). After suspension of versioning, previous versions are not deleted.
    - After versioning is enabled, when an obj. is deleted, Delete Marker is put on it instead of permanently deleting. This way we can recover accidentally deleted obj.

- **Replication: (SRR [Same region replication] & CRR [Cross region repli.]) {Only works if versioning is Enabled}** - You can have buckets in same or diff. accounts as well. And proper IAM permissions must be given to S3.
    - Use cases: CRR - Compliance, low latency access, replication across acct., SRR - log aggre., live replication, replica. b/w prod. and test accounts
    - After this is enabled, Only new objects will be replicated and existing old objects can be replicated using S3 Batch Replication.
    - For delete operations, delete markers can be replicated from source to target by turning it on, deletions with version id are not replicated.
    - There is no chaning of replications like 1->2->3 BUT 1->3 X(not possible)

- **S3 Storage Classes:**
    - You can move b/w below classes manually or using S3 Lifecycle Config to move it autom.
    - S3 Durability (how frequent loss of object might happen) and Availability (how readily a service is available)
![alt text](image-7.png)

- **Storage Class Comaprison**
![Storage Class Comaprison](image-9.png)
    1. S3 Standard - Gen. Purp.  (No Retrival charges)
    2. S3 Standard IA (Retrival charges are applied on basis of per GB retrieved.)
    3. S3 One Zone IA (")
    4. S3 Glacier Instant Retrieval (")
    5. S3 Glacier Flexible Retrieval (")
    6. S3 Glacier Deep Archive (")
    7. S3 Intelligent Tiering  (No Retrival charges) [Smaller objects (<128 KBs) may be stored, but will always be charged at the Frequent Access tier rates, and are not charged the monitoring and automation charge.]
![alt text](image-8.png)
- **S3 Storage Price Comparison**
![S3 Storage Price Comparison](image-10.png)

- **S3 Lifecycle Rules:** It has transition actions to configure objects to transition to another storage class. And also it has expiration actions which configures object to expire(delete) after defined time. It also can be used to delete old versions of life if versioning enabled. Can also be used to delete incomplete Multi-part uploads 

- **S3 Analytics:** - Storage Class Analysis: Helps you decide when to transition objects to right storage class. Recommendations for only standard and std. IA (not for one zone or glacier)
    - Report is updated daily. - 24 to 48 hrs to start seeing data analysis

- **S3 Event Notifications** - Events are: s3:ObjectCreated, s3:ObjectRemoved, etc. You can also apply filters for objects like (*.jpg) for event notif. to be triggered only when this filters get satisfied with specified events. 
    For this events to succesfully trigger later services, we need to attach resource based policies to later resources like Lambda or SNS or SQS. We use this instead of creating IAM for S3.
![alt text](image-11.png)
    - Event Notif. with EventBridge, all events end up in EB, no matter what (Not sure abt. it). EB has over 18 services as detina. AND you can have advanced filtering options with JSON rules. You can send data to multiple destinations as well

- **S3 Performance:**
    - Baseline Perf. - 5,500 GET/HEAD reqs. and 3,500 PUT/COPY/POST/DELETE reqs. per Prefix per Second in a bucket. 
    - Multi part upload is necessary for files >5GB and is advisable to use for files >100 MB. S3 Transfer Accereration is used to increase transfer speeds by utilizing nearer edge locations and sending files from that edge pt. through Fast private aws connection.
![alt text](image-12.png)
![S3 perf. - Byte Range Fetches](image-13.png)

- **S3 Encryption:**
![alt text](image-14.png)
    - SSE-S3 type of encryption:
![alt text](image-15.png)
    - SSE-KMS ":
![alt text](image-16.png)
        There are some limitations: - You may be impaceted by KMS limits, - When you upload, you also invoke GenerateDataKey KMS API and when you download you use Decrypt KMS API. You only have 5500, 10000, 30000 req per second as KMS quota pr sec.
    - SSE-C ": (can only be done from console)
![alt text](image-17.png)
    - CSE type of encryption:
 ![alt text](image-18.png)
    - Encryption in Transit: If using https as endpoint instead of http, you can encrypt data in flight. It is recommended all the time and when using sse-c, it is mandatory.
    - Forced Encryption in Transit (aws:SecureTransport): It is used to force encryption in transit! If anyone uses http endpoint for req., they would be denied but if someone uses https, they might be allowed as SecureTransport would become True.
    - DSSE-KMS (Dual Layer SSE)

    - Default Encryption in S3 is now SSE-S3. You can also have checks on if any data is going encrypted or not by "Force Encryption" using Bucket Policy.
![alt text](image-19.png) 

- **S3 Access Points (When you have multiple app. having diff. sets of accesses needed)**
![alt text](image-20.png)
    - Access Point having VPC origin
![alt text](image-21.png)

- **S3 Object Lambda (Access point):** When you just need to make some changes to data when Retrieving it.
    - Firstly, app will invoke s3 object lambda a-p which will trigger lambda and then data will be fetched and changed data will be sent back to the user
![alt text](image-22.png)

- **S3 Object Lens:** It is used to understand, analyze and optimize storage across entire AWS org. Discover anonalies, cost efficiencies, apply data protection best practices across AWS org.
![alt text](image-23.png)
    - Metrics:
        1. Summary Metrics:
        2. Cost optimization metrics:
        3. Data protection metrics:
        4. Access-management metrics:
        5. Event metrics:
        6. Perf. metrics:
        7. Activity metrics:
        8. Detailed Status code metrics:

        You have 2 types of metrics in storage lens, 1. Free and 2. Paid. 
    
### Amazon EBS (on EC2 instances)

- EBS Volume is a network drive (not physical drive) which you can attach to your instances while they run. This allows us to have persistent data even after instances terminate. Some EBS volume types can be mounted to multiple instances.
- They are bound to a specific AZ.
![alt text](image-24.png)
- There is an delete on termination attb. attached to the EBS in EC2's console settings, which if turned on will delete ebs on termination of ec2 instance.
    EBS Elastic Volumes: Changing the EBS volumes and pereformance (IOPS) types as well without detaching or restarting your instance.
![alt text](image-25.png)

### Amazon EFS

- EFS is a managed NFS (N/w File System) that can be mounted on many EC2. EFS works with EC2 instances in multi-AZ. They are highly scalable, expensive (compared to EBS). 'Pay-per-use'.
![alt text](image-26.png)
    - EFS Performace Classes:
![alt text](image-27.png)
    - EFS Storage Classes:
![alt text](image-28.png)

### EBS V/S EFS
![alt text](image-29.png)
![alt text](image-30.png)
- Instance store is storage attached to EC2 itself. so if you terminate EC2, instance store also goes

### AWS Backup

- It is a fully managed service that centrally manage and automate backups across AWS services. No need to create script or processeses. - Supports Cross-region and also Cross-accounts backup.
- Supported services:   
![alt text](image-32.png)
![alt text](image-33.png)
![alt text](image-31.png)
- Backup Vault Lock:
![alt text](image-34.png)

## Database

- Traditional architecture (RDBMS) lacks horizontal write scaling and can only have horizontal read scaling by adding more read replicas but also upto a certain number only. Although it can have vertical scaling for both opn.
- NoSQL DBs are distributed and can have horizontal scaling. - Can't perform any JOINS or Aggregation functions, so all of the necessary and related data is present in one row.

### DynamoDB
![alt text](image-35.png)

    - Dynamodb is made up of Table and each Table would have a Primary Key that has to be decided at creation time only. - A table can have infinite number of items. - Each time has attbs.(which can be added over time - can be NULL). - Max size of an item is 400 KB. - Data types supported are: Scalar Types (String, Number, Binary, Boolean. Null), Document Types (List, Map), Set Types (String set, Number set, Binary set).
    
    - Defining a primary key in it can be done in 2 ways:
        1. Partition Key (Hash): Here, Part. key must be unique and diverse so that data is well distributed. Eg. User_id
        2. Partition Key + Sort Key (Hash + Range): Combination must be unique. Data is grouped by Part. key. Eg. User_id - Part. key and Game_id - Sort key for users-games table.
    
    - Read/Write Capacity modes: => Switching can be done once every 24 hrs only.
        1. Provisioned mode - 
![alt text](image-36.png)


    - 1 WCU(write capacity unit) represents 1 write per second for an item up to 1KB in size. If item is larger than 1KB, more WCUs are consumed.

    - RCUs are calculated based on the type of read opn. like Eventually consistent or Strongly consistent read (uses 2x RCUs). 1 RCU represents 1 Strongly consis. read or 2 Eventually consis. read per second for items upto 4KB in size
    
    - DynamoDB Partitions - Internal: Data is stored in partitions and part. keys go through a hashing algorithm to know which partition to go to. WCUs and RCUs are spread evenly across partitions. 
    
    - **DynamoDB - Throttling:**
![alt text](image-37.png)

        2. On-demand mode(expensive than provisioned) 
![alt text](image-38.png)

    - **Basic Dynamodb apis:**

        - Writting data:
                PutItem :- Inserts a new item or replaces an existing one with the same primary key. - Consumes Write Capacity Units (WCUs).  

                UpdateItem :- Modifies attributes of an existing item or creates it if not present.  - Supports Atomic Counters for incrementing numeric values unconditionally.  

                Conditional Writes  :- Operations only proceed if specified conditions are met; otherwise, they fail.  - Helps with concurrent access to items with no performance impact.  

        - Reading data:
                GetItem: (Used for getting single item, doesn't work on GSI)- Reads an item based on its primary key (HASH or HASH+RANGE).  - Default: Eventually Consistent Read; optional: Strongly Consistent Read (more RCUs).  - Use ProjectionExpression to return specific attributes.  

                Query:- Retrieves items using KeyConditionExpression (partition key required, sort key optional).  - Partition key must use '='; sort key supports '=', '<', '<=', '>', '>=', BETWEEN, BEGINS_WITH. (FilterExpression filters 'non-key attributes' after query execution.)  - Returns up to 1 MB or the number of items set in Limit.  - Supports pagination and can query a table, LSI, or GSI.  

                Scan:- Reads the entire table and filters afterward (inefficient).  - Returns up to 1 MB; use pagination to continue.  - Consumes high RCU; limit impact using Limit or reduce result size.  - Use Parallel Scan to increase throughput (scans run in parallel across segments).  - Can apply ProjectionExpression and FilterExpression with no extra RCU cost.  
        
        - Deleting data:
                DeleteItem:- Deletes a single item, optionally using a condition.  

                DeleteTable:- Deletes the entire table and all items faster than deleting individually.

        - Batch Operations:
                BatchWriteItem :- Performs up to 25 PutItem/DeleteItem operations per call (max 16 MB total, 400 KB per item). - Cannot update items. - UnprocessedItems must be retried (use exponential backoff or increase WCU).  

                BatchGetItem :- Retrieves up to 100 items (max 16 MB) from one or more tables. - Items are fetched in parallel to reduce latency. - UnprocessedKeys must be retried (use exponential backoff or increase RCU).  

**PartiQL**: - SQL-compatible query language for DynamoDB.  - Supports SELECT, INSERT, UPDATE, DELETE operations. - Can run across multiple tables. - Usable via AWS Console, NoSQL Workbench, APIs, CLI, and SDK.

- **Local Secondary Indexes (LSI) [Part to the ori. base table]:** They are alternative sort key (Part. key remanis the same). - It could be of any scalar type of attb. -We can have upto 5 LSIs per table. - They need to be defined at the time of table creation. - Attb projection: You can have all or some attb. of the base table. It uses main tables RCU and WCU.

- **Global Secondary Indexes (GSI) [Separate from base table]:** It has alternative primary key from base table. - It speeds up query on non-key attb. - Index key consists of scalar type attb. - Same attb. projection as LSI - You must provision separate RCUs and WCUs for the index - Can be added or modified later on as well unlike LSI. -> If writes are throttled on GSI, then main table will also be throttled.    

- **DynamoDB Accelerator (DAX):** Fully managed, highly available, seamless in-memory cache for DynamoDB. - Doesn't req. any app. logic modif. - Solves Hot key prob. (too many reads). - 5 mins TTL for cache by default. - Multi-AZ is preferable. - Secure.

- DAX (Should be used for caching objects or individual query or scan caches.) v/s Elasticache (Used to store some computed/aggregation results to be reused.)

- **D-DB Streams:** List of all modifications done on the table (Create/Update/Delete). - They can be sent to - Kinesis, Lambda, Kinesis Client lib. - Data retention upto 24 hrs. - Made up of shards just like Kinesis Data Streams
    - You have the ability to choose what would be written to the stream like Keys_Only, New_image, Old_image, New_and_old_image of the item.
    - Use-cases: React to changes in real time (to send welcome mail or something), - insert in some other services table - Implement CRR
![alt text](image-39.png)
    - DB Streams and Lambda:
    ![alt text](image-40.png)   

- **D-DB TTL:** It is based upon an attb. inside db table. It is in Unix Epoch format (basically time is in number and not proper timestamp or time format like 1:00 am or so on.) 
![alt text](image-41.png)

- You can use D-DB with S3 for - 1. Storing large objects of app in s3 and then just url of it in db. 2. Storing s3 object's metadata inside db table for easiness of querying.

- D-DB Security: Provides multiple layers of protection for your data.  
    - VPC Endpoints allow access to DynamoDB **without using the Internet**. - Access is fully controlled using **IAM policies and roles**. - Data is **encrypted at rest using AWS KMS** and **in-transit using SSL/TLS**. - Backup & Restore is supported, including **Point-in-Time Recovery (PITR)** like RDS, with **no performance impact**.

- **D-DB Global Tables:** Fully replicated, **multi-region and multi-active** tables for high availability and low latency. - Enables **real-time replication** across regions.

- **D-DB Local:** A local version of DynamoDB for development and testing. - Does **not require Internet** or connection to AWS services.

- **D-DB Migration:** You can use **AWS DMS (Database Migration Service)** to migrate data from sources like **MongoDB, Oracle, MySQL, S3**, etc., into DynamoDB.

- **D-DB User Access:** Clients like **web and mobile apps** interact with DynamoDB using **temporary AWS credentials**.  - These are obtained from **Identity Providers** such as:  Amazon Cognito User Pools,  - Google, Facebook, OpenID Connect  

- **D-DB Fine-Grained Access Control:** Control what each user can access inside DynamoDB.  - Use **Web Identity Federation** or **Cognito Identity Pools** to assign **IAM roles per user**.  - IAM roles can include **Conditions** to restrict access at:  
        - **Row level**: using `LeadingKeys` (limit access by primary key).  
        - **Attribute level**: limit visibility of specific attributes in items.

### RDS

- It is a hosted relational db. - It can be any of the follow.: - Aurora, MySQL, PGSQL, MariaDB, Oracle, SQL Server. - Offer full ACID compliance

- It is not used for Big Data.

- **Aurora (Compatible for MySQL (3x faster) and PGSQL(5x faster))** and also it is cheap compared to commercial dbs (1/10th times cheaper). - Has upto 128TB per db volume. - Upto 15 read replicas (replication across regions and AZs). - Cont. backup to S3. - Automa. scaling with Aurora serverless. 

    - Security: VPC n/w isolation. At-rest with KMS and in-transit with SSL.

- Locks in RDS: Rel. db implicitly have locks to prevent two things writing to it at the same time, or reading while a write is in process. We can also have explicit locks over tables and rows.

    - Types of Locks:
        1. Shared Locks: Allows reads, prevent writes. Can be held by mult. transactions (Syntax: FOR SHARE)
        2. Exclusive Locks: Prevents all reads and writes to resouces. Only one transac. can hold an exclus. lock. (Syn.: FOR UPDATE)
    - Example:
![alt text](image-42.png)

- **RDS Ops Guidelines:** Best practices to ensure performance and resilience of Amazon RDS. - Use **CloudWatch** to monitor memory, CPU, storage, and replica lag.  - Schedule **automated backups** during times of low write IOPS.  - If I/O is insufficient, **recovery after failure will be slow** – consider migrating to higher I/O instance types.- Use **General Purpose or Provisioned IOPS** storage for better performance.  
    - Set **DNS TTL to 30 seconds or less** in your applications.  - Always **test failover scenarios** before they're needed in production. - Provision **enough RAM** to hold your entire working data set.  
    - If **ReadIOPS is small and stable**, system is in good shape. - Use **API Gateway rate limits** to throttle and protect your RDS backend.

- **RDS Query Optimization:** - Use **indexes** to speed up SELECT statements.  - Run **EXPLAIN plans** to identify missing or inefficient indexes.  - Avoid **full table scans** by optimizing WHERE clauses.  
    - Periodically run **ANALYZE TABLE** to update table statistics. - Apply **engine-specific** query tuning techniques.

- **RDS MySQL/MariaDB Tweaks:** - Keep tables **well under 16TB**, preferably **under 100GB**. - Ensure **RAM can hold indexes** of frequently accessed tables.- Try to stay **under 10,000 tables** total. - Use **InnoDB** as the preferred storage engine.

- **RDS PostgreSQL Tweaks:** - While **loading data**, disable backups and Multi-AZ. - Tune parameters like `maintenance_work_mem`, `max_wal_size`, and `checkpoint_timeout`. - Temporarily disable `synchronous_commit` and `autovacuum`, and ensure tables are **logged**. - Use **autovacuum** in general operations.

- **RDS SQL Server Tweaks:** - Monitor **failovers using RDS DB Events**.  - Avoid enabling **simple recovery mode**, **offline mode**, or **read-only mode** – these break Multi-AZ.  - Deploy your instances across **all Availability Zones (AZs)**.

- **RDS Oracle:** - "Oracle is its own beast" – requires specific handling not covered in these general tweaks.

### DocumentDB [More flexible than DynamoDB *(_ig in queying and indexing_)*]

- As aurora is aws imple. of mysql and pgsql, Doc-DB is aws imple. of MongoDB (NoSQL DB) - Used to store, query and index JSON data. - Auto. scales upto millions of req. per seconds.

### Amazon MemoryDB for Redis

- Redis (It is intended to be used as cache with some durability) compatible, durable, in-memory database service. - Gives ultra-fast perf. with over 160 million req. per second - has redis-compatible apis. - durable in-memory data storage with Multi-AZ transactional log. - scale seamlessly from 10s GBs to 100s TBs of storage. Use cases: web and mobile apps, online gaming, media streaming, etc.
![alt text](image-43.png)

### Amazon Keyspaces (for Apache Cassandra)

- It is open-source NoSQL Distributed DB. - It is fully managed Apache cassandra compatible db service. - It is serverless, scalable, highly available, fully managed by AWS. - Autom. scales table acc. to traffic. - Tables are replicated 3 times across mult. AZ. Uses Cassandra Query Lang. (CQL). - Single digit millisecond latency at any scale, 1000s of req. per sec. - Capacity in 2 modes: On-demand and provisioned with auto-scaling. - Encryp., backup and PITR upto 35 days. Use cases: Store IOT data, time-series data, etc.

### Amazon Neptune

- Amazon Neptune: A **fully managed graph database** designed for highly connected datasets like **social networks**.  

    - Ideal for use cases where entities (like users, posts, comments, likes) are **interrelated** and form complex relationships (graph). - Supports scenarios such as Users being friends with each other. - These relationships form a **graph structure**, making Neptune the perfect fit.

- Neptune Infra and Performance:  - **Replicated across 3 AZs** for high availability. - Supports **up to 15 read replicas** for scalable reads.   - Can **store billions of relationships** with **millisecond-level query latency**. - Built to handle **complex and deeply connected queries** efficiently.

- Neptune Use Cases:  
    - **Social Networks**, **Knowledge Graphs** (e.g., interlinked Wikipedia articles), **Fraud Detection**, **Recommendation Engines**

- Query Language: Gremlin, openCypher, SPARQL
- Example Queries:  
    - **SPARQL**:  ``` SELECT ?person WHERE {  :Alice :knows ?person .} ```  
    - **Gremlin**:  ``` g.V().has('name', 'Alice').out('knows').values('name') ```  
    - **openCypher**: ```MATCH (a:Person {name: "Alice"})-[:KNOWS]->(b)  RETURN b.name ```


### Amazon Timestream

- Fully managed, fast, scalable, serverless Time series DB. - Auto. scales up/down to adjust capacity. - Store trillion of events per day. - 1000s faster and 1/10th of Rel. DBs. - Scheduled queries, multi-measure records, SQL compat. - Data storage tiering: Recent data kept in memory and historical data is kept in cost-optimized storage. - Built-in time series analytics functions (to find patterns in time-series data) - Encryp. in transit and at rest. Use cases: Iot apps, operational app., real-time analytics, etc.

- Architecture:
![alt text](image-44.png)


### Amazon Redshift

- Fully managed, petabyte-scale data warehouse. -It achieves so by using **ML, Massively parallel processing query execution, columnar storage** (also has column compression). Designed for OLAP, not OLTP

- Fast querying capabilities using SQL based clients and BI tools, just using ODBC and JDBC. You can connect any analytical and visualization tool you want on top of it. - Scale up and down based on demand. - Monitoring via cloudwatch (you can also add user-defined custom metrics using custom metrics feature)/ cloudtrail.

- Architecture:
    - It consists of cluster which has Leader node and for each leader node there can be around 1 to 128 Compute nodes depending on the node type. - Each cluster can store one or more dbs. - Data is stored on compute nodes and Leader node manages the communication with client programs and all comm. with compute nodes. - Leader node receives queries from client app., parses it and develops query execution plan which are ordered steps to process these queries. And then co-ordinates parallel execution plan with the compute nodes and then aggregates results and returns them as well. Compute nodes get query execution plan and complete the task by sharing data and so on... Each compute node has its own dedicated CPU, memory and attached disk storage determined by the node type chosen. Within compute nodes, we have compute slices and portion of storage and disk is allocated to each slice (no. of slices per node is determined by node size of cluster)
    
    ![alt text](image-45.png)

- **Redshift Spectrum:** Query exabytes of unstructured data in S3 without loading. - Limited Concurrency. - Horizontal Scaling. - Separate storage and compute resources. - Wide variety of open source data formats (including avro, csv, grok, ion, json, orc, parquet, rcfile, regx, sarat, sequencefile, text files and tsv). - Support of gzip and snappy compression.

- **Redshift Durability and Scaling:** Replication within cluster. - Backup to S3 (3 copies are maintained of your data, one in original, one in replica within cluster and one in S3). - For disaster recovery, automated snapshots are maintained in another region as well. - Failed drives/nodes are automatically replaced - As it is limited to 1 AZ, if AZ fails then you have to wait until it resumes. and if you have snapshot of it then you can resume it in diff. AZ inside same region. But now, RA3 clusters have ability to be in multi-AZ. 

    - Veritcal and horizontal scaling on demand. During scaling: - A new cluster is created while old one remains on. CNAME is flipped to new cluster (with just few minutes of downtime). - Then data is moved in parallel to new compute nodes

- **Redshift Distribution Styles:**
    1. AUTO: Redshift figures out based on size of the data
    2. EVEN: Rows are distributed across slices in round-robin fashion (Usedul when there are no joins necessary on table and also when you cant decide between Key or All distrib.)
    3. KEY: Rows are distributed based on one column
    4. ALL: Entire table is copied to every node (Appro. for relatively small tables)

- **Importing/Exporting data:**

    - If you want to load data into your cluster, you can use COPY command to do it most efficiently in distributed parallelized manners.

    - **COPY** Command: Most efficient way to load data into Redshift from external sources like S3, EMR, DynamoDB, or remote hosts (via SSH). - Requires IAM roles or key-based access. - If loading from S3, needs a manifest file (JSON) listing data files. - Supports decrypting data from S3 using hardware-accelerated SSL. - Can auto-compress data during load (gzip, lzop, bzip2). - Can apply **automatic compression** to optimize storage. - For **narrow tables** (many rows, few columns), use a **single COPY transaction** to avoid hidden metadata overhead.   - Used **only for loading from external sources**, not for intra-Redshift data transfers.

    - **UNLOAD** Command: Used to export data **from Redshift to S3** in parallel. - Useful for archiving or external processing.

    - Enhanced VPC Routing: Ensures COPY/UNLOAD traffic stays within VPC. - Prevents traffic from going over the public internet. - Requires correct VPC setup (endpoints, NAT, IGW, etc.).

    - Auto-Copy from S3: Monitors an S3 bucket and **automatically loads new data** into Redshift (no manual COPY).  

    - **Aurora Zero-ETL:** Automatically replicates data from Amazon Aurora **into Redshift** in real-time.

    - **Redshift Streaming Ingestion:** Streams real-time data from **Kinesis Data Streams** or **MSK (Kafka)** directly into Redshift.

    - **Intra-Redshift** Data Handling: - Use **INSERT INTO SELECT** or **CREATE TABLE AS** to handle data **already inside Redshift** (not COPY).  

    - Snapshot Copy to Another Region:  
        - For KMS-encrypted clusters:  
            - Create a **KMS key** in the destination region.  
            - Create a **snapshot copy grant** using that key.  
            - In the source region, **enable snapshot copy** using the created grant.  
            - Enables secure, cross-region snapshot replication.

    - **DBLINK:** Extension to connect **Redshift with PostgreSQL (RDS)**. - Enables syncing or combining capabilities of Redshift (columnar) and Postgres (row-based). - Both must be in same AZ. - Requires proper **VPC security group config** and **SQL setup** in RDS PostgreSQL to establish the link.
    
- Redshift Integration with other services like S3, DynamoDB, EMR/EC2, Data Pipeline, DMS.

- **Redshift Workload Management (WLM)**: Prioritize short, fast queries vs long, slow queries. It works bt creating Query Queues at runtime acc. to service classes. You can modify WLM to create separate queues for short and long running queries. You can do all of it using console, cli or redshift api.

- **Redshift Concurrency Scaling:** Auto. adds cluster capacity to handle increase in concurrent read queries. - Can support unlimited concurrent users and queries. WLM queues manage which queries are sent to the concurrency scaling cluster.

- There also exists ***Automatic Workload Management*** which can create upto 8 queues (Default 5 queues with even memory allocation). - Large queries (i.e big hash joins) -> Concurrency lowered and Small queries (i.e inserts, scans, aggre.) -> Concurrency raised. - Conifguring query queues can be done by setting up priority queue or set concurrency scaling mode, user groups, etc.

- There is another type of WLM, and it is ***Manual Workload Management:*** One default queue with concurren. level of 5 (i.e 5 queries at once) and also superuser queue (with concurr. level 1). you can defined upto 8 queues with conc. level of upto 50. You can also define query hopping.

- **Short Query Acceleration (SQA):** Prioritize short-running queries over long-running ones. - Short queries run in a dedicated space, wont wait in queues behind long queries. - This can be used in place of WLM queues for short queries. - Works with: Create Table as (CTAS), Read only queries. - Uses ML to predict a query's exec. time. - Can configure how many second is 'short'

- **VACUUM** Command: It is used to recover space from deleted rows. 
    There are 4 types of it:
        1. VACUUM FULL (default): It resorts all rows and reclaims space from deleted.
        2. VACUUM DELETE ONLY: It justs reclaims deleted rows.
        3. VACUUM SORT ONLY: It just resorts all rows and doesn't reclaim space.
        4. VACUUM REINDEX: It is used for re-initializing interleaved indexes (so here it will reanalyze distib. of values in table sort column and then perform full vacuum)

- **Redshift Anti-patterns:** - Small Datasets (use RDS), OLTP (use RDS or D-DB instead), Unstruct. data (ETL first with EMR, Glue etc.), BLOB data (store references to large binary files in s3)

- **Resizing Redshift Clusters:**

    - **Elastic Resize**: - Used to quickly **add/remove nodes of the same type** in a Redshift cluster. - Minimal downtime (a few minutes), often maintains active connections. - Limited to **doubling or halving** cluster size for some node types (e.g., DC2, RA3). - Best for **scaling capacity** without changing node types.  

    - **Classic Resize**:  - Used when you need to **change node types** or make more complex size changes. - Cluster becomes **read-only** during the resize (can take **hours or days**). - Necessary when elastic resize limitations are not sufficient.  

    - **Snapshot–Restore–Resize Strategy**: Helps **minimize downtime** during a classic resize.   - Ensures original cluster remains available while new one is provisioned.
        - Steps:  
            1. **Take a snapshot** of the original cluster.  
            2. **Restore** that snapshot into a new cluster.  
            3. **Resize** the new cluster as needed (change node types or size).  
            4. **Switch traffic** to the new resized cluster once ready.  

- **RA3 Nodes, Cross-region Data sharing, Reshift ML:**

    - **RA3 Node Types** (2019/2020):  - Decouples **compute and storage**—scale each independently. - Uses **managed storage** to optimize costs and performance. - Required for **Cross-Region Data Sharing**.

    - **Redshift Data Lake Export** (2020): Export query results to **Amazon S3** in **Apache Parquet** format. - Parquet is **twice as fast** to unload, **6× smaller**, and **partitioned automatically**.  - Data is compatible with **Athena**, **Redshift Spectrum**, **EMR**, **SageMaker**, etc.

    - **Spatial Data Types** (2021/2022): Support for **geometry** and **geography** types for mapping/GIS applications.

    - **Cross-Region Data Sharing** (2022): Share **live data across clusters and regions** without copying.  - Works across **accounts**.  - **Only available with RA3 nodes**.

    - **Amazon Redshift ML (2021)**:  - Create and deploy **ML models with SQL commands** via `CREATE MODEL`. - Trains models using **Amazon SageMaker Autopilot**.- Predictions available via **SQL functions** in Redshift. - Involves **additional SageMaker and S3 costs**.  
    - High-level flow:  1. Export training data from Redshift to S3. 2. Train with SageMaker Autopilot. 3. Register prediction function in Redshift. 4. Use SQL to get real-time predictions.

- **Redshift Security Concerns:**

    -  **Hardware Security Module (HSM) Integration**: Redshift can integrate with **HSM** for enhanced encryption key management. - To establish a **trusted connection** between Redshift and HSM:
        - Use a **client certificate** and a **server certificate**.

        - **Migrating to HSM encryption**: - You **cannot add HSM encryption** to an existing unencrypted cluster. - Instead, **create a new HSM-encrypted cluster** and **manually migrate data** to it.
    
    - **Access Control via SQL GRANT/REVOKE** - Redshift uses standard SQL commands for access control: - `GRANT <permission> ON <object> TO <user_or_group>`. - Permissions include: `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `DROP`, `ALL`, etc. - Can be applied to individual **users** or **user groups**. - To revoke privileges: Use `REVOKE <permission> ON <object> FROM <user_or_group>`.

    - Key points: - Use **GRANT/REVOKE** for fine-grained control of access. - Use **certificates** to securely connect to HSMs. - **Cluster encryption method (e.g., HSM)** must be decided at creation—**not modifiable afterward**.

- **Redshift Serverless:** Automatic scaling and provisioning for your workload, optimizes your cost and perf. (Pay only for what you use). - Uses ML (under hood) to maintain perf. across variable and sporadic workloads. - Easy spinup of development and test env. - Easy ad-hoc business analysis. - Once you start it, you get a connection url which you can connect to through JDBC or ODBC. You can also use console's query editor as well.
    - To use it, you need an IAM role. Once done, you just have to define name of the db, admin user cred., VPC, Encryp. settings and Audit logging. - You can also manage snapshots and recovery points after creation.
    - Capacity is measure in Redshift Processing Units (RPUs). You only pay for 'RPU-hours (per second) + Storage'
    - You can have Base RPUs (it defaults to auto) and then you can also adjust RPUs afterwards. - You can also have Max RPUs set.
    - Redshift serverless can do everything Redshift did except: - Parameter Group, WLM, Aws partner integration, maintenance windows/ version tracks. - There are no public endpoints in Redshift serverless, you must have to access it within VPC

    - **Monitoring:** - You are provided with monitoring views like: SYS_QUERY_HISTORY, SYS_LOAD_HISTORY, etc. for monitoring. - You can also use CloudWatch logs, metrics published to cloudwatch are QueriesCompletedPerSecond, QueryDuration, QueriesRunning, etc. And you can break it down by various dimensions like DatabaseName, latency, QueryType, etc.

- **Redshift Materialized Views:** Just like views (which are just table-like snapshots of query performed on table, we can further query it as well just like a normal table) but also stores the results of query. This improves the perf. as we using pre-computed results and are not querying whole table again. - You can keep refreshing the view to have latest data. - You can also stack materialized views.
    - Useful for predictable and recurring queries

- **Redshift Data Sharing:** Securely share live data across redshift clusters for read purposes. - Useful for sharing data between dev/test/prod.. cross-group collab. - You can share DBs, schemas, tables, views or UDFs as well. - It works on Publisher/Subscriber architecture where producer controls the security, we also have isolation ( Consumer cluster doesn't affect producer clusters working) and also data is live and transactionally consistent.
    - To use it, both clusters must be encrypted and must use RA3 nodes. - Cross region data sharing involves transfer charges. Types of data shares: Standard, AWS Data Exchange, AWS Lake Formation - managed

- **Redshift Lambda UDF:** Use custom functions in AWS lambda (using any lang. you want) inside SQL queries to do anything you want. - You can do it with using 'CREATE EXTERNAL FUNCTION'. ` CREATE EXTERNAL FUNCTION <func_name_in_redshift>(INT,INT) RETURNS INT VOLATILE LAMBDA '<lambda_func_name>' IAM_ROLE '<iam_role>';` - Must grant usage on language exfunc for permissions. - You can use AWSLambdaRole IAM policy to grant permissions for Lambda to your cluster's IAM role or you can create another role for it as well. But make sure that you pass on the proper role while creating ext. func. - Redshift communicates with Lambda using JSON.

- **Redshift Federated Queries:** Query and analyze across DBs, warehouses and lakes. - Ties Redshift to RDS or Aurora. - Incorporate live data from RDS into your redshift queries, avoid the need for ETL pipelines. - Offloads computations to remote DBs to reduce data movement by using instances of RDS or so (Cost will be incurred on those external db as you will be using them for computations)
    - To use RDS with it, you must first need to establish connection between redshift and RDS/Aurora by putting them in same VPC subnet or by using VPC peering (for this to work you cant have overlapping IP address ranges). - Credentials must be stored in AWS secrets manager. - You can connect using CREATE EXTERNAL SCHEMA (can also connect to S3/Redshift spectrum this way)

- We also have Redshift System tables and Views which contain info about how Redshift is functioning. Types of these tables are: SYS views (monitor query and workload usage), STV tables, SVV views, STL views, SVCS views, SVL views (details about queries on main cluster)

- **Redshift Data API:** Secure HTTP endpoint for SQL statements to Redshift clusters (provisioned or serverless) and have individual or batch queries. You can use it through SDK (which means you can use it any of various supported language). - It is asynchronous and does not require to use drivers or managing connections. - Passwords are sent via AWS secret manager and not directly in api, you can also have temp. credentials in redshift. 
    - You can also use Data API with other AWS services and not just SDK, services are Step functions, Eventbridge, EC2, Lambda, API Gateway, Sagemaker, Batch.
    - Some More points are:
    ![alt text](image-46.png)

## Migration and Transfer

### Application Discovery Service & Application Migration Service

- Applicaton Discovery Service: Plan migration projects by gathering information about on-premises data centers. - Server utilization data and dependency mapping are imp. for migrations. - It will help you to understand what you need to move and how they are interconnected.
    - There are 2 types for discovery:
    ![alt text](image-47.png)

- Application Migration Service (MGN): - It helps with the actual migration of application to AWS. - Used to be called 'CloudEndure Migration'. - It does so by replicating current data and then after you can shut down already hosted server. 
![alt text](image-48.png)

### Database Migration Service (DMS)

- Quickly and securely migrate dbs to aws. It is resilient and self-healing. - Source db can remain available while this happens. - It supports Homogeneous and Heterogeneous replications. - It also provides continuous data replication using CDC. - To use DMS, you must create EC2 instance to perform the replication tasks.
    - Sources & Targets:
    ![alt text](image-49.png)

- DMS Schema Conversion Tool: To convert your db schema from one engine to another.

- DMS Continuous Replication:
![Example](image-50.png)

- DMS Multi-AZ Deployment:
![alt text](image-51.png)

### AWS Datasync

- Move large amount of data Securely (uses SSL/TLS) to and from On-premises/other cloud to AWS (needs agent), from AWS to AWS (no agent needed). - It can sync to S3 (any storage class), EFS, FSx (windows, Lustre, NetApp, OpenZFS). - Replication task can be scheduled hourly, daily or weekly. - File permissions and metadata are preserved (NFS POSIX) 
- One agent task can use 10 Gbps, you can bandwidth limit
- Architecture of on-premise to AWS: If you dont have enough bandwidth, then you can use snowcone (as it comes with datasync on it).
![alt text](image-52.png)
- AWS to AWS services (metadata is also copied):
![alt text](image-53.png)

### AWS Snow Family

- If it takes more than 1 week to transfer data, use Snow devices.
![alt text](image-55.png)

- AWS Snowball:
![alt text](image-54.png)

    - We can also do Edge Computing with Snowball.
    ![alt text](image-56.png)

### AWS Transfer Family

- A fully managed service for file transfers into and out of Amazon S3 ot Amazon EFS using FTP protocol. It supports: AWS Transfer for FTP, " FTPS (FTP over SSL), " for SFTP (Secure FTP).
![alt text](image-57.png)

## Compute

### EC2

[Amazon EC2 offers a variety of instance types, each optimized for different workloads. Here's an extensive list of EC2 instance families and their typical use cases:

General Purpose Instances
T-Series (T2, T3, T3a, T4g): Burstable performance instances, ideal for web servers, small databases, and development environments.

M-Series (M5, M6a, M6g, M6i, M7a, M7g, M7i, etc.): Balanced compute, memory, and networking, suitable for enterprise applications, gaming servers, and caching.

Compute Optimized Instances
C-Series (C5, C6a, C6g, C6i, C7a, C7g, etc.): High-performance processors for compute-intensive applications like gaming, scientific modeling, and machine learning inference.

Memory Optimized Instances
R-Series (R5, R6a, R6g, R6i, R7a, etc.): Optimized for memory-intensive applications such as high-performance databases and big data analytics.

X-Series (X1, X1e, X2gd, X2idn, etc.): Designed for large-scale in-memory databases like SAP HANA.

U-Series (U-3tb1, U-6tb1, U-9tb1, etc.): Ultra-high memory instances for enterprise-grade applications.

Storage Optimized Instances
I-Series (I3, I3en, I4g, I4i, I7i, etc.): High-speed storage for transactional workloads like NoSQL databases.

D-Series (D2, D3, D3en): Optimized for dense storage applications such as Hadoop and data warehousing.

H-Series (H1): Designed for high disk throughput applications.

Accelerated Computing Instances
P-Series (P3, P4d, P5, etc.): GPU-powered instances for deep learning and AI workloads.

G-Series (G4ad, G4dn, G5, etc.): Optimized for graphics-intensive applications like video rendering and gaming.

F-Series (F1, F2): FPGA-based instances for hardware acceleration.

Inf-Series (Inf1, Inf2): Designed for machine learning inference workloads.

Trn-Series (Trn1, Trn2): Optimized for training deep learning models.

High-Performance Computing (HPC) Instances
Hpc-Series (Hpc6a, Hpc6id, Hpc7a, Hpc7g): Designed for large-scale scientific simulations and engineering workloads.]

- EC2 in Big data:
    
    - Types of instances:
        1. On demand: Don't know much but cant afford to lose data
        2. Spot: As they can be taken away by AWS anytime, you need to maintain checkpointing feature if you want to use it in big data.    
        3. Reserved: Long running clusters, dbs for over a year or so. (if reserved priorly then you can get huge discounts)
    
- Auto Scaling: You can leverage it for EMR (as EMR (Master, Compute (contain data) and Task (dont contain data) nodes) clusters use EC2). 
    - It is automated for D-DB, Auto-scaling grps, etc.

- EC2 Graviton Instance: Amazon's own family of processors which powers several EC2 instance types for Gen. purpose, Comp. optimized, Mem. optim., Stor. optimi., Acce. comput.
![alt text](image-58.png)

### Lambda

- A way to run code snippets in cloud. - It is serverless, continuosly scaling. - Why to use it? - Because running servers can get expensive when scaling, and there are times when you wont have any work on server. With lambda, you only pay for the processing time you have used.
    - Main uses of Lambda: - Real time file processing, Real time stream processing, ETL, Cron replacement, Process AWS events.

- Supported Languages: Python, Java, Node.js, etc.

- Services (somewhat partial) that can trigger Lambda are:
    ![alt text](image-59.png)
    - For Kinesis, Lambda continuously polls from stream and stream doesn't directly push new data

Lambda with Opensearch for logs from S3 (**Opensearch is search engine and also analytics engine, You can search, query, visualize data**)

- Lambda with redshift can be used to automatically copy new data from S3 to redshift, just like COPY cmd. But as Lambda is a **Stateless Service, it can't keep track of where you left off by itself**. To solve it, you can use D-DB to store where it left

- Lambda + Kinesis:
![alt text](image-60.png)

- Lambda - File System Mouting: Lambda functions can access EFS file systems if they are running in vpc.
![alt text](image-61.png)
- Lambda Storage options:
![alt text](image-62.png)

### AWS SAM (Serverless App. Model)

- Framework for developing and deploying serverless applications. - All the config. is YAML code, it generates complex CloudFormation from SAMYAML file. Supports anything from C-F. - SAM use CodeDeploy to deploy Lambda functions. - SAM can help you to run Lambda, API Gateway, DynamoDB locally.

- AWS SAM - Recipe (You must include Transform header which indicates its SAM template)
![alt text](image-63.png)
    - Flow:
![alt text](image-64.png)
    - SAM sync: It is set of features to reduce latency while deploying resources to AWS. - Sync your project (SAM template) to AWS. Sync. code changes to AWS without updating infra. (uses Service API and bypass C-F)
![alt text](image-65.png)

### AWS Batch

- Allows to run batch jobs based on docker images. - Dynamic provisioning of instances (EC2 & Spot instances). - Fully serverless, pay for the underlying EC2 instances. - You can schedule batch jobs using CloudWatch events or orchestrate batch jobs using AWS Step function.

- Batch V/S Glue:
![alt text](image-66.png)


## Containers

- Docker is a software dev. plat. to deploy apps. - Apps are packaged in containers that can be run on any OS. - Apps run the same everywhere, works with any lang, tech, OS. - Docker images are stored in Docker Repositories on either Docker Hub (public repo.) or **Amazon ECR (private repo.) [There also exists a public repo in ECR called ECR Public Gallery]**
    - Use cases: Microservice architecture, etc.

- Docker v/s VMs
![alt text](image-67.png)

- Getting Started with Docker: You would need Dockerfile to initliaze project and installing necessary dependencies on container.
![alt text](image-68.png)

- Docker Container Management on AWS
    - Amazon ECS: Amazon's own container platform
    - Amazon EKS: Amazon managed Kubernetes(which is open-source)
    - Amazon Fargate: Amazon's own 'serverless' container platform. - Works with ECS and EKS.
    - Amazon ECR: Store container images.

### Amazon ECS:

- ECS - EC2 Launch Type: Here you have to manage underlying EC2 instance for ECS cluster by yourself. - Each cluster must run ECS agent to register instance in ECS cluster. - AWS takes care of starting and stopping containers.
![alt text](image-69.png)

- ECS - Fargate Launch Type: You don't provision infrastructure/instances, all serverless. - You just create task definitions. Then AWS runs those ECS tasks based on CPU/RAM necessary. - To scale, just increase number of ECS tasks (no more EC2 instances) [Task ig are individual containers running which can respond to call.]

- Amazon ECS - IAM Roles for ECS
    - EC2 Instance Profile (valid only if you are using EC2 Launch Type):
    ![alt text](image-70.png)

- Amazon ECS - Load Balancer Integrations: ALB is supported and works for most use cases. But sometimes, you might need N/W Load balancer.

- Amazon ECS - Data Volumes [Persistant data - EFS & also you can't mount S3 as file system for ECS tasks.]
![alt text](image-71.png)

- Amazon ECR: Store and manage Docker Images on AWS. - Fully integrated with ECS, backed by Amazon S3.
![alt text](image-72.png)

### Amazon EKS:

- Kubernetes is an open-source system for automatic deployment, scaling and management of containerized (usually Docker) app. It supports deploy. through 2 modes: 1. EC2 instances or 2. Fargate. - Kubernetes is cloud-agnostic

![alt text](image-73.png)

    - Node types: 
        - Managed Node groups: Creates and manages nodes (EC2 instances) for you. Nodes are part of Auto scaling group managed by EKS. - Supports on-demand or spot instances.
        
        - Self Managed Nodes: Nodes created by you and handled by EKS. - Supports on-demand or spot instances.

        - AWS Fargate
        
- EKS Volumes:
![alt text](image-74.png)