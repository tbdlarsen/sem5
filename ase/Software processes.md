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



### Reuse-oriented software engineering
Based on reusing software. Although the initial requirements specification stage and the validation stage are comparable with other software processes, the intermediate stages in a reuse oriented process are different.
![[Reuse-oriented software engineering.png]]

###### Component analysis
Given the requirements specification, a search is made for components to implement that specification, as good as possible.
###### Requirements modification
Requirements are analyzed using information about the components that have been discovered, they are then modified to fit the components. If impossible search for alternative solutions
###### System design with reuse
Designing the framework or reuse of an existing one. Designers take into account the components and organize the framework to fit them.
###### Development and integration
Software that cannot be externally procured is developed, and the components and COTS systems are integrated to create the new system


There are three types of software component that may be used in a reuse-oriented process. These are web services, Collections of objects that developed to be integrated with a component framework e.g. .Net or J2EE, and lastly, stand-alone software that are configured to be used in a specific environment.


#todo Integration and configuration model, see slides
#todo Coping with change
#todo elaborate fundamental development activities.
