Introduction to what makes software engineering, what requirements there are for good software engineering. And the ethics of software engineering.
### Reasons for software failures
* Increasing demands
	* Faster development
	* Larger and more complex products
* Low expectations
	* Lack of software methods and techniques
	Causes more expensive and less reliable software.
	Can be fixed by better education and training.


### Software development
* Target group
	* Professional rather than individual
* Not only coding but also all associated documentation and configuration data, (guides, etc).
##### General software information

| Question                                                                    | Answer                                                                                                                                                                                                                                                      |
| --------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| What is software?                                                           | Computer programs and associated documentation. Software products may be [[#Generic]] or [[#bespoke (customized)]].                                                                                                                                         |
| What are the attributes of good software?                                   | Good software should deliver the required functionality and adhere to the characteristics in [[#Good software characteristics]] which include performance, maintainability, dependability, and usability.                                                   |
| What is software engineering?                                               | [[#Software engineering]] is a discipline that is concerned with all aspects of software production.                                                                                                                                                        |
| What are the fundamental software activities?                               | Software specification, software development, software validation and software evolution.  This is called the [[#Software process]].                                                                                                                        |
| What is the difference between software engineering and computer science?   | Computer science is focuses on theory and fundamentals, software engineering focuses on the practicalities with developing and delivering software. [[#Related fields]].                                                                                    |
| What is the difference between software engineering and system engineering? | System engineering is concerned with all aspects of computer-based systems development i.e. hardware, software, process engineering etc. Software engineering is more general process. [[#Related fields]].                                                 |
| What are the key challenges facing software engineering?<br>                | The [[#General issues affecting software]] include coping with increasing diversity, reduced delivery times and security.                                                                                                                                   |
| What are the costs of software engineering?                                 | Roughly 60% of software costs are development costs; 40% are testing costs. For [[#bespoke (customized)]] software, evolution costs often exceed development costs.                                                                                         |
| What are the best software engineering techniques and methods?              | While all software project have to be professionally managed and developed, different techniques are appropriate for different types of system due to high [[#Software engineering diversity]].  Therefore one cannot say one method is better than anoter. |
| What Differences has the web made to software engineering?                  | It has led to the availability of software services and the possibility of developing highly distributed service-based systems. Web-based systems development has let to important advances in programming languages and software reuse                     |

##### Software product types
###### Generic 
stand-alone systems developed by an organization and open to the market (not necessarily open-source) e.g. word processors, drawing packages, project management tools etc.
###### bespoke (customized) 
Products commissioned by a particular customer. e.g. systems to support a particular business
The main difference between the two is that in generic products the organization that develops the product controls the software specification, and the customer adapts it and vice versa for bespoke products.
Although it is becoming more usual to blur these two e.g. Enterprise Resource Planning (ERP) systems such as SAP are an example of this, where the large complex system is adapted by the company be incorporating its business rules and processes etc.

Software development is not only the code but also how the developer makes the program available for the costumer, the characteristics can be boiled down to four categories.

###### Good software characteristics

| Product characteristics    | Description                                                                                                                                                                                                        |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Maintainability            | Software should be written  so that is can evolve to meet the changing needs of customers. This is crucial because change is inevitable in a changing business environment.                                        |
| Dependability and security | Dependability includes characteristics including reliability, security and safety. Dependable software should not cause problems in case of system failure and should minimize attack surface for malicious users. |
| Efficiency                 | Efficiency includes responsiveness, processing time, memory utilization etc. As to not waste resources                                                                                                             |
| Acceptability              | The software must be understandable, usable, and compatible with other systems users may use.                                                                                                                      |





### Software engineering
The definition of software engineering includes two key phrases:
* Engineering discipline
	looking for solutions within financial and organizational constraints and applying theories, methods and tools where they are appropriate to make the solutions.
* All aspects of software production
	Software engineering is concerned with technical processes of software development along with project management and the development of tools, methods and theories to support software production.
a large part of software engineering is choosing the best compromise within a given time frame to produce a product that meets the required quality.

###### Importance of software engineering
software engineering is important for two reasons;
* We rely on advanced software and we need to be able to produce reliable and trustworthy systems economically and quickly
* It is usually cheaper, compared to running is as if it was a personal project. 
###### Software process
the systematic approach to software engineering is usually called a software process.
this comprises four fundamental activities;
* Software specification
	Customers and engineers define the software and constraints.
* Software development
	Designing and programming the software.
* Software validation
	Checking software to ensure customers needs are met.
* Software evolution
	software is modified to reflect changing customer and market requirements.
###### Related fields
Software engineering is related to both computer science and system engineering, where comp Sci is theory based and system engineering is more concerned with all aspects of software engineering.

###### General issues affecting software
There are three general issues that affect many different types of software:
* Heterogeneity, diverse systems, 
	Software has to apply across networks in distributed systems so it has to be compatible with legacy systems along with newer ones, and across operating systems etc.
* Business and social change
	Business and social changes fast, so software has to be able to evolve along with it.
* Security and trust
	Security is very important especially in web services.

These issues are non-independent meaning more than one can apply to a single piece of software


### Software engineering diversity
There exists no one-fits-all method to software engineering, it is largely dependent on what type of software is being developed. 
Among these types of applications are;
* Stand-alone applications
* Interactive transaction-based applications
* embedded control systems
* Batch processing systems
* Entertainment systems
* Systems for modeling and simulation
* Data collection systems
* System of systems

It is important to note that these are not set-in-stone categories and systems may require some aspects from one category along with others.
All systems should adhere to the methods in [[#Good software characteristics]]

###### Web 
the web has changed software business from being mostly monolithic (one machine) to being distributed web services i.e. cloud. This has cut costs as the software does not have to be on every computer that uses it. It has also changed the business model where nowadays a lot of software is free but with ads. A summation of these changes are;
* Software reuse has become the dominant approach for web-based systems. when building these systems, you think about how you can assemble them for pre-existing software components.
* It is now generally recognized that it is impractical to specify all the requirements for such systems in advance, They should be developed and delivered incrementally.
* User interfaces are constrained by the capabilities of web browsers.  This approach generally has poorer interfaces as opposed to user interfaces designed for PC systems.



## Software engineering ethics
The ethics of software engineering. This is where the acceptable behavior is not bound by law, but by morals. Some of these examples include;
* Confidentiality
	  Respecting the confidentiality of employees or clients.
* Competence
	  Not misrepresenting ones level of competence.
* Intellectual property rights
	  Beware of local laws governing the use of intellectual property rights such as patents or copyrights.
* Computer misuse
	  Not using other peoples computers in malicious or unintended ways.

For more info on Ethics standard practice refer to the [ACM/IEEE code of Ethics](https://www.acm.org/code-of-ethics/software-engineering-code). 




# KEY POINTS

* Software engineering is an engineering discipline that is concerned with all aspects of software production, [[#Software engineering]].
* Software is not just a program or programs but also includes documentation. Essential software product attributes are maintainability, dependability, security, efficiency and acceptability, [[#Good software characteristics]].
* The software process includes all of the activities involved in software development. The high-level activities of specification, development, validation, and evolution are part of all software processes, [[#Software process]].
* The fundamental notions of software engineering are universally applicable to all types of system development. These fundamentals include software processes, dependability, security, requirements and reuse.
* There are many different types of systems and each requires appropriate software engineering tools and techniques for their development. There are few specific design and implementation techniques there are applicable across all kinds of systems, [[#Software engineering diversity]].
* The fundamental ideas of software engineering are applicable to all types of software systems. These fundamentals include managed software processes, software dependability and security, requirements engineering, and software reuse.
* Software engineers have responsibilities to the engineering profession and society. They should not simply be concerned with technical issues.
* Professional societies publish codes of conduct that set out the standards of behavior expected of their members.

