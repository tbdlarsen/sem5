Understanding software processes and software process models. Fundamental process activities of software requirements engineering, software development, testing, and evolution. How to cope with changes and the Rational Unified Process' integration with good software engineering practice to create adaptable software processes.

### The fundamental process activities
###### Software specification
The functionality of the software and constrains on its operation must be defined.
###### Software design and implementation
The software to meet the specification must be produced.
###### Software validation
The software must be validated to ensure that it does what the customer wants.
###### Software evolution
The software must evolve to meet changing customer needs

As well as activities process descriptions may also include, products - the outcome, roles and pre- and post-conditions. 
Software processes can either be plan-driven where every  thing is planned in advance, or agile where the processes is incremental.

### Software process models
These are the frameworks of the software process that are used to explain the approach to the software development.

###### The waterfall model
This model takes the [[#The fundamental process activities]] and represents them as separate process phases such as requirements specification, software design, implementation, testing, etc.
![[Waterfall-model.jpg]].
This is an example of a plan-driven process because in principle you must plan and schedule all of the process activities before starting work in them.
The principal stages of the waterfall model directly reflect [[#The fundamental process activities]].
###### Requirements analysis and definition
The system's services, constrains, and goals are established by consultation with system users. They are then defined in detail and serve as a system specification.
###### System and software design
allocates the requirements to either hardware or software systems by establishing an overall system architecture. Software design involves identifying and describing the fundamental software system abstractions.
###### Implementation and unit testing
The software design realized as a set of programs and unit tests.
###### Integration and system testing
Individual program units or programs are integrated and tested as a complete system to ensure that the software requirements have been met. It is then delivered to the customer.

###### Operation and maintenance
 Correcting errors which were not discovered earlier, improving the implementation and enhancing the system's service as new requirements are discovered. Normally the longest phase.

This model should be used when requirements are well understood and unlikely to change.


### Incremental development
Developing initial implementation, and evolving it through several versions until an adequate system has been developed.
![[Incemental development.jpg]]

It is used for it is easier to change the solution incrementally, to be used when the problem may not be final. The three important benefits, compared to [[#The waterfall model]] are; The cost of accommodating changing customer requirements is reduced because the amount of analysis and documentation that has to be redone is reduced. It is easier to get customer feedback and it has more rapid delivery.

The incremental development is one of the most common approaches to software development.
The problems of the incremental approach from a management perspective;
1. The process is not visible. Depending on release frequency it is not cost-effective to document every version of the project.
2. System structure tends to degrade as new increments are added. 


### Integration and configuration
Based on reusing software. Although the initial requirements specification stage and the validation stage are comparable with other software processes, the intermediate stages in a reuse oriented process are different.
![[Integration and configuration.png]]

###### Requirement specification
Inclusion of brief description of initial requirements for the product.
###### Software discovery and software evaluation
A search is made based on the requirement specification to find software that provide the functionality required, these are then evaluated. 
###### Requirements refinement
Refinement of the requirements based on the found software and how it is compatible with the requirements.
###### Application system configuration
Configuring an off-the-shelf solution if one is suitable.
###### Component adaptation and integration
if not off-the-shelf solution is available, configure individual components or modify to suit the problem solution.


There are three types of software component that may be used in a reuse-oriented process. These are web services, Collections of objects that developed to be integrated with a component framework e.g. .Net or J2EE, and lastly, stand-alone software that are configured to be used in a specific environment.


### Coping with change
Change in software development is inevitable and expensive but there are some methods to use to reduce the cost and increase the adaptability of the software.

Approaches to reduce change cost;
###### Change anticipation
Including activities to anticipate or predict possible areas that are subject to change in the [[#software process]]. An example of this is [[#System Prototyping]] which provides users with a quick solution that is easier to change than the finished product.
###### Change tolerance
Designing the solution so that changes can be made easily, involving some form of [[#Incremental development]]. Proposed changes can then be made in upcoming increments so that only a single increment may have to be altered, and only affect the [[#Incremental Delivery]]


###### System Prototyping
An early version of the software system used to demonstrate concepts, try design options etc. 
![[Prototype development.png]]

**Establish prototype objectives**
The objectives of the prototype should be made clear from the start. E.g. If the goal is to create the UI or Demonstrate application to managers.

**Define prototype functionality**
Defining the prototypes functionalities, what to keep in and importantly what to keep out.

**Develop prototype**
Actually develop the prototype

**Evaluate prototype**
What the testers of the prototype think of the prototype, one important thing to note is that the users of the prototype may not use it as they would the final product.


###### Incremental Delivery
developing and delivering the software in increments, where each increments provides additional functionality from the last. 
![[Incremental Delivery.png]]

Incrementally delivering the software system has a list of pros and cons
**Pros**
* Customers can use early increments as [[#System Prototyping|prototypes]] and gain the same benefits while negating the cons. 
* If the first increments satisfies the users requirements they do not have to wait for the final system before using it.
* It has the benefits of [[#Incremental development]] meaning it should be relatively easy to incorporate customer changes.
* As the most critical system requirements are delivered the most critical system services receive the most testing
**Cons**
* Iterative delivery is problematic when a new system is supposed to replace an old one. Users need the full functionality while only receiving it piece-wise. Often it is impractical to use the old system along with the new one until it is finished.
* Most systems require a set of basic functionalities to be used across different parts of the system. As requirements are not defined in detail until an increment is to be implemented, finding common facilities to be used across the system is hard.
* The essence of the iterative process is that the specifications are not yet fully developed and change between increments. This is often opposite of how companies work were the specifications are mostly set in the contract before development begins.
 #todo Coping with change
#todo elaborate fundamental development activities.
