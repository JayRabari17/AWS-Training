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
    Amazon AppFlow [SaaS App.]
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
    AWS DataSync [Move files to and fro AWS]
    AWS Transfer Family [Over file transfer protocols]
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
    5. ORC V/S Parquet: ![alt text](image-288.png)

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
![alt text](image-287.png)

**[You cannot move data to standard ia and one zone ia before 30 days but can move to other classes within 1 day as well]**

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

- **S3 Lifecycle Rules:** It has **transition actions** to configure objects to transition to another storage class. And also it has **expiration actions** which configures object to expire(delete) after defined time. It also can be used to delete old versions of life if versioning enabled. Can also be used to delete incomplete Multi-part uploads
**[Deletions are preferred over transition]** 

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

**[Customer managed key has more customization and also has more granular access control than aws managed key (AMK) ; - S3 Glacier vault is used to enforce regulatory and compliance controls on data access (you can specify controls such as “write once read many” (WORM) in a vault lock policy and lock the policy from future edits)]**
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

- **S3 Select**: There also exists s3 select to directly query only a subset of data from an object, using simple SQL expressions. It works on an object stored in CSV, JSON, or Apache Parquet format. It also works with an object that is compressed with **GZIP or BZIP2 (for CSV and JSON objects only)**, and a server-side encrypted object. You can specify the format of the results as either CSV or JSON, and you can determine how the records in the result are delimited.

- **S3 Glacier Select**: It works on glacier storage class and does not work on parquet format.
    
### Amazon EBS (on EC2 instances)

- EBS Volume is a network **drive** (not physical drive) which you can attach to your instances while they run. This allows us to have persistent data even after instances terminate. Some EBS volume types can be mounted to multiple instances.
- They are **bound to a specific AZ.**
![alt text](image-24.png)
- There is an delete on termination attb. attached to the EBS in EC2's console settings, which if turned on will delete ebs on termination of ec2 instance.
    EBS Elastic Volumes: Changing the EBS volumes and pereformance (IOPS) types as well without detaching or restarting your instance.
![alt text](image-25.png)

### Amazon EFS

- EFS is a managed NFS (N/w File System) that can be mounted on many EC2. EFS works with EC2 instances in multi-AZ. They are highly scalable, expensive (compared to EBS). 'Pay-per-use'.
![alt text](image-26.png)
    - EFS Performace Classes:
![alt text](image-27.png)
In bursting throughput mode, throughput increases as total size of data increases.
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
    
    - **Read/Write Capacity modes**: => Switching can be done once every 24 hrs only.
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

- **DynamoDB Accelerator (DAX):** Fully managed, highly available, seamless in-memory cache for DynamoDB. - Doesn't req. any app. logic modif. - Solves Hot key prob. (too many reads). - 5 mins TTL for cache by default. - Multi-AZ is preferable. - Secure. **[When throughput occurs, DAX can throttle req. AND also DAX does not automatically retry requests.]**

- DAX (Should be used for caching objects or individual query or scan caches.) **v/s** Elasticache (Used to store some computed/aggregation results to be reused.)

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

**[AWS Application Auto Scaling is used to adjust provisioned capacity according to usage patterns]**

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

**[We can inovke lambda function through a stored procdure or native function]**

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
            - Create a **KMS key** in the destination region [or use customer encyrption key through KMS only as you can not use kms key from another region ]
            - Create a **snapshot copy grant** using that key.  
            - In the source region, **enable snapshot copy** using the created grant.  
            - Enables secure, cross-region snapshot replication.

    - **DBLINK:** Extension to connect **Redshift with PostgreSQL (RDS)**. - Enables syncing or combining capabilities of Redshift (columnar) and Postgres (row-based). - Both must be in same AZ. - Requires proper **VPC security group config** and **SQL setup** in RDS PostgreSQL to establish the link.
    
- Redshift Integration with other services like S3, DynamoDB, EMR/EC2, Data Pipeline, DMS.

- **Redshift Workload Management (WLM)**: Prioritize short, fast queries vs long, slow queries. It works bt creating Query Queues at runtime acc. to service classes. You can modify WLM to create separate queues for short and long running queries. You can do all of it using console, cli or redshift api.

- **Redshift Concurrency Scaling:** Auto. adds cluster capacity to handle increase in concurrent read queries. - Can support unlimited concurrent users and queries. WLM queues manage which queries are sent to the concurrency scaling cluster.

- There also exists ***Automatic Workload Management*** which can create upto 8 queues (Default 5 queues with even memory allocation). - Large queries (i.e big hash joins) -> Concurrency lowered and Small queries (i.e inserts, scans, aggre.) -> Concurrency raised. - Conifguring query queues can be done by setting up priority queue or set concurrency scaling mode, user groups, etc.

**[Auto. WLM does not by itself provide the additional compute resources for scaling read and write capacity on-demand like concurrency scaling does.]**

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

    - **Snapshot–Restore–Resize Strategy**: Helps **minimize downtime** during a classic resize. - Ensures original cluster remains available while new one is provisioned.
        - Steps:  
            1. **Take a snapshot** of the original cluster.  
            2. **Restore** that snapshot into a new cluster.  
            3. **Resize** the new cluster as needed (change node types or size).  
            4. **Switch traffic** to the new resized cluster once ready.  

- **RA3 Nodes, Cross-region Data sharing, Reshift ML:**

    - **RA3 Node Types** (2019/2020):  - Decouples **compute and storage**—scale each independently. - Uses **managed storage** to optimize costs and performance. - Required for **Cross-Region Data Sharing**. [Also has ability to automatically offload infrequently accessed (cold) data to S3]

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

**[Dynamic data masking policies hide, obfuscate, or pseudonymize data that matches a given format ; Amazon Redshift supports column-level access control for data in Redshift via column-level GRANT and REVOKE statements]**

## Migration and Transfer

### Application Discovery Service & Application Migration Service

- Applicaton Discovery Service: Plan migration projects by gathering information about on-premises data centers. - Server utilization data and dependency mapping are imp. for migrations. - It will help you to understand what you need to move and how they are interconnected.
    - There are 2 types for discovery:
    ![alt text](image-47.png)

- Application Migration Service (MGN): - It helps with the actual migration of application to AWS. - Used to be called 'CloudEndure Migration'. - It does so by replicating current data and then after you can shut down already hosted server. 
![alt text](image-48.png)

### Database Migration Service (DMS)

- Quickly and securely migrate dbs to aws. It is resilient and self-healing. - Source db can remain available while this happens. - It supports Homogeneous and Heterogeneous replications. - It also provides continuous data replication using CDC. - To use DMS, you must create EC2 instance to perform the replication tasks. **[- AWS DMS does not migrate empty tables.]**
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
![alt text](image-286.png)
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

- Amazon ECS - Load Balancer Integrations: **ALB (works on layer 7 and cannot perform routing traffic, etc.)**  is supported and works for most use cases. But sometimes, you might need N/W Load balancer.

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

        [- EKS Karpenter: Automatically provisioning and deprovisioning of nodes based on the specific scheduling needs of pods, allowing efficient scaling and cost optimization.]
        
- EKS Volumes:
![alt text](image-74.png)


## Analytics

### Glue

- Service used to create table definitions and performing ETL (ETL jobs uses Apache Spark under the hood). - Serverless discovery and definition of table definitions and schema. - Main use is to serve as central metadata repository for data lake. - It will discover those schemas out of your unstructured data sitting in S3 and publish table def. for use in analysis tools.

- Custom ETL jobs can be trigger/event-driven, on-schedule, on-demand 

- **GLUE Crawler/ Data Catalog**: It scans S3 repositories and creates schema. - Can run periodically. - Populates Glue Data Catalog with table defintions. Once data is cataloged, then it can be queried like structured data using Athena, Spectrum, EMR or QuickSight.
![alt text](image-75.png)
    - **Glue Crawler and S3 Partitions**: G-C will extract partitions based on how the S3 data is organised. So, partition your data in S3 accordingly like if you need data per year or must you need according to devices?
    ![alt text](image-76.png) 

- **Glue + Hive**: Hive lets you run SQL-like (bcz it uses HiveQL) queries from EMR. - Glue Data Catalog can serve as 'Hive metastore' or you can also import Hive metastore into Glue.

- **GLUE ETL**: - Auto. code gen. - Scala or Python. - Encryption: Server-side (at rest) or SSL (in-transit). - Can be event-driven. - Can provision add. DPUs to increase perf. of underlying jobs. - Enabling job metrics can help you understand max. capacity in DPUs you need. - You can also plot max. needed executors (1 DPU = 2 executors) vs max. allocated executors in Glue console as well as data movement. - Errors can be reported to cloudwatch (could also integrate with SNS for notif.).
    - If generated code isn't proper, you can modify it as well. - You can also provide your own code (Spark(Scala) or PySpark(Py) scripts).
    - Target can be S3, JDBC(RDS/Redshift) or Glue D-C.
    - Glue Scheduler used to schedule the jobs. OR you can use Glue Triggers to automate job runs based on events.

- **GLUE ETL: The DynamicFrame** (Main struct. that we might be interating with): A DynamicFrame is a collection of DynamicRecords. - DynamicRecords are self-describing, have a schema. - Very much like a Spark DF but with more ETL stuff. - Scala and Python APIs
![alt text](image-77.png)
    - **AWS GLUE ETL: Resolve Choice**: Deals with ambiguities in DF and returns a new one. For eg. if two fields have same name. Four ways:
        
        1. make_cols: creates a new column for each type. (i.e price - price_string and price_double)
        2. cast: casts all values to a specified type.
        3. make_struct: creates a structure that contains each d-type.
        4. project: projects every type to a given type

- **GLUE ETL - Transformations**: There are many tranformations that you can use on your data. They are:  
    1.  Bundled Transformations: - DropFields, DropNullFields: Remove (null) fields. - Filter: Specify a function to filter records. - Join: To enrich data. - Map: add fields, delete fields, perform external lookups.
    2. Machine Learning Transformations: - **Findmatches ML**: Identify duplicate or matching records in your dataset even when the records do not have common unique identifier and no fields match exactly.
    3. Format conversions: CSV, JSON, Avro, Parquet, ORC, XML
    4. Apache Spark Transformation (All of the trans. that are part of Apache Spark even like K-means.) 

- **Glue ETL - Modifying Glue D-C**: Glue ETL script can update your schema and also partitions if necessary.
    1. Adding new partitions: Either re-rerun G-C or have the script use enableUpdateCatalog and partitionKeys options.
    2. Updating table schema: Either re-run G-C or use enableUpdateCatalog/updateBehavior from script.
    3. Creating new table: enableUpdateCatalog/updateBehavior with setCatalogInfo

    Restrictions: - S3 Only. - JSON, CSV, parquet only. - Parquet req. special code though. - Nested schema are not supported.

- **Running Glue jobs**: Time-based schedule (cron-style). 
    - Job bookmarks (persist state from job run, - prevents reprocessing of old data, - allows you to  process new data only when re-running on schedule, - works with s3 sources, - works with rel. db. via JDBC. [only handles new rows and not updated rows]).  
    - After completion of jobs And using Cloudwatch, you can fire off a lambda or sns notif. when ETL succeeds or fails OR invoke EC2, send event to kinesis, activate Step Function 

- **Glue cost model**: 
![alt text](image-78.png)
Notebook on development endpoint.

- **Glue Anti-patterns**: 
![alt text](image-79.png)
using multiple engines like hive, pig, etc. - EMR would be better for it

- Streaming data can be captured from kinesis or kafka and Glue supports serverless streaming ETL with cleaning and tranforming data in-flight running on Apache spark structured streaming.

- **Glue Studio**: Visual interface (no-code, although you can have some custom tranformations by writing your own code) for ETL Workflows. - Visual Job editor (- create DAG's for complex workflow), -sources include S3, Kinesis, Kafka, JDBC. - Tranform/sample/Join data. - Target to S3, or Glue D-C. - Visual Job Dashboard (Overviews, status and run times)

- **Glue Data Quality**: It is a feature that you can use inside your job to evaluate the quality of data coming in and if it violates certain parameters or rules defined by you, you can automatically fail the job or log it into cloudwatch. - It uses Data Quality Definition Language (DQDL).
![alt text](image-80.png)

- **Glue DataBrew** [Just for doing T in ETL]: Visual data processing tool, 'UI for pre-processing large datasets.' - i/p from S3, data warehouse, or database. - o/p to S3. - over 250 ready-made transformations (drag & drop). - You can create "recipies" of tranformations that can be saved as jobs within a larger project. - You can also define data quality rules in here. - may also create datasets with custom sql with redshift snowflake.
    - Security:
![alt text](image-81.png)
    - Handling PII in Databrew Transformation: 1. Substitution (Replace with random) (REPLACE_WITH_RANDOM), 2. Shuffling(SHUFFLE_ROWS), 3. Deterministic Encryption (same value results in same encrypted)(ENCRYPT), 4. Probab. Encryption, 5. Decryption, 6. Nulling out or deletion (DELETE), 7. Masking out (MASK_CUSTOM, _DATE, _DELIMITER, _RANGE), 8. Hashing (Crypto. Hash)

- **Glue Workflows**: Design multi-job, multi-crawler ETL processes run together. When choosing between step-func, glue workflow (Designed mostly for and within Glue part of AWS) and mwaa. You can create these workflows from aws blueprint or console (graphically) or api.
![alt text](image-82.png)
    - Triggers within workflow can start jobs or crawlers. - It can be on-scheduled basis based on cron expression. - Triggers can be fired/started also on demand and also through eventbridge events.
    ![alt text](image-83.png)

### Lake Formation

- Made on top of Glue. - Makes it easy to set up a secure data lake in days. - It manages loading data from external sources and monitoring data flows. - Setting up partitions. - Helps in managing encryption, keys. - Define tranform. jobs and monitoring them. - Access control. - Auditing. -  Anything that can be done with glue, can be done with lake formation
![alt text](image-84.png)
    EMR can also query lake formation now

- Pricing: Lake formation doesn't cost anything but underlying services like s3, emr, glue, athena and redshift incur charges

- Process of creating data lake:
![alt text](image-85.png)

- **Lake Formation Finer points (for exam)**:![alt text](image-86.png)
- **L-F - Governed Tables and Security (ACID compliance with even data lake)** (Concurrently do row-level access/updates/deletes without worrying with mix-up between mult. users): Governed Tables support ACID Transactions across multiple tables. - New type of S3 table, - works with streaming data too (Kinesis), - can query with Athena.- You can have granular access control with row-level and cell-level security in both governed and s3 tables. - incur additional charges.
    - with new features, you need to manage and perform storage optimization with automatic compaction feature
    - Data Filters (Column, Row and Cell level) in L-F: ![alt text](image-87.png)

### Amazon Athena

- Serverless interactive queries (SQL) of S3 data. - No need to load data, stays in S3. - Uses Presto under the hood. - Serverless - Supports many data formats like CSV, TSV, JSON, ORC, Parquet, Avro and also Snappy, Zlib, LZO, Gzip compression formats. - Structured, Unstrutured, Semi-structured.
    - Examples: ![alt text](image-88.png)

- **Athena Workgroups** (For isolation and managing access to people):  Can organize users/teams/apps/workloads into workgroups and can control and track costs by workgroup. - Integrates with IAM, CloudWatch, SNS. - Each workgroup can have: Query history, Data limits (limit to how much queries may scan by workgroup), IAM policies, Encryption settings.

- Athena Cost Model: Pay as you go, $5 per TB scanned, successfull or canceled queries count and failed doesn't. - No charge for DDL. - Columnar formats and also partitioning save a lot of money and give better perf. - Glue and S3 charges are excluded.
![alt text](image-89.png)

- Athena Anti-patterns: 1. Highly Formatted reports (Use Quicksight). 2. ETL

- Athena: Optimizing Perf. 
![alt text](image-90.png) You can use MSCK REPAIR TABLE to update current metadata table with new partition added anytime.

- Athena ACID Transaction support: - powered by 'apache iceberg'. To use it, just add "table_type = ICEBERG in create tabl"e command. - This allows concurrent users to safely make row-level modifications. - Compatible with EMR, Spark, anything that supports Iceberg table format. - Gives you time travel operations/queries (near past time) (recover data with select statement which are recently deleted) - Similar to governed table in L-F
![alt text](image-91.png)

- ***Apache Iceberg***: It is a table format for large scale data lakes (petabyte-scale) originally created from Netflix. - Offers ACID-compliance. - Schema evolution safely as data evolves. - Can also support partitioning. - Time travel queries. - Offers efficient metadata management and works with spark, flink, presto, trino, hive and NOW with Glue, Athena and EMR
![alt text](image-92.png)
- Iceberg + AWS Glue (Glue D-C)/S3 + Athena (in fig, instead of spark, you can think of athena)
![alt text](image-93.png)
    To use Glue D-C with iceberg you must make it compatible.
    ![alt text](image-94.png)

- Athena Finegrained access to aws glue d-c: - IAM based DB and table-level security (Broader than data filters in L-F) -> You can have policies that grants certain operations to the glue dbs. and also need a role for athena to use glue and your db. - You can have policies to block certain opn like show all table and stuff.

- Athena CTAS (Create Table as Select): Creates a new table from result of queries. - Also can be used to create a new table that's subset of another. - Can also be used to convert data to a diff. format.

- Athena for Spark (kinda like On top of): ![alt text](image-98.png)

**[Partitioning [should be used when data is having low cardinality] means Partitioning means organizing data into directories (or "prefixes") and Bucketing [should be used when data is having high cardinality and we need to store data as evenly as possible.] which means records that have the same value for a property go into the same bucket. ; => The UNLOAD statement is useful when you want to output the results of a SELECT query in a non-CSV format (Parquet, ORC, Avro, and JSON) but do not require the associated table. ; -> Athena allows you to set two types of cost controls: per-query limit and per-workgroup limit. For each workgroup, you can set only one per-query limit and multiple per-workgroup limits. ; Athena can only query Std. and std. ia classes]**
- **Athena Federated Queries**: 
![alt text](image-99.png)
![alt text](image-101.png)

### Apache Spark

- It is distributed processing framework for big data. It performs opn. in-memory. Supports Java, Scala, Python, R. - Spark is not meant for OLTP. - Features like Real-time analytics, Batch processing, ML, Spark streaming (integrated with kinesis, kafka, on EMR), Graph processing

- Working of Spark:
![alt text](image-95.png)

- Spark Components:
![alt text](image-96.png)

- Spark Structured Streaming:
    - As spark works on datasets (consider them as database only), they can be created as continuosly growing datasets from streaming data by appending it to dataset as it comes.
    - You can use spark streaming with kinesis (K Client Lib.)

    - Spark + Redshift: ![alt text](image-97.png)

**[Partition pruning allows Athena to skip irrelevant partitions during query execution]**
### Amazon EMR

- It is a managed Hadoop framework on EC2 instances. - Includes Spark, Hbase, Presto, Flink, Hive and more. - EMR notebooks can be used to run your scripts on your clusters. - Several integration points

- Cluster in EMR:
![alt text](image-100.png)

- Transient(Termminate when all steps are completed, i.e Loading, processing, storing data then shut down) vs Long-running clusters (must be manually terminated) ![alt text](image-102.png)

- EMR Usage: - Frameworks and app. are specified at cluter launch. - If you have long running cluster, then you can just connect to it. - OR submit ordered steps via console like processing s3/hdfs data and o/p to somewhere

- EMR/AWS Integration:
![alt text](image-103.png)

- Storage on EMR: 1. HDFS, 2. EMRFS (EMR File system) (Access S3 as if it was HDFS), 3. Local file system, 4. EBS for HDFS (deletes when cluster is terminated)
![alt text](image-105.png)
![alt text](image-104.png)

- EMR Pricing is per hour + EC2 charges. If you need to add temp. computing capab., you can add TaskNodes and you can also add/remove core nodes(bu rem. core needs may have data loss risk)

- EMR Managed Scaling (Prior was " automated ")![alt text](image-106.png)

- Hadoop: Framework for distrib. processing. 
![alt text](image-107.png)

- **EMR Serverless** (EMR on EKS): To start we just choose our release and runtime (Spark, Hive, Presto)
![alt text](image-108.png)
![alt text](image-109.png)
    - EMR Serverless Application Lifecycle: ![alt text](image-110.png)
- **Spark takes 10% more overhead capacity, so make sure that your initial capac. is 10% more than its needed**
- EMR Serveless Security
![alt text](image-111.png)

- **EMR on EKS**: ![alt text](image-112.png)

### Amazon Kinesis Data Streams

- Made of multiple shards. - You need to provision shards ahead of time. - data gets div. into shards. - Shard defines stream capacity in terms of ingestion and consumption rates. - It takes data from producers and give it to consumers of data.
![alt text](image-113.png)
    - You have retention period between 1 to 365 days. - Ability to repocess/replay data. - Once data is inserted into Kinesis, it is immutable. - Data shares the same partition goes to the same shard.
    - Capacity modes:
        1. Provisioned mode: Choose the number of shards provisioned, can scale manually or through API. Each shard gets 1 MB/s or 1000 records per second for i/p and for o/p each shard gets 2 MB/s (applicable to classic or enhanced fan-out consumer). - Pay for shard provisioned per hour.
        2. On-demand mode: No need to manage/provision capacity. - Default capacity is provisioned (4 MB/s or 4000 records per second) and then scales auto. based on observed throughput peak during last 30 days. - Pay per stream per hour and data in/out per GB.
    
    - Security: ![alt text](image-114.png)

- **Kinesis Producers**: 
![alt text](image-115.png)
Kinesis Agent is a linux program that is used to send logs from instance to kinesis data stream

    - SDK:
        - PutRecord(s) API
        - Exception during API calls: 1. ProvisionedThroughputExceeded Exception - Happens when sending more data (> MB/s or rec./s). - Make sure you dont have a hot shard (shard containing key getting accessed too much than others.) -> Soln.: Retries with backoff, increase shards, ensure partit. key is good one (more distrib.)

    - Producer Library: Easy to use and highly configurable C++/Java lib. - used for building high perf., long-running producers. - Auto. retry mechanisms. - has 2 types of apis: Synchronous and Asynchronous. - submits metrics to cloudwatch. - supports 'batching' (helps in increase throughput by going over the defined size and decrease cost). - configuration must be imple. by user, if needed. - KPL records are only 'decoded' with KCL or special helper library.
        - Batching in KPL:
        ![alt text](image-116.png)

        - When not to use KPL: 1. When we have an app that can't tolerate delays then we need to use AWS SDK directly.
        ![alt text](image-117.png)

    - Kinesis Agent: Monitor log files and sends them to Kinesis Data Streams. - Java based agent built on top of KPL. - needs to be installed 
    ![alt text](image-118.png)

- **Kinesis Consumers**: 

    - SDK:
       - **Classic**:
        ![alt text](image-119.png)

            GetRecords API: Records are polled by consumers from shard. Each shard has 2 MB total aggregate throughput. - This API can give data upto 10 MB/s (but then would have cooldown or throttle for 5 seconds) or 10,000 rec./s. You can have 5 GetRecords API per shard per second = 200 ms latency, i.e if 5 app. consume from shard, then each app. can have upto 400 KB/s received data. This can be solved by Enhanced-fanout

        - Client Library (KCL): Java-first lib. but exists for other languages too (Go, Python, .NET, etc.). - Read records from kinesis produced with KPL. - Share multiple shards with multiple consumers in one group, shard discovery. - Checkpointing feature to resume progess by leveraging D-DB for co-ord. and checkpointing. - Record processors will process the data. 
            - If you get ExpiredIteratorException then you should increase WCU in D-DB.
        ![alt text](image-120.png)
        
        - Kinesis Connector Library (can be replaced by Firehose or Lambda and is somewhat deprecated): Older Java Lib. and leverages KCL library. - Write data to: Amazon S3, D-DB, Redshift, Opensearch.

        - Lambda sourcing from Kinesis: It can source records from K-D-S. Lambda consumer has a library to de-aggregate record from KPL. - can be used to do light-weight ETL to S3, D-DB, Redshift, Opensearch, anywhere. - It can be used to send notif./email in real time. - Lambda has configurable batch size.

        - **Enhanced Fan Out**: Works with KCL 2.0 and AWS Lambda from and After Nov. 2018. Here instead of all consumers having aggregate of 2 MB/s per shard, each consumer can have 2 MB/s provisioned throughput per shard means that 2 MB/s per shard per consumer because it pushes data to consumer over HTTP/2. Reduce latency to ~70 ms

        - **Standard/Classic Consumers v/s Enhanced Fan out**: ![alt text](image-121.png)

**[A high IteratorAge could mean that the data is not being processed in a timely manner. One way to increase throughput when you use Kinesis Data Streams and Lambda is to increase the parallelization factor. This solution can cause multiple Lambda function invocations to concurrently process one shard. Therefore, this solution could increase performance.]**
    
- **Scaling K-D-S**: 

    - Operations: 
        1. Adding Shards: It is also called 'Shard splitting'. - Can be used to increase Stream Capacity (1 MB/s out data per shard). - can be used to divide 'hot shard'. - Once old shard is closed and deleted once the data expires.
        ![alt text](image-122.png)
        2. Merging Shards: It is used to decrease Stream capacity and save costs. - can be used to group 2 shards with low traffic. - Old shards are closed and deleted based on data expiration

    - **Out of order records** even though user gave data according to parti. key are fetched due to resharding. To prevent it, after a reshard, read your parent shard completely. This logic must be written by you if not using KCL.
    ![alt text](image-123.png) 

    - **Auto scaling** is not a native feature of Kinesis. - you need to make an api call to change number of shards with UpdateShardCount

    - Limitations: 1. Resharding must be planned in advance bcz it can't be done parallely. 2. And you can perform one resharding opn. at a time and it takes few seconds. For eg., 1000 shards' splitting to 2000 might take 8.3 hours. 
    ![alt text](image-124.png)

    - Handling duplicates for producers in K-D-S: Producer retries can create duplicates due to network timeouts. ![alt text](image-125.png)
    - Handling duplicates for consumers in K-D-S: Consumer retries can make your app read same data twice. ![alt text](image-126.png)

- Security:
![alt text](image-127.png)

### Amazon Data Firehose (previously known Kinesis Data Firehose) [Near real time service]

- It is used to store data into target destinations. - It is fully managed with no adminis. req.. - It is  near real time (buffer based on time and size, optionally can be disabled) - Load data into redshift/s3/opensearch/splunk. - Auto. scaling, - supports many data formats. - data conversion from JSON to parquet/orc (only for S3) [But for csv to json, you must use lambda]. - Data transformation through AWS lambda. - Supports compression only when target is S3. - Pay for the amount of data passed through. - Spark and KCL can't read from KDF.
![alt text](image-128.png)

- Data firehose delivery diagram:
![alt text](image-129.png)

- Firehose buffer accumulates records and is flushed based on time and size rules. Firehose will auto. increase buffer size to increase throughput.
**[- BUT When Kinesis Data Firehose's delivery stream scales, it can cause an effect on the buffering LIKE The overall buffer size (SizeInMBs) of the delivery stream scales proportionally but inversely. For example, if the capacity of Kinesis Data Firehose increases by two times the original buffer size limit, the buffer size is halved.]**

- **Data Streams v/s Firehose**: ![alt text](image-130.png)

- Troubleshooting problems:
    - Performace: ![alt text](image-131.png)
    - Producer side: ![alt text](image-132.png)
    - Consumer: ![alt text](image-133.png) ![alt text](image-134.png) ![alt text](image-135.png)

### Kinesis Data Analytics which is being supplanted/replaced by Managed service for Apache Flink - just a way to query stream data

- K-D-A for SQL app. (still left to be replaced): ![alt text](image-136.png)
- K-D-A + Lambda: ![alt text](image-137.png)

- K-D-A always used Flink(just a framework for processing data streams) under the hood. - but now supports Python or Scala. - Flink is a framework for processing data streams. - and is serverless.
![alt text](image-138.png)

- Random Cut Forest: It is a SQL function offered by K-D-A for anonmaly detection on any numeric columns in a stream.

- Costs: ![alt text](image-139.png)

### Amazon MSK (Managed Streaming for Apache Kafka)

- Alternative to Kinesis. - Fully managed Kafka on AWS. - Allow you to create, update, delete clusters. - MSK creates & manages Kafka broker nodes & Zookeeper nodes for you. - Auto. recovery from kafka failures. - Data is stored on EBS volumes. - Default msg size of 1 MB. but there is possib. of sending large messages (upto 10 MB)

- Architecture: ![alt text](image-140.png)

- Configurations: ![alt text](image-141.png)

- Security:
![alt text](image-142.png)
Kafka ACLs are not managed from IAM but within Kafka cluster.

- MSK - monitoring: ![alt text](image-143.png)

- **MSK Connect**: Managed Kafka connect (service used to connect Kafka to somewhere else and vice-versa) workers on AWS. - Auto scaling capabilities for workers. - pricing based on per-worker-per-hour
![alt text](image-144.png)

- **MSK Serverless**: ![alt text](image-145.png)

- **Kinesis Data Streams v/s MSK**: (Most of the times, choose K-D-S over MSK) ![alt text](image-146.png)

### Amazon Opensearch

- It was initially created as search engine, but currently it is also widely used for analysis and reporting (Petabyte-scale). - It is based on Lucene (Open source software).

- **Dashboards**: It is a visualization tool inside Opensearch for querying and analyzing and visualizing data stored in opensearch.
![alt text](image-147.png)

- Opensearch applications: - Full-text search - Log analytics - Application Monitoring - Security Analysis - Clickstream Analytics

- Opensearch concepts: ![alt text](image-148.png)

- **Index**: An index is split into shards. And each shard lives onto a node. - While storing, documents are hashed to particular shard.
![alt text](image-149.png) 

- There also exists redundancy in here.

- Different modes of opensearch:
    1. Fully managed (not serverless - thats diff.) ![alt text](image-150.png)

- Opensearch options: - Dedicated master node. - Domains (== Clusters). - Snapshots to S3. - Zone awareness.

- Security: ![alt text](image-151.png)

- Securing Dashboards with using Cognito bcz congnito is a web based service that is inside opensearch and needs to be visible even if opensearch is in VPC.

- Opensearch Anti-patterns: ![alt text](image-152.png)

- Storage types in Opensearch: ![alt text](image-153.png)

- Index State Management: Automates index management policies. for eg. you might have an index that are broken up for months and you just want data for just few years...
![alt text](image-154.png) ![alt text](image-155.png)

- Cross cluster replication: ![alt text](image-156.png)

- Opensearch Storage and Stability: ![alt text](image-157.png)

- Opensearch Performance: Memory pressure in JVM can result if: - you have unbalanced shard allocation across nodes. - you have too many shards in a cluster. To solve it, use fewer shards (if you have JVMMemoryPressure) by deleting old or unused indices.

- **Opensearch Serverless**: - On-demand autoscaling. - works against 'collections' instead of provisioned domain, and they are of types 'search' or 'time series' collections. - Always encrypted with KMS key. - Capacity here is measured in terms of OCUs ![alt text](image-158.png)

### Amazon Quicksight

- Business analytics and visualization tool in the cloud. - is fast, easy and fully serverless. ![alt text](image-159.png)

- Data Sources: ![alt text](image-160.png)

- SPICE (Super fast Parallel In-memory Calculation Engine): - uses columnar storage, in-memory, machine code generation. -accelerates interactive queries on large datasets. - each user gets 10 GB of spice. - it can accelerate queries that would time out in direct query mode (i.e Athena) but still it has a limit of 30 mins., if it takes more time than that, SPICE will time out.

- Use cases: - Interactive ad-hoc exploration/visualization of data. - Dashboards and KPIs. - **Analyze/visualize data from: -logs in s3, on-prem. db, RDS, Athena, Redshift, any SaaS app. like Salesforce or any JDBC/ODBC data source**

- Quicksight Anti-patterns: - ETL, use glue instead

- Security: ![alt text](image-161.png) ![alt text](image-162.png)

- Quicksight + Redshift Security: ![alt text](image-163.png) If you have enterprise edition of Quicksight there is a way to use Quicksight from cross region to data source (RDS/Redshift). ![alt text](image-164.png) OR ![alt text](image-165.png). For cross-account access: ![alt text](image-166.png)

- User Management: ![alt text](image-167.png)

- **Pricing**:
![alt text](image-168.png)
- With enterprise edition you get encryption at rest, microsoft active directory integration and SSO using SAML

- **Dashboards**: ![alt text](image-169.png)

- Quicksight ML Insights: ![alt text](image-170.png)

- Quicksight Calculated Fields: - Creates new fields based on others ![alt text](image-171.png)

- Level Aware Calculations (LAC): Control granularity of calculations (which may be independent and before agg. done at display level) ![alt text](image-173.png)

- LAC-W (window): Aggregate over a window or partition. - values calculated over some window are added to each row. ![alt text](image-172.png)

- FLOAT vs FIXED d-type: If you are using calculated fields, precision can become an isse with FIXED dtype (as FIXED deals with only 4 decimal points). - Rounding and calculations can cause accuracy/overflow issues. To solve it, use FLOAT dype which has precision of 16 significant digits.

## Application Integration

### Amazon SQS

- It is fully managed and can have multiple consumers and multiple producers. - It can scale from 1 msg/s to 15,000 msg/s. - Default retention period of messages is 4 days and max. of 14 days. - No limit to number of msgs. in queue. - Low latency (<10 ms on publish and receive). - Horizontal scaling in terms of consumers. - can have duplicate msgs (at least once delivery, occasionally). - can have out of order msgs (best effort ordering). - Limitations of 256 KB per msg sent. [Max Visibility timeout of 12 hours while default is 30 seconds. - Also has replayability]

- Producing Messages: Each msg would have a body, a msg attb. (optional), delay delivery (optional). - You get back a msg identitifer and MD5 hash of the body back from the SQS. ![alt text](image-174.png)

- Consuming Messages: - polls SQS for messages (receive upto 10 msgs at a time). - process the msg within visibility timeout. - delete msg using msg id and receipt handle. ![alt text](image-175.png)

- **SQS FIFO Queue**: - Lower throughput (upto 3000 per second with batching and only 300 without batching). - Messages are processed in order (FIFO) by consumer. - Messages are sent exactly **once**. - 5 min. interval de-duplication using 'Duplication ID'. 

- SQS Extended Client: If you want to send large messages (>256KB msg size limit) then you can use this Java lib. which uses S3 as companion. ![alt text](image-176.png)

- Use cases: ![alt text](image-177.png)

- SQS Limits: Max. of 120,000 in-flight messages being processed by consumers. - Batch req. has a max. of 10 messages - max 256 KB. - msg content is XML, JSON, Unformatted text. - Standard queues have unlimited TPS. - FIFO queues support upto 3,000 msgs/s. - max msg size is 256KB. data retention from 1 min to 14 days. - Pricing: - Pay per API req., pay per network usage

- Security: ![alt text](image-178.png)

- **Kinesis v/s SQS**: ![alt text](image-179.png) ![alt text](image-180.png) ![alt text](image-181.png)

- **Dead Letter Queues**: If you have a msg that can't be successfully processed by consumer then after 'MaximumReceives' threshold, you can move that msg into DLQ. ![alt text](image-182.png)

    - Redrive to Source: Feature to help consume messages in DLQ to understand what is wrong with them. - When our code is fixed, we can redrive the msgs from DLQ back into source queue (or any queue) in batches without writing custom code. ![alt text](image-183.png)

### Amazon SNS

- What if you want to send msg to more than one app. at the same time. Then you can use SNS which uses Pub/Sub model. - Producer send msg only to SNS topic. ![alt text](image-184.png) ![alt text](image-185.png)

- To publish in SNS, you need to use Topic Publish (using SDK) where you can create a topic, create subscriptions, publish to the topic and subscibers will automatically get all of the msg OR you can also use Direct Publish (for mobile app SDK) where you create a plat. app, plat. endpoint and publish to that endpoint.

- SNS Security: ![alt text](image-186.png)

- **SNS + SQS Fan out**: ![alt text](image-187.png) 
    - As each prefix in S3 can have only 1 event type, we can use 1 SNS with Fan out with multiple queues and other services also can be used. ![alt text](image-188.png)

- SNS + Amazon S3 through Kinesis Data Firehose: ![alt text](image-189.png)

- SNS FIFO Topic (Only can use SQS): ![alt text](image-190.png)

- You can also use Fan out with SQS FIFO.
- You can also message filtering to filter and send only filtered messages. ![alt text](image-191.png)

### AWS Step Functions

- Used to design workflows with advanced error handling and retry mechanisms outside of the code. - Easy visualization. - Audit of history of workflows. - Ability to wait for an arb. amount of time and also has a max. exec. time of a state machine with upto 1 year.
- Examples are: Using step function for creating a model building, creating a batch processing workflow ![alt text](image-192.png)

- Your workflow is called a 'state machine'. Each step in workflow is a 'state'. ![alt text](image-193.png)

### Amazon AppFlow: Fully managed service that enables you to securely transfer data bet.n SAAS app. and AWS ![alt text](image-194.png)

### Amazon Eventbridge (formerly CloudWatch Events) [can also integrate 3rd party SaaS apps and custom]

- With it, you can schedule CRON jobs (scheduled scripts), you can create event patterns (which are event rules to react to a service doing something), trigger lambda functions, send SQS/SNS messages. 
- Event Rules: ![alt text](image-195.png)
- You can have diff. types of event buses for diff. services. ![alt text](image-196.png)

- Schema Registry: Eventbridge can analyze events and infer the schema. It also allows you to generate code for your app, so that app can know in advance how data is struct. in event bus. - Schema can also be versioned.

- Resouce based policy: - Manage permissions for a specific Event Bus. ![alt text](image-197.png)

### Amazon MWAA (Managed Workflow for Apache Airflow)

- Apache airflow is a batch-oriented workflow tool. - It can develop, schedule and manage your workflows and also control how data flows and also your data pipeline. - Workflows are created using python code and DAGs are created in this code. - Uses Queues for holding the tasks. -- Has built-in retry mechanism.
- Amazon MWAA provides a managed service for Apache airflow so you dont have to deal with installing and maintaining it.
- Use cases: - Complex Workflows, ETL coordination, Preparing ML data
![alt text](image-198.png)

- Your DAGs(python code) gets uploaded to S3. - Then MWAA picks it up and orchestrates and schedules the pipeline defined by each DAG. - Runs within VPC. - Private or public endpoints are needed. - Auto scaling (Airflow workers autoscale upto the limits you define)
![alt text](image-199.png)
- Architecture: ![alt text](image-200.png)

### Engineering Pipelines

- Real-time Layer: ![alt text](image-201.png) Picture contains two options at start (D-S or Firehose), those are just examples.

- Video Layer: ![alt text](image-202.png)

- Batch Layer: ![alt text](image-203.png)

- Analytics Layer: ![alt text](image-204.png)

## Security, Identity and Compliance 

### Principle of Least Privilege

- Grant only the permissions required to perform task. - Start with broader permissions while developing and then lock it down once you have a better idea of exact services and operations req. by workload. - There is also a tool named IAM Access Analyzer that generates least prvilege policies based on your access activity. ![alt text](image-205.png)

### Data Masking and Anonymization - Dealing with PII or other sensitive data. 

- Masking obscufates (makes it unclear) data. ![redshift query for the same](image-206.png)

- Anonymization: Techniques: - Replace with random, Shuffle, Encrypt (deterministic or probab.), Hashing

OR just delete PII or don't even import in the first place

### Key Salting - Append or Prepend a random value ('salt') to data before hasing it.

- It prevents pre-computed 'rainbow table' attack where adversaries use pre-generated hashes of commonly used pass. to find matches. - Also ensures that same piece of data does not produce same hash across diff. instances due to unique salt. - Make sure to use strong, cryptographically secure random valus as salt. - also rotate salts periodically. - Each user should have a unique salt.

![Both have same passwords](image-207.png)

### Keeping data where it belongs - Some regions might have stricter policies and you can't store certain data there

![alt text](image-208.png) ![alt text](image-209.png)


### IAM: Users (Indiviudal people), Groups (Users can be aggre. to groups) & Policies (Actual permissions that are assigned to users/groups.) & also Roles (Assigned to services to access another service on our behalf)

- Whenever user is in multiple groups then they would have applicable policies from both of the groups through group inheritance.
- Policies Structure:
![alt text](image-210.png)

- IAM also has a Password Policy which allows you to create a policy in which you define what every users pass. should contain. - To further improve security, IAM also has MFA. MFA can be implemented by two ways: 1. Virtual MFA, or 2. Hardware devices containing security key.

### Encryption 101

- **Encryption in-flight** using **TLS/SSL**: - data is encrypted before sending and after receiving. - TLS certifications help with encryption (HTTPS). - Encryption in flight ensures no MITM (man in the middle) can happen.

- **Server-side** encryption at rest: - Data is encrypted after being received by server. and data is decrypted before being sent. - stored in encrypted form.

- **Client-side** encryption: - Data is encrypted at client side and then sent to server. Also decryption happens at client side.

### AWS KMS (Key Management Service) [Are region-specific BUT can use key from one acc. to another]

- Anytime you hear encryption for AWS service, most likely it will be KMS. - In KMS, AWS manages encryption keys for us. - Fully integrated with IAM for authorization. - Easy way to control access. - you can audit KMS key usage using CloudTrail. - Integrates with AWS services seamlessly. - Never ever store your secrets in plain-text, especially in your code. - you can have KMS key encryption available through API calls.

- **Key Types**: 1. Symmetric 2. Asymmetric (Public key is used while sending and private key will be used on receiver side) ![alt text](image-211.png)

- **Types of KMS Keys & Auto. Key Rotations**: ![alt text](image-212.png)

- Example of copying snapshots across regions: ![alt text](image-213.png)

- Steps for copying snapshots across accounts: 1. Create a snapshot, encrypted with your own KMS Key (Customer managed). 2. Attach a KMS policy to authorize cross account access. 3. share encrypted ss and 4. then (on receiver side) create a copy, encrypt (doubtful) it with CMK

- **KMS Key Policies**: ![alt text](image-214.png)

### Amazon Macie

- It is fully managed data security and data privacy service that uses ML and pattern matching to discover and protect your sensitive data in AWS. - It helps identify and alert you to sensitive data such as PII. ![alt text](image-215.png)


### AWS Secrets Manager

- Newer service, meant for storing secrets (like mostly for username and password, but other var. can also be stored for custome use case). - Capability to force rotation of secrets every X days. - Auto. gen. of secrets on rotation. - Integration with AWS services like RDS (Mostly meant for this service only), etc. - Secrets can be encrypted using KMS.
 - Multi-region secrets: ![alt text](image-216.png)

 ### AWS WAF (Web App. Firewall)

 - Protects your web app. from common web exploits (Layer 7 - that is HTTP and Layer 4 is with TCP/UDP). - Can be deployed on App. Load Balancer (cant be deployed on n/w load balancer), API Gateway, CloudFront, AppSync GraphQL API, Cognito user pool

 - Define Web ACL rules: like creating IP set (upto 10,000 IP add. in one) ![alt text](image-217.png)

 **[Can be deployed with Cloudfront, application load balancer, API Gateway]**


### AWS Shield - protect from DDoS attacks

- DDoS = Distrib. Denial of Service - which means many req. at the same time.

- Two tiers: 1. Shied Standard (Free and act. for every user), 2. Shield Advanced ![alt text](image-218.png)

### Services' Security

#### Kinesis

    - **Kinesis Data Streams**:  
        - **Encryption in flight**: via **HTTPS (SSL endpoints)**.  
        - **Encryption at rest**: using **KMS (server-side)**.  
        - **Client-side encryption**: must be implemented manually using custom libraries and the **Kinesis Producer Library (KPL)**.  
        - **VPC Endpoint**/**PrivateLink**.  
        - **Access note**: Using **KCL** requires **read/write access to DynamoDB** for checkpointing.

    - **Kinesis Data Firehose**:  
        - **Server-side encryption**: with **KMS**.  
        - **IAM roles**: required for delivering data to **S3, Redshift, Elasticsearch, or Splunk**.  
        - **VPC Endpoint**: supported for private access.

    - **Kinesis Data Analytics**:  
        - **IAM roles**: allow reading from streams and writing to destinations like **Kinesis Streams** or **Firehose**.  
        - **Secure integration** with input/output sources through IAM permissions.

#### SQS

    - **Encryption in flight**: via **HTTPS**.  
    - **Server-side encryption**: via **KMS**.  
    - **IAM policy**: required to use the service.  
    - **Queue access policies**: similar to **S3 bucket policies**, for additional control.  
    - **Client-side encryption**: must be done manually.  
    - **VPC Endpoint**: supported for private access.

#### **AWS IoT**:  
    - **Thing security**:  
        - Uses **X.509 certificates** or **Cognito identities**.  
        - Controlled through **IoT policies** (JSON format).  
        - Policies can apply to **groups** or **individual things**.  
        - Devices can be **revoked at any time**.  
    - **User access**:  
        - Managed with **IAM policies** (users, groups, roles).  
        - Controls API-level access.  
    - **Rules Engine**:  
        - Requires IAM **roles attached to rules** to perform actions (e.g., send data to Kinesis).


#### **S3 (Simple Storage Service)**:  
    - **Access control**:  
        - **IAM policies**, **bucket policies**, **ACLs**.  
    - **Encryption in flight**: via **HTTPS**.  
    - **Encryption at rest**:  
        - Server-side: **SSE-S3 (With it, each object is encrypted with a unique key)**, **SSE-KMS**, **SSE-C**.  
        - Client-side: via **S3 encryption client**.  
    - **Additional security**:  
        - **Versioning**, **MFA Delete**, **CORS**, **VPC Gateway Endpoint**.  
        - **Glacier Vault Lock** (WORM policy) for compliance and immutability.

#### D-DB

    - **Encryption in transit**: via **TLS/HTTPS**.  
    - **Encryption at rest**:  
        - **KMS** encryption for base tables and indexes.  
        - Three key options:  
            1. **AWS-owned key** (free)  
            2. **AWS-managed key** (`aws/dynamodb`, incurs charges)  
            3. **Customer-managed key** (user-defined, incurs charges)  
    - **Access control**: via **IAM policies** for API, DAX, and tables.  
    - **DynamoDB Streams**: encrypted same as the table.  
    - **VPC Endpoint**: supported via **gateway endpoint**.

#### **RDS (Relational Database Service)**:  
    - **Network isolation**: Deployed within a **VPC**.  
    - **Access control**: via **Security Groups** (specific ports, IPs, CIDR blocks).  
    - **Encryption at rest**: via **KMS**.  
    - **Encryption in flight**: via **SSL** (JDBC connection).  
    - **IAM policies**: control access to **RDS API**, not internal database users.  
    - **IAM Authentication**: supported for **PostgreSQL, MySQL, MariaDB** (not full access control).  
    - **User permissions**: managed **within the DB**, not through IAM.  
    - **TDE (Transparent Data Encryption)**: Supported by **SQL Server** and **Oracle** on top of KMS.

#### **Aurora**:  
    - Similar security model to **RDS**.  
    - **VPC**, **Security Groups**, **KMS**, and **SSL** supported.  
    - **IAM Authentication**: for **MySQL and PostgreSQL only**.  
    - **No support** for Oracle or SQL Server.

#### **Lambda**:  
    - **IAM Role**: each function requires an IAM role to define what resources it can access.  
    - **Data access**: IAM role controls access to **sources and targets** (e.g., S3, DynamoDB).  
    - **Secrets encryption**: via **KMS** for environment variables.  
    - **SSM Parameter Store**: can be used for encrypted configuration values.  
    - **VPC integration**: deploy Lambda within a **VPC** to access private resources (e.g., RDS).  
    - **CloudWatch Logs**: access controlled via IAM roles.

#### **Glue**:  
    - **IAM policies**: control access to Glue jobs and services.  
    - **SSL enforcement**: for JDBC database connections (**encryption in flight**).  
    - **Data Catalog**:  
        - Encrypted using **KMS** (encryption at rest).  
        - **Resource policies** can be used (similar to S3 bucket policies).  
    - **Connection password encryption**: with **KMS**.  
    - **Data written by Glue**: can use **SSE-S3** or **SSE-KMS**.  
    - **CloudWatch Logs encryption**: supported.  
    - **Job bookmarks**: can be encrypted for enhanced security.    


#### EMR

    - **Access & Roles**:
    - SSH access via **EC2 key pair**.
    - IAM roles attached to **EC2 instances**:
        - Needed for **S3 (EMRFS)** and **DynamoDB** access.

    - **Security Groups**:
    - Separate for **Master node** and **Core/Task nodes**.
    - Required for **node-to-node** communication (e.g., Spark, MapReduce).

    - **Authentication**:
    - **Kerberos**: integrates with **Active Directory**.
    
    - **Authorization**:
    - **Apache Ranger** (open source Role Based Access Control): must be set up on an **external EC2 instance** and connected to EMR.

EMR Encryption

    - **At-Rest: EMRFS (S3 Data)**:
    - Options: **SSE-S3**, **SSE-KMS**, **Client-side encryption**.
    - **SSE-C (SSEC)** is **not supported** by EMRFS.

    - **At-Rest: Local Disks**:
    - **HDFS encryption** (open source).
    - **Instance Store (NVMe)**:
        - Use **NVMe** or **LUKS encryption**.
    - **EBS Volumes**:
        - Use **EBS encryption via KMS** (supports root volume).
        - **LUKS** cannot encrypt root volume.

    - **In-Transit Encryption**:
    - **Node-to-node**: via **SSL**.
    - **EMRFS (S3)**: end-to-end encryption via **TLS**.

![alt text](image-219.png)

#### Opensearch

    - **Network Isolation**: through **VPC**.
    - **Access Control**:
    - Use **OpenSearch policies** (e.g., IP restrictions).
    - **Encryption**:
    - **At-rest**: via **KMS**.
    - **In-transit**: via **TLS/HTTPS endpoints**.
    - **Authentication**:
    - IAM or **Amazon Cognito** (e.g., **SAML** with AD).

#### Redshift

    - **Network Isolation**: via **VPC**.
    - **Security Groups**: to restrict cluster access.

    - **Encryption**:
    - **In-transit**: via **JDBC with SSL**.
    - **At-rest**:
        - Use **KMS** or **Custom HSM** (Hardware Security Module).
        - Supports **SSE-S3** as well.

    - **IAM Roles**:
    - Attach IAM roles to Redshift for **S3 integration**.
    - Used with **COPY** and **UNLOAD** commands.
    - Alternatively, embed **access/secret keys** in SQL.

#### Athena

    - **Access Control**:
    - Managed by **IAM policies**.

    - **Underlying Data**:
    - Stored in **S3** → inherits **S3 security**:
        - **IAM policies**, **bucket policies**, and **ACLs**.

    - **Encryption**:
    - At-rest: **SSE-S3**, **SSE-KMS**, **Client-side encryption**.
    - In-transit: via **TLS** between Athena and S3.
    - **JDBC driver** supports **SSL**.

    - **Fine-Grained Access**:
    - Managed via **AWS Glue Catalog security**.

#### Quicksight

    - **Authentication**:
    - **Standard edition**: IAM or email login.
    - **Enterprise edition**: **Active Directory / SAML-based federation**.
    - Supports **MFA (Multi-Factor Authentication)**.

    - **Encryption**:
    - **At-rest**: for data and **SPICE engine**.

    - **Granular Data Access**:
    - **Row-Level Security (RLS)**.
    - **Column-Level Security (CLS)**.

## Networking and Content Delivery

### VPC & Subnets Primer

- VPC: Private network to deploy your resources (regional resource)

- Subnets: Allows you to partition your network inside your VPC (AZ level resource). - To define access to internet and b/w subnets, we use Route Tables

    - Public Subnet: Can access Internet and vice-versa. 
    - Private Subnet: Not accessible by Internet.

- When you create an AWS account, automatically a VPC is created in each region and only public subnet is created for you to access it.

- **Internet Gateway** - routes/allows public subnet access to internet & **NAT Gateway(AWS-managed)/NAT Instances(self-managed) [are placed in public subnet]** - allows private subnet access to internet but not vice-versa. ![alt text](image-220.png)

### Network ACLs & Security Groups

- N/w ACL (First mechanism of defense) [Only used within subnets]: A firewall which controls traffic from and to subnet. - Can have ALLOW and DENY rules. - Are attached at subnet level. - Rules only include IP Add.

- Security Group (2nd one): A firewall that controls traffic to and from an ENI/EC2 Instance. - Can have allow rules only. - Rules include IP add. and other security groups\

![alt text](image-221.png)

- VPC Flow Logs: Capture info. about IP traffic going into your interfaces: VPC, Subnet, ENI ![alt text](image-222.png)

- **VPC Peering**: Connect 2 vpc privately using AWS' n/w. - Make them behave as if they were one. They must not have overlapping CIDR (IP ranges). - vpc peering is not transitive(must be established for each vpc)

- **VPC Endpoints (Only for S3 and D-DB) & VPC Endpoint Interface**: Endpoints allow you to connect to AWS services using a private n/w instead of public. - gives you enhanced security and lower latency to access AWS services. 
    - VPC Endpoint Gateway: Only for S3 & D-DB.
    - VPC Endpoint Interface: most services (including S3 & D-DB)
    - All only to be used within VPC.

- **Site-to-site VPN (Through internet) - Connect on-premise vpn to aws & Direct Connect (Private line) - establish a physical connection b/w on-premises and aws**: ![alt text](image-223.png)

- VPC Cheat Sheet: ![alt text](image-224.png)

- AWS PrivateLink (from VPC Endpoint Services family): Most secure & scalable way to expose a service to 1000's of VPC (From a marketplace provider pov) ![alt text](image-225.png)

### Amazon Route 53

- **DNS (Domain Name System)**: translates human friendly hostnames (urls) to machine IP addresses. - Uses hierarchical naming structure (like .com incorporates all of the .com websites and which be further divided by www or api.google.com or so) and is the backbone of the internet.
    - DNS Terminologies: Domain Registrar, DNS Records, Zone file, Name server, Top Level Domain, Second Level Domain... ![alt text](image-226.png) 
    - Working of DNS: ![alt text](image-227.png)

- **Route 53** is a highly available, scalable, fully managed and authoritative(meaning you can update DNS records) DNS. - It is also a domain registrar (meaning you can register your own domains there). ![alt text](image-228.png)

- Records: How you want to route traffic for a domain. ![alt text](image-229.png)
    - Record Types: A (maps hostname to IPv4), AAAA (maps hostname to IPv6), CNAME (maps hostname to another hostname) - target is a domain name that must have an A or AAAA record, can't create CNAME for top node of a DNS namespace (zone apex), for eg., you can't create example.com but you can create for www.example.com, NS (Name servers for a hosted zone, controls how traffic is routed for a domain) - Ip add. of servers that can help you get IP add. of dest

- Hosted Zones: A container for records that define how to route traffic to a domain and its subdomains ![alt text](image-230.png) ![alt text](image-231.png)

### AWS CloudFront (CDN)

- It is content-delivery network which caches content of your websites at edge locations to improve read performace. - Around 216 points of presence (edge locations). - DDoS protection (bcz world-wide integrations with aws shield and aws web app firewall)

- Sources of origin of caching data: ![alt text](image-232.png)

- Working from a high level:![alt text](image-233.png)

- **CloudFront v/s S3 CRR**: ![alt text](image-234.png)

- You can also use CloudFront to make your private S3 files accessible to public by creating an Origin Access Control (OAC) and adding OAC to S3 bucket policy.

- You can use Cloudfront with ALB or EC2 as origin as well using **VPC Origins** - this allows you to deliver content from your app hosted in your VPC private subnets (no need of exposing them to internet). ![alt text](image-235.png) OR prior to vpc origins, you could only connect your public ec2 instances to cloudfront. ![alt text](image-236.png)

- Cache Invalidation: If you updated your files of your back-end, but cloudfront would only refresh its cache after TTL has expired. - However you can force an entire or partial cache refresh by performing Cache invalidation (invalidating all of your cached file or files at a part. path)

## Management and Governance

### Amazon CloudWatch 

- **CloudWatch Metrics**: - Cloudwatch provides metrics for every services in AWS. - Metric is just a variable to monitor (CPUUtilization, NetworkIn...). - Metrics belong to namespaces (and each service has one namespace). - Dimension is an attribute of a metric (intance id, env., etc.) [for eg. Cpu utiilization metric can be related to specific instance id or so..]. You can have upto 30 dimensions per metric. - Metrics have a timestamp. - Once you have a lot of metrics, you can create a cloudwatch dashboard of metrics. - You can also create 'custom metrics' (for eg., metric for RAM).

- **Metric Streams**: Continually stream cloudwatch metrics to a destination of *your choice*, with a near-real time delivery and low latency. ![alt text](image-237.png)

- **Cloudwatch Logs**: Perfect place to store application logs. To start with it, you must define:
    1. Log groups: arbitrary name, usually represents application.
    2. Log stream: Within log group, you would have multiple log streams and they represent log instance within app/log files/containers.
    3. Log expiration policies: can define how long can log stay. (never expire, 1 day to 10 yrs.)
    - You can **send cloudwatch logs (export)** to: S3 (Batch export might take upto 12 hours - api call is CreateExportTask, not real time - for real time use Logs subscrip.), K-D-S, K-D-F, Lambda, Opensearch
    - Logs are encrypted by default. - Can setup KMS-based encryption with your own keys
    - **Sources**: ![alt text](image-238.png)


- **Cloudwatch logs Insights**: To query cloudwatch logs. - With it, you can search and analyze cloudwatch logs![alt text](image-239.png) ![alt text](image-240.png)

- **Cloudwatch Contributor Insights**: Analyze log data and create time series reports. - Display contributor data. ![alt text](image-285.png)

- **Cloudwatch log insights v/s contributor insights**: Contributor Insights identifies the top contributors to specific metrics (finding top contributors for patterns), while Log Insights provides interactive searching and analysis of log data (query and explore log data, find specific events and perf. aggregation)

- **Cloudwatch logs Subscriptions**: Get real time log events from Cloudwatch logs for processing and analysis. - Send to K-D-S, K-D-F, Lambda. - You can also have filter using Subscription Filter. ![alt text](image-241.png)

- **Cloudwatch logs Aggregation (Multi-region and account)**: ![alt text](image-242.png)
    - Also you can send cloudwatch log events to resource in diff. AWS account ![alt text](image-243.png)

- By default, logs from your EC2 will not go to cloudwatch. - You need to run a Cloudwatch agent on EC2 to push the log files you want. ![alt text](image-244.png)
- Cloudwatch Logs Agent (old one) & Unified Agent (latest one): ![alt text](image-245.png)
    - Metrics supported by Unified agent: ![alt text](image-246.png)

- **Cloudwatch Alarms**: Alarms are used to trigger notifications for any metric. - Various options (sampling, %, min, max, etc.). - Alarm states: OK, Insuff. data and ALARM (when alarm notifies). - Period: Length of time in seconds to evaluate metric

    - Alarm Targets: ![alt text](image-247.png)

- Composite Alarms: As alarms are on a single metric, we can create a composite alarm from multiple other alarms. - you can have AND or OR conditions with it. ![alt text](image-248.png)

- You can recover your EC2 instances if status checks metric is monitored. ![alt text](image-249.png)

- More about alarms: ![alt text](image-250.png)

### AWS CloudTrail 

- Provides governance, compliance and audit for your AWS account. - It is enabled by default. - Get an history of events/API calls made within your AWS accounts by: - Console, SDK, CLI, AWS service. - Can put logs from cloudwatch logs or s3. - A trail can be applied to all regions or a single region. - If a resource is deleted in AWS, check CloudTrail first.

- Events: Two types: 1. Management Events (Op.n perf. on resources in your AWS account. by default, they are logged), 2. Data Events (by default, data events are not logged) ![alt text](image-251.png)

- **Cloudtrail Insights**: Enable Cloudtrail insights to detect unusual activity in your account. - It can help detect inaccurate resource provisioning, hitting service limits, bursts of aws iam actions. - It analyzes normal management event to create a baseline and then continuously analyze write events to detect unusual pattterns. Anomalies appear in cloudtrail console. Events can also be sent to s3 or eventbridge event can also be generated.

- Events retention: Event are stored for 90 days in cloudtrail. To keep events beyond this period, log them to s3 and use athena

- **Cloudtrail Lake**: Managed data lake for cloudtrail events. - Integrates collection, storage, preparation and optimization for analysis and query. - Events are converted to ORC format. - Enables querying cloudtrail data with sql. - To enable it, use 'Create event data store' menu choice in the console. ![alt text](image-253.png)
    - By default, data is retained for upto 7 years. - You can specify event types to be tracked (i.e management events or data events) ![alt text](image-252.png)
    - Querying cloudtrail lake: ![alt text](image-254.png)
**[AWS CloudTrail Lake is designed specifically for the aggregation, management, and analysis of audit logs across multiple AWS accounts and services. It provides a centralized solution that enables enterprises to consolidate their AWS CloudTrail logs in one place.]**

### AWS Config

- It is a per-region service (can be aggre. across regions and accounts) which helps with auditing and recording compliance (settings/security sett.) of your AWS resources. - Helps record config. and changes over time. - It can be used to solve questions questions like: - Is there unrestricted ssh access to my security groups? Do my buckets have any public access? How has my ALB configurations changed over time?
    - You can receive alerts (SNS notif.) for any changes - You can also store config. data into s3 and then query it using athena. - You can use over 75 AWS config rules and also make custom **config rules** (must be defined in lambda) ![alt text](image-255.png)
    - As **config resource**, you can view compliance of a resource over time, view config. of a resource over time, view cloudtrail api calls of a res. over time.
    - **Auto-remediations**: Although you can't deny any actions but you can remediate and make non-compliant resources compliant using SSM Automation Documents ![alt text](image-256.png)
    - Config rules - Notification: ![alt text](image-257.png)

- ***Cloudwatch v/s Cloudtrail v/s Config***: ![alt text](image-258.png) 
    - Exemplary actions for an ELB: ![alt text](image-259.png)

### Deploying and managing infrastruture at scale

- **AWS CloudFormation**: It is a declarative way of outlining your AWS infrastruture, for any resources (most of them are supported). - Creates services in the same order and with exact same config. as specified

    - Benefits: - Infrastructure as code (IaC), Cost, productivity (ability to dest. and recreate app on the fly, auto. gene. of diagram of project), you can use already existing templates from internet as well (Dont re-invent wheel) And it supports almost all resources (also you can create custom resources if you want.) ![alt text](image-260.png) 
    - CloudForm. + Infrastructure Composer (to visualize diagrams and create stacks as well by drag and drop): ![alt text](image-261.png)
    - When using cloudformation, it is not advised to update anything manually, always do anything through cloudformation service only.

### Amazon SSM (Simple Systems Manager) Parameter Store

- It is a secure storage for configuration and secrets.- Optional seamless encryption using KMS. - Serverless, scalable, durable, easy SDK. - Version tracking of config./secrets. - security is provided through IAM. - notif. using Eventbridge. - Full integration with CloudFormation (meaning you can leveage to use parameters from parameter store as input param. for stack) ![alt text](image-262.png)
 - By creating hierarchies, you can easily manage and control accesses across your org. ![alt text](image-263.png) You can have access to secrets of secret manager using secret_id_in_Secret..
 - You have two tiers of parameter tiers (Standard and Advanced): ![alt text](image-264.png). You can also have parameter policies (only in advanced tier though) to add a TTL to a parameter to force updating or deleting sensitive data such as pass. 

### AWS Well Architected Framework

- It is a tool as well as a framework to create good app. on AWS

- General Principles: 
1. Stop guessing your capacity needs - Instead use auto-scaling groups and so on...
2. Test systems at production scale - With AWS, you can perform big test on big infra. and then instantly shut it down which makes it easy to do so..
3. Automate to make architectural exp. easier (like using cloudformation temp. to easily deploy app. in multiple env. for experimentation)
4. Allow for evolutionary architecture (Design based on changing req.)
5. Drive architectures using data
6. Improve through game days (try your app. in good prod. and see how you can improve OR simulate application by putting a lot of pressure on architecture)

- Principles: They need to be considered as synergy meaning if you improve one of them, there are many chances that some other will also improve.
1. Sustainability
2. Security
3. Reliability
4. Operational Excellence
5. Performance efficiency
6. Cost optimization

- **Well Architected Tool**: Free tool to review your archi. against 6 pillars. - You select your workload and answer questions and you will get answers to be reviewed against 6 pillars (results can be seen in dashboard.)

### Amazon Managed Grafana

- Grafana is a popular open-source platform used to monitor, visualize and alert on **metrics and logs**.
- AMG is integrated with IAM identity center and SAML for user management and permissions. - Compatible with grafana plugins and alerts. - It is fully managed, scales auto. - Data is encryp. at rest and in-transit (can also use kms key of your own)
- Data sources: ![alt text](image-265.png)

### Amazon DataZone - Cloud based management service that helps org. catalog, discover, share and govern data across various sources (AWS, on-premises systems, and third-party sources) [centralized platform for data cataloging, access control, and data governance]

## Sagemaker/ML

- **Sagemaker**: Fully managed service for dev./data scientists to build ML models. ![alt text](image-266.png)

### Sagemaker Feature Store

- A feature is just a property used to train ML model. - ML models req. fast and secure access to feature data for training. - It's also a challenge to keep it organized and share features across diff. models.
- Sources: ![alt text](image-267.png)
- In feature store, we have feature groups and each feature group contains record identifier, feature name and event time. - Data ingestion can be streaming (Online store is used) or Batch (S3 store). ![alt text](image-268.png)

### Sagemaker ML Lineage Tracking

- Creates & stores ML workflow (MLOps). - Keep a running history of models. - Tracking for auditing and compliance. - Auto. or manually-created entities. - Integrated with AWS Resource Access Manager for cross-account lineage. ![alt text](image-269.png)
- Entities in lineage tracking: ![alt text](image-270.png). To query lineage, use LineageQuery API from Python

### Sagemaker Data Wrangler

- It is a visual interface (in Sagemaker Studio) to prepare data for ML. - Import data. - Visualize data. - Transform data (300+ transform. to choose from) [Think of it as a code generation tool]
![alt text](image-271.png)
- Sources: ![alt text](image-272.png)
- After visualizing, transforming and also sometimes training a quick model, you can export whole data flow. ![alt text](image-273.png)
- Data wrangler troubleshooting: ![alt text](image-274.png)

## Developer Tools

- **Access Keys** (managed by user, access_key ~= username & secret_access_key~=password), **CLI** (A tool that enables you to interact with AWS services using command in your command shell & with it you get direct access to public APIs of AWS services), **SDK** (Language specific set of APIs (set of libraries) which enables you to manage AWS services programmatically) [CLI is built on top of AWS SDK for python (boto3)]

### AWS CDK

- Allows you to define cloud infrastruture using a familiar lang. - CDK is used to convert our known langauge code to YAML file which can then be used to directly deploy our code to cloud ![alt text](image-275.png)  

### AWS CodeDeploy

- We want to deploy our app. automatically (independent of Cloudformation stack) ![alt text](image-276.png)
    - CodeDeploy can deploy application content that runs on a server and is stored in Amazon S3 buckets, GitHub repositories, or Bitbucket repositories. CodeDeploy can also deploy a serverless Lambda function. You do not need to make changes to your existing code before you can use CodeDeploy.

### AWS CodeCommit

- It is discontinued now (and aws suggests to use external git alternatives like Github) ![alt text](image-277.png)

### AWS CodeDeploy

- It is code building service in the cloud which compiles source code, run tests and produces packages that are ready to be deployed (by CodeDeploy) ![alt text](image-278.png)

### AWS CodePipeline

- Orchestrate diff. steps to have the code auto. be pushed to production. - Basis for CI/CD ![alt text](image-279.png)

### AWS Cost Explorer

- (Only billing service that AWS might ask) Used to visualize, understand and manage your AWS costs and usage over time. ![alt text](image-280.png)

### Amazon API Gateway

- API G/w + Lambda = No infra. to manage. - We can have continuosly streaming data as we have support for WebSocket protocol. - Handle API versioning. - Handle diff. env. - Trans. and validate req. and responses. ![alt text](image-281.png)

- API gateway Integrations: ![alt text](image-282.png)

- API endpoint types: 
    1. Edge optimized (default): For global clients
    2. Regional: For clients within the same region
    3. Private: Can only be accessed from your VPC using VPC endpoint interface (ENI) ![alt text](image-283.png)

- Security: ![alt text](image-284.png)
