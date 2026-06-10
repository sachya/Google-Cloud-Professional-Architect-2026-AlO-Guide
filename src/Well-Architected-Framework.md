> [!IMPORTANT]
> This page provides a one-page view of all of the pages in the [Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework). You can print this page or save it in PDF format by using your browser's print function.
>
> This page doesn't have a table of contents. You can't use the links on this
> page to navigate within the page.

<br />


The Well-Architected Framework provides recommendations to help
architects, developers, administrators, and other cloud practitioners design and
operate a cloud topology that's secure, efficient, resilient, high-performing,
cost-effective, and sustainable.

A cross-functional team of experts at Google validates the recommendations in
the Well-Architected Framework. The team curates the Well-Architected Framework to
reflect the expanding capabilities of Google Cloud, industry best practices,
community knowledge, and feedback from you. For a summary of the significant
changes to the Well-Architected Framework, see
[What's new](https://docs.cloud.google.com/architecture/framework/whats-new).

The Well-Architected Framework is relevant to applications built for the cloud *and*
for workloads migrated from on-premises to Google Cloud, hybrid cloud
deployments, and multi-cloud environments.

## Well-Architected Framework pillars and perspectives

The recommendations in the Well-Architected Framework are organized into pillars and
cross-pillar perspectives, as shown in the following diagram.

![Well-Architected Framework.](https://docs.cloud.google.com/static/architecture/framework/images/af-infographic.svg)
![Well-Architected Framework.](https://docs.cloud.google.com/static/architecture/framework/images/af-infographic.svg)

- A *pillar* in the Well-Architected Framework provides
  principles and recommendations for a specific non-functional focus area:
  security, reliability, performance, cost, operations, or sustainability.

- A *perspective* in the Well-Architected Framework
  is a cross-pillar view of recommendations for a specific technology, domain, or
  sector. The recommendations in a perspective align with the general principles
  and recommendations in the pillars.

  For example, the financial services (FS) perspective recommends a disaster
  recovery strategy that meets regulatory requirements for data residency. This
  FS-specific recommendation aligns with the reliability pillar's principle about
  realistic targets, because the data residency requirements influence the choice
  of failover region and, consequently, the recovery objectives.

### Pillars

[Operational excellence](https://docs.cloud.google.com/architecture/framework/operational-excellence)
:   Efficiently deploy, operate, monitor, and manage your cloud workloads.

[Security, privacy, and compliance](https://docs.cloud.google.com/architecture/framework/security)
:   Maximize the security of your data and workloads in the cloud, design for
    privacy, and align with regulatory requirements and standards.

[Reliability](https://docs.cloud.google.com/architecture/framework/reliability)
:   Design and operate resilient and highly available workloads in the cloud.

[Cost optimization](https://docs.cloud.google.com/architecture/framework/cost-optimization)
:   Maximize the business value of your investment in Google Cloud.

[Performance optimization](https://docs.cloud.google.com/architecture/framework/performance-optimization)
:   Design and tune your cloud resources for optimal performance.

eco [Sustainability](https://docs.cloud.google.com/architecture/framework/sustainability)
:   Build and manage cloud workloads that are environmentally sustainable.

### Cross-pillar perspectives

[AI and ML](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml)
:   A cross-pillar view of technology-specific recommendations for AI and ML
    workloads.

[Financial services](https://docs.cloud.google.com/architecture/framework/perspectives/fsi)
:   A cross-pillar view of recommendations for FS workloads.

## Core principles

<br />

Before you explore the recommendations in each pillar of the Well-Architected Framework,
review the following core principles:

### Design for change

No system is static. The needs of its users, the goals of the team that builds
the system, and the system itself are constantly changing. With the need for change
in mind, build a development and production process that enables teams to
regularly deliver small changes and get fast feedback on those changes.
Consistently demonstrating the ability to deploy changes helps to build trust
with stakeholders, including the teams responsible for the system, and the users
of the system. Using
[DORA's software delivery metrics](https://dora.dev/guides/dora-metrics-four-keys/)
can help your team monitor the speed, ease, and safety of making changes to the
system.

### Document your architecture

When you start to move your workloads to the cloud or build your applications,
lack of documentation about the system can be a major obstacle. Documentation
is especially important for correctly visualizing the architecture of your
current deployments.

Quality documentation isn't achieved by producing a specific
amount of documentation, but by how clear content is, how useful it is, and how
it's maintained as the system changes.

A properly documented cloud architecture establishes a common language and
standards, which enable cross-functional teams to communicate and collaborate
effectively. The documentation also provides the information that's necessary to
identify and guide future design decisions. Documentation should be written with
your use cases in mind, to provide context for the design decisions.

Over time, your design decisions will evolve and change. The change history
provides the context that your teams require to align initiatives, avoid
duplication, and measure performance changes effectively over time. Change logs
are particularly valuable when you onboard a new cloud architect who is not yet
familiar with your current design, strategy, or history.

[Analysis by DORA](https://dora.dev/capabilities/documentation-quality/)
has found a clear link between documentation quality and organizational
performance --- the organization's ability to meet their performance and
profitability goals.

### Simplify your design and use fully managed services

Simplicity is crucial for design. If your architecture is too complex to
understand, it will be difficult to implement the design and manage it over
time. Where feasible, use fully managed services to minimize the risks, time,
and effort associated with managing and maintaining baseline systems.

If you're already running your workloads in production, test with managed
services to see how they might help to reduce operational complexities. If
you're developing new workloads, then start simple, establish a minimal viable
product (MVP), and resist the urge to over-engineer. You can identify
exceptional use cases, iterate, and improve your systems incrementally over
time.

### Decouple your architecture

[Research from DORA](https://dora.dev/capabilities/loosely-coupled-teams/)
shows that architecture is an important predictor for achieving continuous
delivery. Decoupling is a technique that's used to separate your applications
and service components into smaller components that can operate independently.
For example, you might separate a monolithic application stack into individual
service components. In a loosely coupled architecture, an application can run
its functions independently, regardless of the various dependencies.

A decoupled architecture gives you increased flexibility to do the following:

- Apply independent upgrades.
- Enforce specific security controls.
- Establish reliability goals for each subsystem.
- Monitor health.
- Granularly control performance and cost parameters.

You can start the decoupling process early in your design phase or incorporate
it as part of your system upgrades as you scale.

### Use a stateless architecture

A stateless architecture can increase both the reliability and scalability of
your applications.

Stateful applications rely on various dependencies to perform tasks, such as
local caching of data. Stateful applications often require additional mechanisms
to capture progress and restart gracefully. Stateless applications can perform
tasks without significant local dependencies by using shared storage or cached
services. A stateless architecture enables your applications to scale up quickly
with minimum boot dependencies. The applications can withstand hard restarts,
have lower downtime, and provide better performance for end users.

<br />

<br />


# Well-Architected Framework: Operational excellence pillar

The operational excellence pillar in the
[Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework)
provides recommendations to operate workloads efficiently on Google Cloud.
Operational excellence in the cloud involves designing, implementing, and
managing cloud solutions that provide value, performance, security, and
reliability. The recommendations in this pillar help you to continuously improve
and adapt workloads to meet the dynamic and ever-evolving needs in the cloud.

The operational excellence pillar is relevant to the following audiences:

- **Managers and leaders**: A framework to establish and maintain operational excellence in the cloud and to ensure that cloud investments deliver value and support business objectives.
- **Cloud operations teams**: Guidance to manage incidents and problems, plan capacity, optimize performance, and manage change.
- **Site reliability engineers (SREs)**: Best practices that help you to achieve high levels of service reliability, including monitoring, incident response, and automation.
- **Cloud architects and engineers**: Operational requirements and best practices for the design and implementation phases, to help ensure that solutions are designed for operational efficiency and scalability.
- **DevOps teams**: Guidance about automation, CI/CD pipelines, and change management, to help enable faster and more reliable software delivery.

To achieve operational excellence, you should embrace automation,
orchestration, and data-driven insights. Automation helps to eliminate toil. It
also streamlines and builds guardrails around repetitive tasks. Orchestration
helps to coordinate complex processes. Data-driven insights enable
evidence-based decision-making. By using these practices, you can optimize cloud
operations, reduce costs, improve service availability, and enhance security.

Operational excellence in the cloud goes beyond technical proficiency in cloud
operations. It includes a cultural shift that encourages continuous learning and
experimentation. Teams must be empowered to innovate, iterate, and adopt a
growth mindset. A culture of operational excellence fosters a collaborative
environment where individuals are encouraged to share ideas, challenge
assumptions, and drive improvement.


For operational excellence principles and recommendations that are specific to AI and ML workloads, see
[AI and ML perspective: Operational excellence](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/operational-excellence)
in the Well-Architected Framework.

## Core principles

The recommendations in the operational excellence pillar of the Well-Architected Framework
are mapped to the following core principles:

- [Ensure operational readiness and performance using CloudOps](https://docs.cloud.google.com/architecture/framework/operational-excellence/operational-readiness-and-performance-using-cloudops): Ensure that cloud solutions meet operational and performance requirements by defining service level objectives (SLOs) and by performing comprehensive monitoring, performance testing, and capacity planning.
- [Manage incidents and problems](https://docs.cloud.google.com/architecture/framework/operational-excellence/manage-incidents-and-problems): Minimize the impact of cloud incidents and prevent recurrence through comprehensive observability, clear incident response procedures, thorough retrospectives, and preventive measures.
- [Manage and optimize cloud resources](https://docs.cloud.google.com/architecture/framework/operational-excellence/manage-and-optimize-cloud-resources): Optimize and manage cloud resources through strategies like right-sizing, autoscaling, and by using effective cost monitoring tools.
- [Automate and manage change](https://docs.cloud.google.com/architecture/framework/operational-excellence/automate-and-manage-change): Automate processes, streamline change management, and alleviate the burden of manual labor.
- [Continuously improve and innovate](https://docs.cloud.google.com/architecture/framework/operational-excellence/continuously-improve-and-innovate): Focus on ongoing enhancements and the introduction of new solutions to stay competitive.

## Contributors

Authors:

- [Ryan Cox](https://www.linkedin.com/in/ryanlcox) \| Principal Architect
- [Hadrian Knotz](https://www.linkedin.com/in/hadrianknotz) \| Enterprise Architect

<br />

Other contributors:

- [Daniel Lees](https://www.linkedin.com/in/daniellees) \| Cloud Security Architect
- [Filipe Gracio, PhD](https://www.linkedin.com/in/filipegracio) \| Customer Engineer, AI/ML Specialist
- [Gary Harmson](https://www.linkedin.com/in/garyharmson) \| Principal Architect
- [Jose Andrade](https://www.linkedin.com/in/jmandrade) \| Customer Engineer, SRE Specialist
- [Kumar Dhanagopal](https://www.linkedin.com/in/kumardhanagopal) \| Cross-Product Solution Developer
- [Nicolas Pintaux](https://www.linkedin.com/in/nicolaspintaux) \| Customer Engineer, Application Modernization Specialist
- [Radhika Kanakam](https://www.linkedin.com/in/radhika-kanakam-18ab876) \| Program Lead, Google Cloud Well-Architected Framework
- [Samantha He](https://www.linkedin.com/in/samantha-he-05a98173) \| Technical Writer
- [Zach Seils](https://www.linkedin.com/in/zachseils) \| Networking Specialist
- [Wade Holmes](https://www.linkedin.com/in/wholmes) \| Global Solutions Director

<br />

<br />

<br />


# Ensure operational readiness and performance using CloudOps

This principle in the operational excellence pillar of the
[Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework)
helps you to ensure operational readiness and performance of your cloud
workloads. It emphasizes establishing clear expectations and commitments for
service performance, implementing robust monitoring and alerting, conducting
performance testing, and proactively planning for capacity needs.

## Principle overview

Different organizations might interpret operational readiness differently.
Operational readiness is how *your* organization prepares to successfully
operate workloads on Google Cloud. Preparing to operate a complex,
multilayered cloud workload requires careful planning for both go-live and
[day-2](https://www.googlecloudcommunity.com/gc/Community-Blogs/Simplify-Day-2-Cloud-Operations-with-Google-Cloud-Solutions-and/ba-p/495539)
operations. These operations are often called *CloudOps*.

## Focus areas of operational readiness

Operational readiness consists of four focus areas. Each focus area consists of
a set of activities and components that are necessary to prepare to operate a
complex application or environment in Google Cloud. The following table
lists the components and activities of each focus area:

> [!NOTE]
> **Note:** The recommendations in the operational excellence pillar of the Well-Architected Framework are relevant to one or more of these operational-readiness focus areas.

| Focus area of operational readiness | Activities and components |
|---|---|
| Workforce | - Defining clear roles and responsibilities for the teams that manage and operate the cloud resources. - Ensuring that team members have appropriate skills. - Developing a learning program. - Establishing a clear team structure. - Hiring the required talent. |
| Processes | - Observability. - Managing service disruptions. - Cloud delivery. - Core cloud operations. |
| Tooling | Tools that are required to support CloudOps processes. |
| Governance | - Service levels and reporting. - Cloud financials. - Cloud operating model. - Architectural review and governance boards. - Cloud architecture and compliance. |

## Recommendations

To ensure operational readiness and performance by using CloudOps, consider the
recommendations in the following sections. Each recommendation in this document
is relevant to one or more of the
[focus areas of operational readiness](https://docs.cloud.google.com/architecture/framework/printable#focus-areas-of-operational-readiness).

### Define SLOs and SLAs

A core responsibility of the cloud operations team is to define service level
objectives (SLOs) and service level agreements (SLAs) for all of the critical
workloads. This recommendation is relevant to the governance
[focus area of operational readiness](https://docs.cloud.google.com/architecture/framework/printable#focus-areas-of-operational-readiness).

SLOs must be specific, measurable, achievable, relevant, and time-bound (SMART),
and they must reflect the level of service and performance that you want.

- **Specific**: Clearly articulates the required level of service and performance.
- **Measurable**: Quantifiable and trackable.
- **Achievable**: Attainable within the limits of your organization's capabilities and resources.
- **Relevant**: Aligned with business goals and priorities.
- **Time-bound**: Has a defined timeframe for measurement and evaluation.

For example, an SLO for a web application might be "99.9% availability" or
"average response time less than 200 ms." Such SLOs clearly define the required
level of service and performance for the web application, and the SLOs can be
measured and tracked over time.

SLAs outline the commitments to customers regarding service availability,
performance, and support, including any penalties or remedies for noncompliance.
SLAs must include specific details about the services that are provided, the
level of service that can be expected, the responsibilities of both the service
provider and the customer, and any penalties or remedies for noncompliance. SLAs
serve as a contractual agreement between the two parties, ensuring that both
have a clear understanding of the expectations and obligations that are
associated with the cloud service.

Google Cloud provides tools like
[Cloud Monitoring](https://docs.cloud.google.com/monitoring)
and service level indicators (SLIs) to help you define and track SLOs.
Cloud Monitoring provides comprehensive monitoring and observability
capabilities that enable your organization to collect and analyze metrics that
are related to the availability, performance, and latency of cloud-based
applications and services. SLIs are specific metrics that you can use to measure
and track SLOs over time. By utilizing these tools, you can effectively monitor
and manage cloud services, and ensure that they meet the SLOs and SLAs.

Clearly defining and communicating SLOs and SLAs for all of your critical cloud
services helps to ensure reliability and performance of your deployed
applications and services.

### Implement comprehensive observability

To get real-time visibility into the health and performance of your cloud
environment, we recommend that you use a combination of
[Google Cloud Observability tools](https://cloud.google.com/products/operations)and
third-party solutions. This recommendation is relevant to these
[focus areas of operational readiness](https://docs.cloud.google.com/architecture/framework/printable#focus-areas-of-operational-readiness):
processes and tooling.

Implementing a combination of observability solutions provides you with a
comprehensive observability strategy that covers various aspects of your cloud
infrastructure and applications. Google Cloud Observability is a unified platform for
collecting, analyzing, and visualizing metrics, logs, and traces from various
Google Cloud services, applications, and external sources. By using
Cloud Monitoring, you can gain insights into resource utilization,
performance characteristics, and overall health of your resources.

To ensure comprehensive monitoring, monitor important metrics that align with
system health indicators such as CPU utilization, memory usage, network traffic,
disk I/O, and application response times. You must also consider
business-specific metrics. By tracking these metrics, you can identify potential
bottlenecks, performance issues, and resource constraints. Additionally, you can
set up alerts to notify relevant teams proactively about potential issues or
anomalies.

To enhance your monitoring capabilities further, you can integrate third-party
solutions with Google Cloud Observability. These solutions can provide additional
functionality, such as advanced analytics, machine learning-powered anomaly
detection, and incident management capabilities. This combination of
Google Cloud Observability tools and third-party solutions lets you create a robust and
customizable monitoring ecosystem that's tailored to your specific needs. By
using this combination approach, you can proactively identify and address
issues, optimize resource utilization, and ensure the overall reliability and
availability of your cloud applications and services.

### Implement performance and load testing

Performing regular performance testing helps you to ensure that your
cloud-based applications and infrastructure can handle peak loads and maintain
optimal performance. Load testing simulates realistic traffic patterns. Stress
testing pushes the system to its limits to identify potential bottlenecks and
performance limitations. This recommendation is relevant to these
[focus areas of operational readiness](https://docs.cloud.google.com/architecture/framework/operational-excellence/operational-readiness-and-performance-using-cloudops#focus-areas-of-operational-readiness):
processes and tooling.

Tools like
[Cloud Load Balancing](https://docs.cloud.google.com/load-balancing)
and
[load testing services](https://docs.cloud.google.com/load-balancing/docs/backend-service-load-testing)
can help you to simulate real-world traffic patterns and stress-test your
applications. These tools provide valuable insights into how your system behaves
under various load conditions, and can help you to identify areas that require
optimization.

Based on the results of performance testing, you can make decisions to optimize
your cloud infrastructure and applications for optimal performance and
scalability. This optimization might involve adjusting resource allocation,
tuning configurations, or implementing caching mechanisms.

For example, if you find that your application is experiencing slowdowns during
periods of high traffic, you might need to increase the number of virtual
machines or containers that are allocated to the application. Alternatively, you
might need to adjust the configuration of your web server or database to improve
performance.

By regularly conducting performance testing and implementing the necessary
optimizations, you can ensure that your cloud-based applications and
infrastructure always run at peak performance, and deliver a seamless and
responsive experience for your users. Doing so can help you to maintain a
competitive advantage and build trust with your customers.

### Plan and manage capacity

Proactively planning for future capacity needs---both organic or inorganic---helps
you to ensure the smooth operation and scalability of your cloud-based systems.
This recommendation is relevant to the processes
[focus area of operational readiness](https://docs.cloud.google.com/architecture/framework/operational-excellence/operational-readiness-and-performance-using-cloudops#focus-areas-of-operational-readiness).

Planning for future capacity includes understanding and managing
[quotas](https://docs.cloud.google.com/docs/quotas/view-manage)
for various resources like compute instances, storage, and API requests. By
analyzing historical usage patterns, growth projections, and business
requirements, you can accurately anticipate future capacity requirements. You
can use tools like
[Cloud Monitoring](https://docs.cloud.google.com/monitoring)
and
[BigQuery](https://docs.cloud.google.com/bigquery)
to collect and analyze usage data, identify trends, and forecast future demand.

Historical usage patterns provide valuable insights into resource utilization
over time. By examining metrics like CPU utilization, memory usage, and network
traffic, you can identify periods of high demand and potential bottlenecks.
Additionally, you can help to estimate future capacity needs by making growth
projections based on factors like growth in the user base, new products and
features, and marketing campaigns. When you assess capacity needs, you should
also consider business requirements like SLAs and performance targets.

When you determine the resource sizing for a workload, consider factors that can
affect utilization of resources. Seasonal variations like holiday shopping
periods or end-of-quarter sales can lead to temporary spikes in demand. Planned
events like product launches or marketing campaigns can also significantly
increase traffic. To make sure that your primary and disaster recovery (DR)
system can handle unexpected surges in demand, plan for capacity that can
support graceful failover during disruptions like natural disasters and
cyberattacks.

Autoscaling is an important strategy for dynamically adjusting your cloud
resources based on workload fluctuations. By using autoscaling policies, you can
automatically scale compute instances, storage, and other resources in response
to changing demand. This ensures optimal performance during peak periods while
minimizing costs when resource utilization is low. Autoscaling algorithms use
metrics like CPU utilization, memory usage, and queue depth to determine when to
scale resources.

### Continuously monitor and optimize

To manage and optimize cloud workloads, you must establish a process for
continuously monitoring and analyzing performance metrics. This recommendation
is relevant to these
[focus areas of operational readiness](https://docs.cloud.google.com/architecture/framework/operational-excellence/operational-readiness-and-performance-using-cloudops#focus-areas-of-operational-readiness):
processes and tooling.

To establish a process for continuous monitoring and analysis, you track,
collect, and evaluate data that's related to various aspects of your cloud
environment. By using this data, you can proactively identify areas for
improvement, optimize resource utilization, and ensure that your cloud
infrastructure consistently meets or exceeds your performance expectations.

An important aspect of performance monitoring is regularly reviewing logs and
traces. Logs provide valuable insights into system events, errors, and warnings.
Traces provide detailed information about the flow of requests through your
application. By analyzing logs and traces, you can identify potential issues,
identify the root causes of problems, and get a better understanding of how your
applications behave under different conditions. Metrics like the round-trip time
between services can help you to identify and understand bottlenecks that are in
your workloads.

Further, you can use performance-tuning techniques to significantly enhance
application response times and overall efficiency. The following are examples of
techniques that you can use:

- **Caching**: Store frequently accessed data in memory to reduce the need for repeated database queries or API calls.
- **Database optimization**: Use techniques like indexing and query optimization to improve the performance of database operations.
- **Code profiling**: Identify areas of your code that consume excessive resources or cause performance issues.

By applying these techniques, you can optimize your applications and ensure
that they run efficiently in the cloud.

<br />

<br />


# Manage incidents and problems

This principle in the operational excellence pillar of the
[Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework)
provides recommendations to help you manage incidents and problems related to
your cloud workloads. It involves implementing comprehensive monitoring and
observability, establishing clear incident response procedures, conducting
thorough root cause analysis, and implementing preventive measures. Many of the
topics that are discussed in this principle are covered in detail in the
[Reliability](https://docs.cloud.google.com/architecture/framework/reliability)
pillar.

## Principle overview

Incident management and problem management are important components of a
functional operations environment. How you respond to, categorize, and solve
incidents of differing severity can significantly affect your operations. You
must also proactively and continuously make adjustments to optimize reliability
and performance. An efficient process for incident and problem management relies
on the following foundational elements:

- **Continuous monitoring**: Identify and resolve issues quickly.
- **Automation**: Streamline tasks and improve efficiency.
- **Orchestration**: Coordinate and manage cloud resources effectively.
- **Data-driven insights**: Optimize cloud operations and make informed decisions.

These elements help you to build a resilient cloud environment that can handle
a wide range of challenges and disruptions. These elements can also help to
reduce the risk of costly incidents and downtime, and they can help you to
achieve greater business agility and success. These foundational elements are
spread across the
[four focus areas of operational readiness](https://docs.cloud.google.com/architecture/framework/operational-excellence/operational-readiness-and-performance-using-cloudops#focus-areas-of-operational-readiness):
Workforce, Processes, Tooling, and Governance.

> [!NOTE]
> **Note:** The [Google SRE Book](https://sre.google/workbook/table-of-contents/) defines many of the terms and concepts that are described in this document. We recommend the Google SRE Book as supplemental reading to support the recommendations that are described in this document.

## Recommendations

To manage incidents and problems effectively, consider the recommendations in
the following sections. Each recommendation in this document is relevant to one
or more of the
[focus areas of operational readiness](https://docs.cloud.google.com/architecture/framework/operational-excellence/operational-readiness-and-performance-using-cloudops#focus-areas-of-operational-readiness).

### Establish clear incident response procedures

Clear roles and responsibilities are essential to ensure effective and
coordinated response to incidents. Additionally, clear communication protocols
and escalation paths help to ensure that information is shared promptly and
effectively during an incident. This recommendation is relevant to these
[focus areas of operational readiness](https://docs.cloud.google.com/architecture/framework/operational-excellence/operational-readiness-and-performance-using-cloudops#focus-areas-of-operational-readiness):
workforce, processes, and tooling.

To establish incident response procedures, you need to define the roles and
expectations of each team member, such as incident commanders, investigators,
communicators, and technical experts. Establishing communication and escalation
paths includes identifying important contacts, setting up communication
channels, and defining the process for escalating incidents to higher levels of
management when necessary. Regular training and preparation helps to ensure that
teams are equipped with the knowledge and skills to respond to incidents
effectively.

By documenting incident response procedures in a runbook or playbook, you can
provide a standardized reference guide for teams to follow during an incident.
The runbook must outline the steps to be taken at each stage of the incident
response process, including communication, triage, investigation, and
resolution. It must also include information about relevant tools and resources
and contact information for important personnel. You must regularly review and
update the runbook to ensure that it remains current and effective.

### Centralize incident management

For effective tracking and management throughout the incident lifecycle,
consider using a centralized incident management system. This recommendation is
relevant to these
[focus areas of operational readiness](https://docs.cloud.google.com/architecture/framework/operational-excellence/operational-readiness-and-performance-using-cloudops#focus-areas-of-operational-readiness):
processes and tooling.

A centralized incident management system provides the following advantages:

- **Improved visibility**: By consolidating all incident-related data in a single location, you eliminate the need for teams to search in various channels or systems for context. This approach saves time and reduces confusion, and it gives stakeholders a comprehensive view of the incident, including its status, impact, and progress.
- **Better coordination and collaboration**: A centralized system provides a unified platform for communication and task management. It promotes seamless collaboration between the different departments and functions that are involved in incident response. This approach ensures that everyone has access to up-to-date information and it reduces the risk of miscommunication and misalignment.
- **Enhanced accountability and ownership**: A centralized incident management system enables your organization to allocate tasks to specific individuals or teams and it ensures that responsibilities are clearly defined and tracked. This approach promotes accountability and encourages proactive problem-solving because team members can easily monitor their progress and contributions.

A centralized incident management system must offer robust features for
incident tracking, task assignment, and communication management. These features
let you customize workflows, set priorities, and integrate with other systems,
such as monitoring tools and ticketing systems.

By implementing a centralized incident management system, you can optimize your
organization's incident response processes, improve collaboration, and enhance
visibility. Doing so leads to faster incident resolution times, reduced
downtime, and improved customer satisfaction. It also helps foster a culture of
continuous improvement because you can learn from past incidents and identify
areas for improvement.

### Conduct thorough post-incident reviews

After an incident occurs, you must conduct a detailed post-incident review
(PIR), which is also known as a
[postmortem](https://sre.google/workbook/postmortem-culture/),
to identify the root cause, contributing factors, and lessons learned. This
thorough review helps you to prevent similar incidents in the future. This
recommendation is relevant to these
[focus areas of operational readiness](https://docs.cloud.google.com/architecture/framework/operational-excellence/operational-readiness-and-performance-using-cloudops#focus-areas-of-operational-readiness):
processes and governance.

The PIR process must involve a multidisciplinary team that has expertise in
various aspects of the incident. The team must gather all of the relevant
information through interviews, documentation review, and site inspections. A
timeline of events must be created to establish the sequence of actions that led
up to the incident.

After the team gathers the required information, they must conduct a root cause
analysis to determine the factors that led to the incident. This analysis must
identify both the immediate cause and the systemic issues that contributed to
the incident.

Along with identifying the root cause, the PIR team must identify any other
contributing factors that might have caused the incident. These factors could
include human error, equipment failure, or organizational factors like
communication breakdowns and lack of training.

The PIR report must document the findings of the investigation, including the
timeline of events, root cause analysis, and recommended actions. The report is
a valuable resource for implementing corrective actions and preventing
recurrence. The report must be shared with all of the relevant stakeholders and
it must be used to develop safety training and procedures.

To ensure a successful PIR process, your organization must foster a blameless
culture that focuses on learning and improvement rather than assigning blame.
This culture encourages individuals to report incidents without fear of
retribution, and it lets you address systemic issues and make meaningful
improvements.

By conducting thorough PIRs and implementing corrective measures based on the
findings, you can significantly reduce the risk of similar incidents occurring
in the future. This proactive approach to incident investigation and prevention
helps to create a safer and more efficient work environment for everyone
involved.

### Maintain a knowledge base

A knowledge base of known issues, solutions, and troubleshooting guides is
essential for incident management and resolution. Team members can use the
knowledge base to quickly identify and address common problems. Implementing a
knowledge base helps to reduce the need for escalation and it improves overall
efficiency. This recommendation is relevant to these
[focus areas of operational readiness](https://docs.cloud.google.com/architecture/framework/operational-excellence/operational-readiness-and-performance-using-cloudops#focus-areas-of-operational-readiness):
workforce and processes.

A primary benefit of a knowledge base is that it lets teams learn from past
experiences and avoid repeating mistakes. By capturing and sharing solutions to
known issues, teams can build a collective understanding of how to resolve
common problems and best practices for incident management. Use of a knowledge
base saves time and effort, and helps to standardize processes and ensure
consistency in incident resolution.

Along with helping to improve incident resolution times, a knowledge base
promotes knowledge sharing and collaboration across teams. With a central
repository of information, teams can easily access and contribute to the
knowledge base, which promotes a culture of continuous learning and improvement.
This culture encourages teams to share their expertise and experiences, leading
to a more comprehensive and valuable knowledge base.

To create and manage a knowledge base effectively, use appropriate tools and
technologies. Collaboration platforms like
[Google Workspace](https://workspace.google.com/)
are well-suited for this purpose because they let you easily create, edit, and
share documents collaboratively. These tools also support version control and
change tracking, which ensures that the knowledge base remains up-to-date and
accurate.

Make the knowledge base easily accessible to all relevant teams. You can achieve
this by integrating the knowledge base with existing incident management systems
or by providing a dedicated portal or intranet site. A knowledge base that's
readily available lets teams quickly access the information that they need to
resolve incidents efficiently. This availability helps to reduce downtime and
minimize the impact on business operations.

Regularly review and update the knowledge base to ensure that it remains
relevant and useful. Monitor incident reports, identify common issues and
trends, and incorporate new solutions and troubleshooting guides into the
knowledge base. An up-to-date knowledge base helps your teams resolve incidents
faster and more effectively.

### Automate incident response

Automation helps to streamline your incident response and remediation
processes. It lets you address security breaches and system failures
promptly and efficiently. By using Google Cloud products like
[Cloud Run functions](https://docs.cloud.google.com/functions)
or
[Cloud Run](https://docs.cloud.google.com/run),
you can automate various tasks that are typically manual and time-consuming.
This recommendation is relevant to these
[focus areas of operational readiness](https://docs.cloud.google.com/architecture/framework/operational-excellence/operational-readiness-and-performance-using-cloudops#focus-areas-of-operational-readiness):
processes and tooling.

Automated incident response provides the following benefits:

- **Reduction in incident detection and resolution times**: Automated tools can continuously monitor systems and applications, detect suspicious or anomalous activities in real time, and notify stakeholders or respond without intervention. This automation lets you identify potential threats or issues before they escalate into major incidents. When an incident is detected, automated tools can trigger predefined remediation actions, such as isolating affected systems, quarantining malicious files, or rolling back changes to restore the system to a known good state.
- **Reduced burden on security and operations teams**: Automated incident response lets the security and operations teams focus on more strategic tasks. By automating routine and repetitive tasks, such as collecting diagnostic information or triggering alerts, your organization can free up personnel to handle more complex and critical incidents. This automation can lead to improved overall incident response effectiveness and efficiency.
- **Enhanced consistency and accuracy of the remediation process**: Automated tools can ensure that remediation actions are applied uniformly across all affected systems, minimizing the risk of human error or inconsistency. This standardization of the remediation process helps to minimize the impact of incidents on users and the business.

<br />

<br />


# Manage and optimize cloud resources

This principle in the operational excellence pillar of the
[Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework)
provides recommendations to help you manage and optimize the resources that are
used by your cloud workloads. It involves right-sizing resources based on actual
usage and demand, using autoscaling for dynamic resource allocation,
implementing cost optimization strategies, and regularly reviewing resource
utilization and costs. Many of the topics that are discussed in this principle
are covered in detail in the
[Cost optimization](https://docs.cloud.google.com/architecture/framework/cost-optimization)
pillar.

## Principle overview

Cloud resource management and optimization play a vital role in optimizing
cloud spending, resource usage, and infrastructure efficiency. It includes
various strategies and best practices aimed at maximizing the value and return
from your cloud spending.

This pillar's focus on optimization extends beyond cost reduction. It emphasizes
the following goals:

- **Efficiency**: Using automation and data analytics to achieve peak performance and cost savings.
- [**Performance**](https://docs.cloud.google.com/architecture/framework/performance-optimization): Scaling resources effortlessly to meet fluctuating demands and deliver optimal results.
- **Scalability**: Adapting infrastructure and processes to accommodate rapid growth and diverse workloads.

By focusing on these goals, you achieve a balance between cost and
functionality. You can make informed decisions regarding resource provisioning,
scaling, and migration. Additionally, you gain valuable insights into resource
consumption patterns, which lets you proactively identify and address potential
issues before they escalate.

## Recommendations

To manage and optimize resources, consider the recommendations in the following
sections. Each recommendation in this document is relevant to one or more of
the
[focus areas of operational readiness](https://docs.cloud.google.com/architecture/framework/operational-excellence/operational-readiness-and-performance-using-cloudops#focus-areas-of-operational-readiness).

### Right-size resources

Continuously monitoring resource utilization and adjusting resource allocation
to match actual demand are essential for efficient cloud resource management.
Over-provisioning resources can lead to unnecessary costs, and
under-provisioning can cause performance bottlenecks that affect application
performance and user experience. To achieve an optimal balance, you must adopt a
proactive approach to right-sizing cloud resources. This recommendation is
relevant to the governance
[focus area of operational readiness](https://docs.cloud.google.com/architecture/framework/operational-excellence/operational-readiness-and-performance-using-cloudops#focus-areas-of-operational-readiness).

[Cloud Monitoring](https://cloud.google.com/monitoring)
and
[Recommender](https://cloud.google.com/recommender)
can help you to identify opportunities for right-sizing. Cloud Monitoring
provides real-time visibility into resource utilization metrics. This visibility
lets you track resource usage patterns and identify potential inefficiencies.
Recommender analyzes resource utilization data to make intelligent
recommendations for optimizing resource allocation. By using these tools, you
can gain insights into resource usage and make informed decisions about
right-sizing the resources.

In addition to Cloud Monitoring and Recommender, consider
using custom metrics to trigger automated right-sizing actions. Custom metrics
let you track specific resource utilization metrics that are relevant to your
applications and workloads. You can also configure alerts to notify
administrators when predefined thresholds are met. The administrators can then
take necessary actions to adjust resource allocation. This proactive approach
ensures that resources are scaled in a timely manner, which helps to optimize
cloud costs and prevent performance issues.

### Use autoscaling

Autoscaling compute and other resources helps to ensure optimal performance and
cost efficiency of your cloud-based applications. Autoscaling lets you
dynamically adjust the capacity of your resources based on workload
fluctuations, so that you have the resources that you need when you need them
and you can avoid over-provisioning and unnecessary costs. This recommendation
is relevant to the processes
[focus area of operational readiness](https://docs.cloud.google.com/architecture/framework/operational-excellence/operational-readiness-and-performance-using-cloudops#focus-areas-of-operational-readiness).

To meet the diverse needs of different applications and workloads,
Google Cloud offers various autoscaling options, including the following:

- [Compute Engine managed instance groups (MIGs)](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups) are groups of VMs that are managed and scaled as a single entity. With MIGs, you can define autoscaling policies that specify the minimum and maximum number of VMs to maintain in the group, and the conditions that trigger autoscaling. For example, you can configure a policy to add VMs in a MIG when the CPU utilization reaches a certain threshold and to remove VMs when the utilization drops below a different threshold.
- [Google Kubernetes Engine (GKE) autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler)
  dynamically adjusts your cluster resources to match your application's
  needs. It offers the following tools:

  - Cluster Autoscaler adds or removes nodes based on Pod resource demands.
  - Horizontal Pod Autoscaler changes the number of Pod replicas based on CPU, memory, or custom metrics.
  - Vertical Pod Autoscaler fine-tunes Pod resource requests and limits based on usage patterns.
  - Node Auto-Provisioning automatically creates optimized node pools for your workloads.

  These tools work together to optimize resource utilization, ensure
  application performance, and simplify cluster management.
- [Cloud Run](https://cloud.google.com/run)
  is a serverless platform that lets you run code without having to manage
  infrastructure. Cloud Run offers built-in autoscaling, which
  automatically adjusts the number of instances based on the incoming
  traffic. When the volume of traffic increases, Cloud Run
  scales up the number of instances to handle the load. When traffic
  decreases, Cloud Run scales down the number of instances to
  reduce costs.

By using these autoscaling options, you can ensure that your cloud-based
applications have the resources that they need to handle varying workloads,
while avoiding overprovisioning and unnecessary costs. Using autoscaling can
lead to improved performance, cost savings, and more efficient use of cloud
resources.

### Leverage cost optimization strategies

Optimizing cloud spending helps you to effectively manage your organization's
IT budgets. This recommendation is relevant to the governance
[focus area of operational readiness](https://docs.cloud.google.com/architecture/framework/operational-excellence/operational-readiness-and-performance-using-cloudops#focus-areas-of-operational-readiness).

Google Cloud offers several tools and techniques to help you optimize
cloud costs. By using these tools and techniques, you can get the best value
from your cloud spending. These tools and techniques help you to identify areas
where costs can be reduced, such as identifying underutilized resources or
recommending more cost-effective instance types. Google Cloud options to
help optimize cloud costs include the following:

- [Committed use discounts (CUDs)](https://docs.cloud.google.com/docs/cuds) are discounts for committing to a certain level of usage over a period of time.
- [Sustained use discounts](https://docs.cloud.google.com/compute/docs/sustained-use-discounts) in Compute Engine provide discounts for consistent usage of a service.
- [Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot) provide access to unused VM capacity at a lower cost compared to regular VMs.

Pricing models might change over time, and new features might be introduced that
offer better performance or lower cost compared to existing options. Therefore,
you should regularly review pricing models and consider alternative features. By
staying informed about the latest pricing models and features, you can make
informed decisions about your cloud architecture to minimize costs.

Google Cloud's
[Cost Management](https://cloud.google.com/cost-management)
tools, such as budgets and alerts, provide valuable insights into cloud
spending. Budgets and alerts let users set budgets and receive alerts when the
budgets are exceeded. These tools help users track their cloud spending and
identify areas where costs can be reduced.

### Track resource usage and costs

You can use tagging and labeling to track resource usage and costs. By
assigning tags and labels to your cloud resources like projects, departments, or
other relevant dimensions, you can categorize and organize the resources. This
lets you monitor and analyze spending patterns for specific resources and
identify areas of high usage or potential cost savings. This recommendation is
relevant to these
[focus areas of operational readiness](https://docs.cloud.google.com/architecture/framework/operational-excellence/operational-readiness-and-performance-using-cloudops#focus-areas-of-operational-readiness):
governance and tooling.

Tools like Cloud Billing and Cost Management help you to get a comprehensive
understanding of your spending patterns. These tools provide detailed insights
into your cloud usage and they let you identify trends, forecast costs, and make
informed decisions. By analyzing historical data and current spending patterns,
you can identify the focus areas for your cost-optimization efforts.

Custom dashboards and reports help you to visualize cost data and gain deeper
insights into spending trends. By customizing dashboards with relevant metrics
and dimensions, you can monitor key performance indicators (KPIs) and track
progress towards your cost optimization goals. Reports offer deeper analyses of
cost data. Reports let you filter the data by specific time periods or resource
types to understand the underlying factors that contribute to your cloud
spending.

Regularly review and update your tags, labels, and cost analysis tools to ensure
that you have the most up-to-date information on your cloud usage and costs. By
staying informed and conducting cost postmortems or proactive cost reviews, you
can promptly identify any unexpected increases in spending. Doing so lets you
make proactive decisions to optimize cloud resources and control costs.

### Establish cost allocation and budgeting

Accountability and transparency in cloud cost management are crucial for
optimizing resource utilization and ensuring financial control. This
recommendation is relevant to the governance
[focus area of operational readiness](https://docs.cloud.google.com/architecture/framework/operational-excellence/operational-readiness-and-performance-using-cloudops#focus-areas-of-operational-readiness).

To ensure accountability and transparency, you need to have clear mechanisms
for cost allocation and chargeback. By allocating costs to specific teams,
projects, or individuals, your organization can ensure that each of these
entities is responsible for its cloud usage. This practice fosters a sense of
ownership and encourages responsible resource management. Additionally,
chargeback mechanisms enable your organization to recover cloud costs from
internal customers, align incentives with performance, and promote fiscal
discipline.

Establishing budgets for different teams or projects is another essential
aspect of cloud cost management. Budgets enable your organization to define
spending limits and track actual expenses against those limits. This approach
lets you make proactive decisions to prevent uncontrolled spending. By setting
realistic and achievable budgets, you can ensure that cloud resources are used
efficiently and aligned with business objectives. Regular monitoring of actual
spending against budgets helps you to identify variances and address potential
overruns promptly.

To monitor budgets, you can use tools like
[Cloud Billing budgets and alerts](https://docs.cloud.google.com/billing/docs/how-to/budgets).
These tools provide real-time insights into cloud spending and they notify
stakeholders of potential overruns. By using these capabilities, you can track
cloud costs and take corrective actions before significant deviations occur.
This proactive approach helps to prevent financial surprises and ensures that
cloud resources are used responsibly.

<br />

<br />


# Automate and manage change

This principle in the operational excellence pillar of the
[Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework)
provides recommendations to help you automate and manage change for your cloud
workloads. It involves implementing infrastructure as code (IaC), establishing
standard operating procedures, implementing a structured change management
process, and using automation and orchestration.

## Principle overview

Change management and automation play a crucial role in ensuring smooth and
controlled transitions within cloud environments. For effective change
management, you need to use strategies and best practices that minimize
disruptions and ensure that changes are integrated seamlessly with existing
systems.

Effective change management and automation include the following foundational
elements:

- **Change governance**: Establish clear policies and procedures for change management, including approval processes and communication plans.
- **Risk assessment**: Identify potential risks associated with changes and mitigate them through risk management techniques.
- **Testing and validation**: Thoroughly test changes to ensure that they meet functional and performance requirements and mitigate potential regressions.
- **Controlled deployment**: Implement changes in a controlled manner, ensuring that users are seamlessly transitioned to the new environment, with mechanisms to seamlessly roll back if needed.

These foundational elements help to minimize the impact of changes and ensure
that changes have a positive effect on business operations. These elements are
represented by the processes, tooling, and governance
[focus areas of operational readiness](https://docs.cloud.google.com/architecture/framework/operational-excellence/operational-readiness-and-performance-using-cloudops#focus-areas-of-operational-readiness).

## Recommendations

To automate and manage change, consider the recommendations in the following
sections. Each recommendation in this document is relevant to one or more of the
[focus areas of operational readiness](https://docs.cloud.google.com/architecture/framework/operational-excellence/operational-readiness-and-performance-using-cloudops#focus-areas-of-operational-readiness).

### Adopt IaC

Infrastructure as code (IaC) is a transformative approach for managing cloud
infrastructure. You can define and manage cloud infrastructure declaratively by
using tools like
[Terraform](https://docs.cloud.google.com/docs/terraform/iac-overview).
IaC helps you achieve consistency, repeatability, and simplified change
management. It also enables faster and more reliable deployments. This
recommendation is relevant to these
[focus areas of operational readiness](https://docs.cloud.google.com/architecture/framework/operational-excellence/operational-readiness-and-performance-using-cloudops#focus-areas-of-operational-readiness):
processes and tooling.

The following are the main benefits of adopting the IaC approach for your cloud
deployments:

- **Human-readable resource configurations**: With the IaC approach, you can declare your cloud infrastructure resources in a human-readable format, like JSON or YAML. Infrastructure administrators and operators can easily understand and modify the infrastructure and collaborate with others.
- **Consistency and repeatability**: IaC enables consistency and repeatability in your infrastructure deployments. You can ensure that your infrastructure is provisioned and configured the same way every time, regardless of who is performing the deployment. This approach helps to reduce errors and ensures that your infrastructure is always in a known state.
- **Accountability and simplified troubleshooting**: The IaC approach helps to improve accountability and makes it easier to troubleshoot issues. By storing your IaC code in a version control system, you can track changes, and identify when changes were made and by whom. If necessary, you can easily roll back to previous versions.

### Implement version control

A version control system like Git is a key component of the IaC process. It
provides robust change management and risk mitigation capabilities, which is why
it's widely adopted, either through in-house development or SaaS solutions. This
recommendation is relevant to these
[focus areas of operational readiness](https://docs.cloud.google.com/architecture/framework/operational-excellence/operational-readiness-and-performance-using-cloudops#focus-areas-of-operational-readiness):
governance and tooling.

By tracking changes to IaC code and configurations, version control provides
visibility into the evolution of the code, making it easier to understand the
impact of changes and identify potential issues. This enhanced visibility
fosters collaboration among team members who work on the same IaC project.

Most version control systems let you easily roll back changes if needed. This
capability helps to mitigate the risk of unintended consequences or errors. By
using tools like Git in your IaC workflow, you can significantly improve change
management processes, foster collaboration, and mitigate risks, which leads to a
more efficient and reliable IaC implementation.

### Build CI/CD pipelines

Continuous integration and continuous delivery (CI/CD) pipelines streamline the
process of developing and deploying cloud applications. CI/CD pipelines automate
the building, testing, and deployment stages, which enables faster and more
frequent releases with improved quality control. This recommendation is relevant
to the tooling
[focus area of operational readiness](https://docs.cloud.google.com/architecture/framework/operational-excellence/operational-readiness-and-performance-using-cloudops#focus-areas-of-operational-readiness).

CI/CD pipelines ensure that code changes are continuously integrated into a
central repository, typically a version control system like Git. Continuous
integration facilitates early detection and resolution of issues, and it reduces
the likelihood of bugs or compatibility problems.

To create and manage CI/CD pipelines for cloud applications, you can use tools
like
[Cloud Build](https://docs.cloud.google.com/build)and
[Cloud Deploy](https://docs.cloud.google.com/deploy).

- **Cloud Build** is a fully managed build service that lets developers define and execute build steps in a declarative manner. It integrates seamlessly with popular source-code management platforms and it can be triggered by events like code pushes and pull requests.
- **Cloud Deploy** is a serverless deployment service that automates the process of deploying applications to various environments, such as testing, staging, and production. It provides features like blue-green deployments, traffic splitting, and rollback capabilities, making it easier to manage and monitor application deployments.

Integrating CI/CD pipelines with version control systems and testing frameworks
helps to ensure the quality and reliability of your cloud applications. By
running automated tests as part of the CI/CD process, development teams can
quickly identify and fix any issues before the code is deployed to the
production environment. This integration helps to improve the overall stability
and performance of your cloud applications.

### Use configuration management tools

Tools like Puppet, Chef, Ansible, and
[VM Manager](https://docs.cloud.google.com/compute/docs/vm-manager)
help you to automate the configuration and management of cloud resources. Using
these tools, you can ensure resource consistency and compliance across your
cloud environments. This recommendation is relevant to the tooling
[focus area of operational readiness](https://docs.cloud.google.com/architecture/framework/operational-excellence/operational-readiness-and-performance-using-cloudops#focus-areas-of-operational-readiness).

Automating the configuration and management of cloud resources provides the
following benefits:

- **Significant reduction in the risk of manual errors**: When manual processes are involved, there is a higher likelihood of mistakes due to human error. Configuration management tools reduce this risk by automating processes, so that configurations are applied consistently and accurately across all cloud resources. This automation can lead to improved reliability and stability of the cloud environment.
- **Improvement in operational efficiency**: By automating repetitive tasks, your organization can free up IT staff to focus on more strategic initiatives. This automation can lead to increased productivity and cost savings and improved responsiveness to changing business needs.
- **Simplified management of complex cloud infrastructure**: As cloud environments grow in size and complexity, managing the resources can become increasingly difficult. Configuration management tools provide a centralized platform for managing cloud resources. The tools make it easier to track configurations, identify issues, and implement changes. Using these tools can lead to improved visibility, control, and security of your cloud environment.

### Automate testing

Integrating automated testing into your CI/CD pipelines helps to ensure the
quality and reliability of your cloud applications. By validating changes before
deployment, you can significantly reduce the risk of errors and regressions,
which leads to a more stable and robust software system. This recommendation is
relevant to these
[focus areas of operational readiness](https://docs.cloud.google.com/architecture/framework/operational-excellence/operational-readiness-and-performance-using-cloudops#focus-areas-of-operational-readiness):
processes and tooling.

The following are the main benefits of incorporating automated testing into your
CI/CD pipelines:

- **Early detection of bugs and defects**: Automated testing helps to detect bugs and defects early in the development process, before they can cause major problems in production. This capability saves time and resources by preventing the need for costly rework and bug fixes at later stages in the development process.
- **High quality and standards-based code**: Automated testing can help improve the overall quality of your code by ensuring that the code meets certain standards and best practices. This capability leads to more maintainable and reliable applications that are less prone to errors.

You can use various types of testing techniques in CI/CD pipelines. Each test
type serves a specific purpose.

- **Unit testing** focuses on testing individual units of code, such as functions or methods, to ensure that they work as expected.
- **Integration testing** tests the interactions between different components or modules of your application to verify that they work properly together.
- **End-to-end testing** is often used along with unit and integration testing. End-to-end testing simulates real-world scenarios to test the application as a whole, and helps to ensure that the application meets the requirements of your end users.

To effectively integrate automated testing into your CI/CD pipelines, you must
choose appropriate testing tools and frameworks. There are many different
options, each with its own strengths and weaknesses. You must also establish a
clear testing strategy that outlines the types of tests to be performed, the
frequency of testing, and the criteria for passing or failing a test. By
following these recommendations, you can ensure that your automated testing
process is efficient and effective. Such a process provides valuable insights
into the quality and reliability of your cloud applications.

<br />

<br />


# Continuously improve and innovate

This principle in the operational excellence pillar of the
[Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework)
provides recommendations to help you continuously optimize cloud operations and
drive innovation.

## Principle overview

To continuously improve and innovate in the cloud, you need to focus on
continuous learning, experimentation, and adaptation. This helps you to explore
new technologies and optimize existing processes and it promotes a culture of
excellence that enables your organization to achieve and maintain industry
leadership.

Through continuous improvement and innovation, you can achieve the following
goals:

- **Accelerate innovation**: Explore new technologies and services to enhance capabilities and drive differentiation.
- **Reduce costs**: Identify and eliminate inefficiencies through process-improvement initiatives.
- **Enhance agility**: Adapt rapidly to changing market demands and customer needs.
- **Improve decision making**: Gain valuable insights from data and analytics to make data-driven decisions.

Organizations that embrace the continuous improvement and innovation principle
can unlock the full potential of the cloud environment and achieve sustainable
growth. This principle maps primarily to the Workforce
[focus area of operational readiness](https://docs.cloud.google.com/architecture/framework/operational-excellence/operational-readiness-and-performance-using-cloudops#focus-areas-of-operational-readiness).
A culture of innovation lets teams experiment with new tools and technologies to
expand capabilities and reduce costs.

## Recommendations

To continuously improve and innovate your cloud workloads, consider the
recommendations in the following sections. Each recommendation in this document
is relevant to one or more of the
[focus areas of operational readiness](https://docs.cloud.google.com/architecture/framework/operational-excellence/operational-readiness-and-performance-using-cloudops#focus-areas-of-operational-readiness).

### Foster a culture of learning

Encourage teams to experiment, share knowledge, and learn continuously. Adopt a
blameless culture where failures are viewed as opportunities for growth and
improvement. This recommendation is relevant to the workforce
[focus area of operational readiness](https://docs.cloud.google.com/architecture/framework/operational-excellence/operational-readiness-and-performance-using-cloudops#focus-areas-of-operational-readiness).

When you foster a culture of learning, teams can learn from mistakes and
iterate quickly. This approach encourages team members to take risks, experiment
with new ideas, and expand the boundaries of their work. It also creates a
psychologically safe environment where individuals feel comfortable sharing
failures and learning from them. Sharing in this way leads to a more open and
collaborative environment.

To facilitate knowledge sharing and continuous learning, create opportunities
for teams to share knowledge and learn from each other. You can do this through
informal and formal learning sessions and conferences.

By fostering a culture of experimentation, knowledge sharing, and continuous
learning, you can create an environment where teams are empowered to take risks,
innovate, and grow. This environment can lead to increased productivity,
improved problem-solving, and a more engaged and motivated workforce. Further,
by promoting a blameless culture, you can create a safe space for employees to
learn from mistakes and contribute to the collective knowledge of the team. This
culture ultimately leads to a more resilient and adaptable workforce that is
better equipped to handle challenges and drive success in the long run.

### Conduct regular retrospectives

Retrospectives give teams an opportunity to reflect on their experiences,
identify what went well, and identify what can be improved. By conducting
retrospectives after projects or major incidents, teams can learn from successes
and failures, and continuously improve their processes and practices. This
recommendation is relevant to these
[focus areas of operational readiness](https://docs.cloud.google.com/architecture/framework/operational-excellence/operational-readiness-and-performance-using-cloudops#focus-areas-of-operational-readiness):
processes and governance.

An effective way to structure a retrospective is to use the
*Start-Stop-Continue* model:

- **Start** : In the *Start* phase of the retrospective, team members identify new practices, processes, and behaviors that they believe can enhance their work. They discuss why the changes are needed and how they can be implemented.
- **Stop** : In the *Stop* phase, team members identify and eliminate practices, processes, and behaviors that are no longer effective or that hinder progress. They discuss why these changes are necessary and how they can be implemented.
- **Continue** : In the *Continue* phase, team members identify practices, processes, and behaviors that work well and must be continued. They discuss why these elements are important and how they can be reinforced.

By using a structured format like the Start-Stop-Continue model, teams can
ensure that retrospectives are productive and focused. This model helps to
facilitate discussion, identify the main takeaways, and identify actionable
steps for future enhancements.

### Stay up-to-date with cloud technologies

To maximize the potential of Google Cloud services, you must keep up with
the latest advancements, features, and best practices. This recommendation is
relevant to the workforce
[focus area of operational readiness](https://docs.cloud.google.com/architecture/framework/operational-excellence/operational-readiness-and-performance-using-cloudops#focus-areas-of-operational-readiness).

Participating in relevant conferences, webinars, and training sessions is a
valuable way to expand your knowledge. These events provide opportunities to
learn from Google Cloud experts, understand new capabilities, and engage
with industry peers who might face similar challenges. By attending these
sessions, you can gain insights into how to use new features effectively,
optimize your cloud operations, and drive innovation within your organization.

To ensure that your team members keep up with cloud technologies, encourage
them to obtain certifications and attend training courses. Google Cloud
offers a wide range of
[certifications](https://cloud.google.com/learn/certification)
that validate skills and knowledge in specific cloud domains. Earning these
certifications demonstrates commitment to excellence and provides tangible
evidence of proficiency in cloud technologies. The training courses that are
offered by Google Cloud and our partners delve deeper into specific
topics. They provide direct experience and practical skills that can be
immediately applied to real-world projects. By investing in the professional
development of your team, you can foster a culture of continuous learning and
ensure that everyone has the necessary skills to succeed in the cloud.

### Actively seek and incorporate feedback

Collect feedback from users, stakeholders, and team members. Use the feedback
to identify opportunities to improve your cloud solutions. This recommendation
is relevant to the workforce
[focus area of operational readiness](https://docs.cloud.google.com/architecture/framework/operational-excellence/operational-readiness-and-performance-using-cloudops#focus-areas-of-operational-readiness).

The feedback that you collect can help you to understand the evolving needs,
issues, and expectations of the users of your solutions. This feedback serves as
a valuable input to drive improvements and prioritize future enhancements. You
can use various mechanisms to collect feedback:

- **Surveys** are an effective way to gather quantitative data from a large number of users and stakeholders.
- **User interviews** provide an opportunity for in-depth qualitative data collection. Interviews let you understand the specific challenges and experiences of individual users.
- **Feedback forms** that are placed within the cloud solutions offer a convenient way for users to provide immediate feedback on their experience.
- **Regular meetings** with team members can facilitate the collection of feedback on technical aspects and implementation challenges.

The feedback that you collect through these mechanisms must be analyzed and
synthesized to identify common themes and patterns. This analysis can help you
prioritize future enhancements based on the impact and feasibility of the
suggested improvements. By addressing the needs and issues that are identified
through feedback, you can ensure that your cloud solutions continue to meet the
evolving requirements of your users and stakeholders.

### Measure and track progress

Key performance indicators (KPIs) and metrics are crucial for tracking progress
and measuring the effectiveness of your cloud operations. KPIs are quantifiable
measurements that reflect the overall performance. Metrics are specific data
points that contribute to the calculation of KPIs. Review the metrics regularly
and use them to identify opportunities for improvement and measure progress.
Doing so helps you to continuously improve and optimize your cloud environment.
This recommendation is relevant to these
[focus areas of operational readiness](https://docs.cloud.google.com/architecture/framework/operational-excellence/operational-readiness-and-performance-using-cloudops#focus-areas-of-operational-readiness):
governance and processes.

A primary benefit of using KPIs and metrics is that they enable your
organization to adopt a data-driven approach to cloud operations. By tracking
and analyzing operational data, you can make informed decisions about how to
improve the cloud environment. This data-driven approach helps you to identify
trends, patterns, and anomalies that might not be visible without the use of
systematic metrics.

To collect and analyze operational data, you can use tools like
[Cloud Monitoring](https://docs.cloud.google.com/monitoring)
and
[BigQuery](https://docs.cloud.google.com/bigquery).
Cloud Monitoring enables real-time monitoring of cloud resources and
services. BigQuery lets you store and analyze the data that you
gather through monitoring. Using these tools together, you can create custom
dashboards to visualize important metrics and trends.

Operational dashboards can provide a centralized view of the most important
metrics, which lets you quickly identify any areas that need attention. For
example, a dashboard might include metrics like CPU utilization, memory usage,
network traffic, and latency for a particular application or service. By
monitoring these metrics, you can quickly identify any potential issues and take
steps to resolve them.

<br />

<br />


# Well-Architected Framework: Security, privacy, and compliance pillar

The Security, Privacy and Compliance pillar in the
[Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework)
provides recommendations to help you design, deploy, and operate cloud workloads
that meet your requirements for security, privacy, and compliance.

This document is designed to offer valuable insights and meet the needs of a
range of security professionals and engineers. The following table describes
the intended audiences for this document:

| Audience | What this document provides |
|---|---|
| Chief information security officers (CISOs), business unit leaders, and IT managers | A general framework to establish and maintain security excellence in the cloud and to ensure a comprehensive view of security areas to make informed decisions about security investments. |
| Security architects and engineers | Key security practices for the design and operational phases to help ensure that solutions are designed for security, efficiency, and scalability. |
| DevSecOps teams | Guidance to incorporate overarching security controls to plan automation that enables secure and reliable infrastructure. |
| Compliance officers and risk managers | Key security recommendations to follow a structured approach to risk management with safeguards that help to meet compliance obligations. |

To ensure that your Google Cloud workloads meet your security, privacy,
and compliance requirements, all of the stakeholders in your organization must
adopt a collaborative approach. In addition, you must recognize that cloud
security is a shared responsibility between you and Google. For more
information, see
[Shared responsibilities and shared fate on Google Cloud](https://docs.cloud.google.com/architecture/framework/security/shared-responsibility-shared-fate).

The recommendations in this pillar are grouped into core security principles.
Each principle-based recommendation is mapped to one or more of the
[focus areas of cloud security](https://docs.cloud.google.com/architecture/framework/printable#focus_areas_of_cloud_security)
that might be critical to your organization. Each
recommendation highlights guidance about the use and configuration of
Google Cloud products and capabilities to help improve your organization's
security posture.

## Core principles

The recommendations in this pillar are grouped within the following core
principles of security. Every principle in this pillar is important. Depending
on the requirements of your organization and workload, you might choose to
prioritize certain principles.

- [Implement security by design](https://docs.cloud.google.com/architecture/framework/security/implement-security-by-design): Integrate cloud security and network security considerations starting from the initial design phase of your applications and infrastructure. Google Cloud provides architecture blueprints and recommendations to help you apply this principle.
- [Implement zero trust](https://docs.cloud.google.com/architecture/framework/security/implement-zero-trust): Use a *never trust, always verify* approach, where access to resources is granted based on continuous verification of trust. Google Cloud supports this principle through products like Chrome Enterprise Premium and Identity-Aware Proxy (IAP).
- [Implement shift-left security](https://docs.cloud.google.com/architecture/framework/security/implement-shift-left-security): Implement security controls early in the software development lifecycle. Avoid security defects before system changes are made. Detect and fix security bugs early, fast, and reliably after the system changes are committed. Google Cloud supports this principle through products like Cloud Build, Binary Authorization, and Artifact Registry.
- [Implement preemptive cyber defense](https://docs.cloud.google.com/architecture/framework/security/implement-preemptive-cyber-defense): Adopt a proactive approach to security by implementing robust fundamental measures like threat intelligence. This approach helps you build a foundation for more effective threat detection and response. Google Cloud's [approach to layered security controls](https://docs.cloud.google.com/docs/security/overview/whitepaper#technology_with_security_at_its_core) aligns with this principle.
- [Use AI securely and responsibly](https://docs.cloud.google.com/architecture/framework/security/use-ai-securely-and-responsibly): Develop and deploy AI systems in a responsible and secure manner. The recommendations for this principle are aligned with guidance in the [AI and ML perspective](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml) of the Well-Architected Framework and in Google's [Secure AI Framework (SAIF)](https://saif.google).
- [Use AI for security](https://docs.cloud.google.com/architecture/framework/security/use-ai-for-security): Use AI capabilities to improve your existing security systems and processes through [Gemini in Security](https://cloud.google.com/security/ai) and overall platform-security capabilities. Use AI as a tool to increase the automation of remedial work and ensure security hygiene to make other systems more secure.
- [Meet regulatory, compliance, and privacy needs](https://docs.cloud.google.com/architecture/framework/security/meet-regulatory-compliance-and-privacy-needs): Adhere to industry-specific regulations, compliance standards, and privacy requirements. Google Cloud helps you meet these obligations through products like Assured Workloads, Organization Policy Service, and our [compliance resource center](https://cloud.google.com/security/compliance/).

## Organizational security mindset

A security-focused organizational mindset is crucial for successful cloud
adoption and operation. This mindset should be deeply ingrained in your
organization's culture and reflected in its practices, which are guided by core
security principles as described earlier.

An organizational security mindset emphasizes that you think about security
during system design, assume zero trust, and integrate security features
throughout your development process. In this mindset, you also think proactively
about cyber-defense measures, use AI securely and for security, and consider
your regulatory, privacy, and compliance requirements. By embracing these
principles, your organization can cultivate a security-first culture that
proactively addresses threats, protects valuable assets, and helps to ensure
responsible technology usage.

## Focus areas of cloud security

This section describes the areas for you to focus on when you plan,
implement, and manage security for your applications, systems, and data. The
recommendations in each principle of this pillar are relevant to one or more of
these focus areas. Throughout the rest of this document, the recommendations
specify the corresponding security focus areas to provide further clarity and
context.

| **Focus area** | **Activities and components** | **Related Google Cloud products, capabilities, and solutions** |
|---|---|---|
| Infrastructure security | - Secure network infrastructure. - Encrypt data in transit and at rest. - Control traffic flow. - Secure IaaS and PaaS services. - Protect against unauthorized access. | - [Firewall Policies](https://docs.cloud.google.com/firewall/docs/firewall-policies-overview) - [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) - [Google Cloud Armor](https://docs.cloud.google.com/armor/docs/cloud-armor-overview) - [Cloud Next Generation Firewall](https://docs.cloud.google.com/firewall/docs/about-firewalls) - [Secure Web Proxy](https://docs.cloud.google.com/secure-web-proxy/docs/overview) |
| Identity and access management | - Use authentication, authorization, and access controls. - Manage cloud identities. - Manage identity and access management policies. | - [Cloud Identity](https://docs.cloud.google.com/identity/docs/overview) - [Google's Identity and Access Management (IAM) service](https://docs.cloud.google.com/iam/docs/overview) - [Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation) - [Workload Identity Federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation) |
| Data security | - Store data in Google Cloud securely. - Control access to the data. - Discover and classify the data. - Design necessary controls, such as encryption, access controls, and data loss prevention. - Protect data at rest, in transit, and in use. | - [Google's IAM service](https://docs.cloud.google.com/iam/docs/overview) - [Sensitive Data Protection](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview) - [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) - [Cloud KMS](https://docs.cloud.google.com/kms/docs/key-management-service) - [Confidential Computing](https://docs.cloud.google.com/confidential-computing/docs/confidential-computing-overview) |
| AI and ML security | - Apply security controls at different layers of the AI and ML infrastructure and pipeline. - Ensure model safety. | - [Google's SAIF](https://saif.google/) - [Model Armor](https://docs.cloud.google.com/security-command-center/docs/model-armor-overview) |
| Security operations (SecOps) | - Adopt a modern SecOps platform and set of practices, for effective incident management, threat detection, and response processes. - Monitor systems and applications continuously for security events. | - [Google Security Operations](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview) |
| Application security | - Secure applications against software vulnerabilities and attacks. | - [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/overview) - [Artifact Analysis](https://docs.cloud.google.com/artifact-analysis/docs/artifact-analysis) - [Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs/overview) - [Assured Open Source Software](https://docs.cloud.google.com/assured-open-source-software/docs/overview) - [Google Cloud Armor](https://docs.cloud.google.com/armor/docs/cloud-armor-overview) - [Web Security Scanner](https://docs.cloud.google.com/security-command-center/docs/concepts-web-security-scanner-overview) |
| Cloud governance, risk, and compliance | - Establish policies, procedures, and controls to manage cloud resources effectively and securely. | - [Organization Policy Service](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview) - [Cloud Asset Inventory](https://docs.cloud.google.com/asset-inventory/docs/asset-inventory-overview) - [Security Command Center Enterprise](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview) - [Resource Manager](https://docs.cloud.google.com/resource-manager/docs) |
| Logging, auditing, and monitoring | - Analyze logs to identify potential threats. - Track and record system activities for compliance and security analysis. | - [Cloud Logging](https://docs.cloud.google.com/logging/docs/overview) - [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview) - [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit) - [VPC Flow Logs](https://docs.cloud.google.com/vpc/docs/flow-logs) |

## Contributors

Authors:

- [Wade Holmes](https://www.linkedin.com/in/wholmes) \| Global Solutions Director
- [Hector Diaz](https://www.linkedin.com/in/hectorgdiaz) \| Cloud Security Architect
- Carlos Leonardo Rosario \| Google Cloud Security Specialist
- [John Bacon](https://www.linkedin.com/in/johnbac/) \| Partner Solutions Architect
- [Sachin Kalra](http://www.linkedin.com/in/thesachinkalra) \| Global Security Solution Manager

<br />

Other contributors:

- [Anton Chuvakin](https://www.linkedin.com/in/chuvakin/) \| Security Advisor, Office of the CISO
- [Daniel Lees](https://www.linkedin.com/in/daniellees) \| Cloud Security Architect
- [Filipe Gracio, PhD](https://www.linkedin.com/in/filipegracio) \| Customer Engineer, AI/ML Specialist
- [Gary Harmson](https://www.linkedin.com/in/garyharmson) \| Principal Architect
- [Gino Pelliccia](https://www.linkedin.com/in/gino-pelliccia-13637025) \| Principal Architect
- [Jose Andrade](https://www.linkedin.com/in/jmandrade) \| Customer Engineer, SRE Specialist
- [Kumar Dhanagopal](https://www.linkedin.com/in/kumardhanagopal) \| Cross-Product Solution Developer
- [Laura Hyatt](https://www.linkedin.com/in/laura-hyatt) \| Customer Engineer, FSI
- [Marwan Al Shawi](https://www.linkedin.com/in/marwanalshawi) \| Partner Customer Engineer
- [Nicolas Pintaux](https://www.linkedin.com/in/nicolaspintaux) \| Customer Engineer, Application Modernization Specialist
- [Noah McDonald](https://www.linkedin.com/in/noah-mcdonald-77b04a173) \| Cloud Security Consultant
- [Osvaldo Costa](https://www.linkedin.com/in/osvaldocostajr) \| Networking Specialist Customer Engineer
- [Radhika Kanakam](https://www.linkedin.com/in/radhika-kanakam-18ab876) \| Program Lead, Google Cloud Well-Architected Framework
- [Samantha He](https://www.linkedin.com/in/samantha-he-05a98173) \| Technical Writer
- [Susan Wu](https://www.linkedin.com/in/susanwu88) \| Outbound Product Manager

<br />

<br />

<br />


# Implement security by design

This principle in the security pillar of the
[Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework)
provides recommendations to incorporate robust security features, controls, and
practices into the design of your cloud applications, services, and platforms.
From ideation to operations, security is more effective when it's embedded as an
integral part of every stage of your design process.

## Principle overview

As explained in
[An Overview of Google's Commitment to Secure by Design](https://static.googleusercontent.com/media/publicpolicy.google/en//resources/google_commitment_secure_by_design_overview.pdf),
*secure by default* and *secure by design* are often used interchangeably, but
they represent distinct approaches to building secure systems. Both approaches
aim to minimize vulnerabilities and enhance security, but they differ in scope
and implementation:

- **Secure by default**: focuses on ensuring that a system's default settings are set to a secure mode, minimizing the need for users or administrators to take actions to secure the system. This approach aims to provide a baseline level of security for all users.
- **Secure by design**: emphasizes proactively incorporating security considerations throughout a system's development lifecycle. This approach is about anticipating potential threats and vulnerabilities early and making design choices that mitigate risks. This approach involves using secure coding practices, conducting security reviews, and embedding security throughout the design process. The secure-by-design approach is an overarching philosophy that guides the development process and helps to ensure that security isn't an afterthought but is an integral part of a system's design.

## Recommendations

To implement the secure by design principle for your cloud workloads, consider
the recommendations in the following sections:

- [Choose system components that help to secure your workloads](https://docs.cloud.google.com/architecture/framework/printable#choose-system-components)
- [Build a layered security approach](https://docs.cloud.google.com/architecture/framework/printable#build_a_layered_security_approach)
- [Use hardened and attested infrastructure and services](https://docs.cloud.google.com/architecture/framework/printable#use_hardened_and_attested_infrastructure_and_services)
- [Encrypt data at rest and in transit](https://docs.cloud.google.com/architecture/framework/printable#encrypt_data_at_rest_and_in_transit)

### Choose system components that help to secure your workloads

This recommendation is relevant to all of the
[focus areas](https://docs.cloud.google.com/architecture/framework/security#focus_areas_of_cloud_security).

A fundamental decision for effective security is the selection of robust system
components---including both hardware and software components---that constitute
your platform, solution, or service. To reduce the security attack surface and
limit potential damage, you must also carefully consider the deployment patterns
of these components and their configurations.

In your application code, we recommend that you use straightforward, safe, and
reliable libraries, abstractions, and application frameworks in order to eliminate
classes of vulnerabilities. To scan for vulnerabilities in software libraries,
you can use third-party tools. You can also use
[Assured Open Source Software](https://cloud.google.com/security/products/assured-open-source-software),
which helps to reduce risks to your software supply chain by using open source
software (OSS) packages that Google uses and secures.

Your infrastructure must use networking, storage, and compute options that
support safe operation and align with your security requirements and risk
acceptance levels. Infrastructure security is important for both internet-facing
and internal workloads.

For information about other Google solutions that support this recommendation,
see
[Implement shift-left security](https://docs.cloud.google.com/architecture/framework/security/implement-shift-left-security).

### Build a layered security approach

This recommendation is relevant to the following
[focus areas](https://docs.cloud.google.com/architecture/framework/security#focus_areas_of_cloud_security):

- AI and ML security
- Infrastructure security
- Identity and access management
- Data security

We recommend that you implement security at each layer of your application and
infrastructure stack by applying a defense-in-depth approach.

Use the security features in each component of your platform. To limit access
and identify the boundaries of the potential impact (that is, the *blast radius*)
in the event of a security incident, do the following:

- Simplify your system's design to accommodate flexibility where possible.
- Document the security requirements of each component.
- Incorporate a robust secured mechanism to address resiliency and recovery requirements.

When you design the security layers, perform a risk assessment to determine the
security features that you need in order to meet internal security requirements
and external regulatory requirements. We recommend that you use an
industry-standard risk assessment framework that applies to cloud environments
and that is relevant to your regulatory requirements. For example, the Cloud
Security Alliance (CSA) provides the
[Cloud Controls Matrix (CCM)](https://cloudsecurityalliance.org/research/cloud-controls-matrix/).
Your risk assessment provides you with a catalog of risks and corresponding
security controls to mitigate them.

When you perform the risk assessment, remember that you have a shared
responsibility arrangement with your cloud provider. Therefore, your risks in a
cloud environment differ from your risks in an on-premises environment. For
example, in an on-premises environment, you need to mitigate vulnerabilities to
your hardware stack. In contrast, in a cloud environment, the cloud provider
bears these risks. Also, remember that the boundaries of shared responsibilities
differ between IaaS, PaaS, and SaaS services for each cloud provider.

After you identify potential risks, you must design and create a mitigation
plan that uses technical, administrative, and operational controls, as well as
contractual protections and third-party attestations. In addition, a threat
modeling method, such as the
[OWASP application threat modeling method](https://owasp.org/www-community/Threat_Modeling_Process),
helps you to identify potential gaps and suggest actions to address the gaps.

### Use hardened and attested infrastructure and services

This recommendation is relevant to all of the
[focus areas](https://docs.cloud.google.com/architecture/framework/security#focus_areas_of_cloud_security).

A mature security program mitigates new vulnerabilities as described in
security bulletins. The security program should also provide remediation to fix
vulnerabilities in existing deployments and secure your VM and container
images. You can use hardening guides that are specific to the OS and application
of your images, as well as benchmarks like the one provided by the
[Center of Internet Security (CIS)](https://www.cisecurity.org/benchmark/google_cloud_computing_platform).

If you use custom images for your Compute Engine VMs, you need to patch the
images yourself. Alternatively, you can use Google-provided
[curated OS images](https://docs.cloud.google.com/compute/docs/images),
which are patched regularly. To run containers on Compute Engine VMs, use
Google-curated
[Container-optimized OS images](https://docs.cloud.google.com/container-optimized-os/docs).
Google regularly patches and updates these images.

If you use GKE, we recommend that you enable
[node auto-upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades)
so that Google updates your cluster nodes with the latest patches. Google
manages GKE control planes, which are automatically updated
and patched. To further reduce the attack surface of your containers, you can
use
[distroless images](https://github.com/GoogleContainerTools/distroless).
Distroless images are ideal for security-sensitive applications, microservices,
and situations where minimizing the image size and attack surface is
paramount.

For sensitive workloads, use
[Shielded VM](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm),
which prevents malicious code from being loaded during the VM boot cycle.
Shielded VM instances provide boot security, monitor integrity, and use
the
[Virtual Trusted Platform Module (vTPM)](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#vtpm).

To help secure SSH access,
[OS Login](https://docs.cloud.google.com/compute/docs/oslogin)
lets your employees connect to your VMs by using
[Identity and Access Management (IAM) permissions](https://docs.cloud.google.com/compute/docs/oslogin/set-up-oslogin#configure_users)
as the source of truth instead of relying on SSH keys. Therefore, you don't need
to manage SSH keys throughout your organization. OS Login ties an
administrator's access to their employee lifecycle, so when employees change
roles or leave your organization, their access is revoked with their account. OS
Login also supports
[Google two-factor authentication](https://support.google.com/accounts/answer/185839),
which adds an extra layer of security against account takeover attacks.

In GKE, application instances run within Docker
containers. To enable a defined risk profile and to restrict employees from
making changes to containers, ensure that your containers are stateless and
immutable. The immutability principle means that your employees don't modify the
container or access it interactively. If the container must be changed, you
build a new image and redeploy that image. Enable SSH access to the underlying
containers only in specific debugging scenarios.

To help globally secure configurations across your environment, you can use
[organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview)
to set constraints or guardrails on resources that affect the behavior of your
cloud assets. For example, you can define the following organization policies
and apply them either globally across a Google Cloud organization or
selectively at the level of a folder or project:

- Disable external IP address allocation to VMs.
- Restrict resource creation to specific geographical locations.
- Disable the creation of Service Accounts or their keys.

### Encrypt data at rest and in transit

This recommendation is relevant to the following
[focus areas](https://docs.cloud.google.com/architecture/framework/security#focus_areas_of_cloud_security):

- Infrastructure security
- Data security

Data encryption is a foundational control to protect sensitive information, and
it's a key part of
[data governance](https://cloud.google.com/learn/what-is-data-governance).
An effective data protection strategy includes access control, data segmentation
and geographical residency, auditing, *and* encryption implementation that's
based on a careful assessment of requirements.

By default, Google Cloud
[encrypts customer data that's stored at rest](https://docs.cloud.google.com/docs/security/encryption/default-encryption),
with no action required from you. In addition to default encryption,
Google Cloud provides options for envelope encryption and encryption key
management. You must identify the solutions that best fit your requirements for
key generation, storage, and rotation, whether you're choosing the keys for your
storage, for compute, or for big data workloads. For example,
[Customer-managed encryption keys (CMEKs)](https://docs.cloud.google.com/kms/docs/cmek)
can be created in
[Cloud Key Management Service (Cloud KMS)](https://docs.cloud.google.com/kms/docs/kms-autokey).
The CMEKs can be either software-based or
[HSM-protected](https://docs.cloud.google.com/kms/docs/hsm)
to meet your regulatory or compliance requirements, such as the need to rotate
encryption keys regularly. Cloud KMS Autokey lets you automate the
provisioning and assignment of CMEKs. In addition, you can bring your own keys
that are sourced from a third-party key management system by using
[Cloud External Key Manager (Cloud EKM)](https://docs.cloud.google.com/kms/docs/ekm).

We strongly recommend that data be encrypted in-transit.
[Google encrypts and authenticates data in transit](https://docs.cloud.google.com/docs/security/encryption-in-transit)
at one or more network layers when data moves outside physical boundaries that
aren't controlled by Google or on behalf of Google. All VM-to-VM traffic within
a VPC network and between peered VPC networks is encrypted. You can use
[MACsec](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/macsec-overview)
for encryption of traffic over Cloud Interconnect connections. IPsec provides
encryption for traffic over
[Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview)
connections. You can protect application-to-application traffic in the cloud by
using security features like
[TLS and mTLS configurations in Apigee](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/ingress-tls)
and
[Cloud Service Mesh](https://cloud.google.com/products/service-mesh)
for containerized applications.

By default, Google Cloud encrypts data at rest and data in transit across
the network. However, data isn't encrypted by default while it's in use in
memory. If your organization handles confidential data, you need to mitigate any
threats that undermine the confidentiality and integrity of either the
application or the data in system memory. To mitigate these threats, you can use
Confidential Computing, which provides a trusted execution environment for your
compute workloads. For more information, see
[Confidential VM overview](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/confidential-vm-overview).

<br />


# Implement zero trust

This principle in the security pillar of the
[Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework)
helps you ensure comprehensive security across your cloud workloads. The principle
of zero trust emphasizes the following practices:

- Eliminating implicit trust
- Applying the principle of least privilege to access control
- Enforcing explicit validation of all access requests
- Adopting an *assume-breach* mindset to enable continuous verification and security posture monitoring

## Principle overview

The *zero-trust* model shifts the security focus from perimeter-based security
to an approach where no user or device is considered to be inherently
trustworthy. Instead, every access request must be verified, regardless of its
origin. This approach involves authenticating and authorizing every user and
device, validating their context (location and device posture), and granting
least privilege access to only the necessary resources.

Implementing the zero-trust model helps your organization enhance its
security posture by minimizing the impact of potential breaches and protecting
sensitive data and applications against unauthorized access. The zero-trust
model helps you ensure confidentiality, integrity, and availability of data and
resources in the cloud.

## Recommendations

To implement the zero-trust model for your cloud workloads, consider the
recommendations in the following sections:

- [Secure your network](https://docs.cloud.google.com/architecture/framework/printable#secure_your_network)
- [Verify every access attempt explicitly](https://docs.cloud.google.com/architecture/framework/printable#verify_every_access_attempt_explicitly)
- [Monitor and maintain your network](https://docs.cloud.google.com/architecture/framework/printable#monitor_and_maintain_your_network)

### Secure your network

This recommendation is relevant to the following
[focus area](https://docs.cloud.google.com/architecture/framework/security#focus_areas_of_cloud_security):
Infrastructure security.

Transitioning from conventional perimeter-based security to a zero-trust model
requires multiple steps. Your organization might have already integrated certain
zero-trust controls into its security posture. However, a zero-trust model
isn't a singular product or solution. Instead, it's a holistic integration of
multiple security layers and best practices. This section describes
recommendations and techniques to implement zero trust for network security.

- **Access control** : Enforce access controls based on user identity and context by using solutions like [Chrome Enterprise Premium](https://chromeenterprise.google/products/chrome-enterprise-premium/) and [Identity-Aware Proxy (IAP)](https://docs.cloud.google.com/iap/docs/concepts-overview). By doing this, you shift security from the network perimeter to individual users and devices. This approach enables granular access control and reduces the attack surface.
- **Network security** : Secure network connections between your on-premises, Google Cloud, and multicloud environments.
  - Use the private connectivity methods from [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview) and [IPsec VPNs](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview).
  - To help secure access to Google Cloud services and APIs, use [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect).
  - To help secure outbound access from workloads deployed on [Google Kubernetes Engine (GKE)](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview) and related products, use [Cloud Service Mesh egress gateways](https://docs.cloud.google.com/service-mesh/docs/security/egress-gateways-best-practices).
- **Network design** : Prevent potential security risks by deleting default networks in existing projects and disabling the creation of default networks in new projects.
  - To avoid conflicts, plan your network and IP address allocation carefully.
  - To enforce effective access control, limit the number of Virtual Private Cloud (VPC) networks per project.
- **Segmentation** : Isolate workloads but maintain centralized network management.
  - To segment your network, use [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc).
  - Define firewall policies and rules at the organization, folder, and VPC network levels.
  - To prevent [data exfiltration](https://en.wikipedia.org/wiki/Data_exfiltration), establish secure perimeters around sensitive data and services by using [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview).
- **Perimeter security** : Protect against DDoS attacks and web application threats.
  - To protect against threats, use [Google Cloud Armor](https://docs.cloud.google.com/armor/docs).
  - Configure security policies to allow, deny, or redirect traffic at the Google Cloud edge.
- **Automation** : Automate infrastructure provisioning by embracing infrastructure as code (IaC) principles and by using tools like Terraform, Jenkins, and [Cloud Build](https://docs.cloud.google.com/build/docs/overview). IaC helps to ensure consistent security configurations, simplified deployments, and rapid rollbacks in case of issues.
- **Secure foundation** : Establish a secure application environment by using the [Enterprise foundations blueprint](https://docs.cloud.google.com/architecture/blueprints/security-foundations). This blueprint provides prescriptive guidance and automation scripts to help you implement security best practices and configure your Google Cloud resources securely.

### Verify every access attempt explicitly

This recommendation is relevant to the following
[focus areas](https://docs.cloud.google.com/architecture/framework/security#focus_areas_of_cloud_security):

- Identity and access management
- Security operations (SecOps)
- Logging, auditing, and monitoring

Implement strong authentication and authorization mechanisms for any user,
device, or service that attempts to access your cloud resources. Don't rely on
location or network perimeter as a security control. Don't automatically trust
any user, device, or service, even if they are already inside the network.
Instead, every attempt to access resources must be rigorously authenticated and
authorized. You must implement strong identity verification measures, such as
multi-factor authentication (MFA). You must also ensure that access decisions
are based on granular policies that consider various contextual factors like
user role, device posture, and location.

To implement this recommendation, use the following methods, tools, and
technologies:

- **Unified identity management** : Ensure consistent identity management across your organization by using a single identity provider (IdP).
  - Google Cloud supports federation with most IdPs, including on-premises [Active Directory](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-active-directory-introduction). Federation lets you extend your existing identity management infrastructure to Google Cloud and enable single sign-on (SSO) for users.
  - If you don't have an existing IdP, consider using [Cloud Identity Premium](https://docs.cloud.google.com/identity/docs/editions) or [Google Workspace](https://workspace.google.com/).
- **Limited service account permissions** : Use [service accounts](https://docs.cloud.google.com/iam/docs/service-account-overview) carefully, and adhere to the principle of least privilege.
  - Grant only the necessary permissions required for each service account to perform its designated tasks.
  - Use [Workload Identity Federation](https://docs.cloud.google.com/iam/docs/workload-identities) for applications that run on Google Kubernetes Engine (GKE) or run outside Google Cloud to access resources securely.
- **Robust processes** : Update your identity processes to align with cloud security best practices.
  - To help ensure compliance with regulatory requirements, implement identity governance to track access, risks, and policy violations.
  - Review and update your existing processes for granting and auditing access-control roles and permissions.
- **Strong authentication** : Implement SSO for user authentication and implement MFA for privileged accounts.
  - Google Cloud supports various MFA methods, including [Titan Security Keys](https://cloud.google.com/security/products/titan-security-key), for enhanced security.
  - For workload authentication, use OAuth 2.0 or signed JSON Web Tokens (JWTs).
- **Least privilege** : Minimize the risk of unauthorized access and data breaches by enforcing the principles of least privilege and separation of duties.
  - Avoid overprovisioning user access.
  - Consider implementing just-in-time privileged access for sensitive operations.
- **Logging** : Enable audit logging for administrator and data access activities.
  - For analysis and threat detection, scan the logs by using [Security Command Center Enterprise](https://docs.cloud.google.com/security-command-center/docs/service-tiers#enterprise-tier) or [Google Security Operations](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview).
  - Configure appropriate log retention policies to balance security needs with storage costs.

### Monitor and maintain your network

This recommendation is relevant to the following
[focus areas](https://docs.cloud.google.com/architecture/framework/security#focus_areas_of_cloud_security):

- Logging, auditing, and monitoring
- Application security
- Security operations (SecOps)
- Infrastructure security

When you plan and implement security measures, assume that an attacker is
already inside your environment. This proactive approach involves using the following
multiple tools and techniques to provide visibility into your network:

- **Centralized logging and monitoring** : Collect and
  analyze security logs from all of your cloud resources through centralized
  [logging and monitoring](https://docs.cloud.google.com/stackdriver/docs).

  - Establish baselines for normal network behavior, detect anomalies, and identify potential threats.
  - Continuously analyze network traffic flows to identify suspicious patterns and potential attacks.
- **Insights into network performance and security** : Use tools like
  [Network Analyzer](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/overview).
  Monitor traffic for unusual protocols, unexpected connections, or sudden spikes
  in data transfer, which could indicate malicious activity.

- **Vulnerability scanning and remediation**: Regularly scan your network and applications for vulnerabilities.

  - Use [Web Security Scanner](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings), which can automatically identify vulnerabilities in your Compute Engine instances, containers, and GKE clusters.
  - Prioritize remediation based on the severity of vulnerabilities and their potential impact on your systems.
- **Intrusion detection** : Monitor network traffic for malicious activity and
  automatically block or get alerts for suspicious events by using
  [Cloud IDS](https://docs.cloud.google.com/intrusion-detection-system/docs/overview)
  and
  [Cloud NGFW intrusion prevention service](https://docs.cloud.google.com/firewall/docs/about-intrusion-prevention).

- **Security analysis** : Consider implementing
  [Google SecOps](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)
  to correlate security events from various sources, provide real-time analysis of
  security alerts, and facilitate incident response.

- **Consistent configurations**: Ensure that you have consistent security
  configurations across your network by using configuration management tools.

<br />


# Implement shift-left security

This principle in the security pillar of the
[Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework)
helps you identify practical controls that you can implement early in the
software development lifecycle to improve your security posture. It provides
recommendations that help you implement preventive security guardrails and
post-deployment security controls.

## Principle overview

*Shift-left security* means adopting security practices early in the software
development lifecycle. This principle has the following goals:

- Avoid security defects before system changes are made. Implement preventive security guardrails and adopt practices such as infrastructure as code (IaC), policy as code, and security checks in the CI/CD pipeline. You can also use other platform-specific capabilities like [Organization Policy Service](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview) and [hardened GKE clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster) in Google Cloud.
- Detect and fix security bugs early, fast, and reliably after any system changes are committed. Adopt practices like code reviews, post-deployment vulnerability scanning, and security testing.

The
[Implement security by design](https://docs.cloud.google.com/architecture/framework/security/implement-security-by-design)
and shift-left security principles are related but they differ in scope.
The security-by-design principle helps you to avoid fundamental design flaws that would
require re-architecting the entire system. For example, a threat-modeling
exercise reveals that the current design doesn't include an authorization
policy, and all users would have the same level of access without it. Shift-left
security helps you to avoid implementation defects (bugs and misconfigurations)
before changes are applied, and it enables fast, reliable fixes after deployment.

## Recommendations

To implement the shift-left security principle for your cloud workloads,
consider the recommendations in the following sections:

- [Adopt preventive security controls](https://docs.cloud.google.com/architecture/framework/printable#adopt_preventive_security_controls)
- [Automate provisioning and management of cloud resources](https://docs.cloud.google.com/architecture/framework/printable#automate_provisioning_and_management_of_cloud_resources)
- [Automate secure application releases](https://docs.cloud.google.com/architecture/framework/printable#automate_secure_application_releases)
- [Ensure that application deployments follow approved processes](https://docs.cloud.google.com/architecture/framework/printable#ensure_that_application_deployments_follow_approved_processes)
- [Scan for known vulnerabilities before application deployment](https://docs.cloud.google.com/architecture/framework/printable#scan_for_known_vulnerabilities_before_application_deployment)
- [Monitor your application code for known vulnerabilities](https://docs.cloud.google.com/architecture/framework/printable#monitor_your_application_code_for_known_vulnerabilities)

### Adopt preventive security controls

This recommendation is relevant to the following
[focus areas](https://docs.cloud.google.com/architecture/framework/security#focus_areas_of_cloud_security):

- Identity and access management
- Cloud governance, risk, and compliance

Preventive security controls are crucial for maintaining a strong security
posture in the cloud. These controls help you proactively mitigate risks. You
can prevent misconfigurations and unauthorized access to resources, enable
developers to work efficiently, and help ensure compliance with industry
standards and internal policies.

Preventive security controls are more effective when they're implemented by
using infrastructure as code (IaC). With IaC, preventive security controls can
include more customized checks on the infrastructure code before changes are
deployed. When combined with automation, preventive security controls can run as
part of your CI/CD pipeline's automatic checks.

The following products and Google Cloud capabilities can help you implement
preventive controls in your environment:

- [Organization Policy Service constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview): configure predefined and custom constraints with centralized control.
- [VPC Service Controls](https://cloud.google.com/security/vpc-service-controls): create perimeters around your Google Cloud services.
- Identity and Access Management (IAM), [Privileged Access Manager](https://docs.cloud.google.com/iam/docs/pam-overview), and [principal access boundary policies](https://docs.cloud.google.com/iam/docs/principal-access-boundary-policies): restrict access to resources.
- [Policy Controller](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/overview) and [Open Policy Agent (OPA)](https://www.openpolicyagent.org/): enforce IaC constraints in your CI/CD pipeline and avoid cloud misconfigurations.

IAM lets you authorize *who* can act on specific resources based
on permissions. For more information, see
[Access control for organization resources with IAM](https://docs.cloud.google.com/resource-manager/docs/access-control-org).

Organization Policy Service lets you set restrictions on resources to specify how they can
be configured. For example, you can use an organization policy to do the
following:

- [Limit resource sharing](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-domains) based on domain.
- [Limit the use of service accounts](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts).
- [Restrict the physical location](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations) of newly created resources.

In addition to using organizational policies, you can restrict access to
resources by using the following methods:

- [Tags with IAM](https://docs.cloud.google.com/iam/docs/tags-access-control): assign a tag to a set of resources and then set the access definition for the tag itself, rather than defining the access permissions on each resource.
- [IAM Conditions](https://docs.cloud.google.com/iam/docs/conditions-overview): define conditional, attribute-based access control for resources.
- Defense in depth: use VPC Service Controls to further restrict access to resources.

For more information about resource management, see
[Decide a resource hierarchy for your Google Cloud landing zone](https://docs.cloud.google.com/architecture/landing-zones/decide-resource-hierarchy).

### Automate provisioning and management of cloud resources

This recommendation is relevant to the following
[focus areas](https://docs.cloud.google.com/architecture/framework/security#focus_areas_of_cloud_security):

- Application security
- Cloud governance, risk, and compliance

Automating the provisioning and management of cloud resources and workloads is
more effective when you also adopt declarative IaC, as opposed to imperative
scripting. IaC isn't a security tool or practice on its own, but it helps you
to improve the security of your platform. Adopting IaC lets you create
repeatable infrastructure and provides your operations team with a known good
state. IaC also improves the efficiency of rollbacks, audit changes, and
troubleshooting.

When combined with CI/CD pipelines and automation, IaC also gives you the
ability to adopt practices such as *policy as code* with tools like OPA. You can
audit infrastructure changes over time and run automatic checks on the
infrastructure code before changes are deployed.

To automate the infrastructure deployment, you can use tools like
[Config Controller](https://docs.cloud.google.com/kubernetes-engine/enterprise/config-controller/docs/overview),
Terraform, Jenkins, and
[Cloud Build](https://docs.cloud.google.com/build).
To help you build a secure application environment using IaC and automation,
Google Cloud provides the
[enterprise foundations blueprint](https://docs.cloud.google.com/architecture/blueprints/security-foundations).
This blueprint is Google's opinionated design that follows all of our
recommended practices and configurations. The blueprint provides step-by-step
instructions to configure and deploy your Google Cloud topology by using
Terraform and Cloud Build.

You can modify the scripts of the
enterprise foundations blueprint to configure an environment that follows Google
recommendations and meets your own security requirements. You can further build
on the blueprint with additional blueprints or design your own automation. The
Google Cloud Architecture Center provides other blueprints that can be
implemented on top of the enterprise foundations blueprint. The following are a
few examples of these blueprints:

- [Deploy an enterprise developer platform on Google Cloud](https://docs.cloud.google.com/architecture/blueprints/enterprise-application-blueprint)
- [Deploy a secured serverless architecture using Cloud Run](https://docs.cloud.google.com/architecture/blueprints/serverless-blueprint)
- [Build and deploy generative AI and machine learning models in an enterprise](https://docs.cloud.google.com/architecture/blueprints/genai-mlops-blueprint)
- [Import data from Google Cloud into a secured BigQuery data warehouse](https://docs.cloud.google.com/architecture/blueprints/confidential-data-warehouse-blueprint)

### Automate secure application releases

This recommendation is relevant to the following
[focus area](https://docs.cloud.google.com/architecture/framework/security#focus_areas_of_cloud_security):
Application security.

Without automated tools, it can be difficult to deploy, update, and patch
complex application environments to meet consistent security requirements. We
recommend that you build automated CI/CD pipelines for your software development
lifecycle (SDLC). Automated CI/CD pipelines help you to remove manual errors,
provide standardized development feedback loops, and enable efficient product
iterations. Continuous delivery is one of the best practices that the
[DORA framework](https://dora.dev/research/?view=detail)
recommends.

Automating application releases by using CI/CD pipelines helps to improve your
ability to detect and fix security bugs early, fast, and reliably. For example,
you can scan for security vulnerabilities automatically when artifacts are
created, narrow the scope of security reviews, and roll back to a known and safe
version. You can also define policies for different environments (such as
development, test, or production environments) so that only verified artifacts
are deployed.

To help you automate application releases and embed security checks in your
CI/CD pipeline, Google Cloud provides multiple tools including
[Cloud Build](https://docs.cloud.google.com/build),
[Cloud Deploy](https://docs.cloud.google.com/deploy/docs),
[Web Security Scanner](https://docs.cloud.google.com/security-command-center/docs/concepts-web-security-scanner-overview),
and
[Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs).

To establish a process that verifies multiple security requirements in your SDLC,
use the
[Supply-chain Levels for Software Artifacts (SLSA)](https://slsa.dev)
framework, which has been defined by Google. SLSA requires security
checks for source code, build process, and code provenance. Many of these
requirements can be included in an automated CI/CD pipeline. To understand how
Google applies these practices internally, see
[Google Cloud's approach to change](https://docs.cloud.google.com/docs/cloud-approach-to-change).

### Ensure that application deployments follow approved processes

This recommendation is relevant to the following
[focus area](https://docs.cloud.google.com/architecture/framework/security#focus_areas_of_cloud_security):
Application security.

If an attacker compromises your CI/CD pipeline, your entire application stack
can be affected. To help secure the pipeline, you should enforce an established
approval process before you deploy the code into production.

If you use Google Kubernetes Engine (GKE) or
Cloud Run, you can establish an approval process by using
[Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs/overview).
Binary Authorization attaches configurable signatures to container images.
These signatures (also called *attestations*) help to validate the image. At
deployment time, Binary Authorization uses these attestations to determine
whether a process was completed. For example, you can use Binary Authorization
to do the following:

- Verify that a specific build system or CI pipeline created a container image.
- Validate that a container image is compliant with a vulnerability signing policy.
- Verify that a container image passes the criteria for promotion to the next deployment environment, such as from development to QA.

By using Binary Authorization, you can enforce that only trusted code runs on
your target platforms.

### Scan for known vulnerabilities before application deployment

This recommendation is relevant to the following
[focus area](https://docs.cloud.google.com/architecture/framework/security#focus_areas_of_cloud_security):
Application security.

We recommend that you use automated tools that can continuously perform
vulnerability scans on application artifacts before they're deployed to
production.

For containerized applications, use
[Artifact Analysis](https://docs.cloud.google.com/artifact-analysis/docs)
to automatically run vulnerability scans for container images.
Artifact Analysis scans new images when they're uploaded to
[Artifact Registry](https://docs.cloud.google.com/artifact-registry).
The scan extracts information about the system packages in the container. After
the initial scan, Artifact Analysis continuously monitors the metadata
of scanned images in Artifact Registry for new vulnerabilities. When
Artifact Analysis receives new and updated vulnerability information
from
[vulnerability sources](https://docs.cloud.google.com/artifact-analysis/docs/vulnerability-scanning#sources),
it does the following:

- Updates the metadata of the scanned images to keep them up to date.
- Creates new vulnerability occurrences for new notes.
- Deletes vulnerability occurrences that are no longer valid.

### Monitor your application code for known vulnerabilities

This recommendation is relevant to the following
[focus area](https://docs.cloud.google.com/architecture/framework/security#focus_areas_of_cloud_security):
Application security.

Use automated tools to constantly monitor your application code for known
vulnerabilities such as the
[OWASP Top 10](https://owasp.org/www-project-top-ten/).
For more information about Google Cloud products and features that support
OWASP Top 10 mitigation techniques, see
[OWASP Top 10 mitigation options on Google Cloud](https://docs.cloud.google.com/architecture/security/owasp-top-ten-mitigation).

Use
[Web Security Scanner](https://docs.cloud.google.com/security-command-center/docs/concepts-web-security-scanner-overview)
to help identify security vulnerabilities in your App Engine,
Compute Engine, and GKE web applications. The scanner
crawls your application, follows all of the links within the scope of your
starting URLs, and attempts to exercise as many user inputs and event handlers
as possible. It can automatically scan for and detect common vulnerabilities,
including
[cross-site scripting](https://en.wikipedia.org/wiki/Cross-site_scripting),
[code injection](https://en.wikipedia.org/wiki/Code_injection),
[mixed content](https://developer.mozilla.org/en-US/docs/Web/Security/Mixed_content),
and outdated or insecure libraries. Web Security Scanner provides early
identification of these types of vulnerabilities without distracting you with
false positives.

In addition, if you use GKE to manage fleets of
Kubernetes clusters, the security posture dashboard shows opinionated,
actionable recommendations to help improve your fleet's security posture.

<br />


# Implement preemptive cyber defense

This principle in the security pillar of the
[Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework)
provides recommendations to build robust cyber-defense programs as part of your
overall security strategy.

This principle emphasizes the use of threat intelligence to proactively guide
your efforts across the core cyber-defense functions, as defined in
[The Defender's Advantage: A guide to activating cyber defense](https://cloud.google.com/security/resources/defenders-advantage).

## Principle overview

When you defend your system against cyber attacks, you have a significant,
underutilized advantage against attackers. As
[the founder of Mandiant states](https://cloud.google.com/security/mandiant),
"You should know more about your business, your systems, your topology, your
infrastructure than any attacker does. This is an incredible advantage." To
help you use this inherent advantage, this document provides recommendations
about proactive and strategic cyber-defense practices that are mapped to the
Defender's Advantage framework.

## Recommendations

To implement preemptive cyber defense for your cloud workloads, consider the
recommendations in the following sections:

- [Integrate the functions of cyber defense](https://docs.cloud.google.com/architecture/framework/printable#integrate_the_functions_of_cyber_defense)
- [Use the Intelligence function in all aspects of cyber defense](https://docs.cloud.google.com/architecture/framework/printable#use_intelligence_in_all_aspects_of_cyber_defense)
- [Understand and capitalize on your defender's advantage](https://docs.cloud.google.com/architecture/framework/printable#understand_and_capitalize_on_your_defenders_advantage)
- [Validate and improve your defenses continuously](https://docs.cloud.google.com/architecture/framework/printable#validate_and_improve_your_defenses_continuously)
- [Manage and coordinate cyber-defense efforts](https://docs.cloud.google.com/architecture/framework/printable#manage_and_coordinate_cyber-defense_efforts)

### Integrate the functions of cyber defense

This recommendation is relevant to all of the
[focus areas](https://docs.cloud.google.com/architecture/framework/security#focus_areas_of_cloud_security).

The Defender's Advantage framework identifies six critical functions of
cyber defense: *Intelligence* , *Detect* , *Respond* , *Validate* , *Hunt* , and
*Mission Control.* Each function focuses on a unique part of the
cyber-defense mission, but these functions must be well-coordinated and
work together to provide an effective defense. Focus on building a robust
and integrated system where each function supports the others. If you need
a phased approach for adoption, consider the following suggested order.
Depending on your current cloud maturity, resource topology, and specific
threat landscape, you might want to prioritize certain functions.

1. **Intelligence**: The Intelligence function guides all the other functions. Understanding the threat landscape---including the most likely attackers, their tactics, techniques, and procedures (TTPs), and the potential impact---is critical to prioritizing actions across the entire program. The Intelligence function is responsible for stakeholder identification, definition of intelligence requirements, data collection, analysis and dissemination, automation, and the creation of a cyber threat profile.
2. **Detect and Respond**: These functions make up the core of active defense, which involves identifying and addressing malicious activity. These functions are necessary to act on the intelligence that's gathered by the intelligence function. The Detect function requires a methodical approach that aligns detections to attacker TTPs and ensures robust logging. The Respond function must focus on initial triage, data collection, and incident remediation.
3. **Validate**: The Validate function is a continuous process that provides assurance that your security control ecosystem is up-to-date and operating as designed. This function ensures that your organization understands the attack surface, knows where vulnerabilities exist, and measures the effectiveness of controls. Security validation is also an important component of the detection engineering lifecycle and must be used to identify detection gaps and create new detections.
4. **Hunt**: The Hunt function involves proactively searching for active threats within an environment. This function must be implemented when your organization has a baseline level of maturity in the Detect and Respond functions. The Hunt function expands the detection capabilities and helps to identify gaps and weaknesses in controls. The Hunt function must be based on specific threats. This advanced function benefits from a foundation of robust intelligence, detection, and response capabilities.
5. **Mission Control**: The Mission Control function acts as the central hub that connects all of the other functions. This function is responsible for strategy, communication, and decisive action across your cyber-defense program. It ensures that all of the functions are working together and that they're aligned with your organization's business goals. You must focus on establishing a clear understanding of the purpose of the Mission Control function before you use it to connect the other functions.

### Use the Intelligence function in all aspects of cyber defense

This recommendation is relevant to all of the
[focus areas](https://docs.cloud.google.com/architecture/framework/security#focus_areas_of_cloud_security).

This recommendation highlights the Intelligence function as a core part of a strong
cyber-defense program. Threat intelligence provides knowledge about threat
actors, their TTPs, and indicators of compromise (IOCs). This knowledge should
inform and prioritize actions across all cyber-defense functions. An
intelligence-driven approach helps you align defenses to meet the threats that
are most likely to affect your organization. This approach also helps with
efficient allocation and prioritization of resources.

The following Google Cloud products and features help you take advantage
of threat intelligence to guide your security operations. Use these features to
identify and prioritize potential threats, vulnerabilities, and risks, and then
plan and implement appropriate actions.

- [Google Security Operations (Google SecOps)](https://cloud.google.com/security/products/security-operations)
  helps you store and analyze security data centrally. Use
  Google SecOps to map logs into a common model, enrich the
  logs, and link the logs to timelines for a comprehensive view of attacks.
  You can also create detection rules, set up IoC matching, and perform
  threat-hunting activities. The platform also provides curated detections,
  which are predefined and managed rules to help identify threats.
  Google SecOps can also integrate with
  [Mandiant frontline intelligence](https://cloud.google.com/security/products/threat-intelligence).
  Google SecOps uniquely integrates industry-leading AI, along
  with
  [threat intelligence from Mandiant](https://docs.cloud.google.com/chronicle/docs/detection)
  and
  [Google VirusTotal](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/virustotal).
  This integration is critical for threat evaluation and understanding who is
  targeting your organization and the potential impact.

- [Security Command Center](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)
  Enterprise, which is powered by Google AI, enables security professionals to
  efficiently assess, investigate, and respond to security issues across
  multiple cloud environments. The security professionals who can benefit
  from Security Command Center include security operations center (SOC) analysts,
  vulnerability and posture analysts, and compliance managers. Security Command Center
  Enterprise enriches security data, assesses risk, and prioritizes
  vulnerabilities. This solution provides teams with the information that they
  need to address high-risk vulnerabilities and to remediate active threats.

- [Chrome Enterprise Premium](https://docs.cloud.google.com/chrome-enterprise-premium/docs/overview)
  offers threat and data protection, which helps to protect users from
  exfiltration risks and prevents malware from getting onto
  enterprise-managed devices. Chrome Enterprise Premium also provides visibility into
  unsafe or potentially unsafe activity that can happen within the browser.

- Network monitoring, through tools like
  [Network Intelligence Center](https://docs.cloud.google.com/network-intelligence-center),
  provides visibility into network performance. Network monitoring can also
  help you detect unusual traffic patterns or detect data transfer amounts
  that might indicate an attack or data exfiltration attempt.

### Understand and capitalize on your defender's advantage

This recommendation is relevant to all of the
[focus areas](https://docs.cloud.google.com/architecture/framework/security#focus_areas_of_cloud_security).

As mentioned earlier, you have an advantage over attackers when you have
a thorough understanding of your business, systems, topology, and
infrastructure. To capitalize on this knowledge advantage, utilize this data
about your environments during cyberdefense planning.

Google Cloud provides the following features to help you proactively gain
visibility to identify threats, understand risks, and respond in a timely manner
to mitigate potential damage:

- Chrome Enterprise Premium helps you enhance security for enterprise devices by
  protecting users from exfiltration risks. It extends
  [Sensitive Data Protection services](https://cloud.google.com/security/products/dlp)
  into the browser, and prevents malware. It also offers features like
  protection against malware and phishing to help prevent exposure to unsafe
  content. In addition, it gives you control over the installation of
  extensions to help prevent unsafe or unvetted extensions. These
  capabilities help you establish a secure foundation for your operations.

- Security Command Center Enterprise provides a continuous
  [risk engine](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn)
  that offers comprehensive and ongoing risk analysis and management. The risk
  engine feature enriches security data, assesses risk, and prioritizes
  vulnerabilities to help fix issues quickly. Security Command Center enables your
  organization to proactively identify weaknesses and implement mitigations.

- Google SecOps centralizes security data and provides
  enriched logs with timelines. This enables defenders to proactively
  identify active compromises and adapt defenses based on attackers' behavior.

- Network monitoring helps identify irregular network activity that might
  indicate an attack and it provides early indicators that you can use to take
  action. To help proactively protect your data from theft, continuously monitor
  for data exfiltration and use the provided tools.

### Validate and improve your defenses continuously

This recommendation is relevant to all of the
[focus areas](https://docs.cloud.google.com/architecture/framework/security#focus_areas_of_cloud_security).

This recommendation emphasizes the importance of targeted testing and
continuous validation of controls to understand strengths and weaknesses
across the entire attack surface. This includes validating the
effectiveness of controls, operations, and staff through methods like the
following:

- [Penetration tests](https://cloud.google.com/security/resources/datasheets/penetration-testing#penetration-testing)
- [Red-blue team](https://services.google.com/fh/files/blogs/google_ai_red_team_digital_final.pdf) and [purple team](https://cloud.google.com/security/resources/datasheets/consulting-services-continuous-purple-team-assessment) exercises
- [Tabletop exercises](https://cloud.google.com/security/resources/datasheets/consulting-services-tabletop-exercise)

You must also actively search for threats and use the results to improve
detection and visibility. Use the following tools to continuously test and
validate your defenses against real-world threats:

- Security Command Center Enterprise provides a continuous risk engine to evaluate
  vulnerabilities and prioritize remediation, which enables ongoing
  evaluation of your overall security posture. By prioritizing issues,
  Security Command Center Enterprise helps you to ensure that resources are used effectively.

- Google SecOps offers threat-hunting and curated
  detections that let you proactively identify weaknesses in your controls.
  This capability enables continuous testing and improvement of your ability
  to detect threats.

- Chrome Enterprise Premium provides threat and data protection features that
  can help you to address new and evolving threats, and continuously update
  your defenses against exfiltration risks and malware.

- Cloud Next Generation Firewall (Cloud NGFW) provides network monitoring
  and data-exfiltration monitoring. These capabilities can help you to validate
  the effectiveness of your current security posture and identify potential
  weaknesses. Data-exfiltration monitoring helps you to validate the strength
  of your organization's data protection mechanisms and make proactive
  adjustments where necessary. When you integrate threat findings from
  Cloud NGFW with Security Command Center and Google SecOps,
  you can optimize network-based threat detection, optimize threat response,
  and automate playbooks. For more information about this integration, see
  [Unifying Your Cloud Defenses: Security Command Center \& Cloud NGFW Enterprise](https://www.googlecloudcommunity.com/gc/Community-Blog/Unifying-Your-Cloud-Defenses-Security-Command-Center-amp-Cloud/ba-p/843202).

### Manage and coordinate cyber-defense efforts

This recommendation is relevant to all of the
[focus areas](https://docs.cloud.google.com/architecture/framework/security#focus_areas_of_cloud_security).

As described earlier in
[Integrate the functions of cyber defense](https://docs.cloud.google.com/architecture/framework/printable#integrate_the_functions_of_cyber_defense),
the Mission Control function interconnects the other functions of the
cyber-defense program. This function enables coordination and unified
management across the program. It also helps you coordinate with other teams
that don't work on cybersecurity. The Mission Control function promotes
empowerment and accountability, facilitates agility and expertise, and drives
responsibility and transparency.

The following products and features can help you implement the Mission Control
function:

- Security Command Center Enterprise acts as a central hub for coordinating and managing your cyber-defense operations. It brings tools, teams, and data together, along with the built-in Google SecOps response capabilities. Security Command Center provides clear visibility into your organization's security state and enables the identification of security misconfigurations across different resources.
- Google SecOps provides a platform for teams to respond to threats by mapping logs and creating timelines. You can also define detection rules and search for threats.
- [Google Workspace](https://workspace.google.com/security/) and Chrome Enterprise Premium help you to manage and control end-user access to sensitive resources. You can define granular access controls based on user identity and the context of a request.
- Network monitoring provides insights into the performance of network resources. You can import network monitoring insights into Security Command Center and Google SecOps for centralized monitoring and correlation against other timeline based data points. This integration helps you to detect and respond to potential network usage changes caused by nefarious activity.
- Data-exfiltration monitoring helps to identify possible data loss incidents. With this feature, you can efficiently mobilize an incident response team, assess damages, and limit further data exfiltration. You can also improve current policies and controls to ensure data protection.

### Product summary

The following table lists the products and features that are described in this
document and maps them to the associated recommendations and security
capabilities.

| Google Cloud product | Applicable recommendations |
|---|---|
| Google SecOps | **Use the Intelligence function in all aspects of cyber defense** : Enables threat hunting and IoC matching, and integrates with Mandiant for comprehensive threat evaluation. **Understand and capitalize on your defender's advantage**: Provides curated detections and centralizes security data for proactive compromise identification. **Validate and improve your defenses continuously** : Enables continuous testing and improvement of threat detection capabilities. **Manage and coordinate cyber-defense efforts through Mission Control**: Provides a platform for threat response, log analysis, and timeline creation. |
| Security Command Center Enterprise | **Use the Intelligence function in all aspects of cyber defense** : Uses AI to assess risk, prioritize vulnerabilities, and provide actionable insights for remediation. **Understand and capitalize on your defender's advantage**: Offers comprehensive risk analysis, vulnerability prioritization, and proactive identification of weaknesses. **Validate and improve your defenses continuously** : Provides ongoing security posture evaluation and resource prioritization. **Manage and coordinate cyber-defense efforts through Mission Control**: Acts as a central hub for managing and coordinating cyber-defense operations. |
| Chrome Enterprise Premium | **Use the Intelligence function in all aspects of cyber defense** : Protects users from exfiltration risks, prevents malware, and provides visibility into unsafe browser activity. **Understand and capitalize on your defender's advantage**: Enhances security for enterprise devices through data protection, malware prevention, and control over extensions. **Validate and improve your defenses continuously** : Addresses new and evolving threats through continuous updates to defenses against exfiltration risks and malware. **Manage and coordinate cyber-defense efforts through Mission Control**: Manage and control end-user access to sensitive resources, including granular access controls. |
| Google Workspace | **Manage and coordinate cyber-defense efforts through Mission Control**: Manage and control end-user access to sensitive resources, including granular access controls. |
| Network Intelligence Center | **Use the Intelligence function in all aspects of cyber defense**: Provides visibility into network performance and detects unusual traffic patterns or data transfers. |
| Cloud NGFW | **Validate and improve your defenses continuously**: Optimizes network-based threat detection and response through integration with Security Command Center and Google SecOps. |

<br />

<br />


# Use AI securely and responsibly

This principle in the security pillar of the
[Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework)
provides recommendations to help you secure your AI systems. These
recommendations are aligned with Google's
[Secure AI Framework (SAIF)](https://safety.google/cybersecurity-advancements/saif/),
which provides a practical approach to address the security and risk concerns of
AI systems. SAIF is a conceptual framework that aims to provide industry-wide
standards for building and deploying AI responsibly.

## Principle overview

To help ensure that your AI systems meet your security, privacy, and compliance
requirements, you must adopt a holistic strategy that starts with the initial
design and extends to deployment and operations. You can implement this holistic
strategy by applying the
[six core elements of SAIF](https://developers.google.com/machine-learning/resources/saif).

Google uses AI to enhance security measures, such as identifying threats,
automating security tasks, and improving detection capabilities, while keeping
humans in the loop for critical decisions.

Google emphasizes a collaborative approach to advancing AI security. This
approach involves partnering with customers, industries, and governments to
enhance the SAIF guidelines and offer practical, actionable resources.

The recommendations to implement this principle are grouped within the
following sections:

- [Recommendations to use AI securely](https://docs.cloud.google.com/architecture/framework/printable#recommendations_to_use_ai_securely)
- [Recommendations for AI governance](https://docs.cloud.google.com/architecture/framework/printable#recommendations_for_ai_governance)

## Recommendations to use AI securely

To use AI securely, you need both foundational security controls and
AI-specific security controls. This section provides an overview of
recommendations to ensure that your AI and ML deployments meet the security,
privacy, and compliance requirements of your organization.


For an overview of architectural principles and recommendations that are specific to AI
and ML workloads in Google Cloud, see the
[AI and ML perspective](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml)
in the Well-Architected Framework.

### Define clear goals and requirements for AI usage

This recommendation is relevant to the following
[focus areas](https://docs.cloud.google.com/architecture/framework/security#focus_areas_of_cloud_security):

- Cloud governance, risk, and compliance
- AI and ML security

This recommendation aligns with the SAIF element about contextualizing AI
system risks in the surrounding business processes. When you design and evolve
AI systems, it's important to understand your specific business goals, risks, and
compliance requirements.

### Keep data secure and prevent loss or mishandling

This recommendation is relevant to the following
[focus areas](https://docs.cloud.google.com/architecture/framework/security#focus_areas_of_cloud_security):

- Infrastructure security
- Identity and access management
- Data security
- Application security
- AI and ML security

This recommendation aligns with the following SAIF elements:

- Expand strong security foundations to the AI ecosystem. This element includes data collection, storage, access control, and protection against data poisoning.
- Contextualize AI system risks. Emphasize data security to support business objectives and compliance.

### Keep AI pipelines secure and robust against tampering

This recommendation is relevant to the following
[focus areas](https://docs.cloud.google.com/architecture/framework/security#focus_areas_of_cloud_security):

- Infrastructure security
- Identity and access management
- Data security
- Application security
- AI and ML security

This recommendation aligns with the following SAIF elements:

- Expand strong security foundations to the AI ecosystem. As a key element of establishing a secure AI system, secure your code and model artifacts.
- Adapt controls for faster feedback loops. Because it's important for mitigation and incident response, track your assets and pipeline runs.

### Deploy apps on secure systems using secure tools and artifacts

This recommendation is relevant to the following
[focus areas](https://docs.cloud.google.com/architecture/framework/security#focus_areas_of_cloud_security):

- Infrastructure security
- Identity and access management
- Data security
- Application security
- AI and ML security

Using secure systems and validated tools and artifacts in AI-based applications
aligns with the SAIF element about expanding strong security foundations to the
AI ecosystem and supply chain. This recommendation can be addressed through the
following steps:

- Implement a secure environment for ML training and deployment
- Use validated container images
- Apply [Supply-chain Levels for Software Artifacts (SLSA)](https://slsa.dev) guidelines

### Protect and monitor inputs

This recommendation is relevant to the following
[focus areas](https://docs.cloud.google.com/architecture/framework/security#focus_areas_of_cloud_security):

- Logging, auditing, and monitoring
- Security operations
- AI and ML security

This recommendation aligns with the SAIF element about extending detection and
response to bring AI into an organization's threat universe. To prevent issues,
it's critical to manage prompts for generative AI systems, monitor inputs, and
control user access.

## Recommendations for AI governance

All of the recommendations in this section are relevant to the following
[focus area](https://docs.cloud.google.com/architecture/framework/security#focus_areas_of_cloud_security):
Cloud governance, risk, and compliance.

Google Cloud offers a robust set of tools and services that you can use
to build responsible and ethical AI systems. We also offer a framework of
policies, procedures, and ethical considerations that can guide the development,
deployment, and use of AI systems.

As reflected in our recommendations, Google's approach for AI governance is
guided by the following principles:

- Fairness
- Transparency
- Accountability
- Privacy
- Security

### Use fairness indicators

[Vertex AI](https://docs.cloud.google.com/vertex-ai/docs/start/introduction-unified-platform)
can detect bias during the data collection or post-training evaluation process.
Vertex AI provides
[model evaluation metrics](https://docs.cloud.google.com/vertex-ai/docs/evaluation/intro-evaluation-fairness)
like *data bias* and *model bias* to help you evaluate your model for bias.

These metrics are related to fairness across different categories like race,
gender, and class. However, interpreting statistical deviations isn't a
straightforward exercise, because differences across categories might not be a
result of bias or a signal of harm.

### Use Vertex Explainable AI

To understand how the AI models make decisions, use Vertex Explainable AI. This
feature helps you to identify potential biases that might be hidden in the
model's logic.

This explainability feature is integrated with
[BigQuery ML](https://docs.cloud.google.com/bigquery/docs/xai-overview)
and
[Vertex AI](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/overview),
which provide feature-based explanations. You can either perform explainability
in BigQuery ML or
[register your model](https://docs.cloud.google.com/bigquery/docs/managing-models-vertex#register_models)
in Vertex AI and perform explainability in
Vertex AI.

### Track data lineage

Track the origin and transformation of data that's used in your AI systems.
This tracking helps you understand the data's journey and identify potential
sources of bias or error.

[Data lineage](https://docs.cloud.google.com/data-catalog/docs/concepts/about-data-lineage)
is a Knowledge Catalog feature that lets you track how data moves through your
systems: where it comes from, where it's passed to, and what transformations are
applied to it.

### Establish accountability

Establish clear responsibility for the development, deployment, and outcomes of
your AI systems.

Use
[Cloud Logging](https://docs.cloud.google.com/logging/docs/overview)
to log key events and decisions made by your AI systems. The logs provide an
audit trail to help you understand how the system is performing and identify
areas for improvement.

Use
[Error Reporting](https://docs.cloud.google.com/error-reporting/docs/grouping-errors)
to systematically analyze errors made by the AI systems. This analysis can
reveal patterns that point to underlying biases or areas where the model needs
further refinement.

### Implement differential privacy

During model training,
[add noise](https://docs.cloud.google.com/bigquery/docs/differential-privacy#add_noise)
to the data in order to make it difficult to identify individual data points but
still enable the model to learn effectively. With
[SQL in BigQuery](https://docs.cloud.google.com/bigquery/docs/introduction-sql),
you can transform the results of a query with differentially private
[aggregations](https://docs.cloud.google.com/bigquery/docs/differential-privacy).

<br />


# Use AI for security

This principle in the security pillar of the
[Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework)
provides recommendations to use AI to help you improve the security of your
cloud workloads.

Because of the increasing number and sophistication of cyber attacks, it's
important to take advantage of AI's potential to help improve security. AI can
help to reduce the number of threats, reduce the manual effort required by security
professionals, and help compensate for the scarcity of experts in the cyber-security
domain.

## Principle overview

Use AI capabilities to improve your existing security systems and processes.
You can use
[Gemini in Security](https://cloud.google.com/security/ai)
as well as the intrinsic AI capabilities that are built into Google Cloud services.

These AI capabilities can transform security by providing assistance across
every stage of the security lifecycle. For example, you can use AI to do the
following:

- Analyze and explain potentially malicious code without reverse engineering.
- Reduce repetitive work for cyber-security practitioners.
- Use natural language to generate queries and interact with security event data.
- Surface contextual information.
- Offer recommendations for quick responses.
- Aid in the remediation of events.
- Summarize high-priority alerts for misconfigurations and vulnerabilities, highlight potential impacts, and recommend mitigations.

## Levels of security autonomy

AI and automation can help you achieve better security outcomes when you're
dealing with ever-evolving cyber-security threats. By using AI for security, you
can achieve greater levels of autonomy to detect and prevent threats and improve
your overall security posture. Google defines four
[levels of autonomy](https://services.google.com/fh/files/misc/google-cloud-product-vision-ai-powered-security.pdf#page=6)
when you use AI for security, and they outline the increasing role of AI in
assisting and eventually leading security tasks:

1. **Manual**: Humans run all of the security tasks (prevent, detect, prioritize, and respond) across the entire security lifecycle.
2. **Assisted**: AI tools, like Gemini, boost human productivity by summarizing information, generating insights, and making recommendations.
3. **Semi-autonomous**: AI takes primary responsibility for many security tasks and delegates to humans only when required.
4. **Autonomous**: AI acts as a trusted assistant that drives the security lifecycle based on your organization's goals and preferences, with minimal human intervention.

## Recommendations

The following sections describe the recommendations for using AI for security.
The sections also indicate how the recommendations align with Google's Secure AI
Framework (SAIF)
[core elements](https://developers.google.com/machine-learning/resources/saif)
and how they're relevant to the
[levels of security autonomy](https://docs.cloud.google.com/architecture/framework/printable#levels_of_security_autonomy).

- [Enhance threat detection and response with AI](https://docs.cloud.google.com/architecture/framework/printable#enhance_threat_detection_and_response_with_ai)
- [Simplify security for experts and non-experts](https://docs.cloud.google.com/architecture/framework/printable#simplify_security_for_experts_and_non-experts)
- [Automate time-consuming security tasks with AI](https://docs.cloud.google.com/architecture/framework/printable#automate_time-consuming_security_tasks_with_ai)
- [Incorporate AI into risk management and governance processes](https://docs.cloud.google.com/architecture/framework/printable#incorporate_ai_into_risk_management_and_governance_processes)
- [Implement secure development practices for AI systems](https://docs.cloud.google.com/architecture/framework/printable#implement_secure_development_practices_for_ai_systems)

> [!NOTE]
> **Note:** For more information about Google Cloud's overall vision for using Gemini across our products to accelerate AI for security, see the whitepaper [Google Cloud's Product Vision for AI-Powered Security](https://services.google.com/fh/files/misc/google-cloud-product-vision-ai-powered-security.pdf).

### Enhance threat detection and response with AI

This recommendation is relevant to the following
[focus areas](https://docs.cloud.google.com/architecture/framework/security#focus_areas_of_cloud_security):

- Security operations (SecOps)
- Logging, auditing, and monitoring

AI can analyze large volumes of security data, offer insights into threat actor
behavior, and automate the analysis of potentially malicious code. This
recommendation is aligned with the following SAIF elements:

- Extend detection and response to bring AI into your organization's threat universe.
- Automate defenses to keep pace with existing and new threats.

Depending on your implementation, this recommendation can be relevant to the
following levels of autonomy:

- **Assisted**: AI helps with threat analysis and detection.
- **Semi-autonomous**: AI takes on more responsibility for the security task.

[Google Threat Intelligence](https://cloud.google.com/security/products/threat-intelligence),
which uses AI to analyze threat actor behavior and malicious code, can help you
implement this recommendation.

### Simplify security for experts and non-experts

This recommendation is relevant to the following
[focus areas](https://docs.cloud.google.com/architecture/framework/security#focus_areas_of_cloud_security):

- Security operations (SecOps)
- Cloud governance, risk, and compliance

AI-powered tools can summarize alerts and recommend mitigations, and these
capabilities can make security more accessible to a wider range of personnel.
This recommendation is aligned with the following SAIF elements:

- Automate defenses to keep pace with existing and new threats.
- Harmonize platform-level controls to ensure consistent security across the organization.

Depending on your implementation, this recommendation can be relevant to the
following levels of autonomy:

- **Assisted**: AI helps you to improve the accessibility of security information.
- **Semi-autonomous**: AI helps to make security practices more effective for all users.

Gemini in
[Security Command Center](https://cloud.google.com/security/products/security-command-center)
can provide summaries of alerts for misconfigurations and vulnerabilities.

### Automate time-consuming security tasks with AI

This recommendation is relevant to the following
[focus areas](https://docs.cloud.google.com/architecture/framework/security#focus_areas_of_cloud_security):

- Infrastructure security
- Security operations (SecOps)
- Application security

AI can automate tasks such as analyzing malware, generating security rules, and
identifying misconfigurations. These capabilities can help to reduce the
workload on security teams and accelerate response times. This recommendation is
aligned with the SAIF element about automating defenses to keep pace with
existing and new threats.

Depending on your implementation, this recommendation can be relevant to the
following levels of autonomy:

- **Assisted**: AI helps you to automate tasks.
- **Semi-autonomous**: AI takes primary responsibility for security tasks, and only requests human assistance when needed.

Gemini in
[Google SecOps](https://cloud.google.com/security/products/security-operations)
can help to automate high-toil tasks by assisting analysts, retrieving relevant
context, and making recommendations for next steps.

### Incorporate AI into risk management and governance processes

This recommendation is relevant to the following
[focus area](https://docs.cloud.google.com/architecture/framework/security#focus_areas_of_cloud_security):
Cloud governance, risk, and compliance.

You can use AI to build a model inventory and risk profiles. You can also use AI
to implement policies for data privacy, cyber risk, and third-party risk. This
recommendation is aligned with the SAIF element about contextualizing AI system
risks in surrounding business processes.

Depending on your implementation, this recommendation can be relevant to the
semi-autonomous level of autonomy. At this level, AI can orchestrate security
agents that run processes to achieve your custom security goals.

### Implement secure development practices for AI systems

This recommendation is relevant to the following
[focus areas](https://docs.cloud.google.com/architecture/framework/security#focus_areas_of_cloud_security):

- Application security
- AI and ML security

You can use AI for secure coding, cleaning training data, and validating tools
and artifacts. This recommendation is aligned with the SAIF element about
expanding strong security foundations to the AI ecosystem.

This recommendation can be relevant to all levels of security autonomy, because
a secure AI system needs to be in place before AI can be used effectively for
security. The recommendation is most relevant to the assisted level, where
security practices are augmented by AI.

To implement this recommendation, follow the
[Supply-chain Levels for Software Artifacts (SLSA)](https://slsa.dev)
guidelines for AI artifacts and use validated container images.

<br />


# Meet regulatory, compliance, and privacy needs

This principle in the security pillar of the
[Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework)
helps you identify and meet regulatory, compliance, and privacy requirements for
cloud deployments. These requirements influence many of the decisions that you need
to make about the security controls that must be used for your workloads in
Google Cloud.

## Principle overview

Meeting regulatory, compliance, and privacy needs is an unavoidable challenge
for all businesses. Cloud regulatory requirements depend on several factors,
including the following:

- The laws and regulations that apply to your organization's physical locations
- The laws and regulations that apply to your customers' physical locations
- Your industry's regulatory requirements

Privacy regulations define how you can obtain, process, store, and manage your
users' data. You own your own data, including the data that you receive from your
users. Therefore, many privacy controls are your responsibility, including controls
for cookies, session management, and obtaining user permission.

The recommendations to implement this principle are grouped within the following
sections:

- [Recommendations to address organizational risks](https://docs.cloud.google.com/architecture/framework/printable#recommendations_to_address_organizational_risks)
- [Recommendations to address regulatory and compliance obligations](https://docs.cloud.google.com/architecture/framework/printable#recommendations_to_address_regulatory_and_compliance_obligations)
- [Recommendations to manage your data sovereignty](https://docs.cloud.google.com/architecture/framework/printable#recommendations_to_manage_your_data_sovereignty)
- [Recommendations to address privacy requirements](https://docs.cloud.google.com/architecture/framework/printable#recommendations_to_address_privacy_requirements)

## Recommendations to address organizational risks

This section provides recommendations to help you identify and address risks to
your organization.

### Identify risks to your organization

This recommendation is relevant to the following
[focus area](https://docs.cloud.google.com/architecture/framework/security#focus_areas_of_cloud_security):
Cloud governance, risk, and compliance.

Before you create and deploy resources on Google Cloud, complete a risk
assessment. This assessment should determine the security features that you need
to meet your internal security requirements and external regulatory
requirements.

Your risk assessment provides you with a catalog of organization-specific risks,
and informs you about your organization's capability to detect and counteract
security threats. You must perform a risk analysis immediately after deployment
and whenever there are changes in your business needs, regulatory requirements,
or threats to your organization.

As mentioned in the
[Implement security by design](https://docs.cloud.google.com/architecture/framework/security/implement-security-by-design)
principle, your security risks in a cloud environment differ from on-premises
risks. This difference is due to the shared responsibility model in the cloud,
which varies by service (IaaS, PaaS, or SaaS) and your usage. Use a
cloud-specific risk assessment framework like the
[Cloud Controls Matrix (CCM)](https://cloudsecurityalliance.org/research/cloud-controls-matrix/).
Use threat modeling, like
[OWASP application threat modeling](https://owasp.org/www-community/Threat_Modeling_Process),
to identify and address vulnerabilities. For expert help with risk assessments,
contact your Google account representative or consult Google Cloud's
[partner directory](https://cloud.google.com/find-a-partner).

After you catalog your risks, you must determine how to address them---that is,
whether you want to accept, avoid, transfer, or mitigate the risks. For
mitigation controls that you can implement, see the next section about mitigating
your risks.

### Mitigate your risks

This recommendation is relevant to the following
[focus area](https://docs.cloud.google.com/architecture/framework/security#focus_areas_of_cloud_security):
Cloud governance, risk, and compliance.

When you adopt new public cloud services, you can mitigate risks by using
technical controls, contractual protections, and third-party verifications or
attestations.

*Technical controls* are features and technologies that you use to protect your
environment. These include built-in cloud security controls like firewalls and
logging. Technical controls can also include using third-party tools to
reinforce or support your security strategy. There are two categories of
technical controls:

- You can implement Google Cloud's security controls to help you mitigate the risks that apply to your environment. For example, you can secure the connection between your on-premises networks and your cloud networks by using [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview) and [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview).
- Google has robust internal controls and auditing to protect against insider access to customer data. Our audit logs provide you with near real-time logs of [Google administrator access](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/overview) on Google Cloud.

*Contractual protections* refer to the legal commitments made by us regarding
Google Cloud services. Google is committed to maintaining and expanding
our compliance portfolio. The
[Cloud Data Processing Addendum (CDPA)](https://cloud.google.com/terms/data-processing-addendum)
describes our commitments with regard to the processing and security of your
data. The CDPA also outlines the access controls that limit Google support
engineers' access to customers' environments, and it describes our rigorous
logging and approval process. We recommend that you review Google Cloud's
contractual controls with your legal and regulatory experts, and verify that
they meet your requirements. If you need more information,
[contact your technical account representative](https://cloud.google.com/contact).

*Third-party verifications or attestations* refer to having a third-party
vendor audit the cloud provider to ensure that the provider meets compliance
requirements. For example, to learn about Google Cloud attestations with
regard to the ISO/IEC 27017 guidelines, see
[ISO/IEC 27017 - Compliance](https://cloud.google.com/security/compliance/iso-27017).
To view the current Google Cloud certifications and letters of
attestation, see
[Compliance resource center](https://cloud.google.com/security/compliance/).

## Recommendations to address regulatory and compliance obligations

A typical compliance journey has three stages: assessment, gap remediation, and
continual monitoring. This section provides recommendations that you can use
during each of these stages.

### Assess your compliance needs

This recommendation is relevant to the following
[focus area](https://docs.cloud.google.com/architecture/framework/security#focus_areas_of_cloud_security):
Cloud governance, risk, and compliance.

Compliance assessment starts with a thorough review of all of your regulatory
obligations and how your business is implementing them. To help you with your
assessment of Google Cloud services, use the
[Compliance resource center](https://cloud.google.com/security/compliance).
This site provides information about the following:

- Service support for various regulations
- Google Cloud certifications and attestations

To better understand the compliance lifecycle at Google and how your
requirements can be met, you can
[contact sales](https://cloud.google.com/support-hub)
to request help from a Google compliance specialist. Or, you can contact your
Google Cloud account manager to request a compliance workshop.

For more information about tools and resources that you can use to manage
security and compliance for Google Cloud workloads, see
[Assuring Compliance in the Cloud](https://services.google.com/fh/files/misc/assuringcompliance_in_the_cloud.pdf).

### Automate implementation of compliance requirements

This recommendation is relevant to the following
[focus area](https://docs.cloud.google.com/architecture/framework/security#focus_areas_of_cloud_security):
Cloud governance, risk, and compliance.

To help you stay in compliance with changing regulations, determine whether you
can automate how you implement compliance requirements. You can use both
compliance-focused capabilities that Google Cloud provides and blueprints
that use recommended configurations for a particular compliance regime.

[Assured Workloads](https://docs.cloud.google.com/assured-workloads)
builds on the controls within Google Cloud to help you meet your
compliance obligations. Assured Workloads lets you do the following:

- Select your compliance regime. Then, the tool automatically sets the baseline personnel access controls for the selected regime.
- Set the location for your data by using organization policies so that your data at rest and your resources remain only in that [region](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones).
- Select the key-management option (such as the key rotation period) that best meets your security and compliance requirements.
- Select the access criteria for Google support personnel to meet certain regulatory requirements such as FedRAMP Moderate. For example, you can select whether Google support personnel have completed the appropriate background checks.
- Use Google-owned and Google-managed encryption keys that are FIPS-140-2 compliant and support FedRAMP Moderate compliance. For an added layer of control and for the separation of duties, you can use customer-managed encryption keys (CMEK). For more information about keys, see [Encrypt data at rest and in transit](https://docs.cloud.google.com/architecture/framework/security/implement-security-by-design#encrypt_data_at_rest_and_in_transit).

In addition to Assured Workloads, you can use Google Cloud
blueprints that are relevant to your compliance regime. You can modify these
blueprints to incorporate your security policies into your infrastructure
deployments.

To help you build an environment that supports your compliance requirements,
Google's blueprints and solution guides include recommended configurations and
provide Terraform modules. The following table lists blueprints that address
security and alignment with compliance requirements.

| Requirement | Blueprints and solution guides |
|---|---|
| FedRAMP | - [Google Cloud FedRAMP implementation guide](https://docs.cloud.google.com/docs/security/compliance/fedramp-implementation-guide) - [Setting up a FedRAMP Aligned Three-Tier Workload on Google Cloud](https://services.google.com/fh/files/misc/fedramp_aligned_workload_solution_guide.pdf) |
| HIPAA | - [Protecting healthcare data on Google Cloud](https://services.google.com/fh/files/misc/protecting_healthcare_data_on_google_cloud_wp.pdf) - [Setting up a HIPAA-aligned workload using Data Protection Toolkit](https://services.google.com/fh/files/misc/hipaa_technical_solution_guide.pdf) |

### Monitor your compliance

This recommendation is relevant to the following
[focus areas](https://docs.cloud.google.com/architecture/framework/security#focus_areas_of_cloud_security):

- Cloud governance, risk, and compliance
- Logging, monitoring, and auditing

Most regulations require that you monitor particular activities, which include
access-related activities. To help with your monitoring, you can use the
following:

- [Access Transparency](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/overview): View near real-time logs when Google Cloud administrators access your content.
- [Firewall Rules Logging](https://docs.cloud.google.com/vpc/docs/firewall-rules-logging): Record TCP and UDP connections inside a VPC network for any rules that you create. These logs can be useful for auditing network access or for providing early warning that the network is being used in an unapproved manner.
- [VPC Flow Logs](https://docs.cloud.google.com/vpc/docs/using-flow-logs): Record network traffic flows that are sent or received by VM instances.
- [Security Command Center Premium](https://docs.cloud.google.com/security-command-center/docs/compliance-management): Monitor for compliance with various standards.
- [OSSEC](https://ossec.github.io/index.html) (or another open source tool): Log the activity of individuals who have administrator access to your environment.
- [Key Access Justifications](https://docs.cloud.google.com/assured-workloads/key-access-justifications/docs/overview): View the reasons for a key-access request.
- [Security Command Center notifications](https://docs.cloud.google.com/security-command-center/docs/how-to-notifications): Get alerts when noncompliance issues occur. For example, get alerts when users disable two-step verification or when service accounts are over-privileged. You can also set up automatic remediation for specific notifications.

## Recommendations to manage your data sovereignty

This recommendation is relevant to the following
[focus area](https://docs.cloud.google.com/architecture/framework/security#focus_areas_of_cloud_security):
Cloud governance, risk, and compliance.

Data sovereignty provides you with a mechanism to prevent Google from accessing
your data. You approve access only for provider behaviors that you agree are
necessary. For example, you can manage your data sovereignty in the following
ways:

- Store and manage [encryption keys](https://docs.cloud.google.com/kms/docs/ekm) outside the cloud.
- Grant access to these keys based on detailed [access justifications](https://cloud.google.com/blog/products/identity-security/control-access-to-gcp-data-with-key-access-justifications).
- [Protect data in use](https://cloud.google.com/blog/products/identity-security/introducing-google-cloud-confidential-computing-with-confidential-vms) by using Confidential Computing.

### Manage your operational sovereignty

This recommendation is relevant to the following
[focus area](https://docs.cloud.google.com/architecture/framework/security#focus_areas_of_cloud_security):
Cloud governance, risk, and compliance.

Operational sovereignty provides you with assurances that Google personnel can't
compromise your workloads. For example, you can manage operational sovereignty
in the following ways:

- [Restrict the deployment](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations) of new resources to specific provider regions.
- [Limit Google personnel access](https://docs.cloud.google.com/assured-workloads/docs/personnel-access-data-controls) based on predefined attributes such as their citizenship or geographic location.

### Manage software sovereignty

This recommendation is relevant to the following
[focus area](https://docs.cloud.google.com/architecture/framework/security#focus_areas_of_cloud_security):
Cloud governance, risk, and compliance.

Software sovereignty provides you with assurances that you can control the
availability of your workloads and run them wherever you want. Also, you can
have this control without being dependent or locked in with a single cloud
provider. Software sovereignty includes the ability to survive events that
require you to quickly change where your workloads are deployed and what level
of outside connection is allowed.

For example, to help you manage your software sovereignty, Google Cloud
supports
[hybrid and multicloud deployments](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices).
If you choose on-premises deployments for data
sovereignty reasons,
[Google Distributed Cloud](https://docs.cloud.google.com/distributed-cloud)
is a combination of hardware and software that brings Google Cloud into
your data center.

## Recommendations to address privacy requirements

Google Cloud includes the following controls that promote privacy:

- Default encryption of all data when it's at rest, when it's in transit, and while it's being processed.
- Safeguards against insider access.
- Support for numerous privacy regulations.

The following recommendations address additional controls that you can
implement. For more information, see
[Privacy Resource Center](https://cloud.google.com/privacy).

### Control data residency

This recommendation is relevant to the following
[focus area](https://docs.cloud.google.com/architecture/framework/security#focus_areas_of_cloud_security):
Cloud governance, risk, and compliance.

Data residency describes where your data is stored at rest. Data residency
requirements vary based on system design objectives, industry regulatory
concerns, national law, tax implications, and even culture.

Controlling data residency starts with the following:

- Understand your data type and its location.
- Determine what risks exist for your data and which laws and regulations apply.
- Control where your data is stored or where it goes.

To help you comply with data residency requirements, Google Cloud lets
you control where your data is stored, how it's accessed, and how it's
processed. You can use
[resource location policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations)
to restrict where resources are created and to limit where data is replicated
between regions. You can use the location property of a resource to identify
where the service is deployed and who maintains it. For more information, see
[Resource locations supported services](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations-supported-services).

### Classify your confidential data

This recommendation is relevant to the following
[focus area](https://docs.cloud.google.com/architecture/framework/security#focus_areas_of_cloud_security):
Data security.

You must define what data is confidential, and then ensure that the confidential
data is properly protected. Confidential data can include credit card numbers,
addresses, phone numbers, and other personally identifiable information (PII).
Using
[Sensitive Data Protection](https://docs.cloud.google.com/sensitive-data-protection),
you can set up appropriate classifications. You can then tag and tokenize your
data before you store it in Google Cloud. Additionally,
Knowledge Catalog offers a [catalog](https://docs.cloud.google.com/dataplex/docs/catalog-overview)
service that provides a platform for storing, managing, and accessing your
metadata. For more information and an example of data classification and
de-identification, see
[De-identification and re-identification of PII using Sensitive Data Protection](https://docs.cloud.google.com/architecture/de-identification-re-identification-pii-using-cloud-dlp).

### Lock down access to sensitive data

This recommendation is relevant to the following
[focus areas](https://docs.cloud.google.com/architecture/framework/security#focus_areas_of_cloud_security):

- Data security
- Identity and access management

Place sensitive data in its own service perimeter by using
[VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview).
VPC Service Controls improves your ability to mitigate the risk of unauthorized
copying or transferring of data (data exfiltration) from Google-managed
services. With VPC Service Controls, you configure security perimeters around the
resources of your Google-managed services to control the movement of data across
the perimeter. Set
[Google Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs)
access controls for that data. Configure
[multifactor authentication (MFA)](https://support.google.com/cloudidentity/answer/175197)
for all users who require access to sensitive data.

<br />


# Shared responsibilities and shared fate on Google Cloud

This document describes the differences between the shared responsibility model
and shared fate in Google Cloud. It discusses the challenges and nuances
of the shared responsibility model. This document describes what shared fate is
and how we partner with our customers to address cloud security challenges.

Understanding the shared responsibility model is important when determining how
to best protect your data and workloads on Google Cloud. The shared
responsibility model describes the tasks that you have when it comes to security
in the cloud and how these tasks are different for cloud providers.

Understanding shared responsibility, however, can be challenging. The model
requires an in-depth understanding of each service you utilize, the
configuration options that each service provides, and what Google Cloud
does to secure the service. Every service has a different configuration profile,
and it can be difficult to determine the best security configuration. Google believes that the shared responsibility model stops short
of helping cloud customers achieve better security outcomes. Instead of shared
responsibility, we believe in *shared fate*.

Shared fate includes us building and operating a trusted cloud platform for
your workloads. We provide best practice guidance and secured, attested
infrastructure code that you can use to deploy your workloads in a secure way.
We release solutions that combine various Google Cloud services to solve
complex security problems and we offer innovative insurance options to help you
measure and mitigate the risks that you must accept. Shared fate involves us
more closely interacting with you as you secure your resources on
Google Cloud.

## Shared responsibility

You're the expert in knowing the security and regulatory requirements for your
business, and knowing the requirements for protecting your confidential data and
resources. When you run your workloads on Google Cloud, you must identify
the security controls that you need to configure in Google Cloud to help
protect your confidential data and each workload. To decide which security
controls to implement, you must consider the following factors:

- Your regulatory compliance obligations
- Your organization's security standards and risk management plan
- Security requirements of your customers and your vendors

### Defined by workloads

Traditionally, responsibilities are defined based on the type of workload that
you're running and the cloud services that you require. Cloud services include
the following categories:

| **Cloud service** | **Description** |
|---|---|
| Infrastructure as a service (IaaS) | IaaS services include [Compute Engine](https://docs.cloud.google.com/compute/docs), [Cloud Storage](https://docs.cloud.google.com/storage/docs/introduction), and networking services such as [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview), [Cloud Load Balancing](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview), and [Cloud DNS](https://docs.cloud.google.com/dns/docs/overview). IaaS provides compute, storage, and network services on demand with pay-as-you-go pricing. You can use IaaS if you plan on migrating an existing on-premises workload to the cloud using lift-and-shift, or if you want to run your application on particular VMs, using specific databases or network configurations. In IaaS, the bulk of the security responsibilities are yours, and our responsibilities are focused on the underlying infrastructure and physical security. |
| Platform as a service (PaaS) | PaaS services include [App Engine](https://docs.cloud.google.com/appengine), [Google Kubernetes Engine (GKE)](https://docs.cloud.google.com/kubernetes-engine/docs), and [BigQuery](https://docs.cloud.google.com/bigquery/docs/introduction). PaaS provides the runtime environment that you can develop and run your applications in. You can use PaaS if you're building an application (such as a website), and want to focus on development not on the underlying infrastructure. In PaaS, we're responsible for more controls than in IaaS. Typically, this will vary by the services and features that you use. You share responsibility with us for application-level controls and IAM management. You remain responsible for your data security and client protection. |
| Software as a service (SaaS) | SaaS applications include [Google Workspace](https://workspace.google.com/), [Google Security Operations](https://docs.cloud.google.com/chronicle/docs/overview), and third-party SaaS applications that are available in [Google Cloud Marketplace](https://docs.cloud.google.com/marketplace). SaaS provides online applications that you can subscribe to or pay for in some way. You can use SaaS applications when your enterprise doesn't have the internal expertise or business requirement to build the application themselves, but does require the ability to process workloads. In SaaS, we own the bulk of the security responsibilities. You remain responsible for your access controls and the data that you choose to store in the application. |
| Function as a service (FaaS) or serverless | FaaS provides the platform for developers to run small, single-purpose code (called *functions*) that run in response to particular events. You would use FaaS when you want particular things to occur based on a particular event. For example, you might create a function that runs whenever data is uploaded to Cloud Storage so that it can be classified. FaaS has a similar shared responsibility list as SaaS. [Cloud Run functions](https://docs.cloud.google.com/functions/docs/2nd-gen/overview) is a FaaS application. |

The following diagram shows the cloud services and defines how responsibilities
are shared between the cloud provider and customer.

![Shared security responsibilities](https://docs.cloud.google.com/static/docs/security/overview/resources/shared_responsibilities.svg)

As the diagram shows, the cloud provider always remains responsible for the
underlying network and infrastructure, and customers always remain responsible
for their access policies and data.

### Defined by industry and regulatory framework

Various industries have regulatory frameworks that define the security controls
that must be in place. When you move your workloads to the cloud, you must
understand the following:

- Which security controls are your responsibility
- Which security controls are available as part of the cloud offering
- Which default security controls are inherited

Inherited security controls (such as our
[default encryption](https://docs.cloud.google.com/docs/security/encryption/default-encryption)
and
[infrastructure controls](https://docs.cloud.google.com/docs/security/infrastructure/design))
are controls that you can provide as part of your evidence of your security
posture to auditors and regulators. For example, the Payment Card Industry Data
Security Standard (PCI DSS) defines regulations for payment processors. When you
move your business to the cloud, these regulations are shared between you and
your CSP. To understand how PCI DSS responsibilities are shared between you and
Google Cloud, see [Google Cloud: PCI DSS Shared Responsibility Matrix](https://services.google.com/fh/files/misc/gcp_pci_dss_v4_responsibility_matrix.pdf).

As another example, in the United States, the Health Insurance Portability and
Accountability Act (HIPAA) has set standards for handling electronic personal
health information (PHI). These responsibilities are also shared between the CSP
and you. For more information on how Google Cloud meets our
responsibilities under HIPAA, see
[HIPAA - Compliance](https://cloud.google.com/security/compliance/hipaa-compliance).

Other industries (for example, finance or manufacturing) also have regulations
that define how data can be gathered, processed, and stored. For more
information about shared responsibility related to these, and how
Google Cloud meets our responsibilities, see
[Compliance resource center](https://cloud.google.com/security/compliance).

### Defined by location

Depending on your business scenario, you might need to consider your
responsibilities based on the location of your business offices, your customers,
and your data. Different countries and regions have created regulations that
inform how you can process and store your customer's data. For example, if your
business has customers who reside in the European Union, your business might
need to abide by the requirements that are described in the
[General Data Protection Regulation](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32016R0679)
(GDPR), and you might be obligated to keep your customer data in the EU itself.
In this circumstance, you are responsible for ensuring that the data that you
collect remains in the
[Google Cloud regions in the EU](https://cloud.google.com/about/locations#europe).
For more information about how we meet our GDPR obligations, see
[GDPR and Google Cloud](https://cloud.google.com/privacy/gdpr).

For information about the requirements related to your region, see
[Compliance offerings](https://cloud.google.com/security/compliance/offerings).
If your scenario is particularly complicated, we recommend speaking with our
[sales team](https://cloud.google.com/contact)
or one of our
[partners](https://cloud.google.com/find-a-partner)
to help you evaluate your security responsibilities.

### Challenges for shared responsibility

Though shared responsibility helps define the security roles that you or the
cloud provider has, relying on shared responsibility can still create
challenges. Consider the following scenarios:

- Most cloud security breaches are the direct result of misconfiguration (listed as [number 3 in the Cloud Security Alliance's Pandemic 11 Report](https://cloudsecurityalliance.org/press-releases/2022/06/07/cloud-security-alliance-s-top-threats-to-cloud-computing-pandemic-11-report-finds-traditional-cloud-security-issues-becoming-less-concerning/)) and this trend is expected to increase. Cloud products are constantly changing, and new ones are constantly being launched. Keeping up with constant change can seem overwhelming. Customers need cloud providers to provide them with opinionated best practices to help keep up with the change, starting with best practices by default and having a baseline secure configuration.
- Though dividing items by cloud services is helpful, many enterprises have workloads that require multiple cloud services types. In this circumstance, you must consider how various security controls for these services interact, including whether they overlap between and across services. For example, you might have an on-premises application that you're migrating to Compute Engine, use Google Workspace for corporate email, and also run BigQuery to analyze data to improve your products.
- Your business and markets are constantly changing; as regulations change, as you enter new markets, or as you acquire other companies. Your new markets might have different requirements, and your new acquisition might host their workloads on another cloud. To manage the constant changes, you must constantly re-assess your risk profile and be able to implement new controls quickly.
- How and where to manage your data encryption keys is an important decision that ties with your responsibilities to protect your data. The option that you choose depends on your regulatory requirements, whether you're running a hybrid cloud environment or still have an on-premises environment, and the sensitivity of the data that you're processing and storing.
- Incident management is an important, and often overlooked, area where your responsibilities and the cloud provider responsibilities aren't easily defined. Many incidents require close collaboration and support from the cloud provider to help investigate and mitigate them. Other incidents can result from poorly configured cloud resources or stolen credentials, and ensuring that you meet the best practices for securing your resources and accounts can be quite challenging.
- Advanced persistent threats (APTs) and new vulnerabilities can impact your workloads in ways that you might not consider when you start your cloud transformation. Ensuring that you remain up-to-date on the changing landscape, and who is responsible for threat mitigation is difficult, particularly if your business doesn't have a large security team.

## Shared fate

We developed shared fate in Google Cloud to start addressing the
challenges that the shared responsibility model doesn't address. Shared fate
focuses on how all parties can better interact to continuously improve security.
Shared fate builds on the shared responsibility model because it views the
relationship between cloud provider and customer as an ongoing partnership to
improve security.

Shared fate is about us taking responsibility for making Google Cloud
more secure. Shared fate includes helping you get started with a secured
[landing zone](https://docs.cloud.google.com/architecture/landing-zones#what-is-a-google-cloud-landing-zone)
and being clear, opinionated, and transparent about recommended security
controls, settings, and associated best practices. It includes helping you
better quantify and manage your risk with cyber-insurance, using our Risk
Protection Program. Using shared fate, we want to evolve from the standard
shared responsibility framework to a better model that helps you secure your
business and build trust in Google Cloud.

The following sections describe various components of shared fate.

### Help getting started

A key component of shared fate is the resources that we provide to help you get
started, in a secure configuration in Google Cloud. Starting with a secure
configuration helps reduce the issue of misconfigurations which is the root
cause of most security breaches.

Our resources include the following:

- [Enterprise foundations blueprint](https://docs.cloud.google.com/architecture/blueprints/security-foundations) that discuss top security concerns and our top recommendations.
- [Secure blueprints](https://cloud.google.com/security/best-practices#deployable-security-blueprints-and-landing-zones)
  that let you deploy and maintain secure solutions using *infrastructure as
  code* (IaC). Blueprints have our security recommendations enabled by
  default. Many blueprints are created by Google security teams and managed
  as products. This support means that they're updated regularly, go through
  a rigorous testing process, and receive attestations from third-party
  testing groups. Blueprints include the
  [enterprise foundations blueprint](https://docs.cloud.google.com/architecture/blueprints/security-foundations)
  and the
  [secured data warehouse blueprint](https://docs.cloud.google.com/architecture/blueprints/confidential-data-warehouse-blueprint).

- [Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework/security)
  recommendations for building security into your designs.

- [Landing zone navigation guides](https://docs.cloud.google.com/architecture/landing-zones)
  that step you through the top decisions that you need to make to build a
  secure foundation for your workloads, including resource hierarchy,
  identity onboarding, security and key management, and network structure.

### Risk Protection Program

Shared fate also includes the
[Risk Protection Program](https://cloud.google.com/security/products/risk-protection-program)
(currently in preview), which helps you use the power of Google Cloud as a
platform to manage risk, rather than just seeing cloud workloads as another
source of risk that you need to manage. The Risk Protection Program is a
collaboration between Google Cloud and two leading cyber insurance
companies, Munich Re and Allianz Global \& Corporate Speciality.

The Risk Protection Program includes
[Cyber Insurance Hub](https://docs.cloud.google.com/risk-manager/docs/overview),
which provides data-driven insights that you can use to better understand your
cloud security posture. If you're looking for cyber insurance coverage, you can
share these insights from Cyber Insurance Hub directly with our insurance
partners to obtain a quote. For more information, see
[Google Cloud Risk Protection Program now in Preview](https://cloud.google.com/blog/products/identity-security/google-cloud-risk-protection-program-now-in-preview).

### Help with deployment and governance

Shared fate also helps with your continued governance of your environment. For
example, we focus efforts on products such as the following:

- [Assured Workloads](https://docs.cloud.google.com/assured-workloads/docs/concept-overview), which helps you meet your compliance obligations.
- [Security Command Center](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview) Premium, which uses threat intelligence, threat detection, web scanning, and other advanced methods to monitor and detect threats. It also provides a way to resolve many of these threats quickly and automatically.
- [Organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview) and [resource settings](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy) that let you configure policies throughout your hierarchy of folders and projects.
- [Policy Intelligence tools](https://docs.cloud.google.com/policy-intelligence/docs/overview) that provide you with insights on access to accounts and resources.
- [Confidential Computing](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/about-cvm), which lets you encrypt data in use.
- [Sovereign Controls by Partners](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/overview), which is available in certain countries and helps enforce data residency requirements.

## Putting shared responsibility and shared fate into practice

As part of your planning process, consider the following actions to help you
understand and implement appropriate security controls:

- Create a list of the type of workloads that you will host in Google Cloud, and whether they require IaaS, PaaS, and SaaS services. You can use the [shared responsibility diagram](https://docs.cloud.google.com/architecture/framework/printable#shared-diagram) as a checklist to ensure that you know the security controls that you need to consider.
- Create a list of regulatory requirements that you must comply with, and access resources in the [Compliance resource center](https://cloud.google.com/security/compliance) that relate to those requirements.
- Review the list of available blueprints and architectures in the [Architecture Center](https://docs.cloud.google.com/architecture) for the security controls that you require for your particular workloads. The blueprints provide a list of recommended controls and the IaC code that you require to deploy that architecture.
- Use the [landing zone documentation](https://docs.cloud.google.com/architecture/landing-zones) and the recommendations in the [enterprise foundations guide](https://docs.cloud.google.com/architecture/blueprints/security-foundations) to design a resource hierarchy and network architecture that meets your requirements. You can use the opinionated workload blueprints, like the secured data warehouse, to accelerate your development process.
- After you deploy your workloads, verify that you're meeting your security responsibilities using services such as the Cyber Insurance Hub, Assured Workloads, Policy Intelligence tools, and Security Command Center Premium.

For more information, see the
[CISO's Guide to Cloud Transformation paper](https://services.google.com/fh/files/misc/ciso-guide-to-security-transformation.pdf).

## What's next

- Review the [core security principles](https://docs.cloud.google.com/architecture/framework/security#core_principles).
- Keep up to date with [shared fate resources](https://cloud.google.com/security/shared-fate).
- Familiarize yourself with available [blueprints](https://cloud.google.com/security/best-practices#deployable-security-blueprints-and-landing-zones), including the security foundations blueprint and workload examples like the secured data warehouse.
- Read more about [shared fate](https://cloud.google.com/blog/products/identity-security/delivering-the-industrys-most-trusted-cloud).
- Read about our underlying secure infrastructure in the [Google infrastructure security design overview](https://docs.cloud.google.com/docs/security/infrastructure/design).
- Read how to implement [NIST Cybersecurity Framework best practices in Google Cloud (PDF)](https://services.google.com/fh/files/misc/gcp_nist_cybersecurity_framework.pdf).

<br />

<br />


# Well-Architected Framework: Reliability pillar

The reliability pillar in the
[Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework)
provides principles and recommendations to help you design, deploy, and manage
reliable workloads in Google Cloud.

This document is intended for cloud architects, developers, platform engineers,
administrators, and site reliability engineers.

*Reliability* is a system's ability to consistently perform its intended
functions within the defined conditions and maintain uninterrupted service. Best
practices for reliability include redundancy, fault-tolerant design, monitoring,
and automated recovery processes.

As a part of reliability, *resilience* is the system's ability to withstand and
recover from failures or unexpected disruptions, while maintaining performance.
Google Cloud features, like
[multi-regional deployments](https://docs.cloud.google.com/architecture/deployment-archetypes/multiregional),
automated backups, and disaster recovery solutions, can help you improve your
system's resilience.

Reliability is important to your cloud strategy for many reasons, including the
following:

- **Minimal downtime**: Downtime can lead to lost revenue, decreased productivity, and damage to reputation. Resilient architectures can help ensure that systems can continue to function during failures or recover efficiently from failures.
- **Enhanced user experience**: Users expect seamless interactions with technology. Resilient systems can help maintain consistent performance and availability, and they provide reliable service even during high demand or unexpected issues.
- **Data integrity**: Failures can cause data loss or data corruption. Resilient systems implement mechanisms such as backups, redundancy, and replication to protect data and ensure that it remains accurate and accessible.
- **Business continuity**: Your business relies on technology for critical operations. Resilient architectures can help ensure continuity after a catastrophic failure, which enables business functions to continue without significant interruptions and supports a swift recovery.
- **Compliance**: Many industries have regulatory requirements for system availability and data protection. Resilient architectures can help you to meet these standards by ensuring systems remain operational and secure.
- **Lower long-term costs**: Resilient architectures require upfront investment, but resiliency can help to reduce costs over time by preventing expensive downtime, avoiding reactive fixes, and enabling more efficient resource use.

## Organizational mindset

To make your systems reliable, you need a plan and an established strategy.
This strategy must include education and the authority to prioritize reliability
alongside other initiatives.

Set a clear expectation that the entire organization is responsible for
reliability, including development, product management, operations, platform
engineering, and
[site reliability engineering (SRE)](https://cloud.google.com/sre).
Even the business-focused groups, like marketing and sales, can influence
reliability.

Every team must understand the reliability targets and risks of their
applications. The teams must be accountable to these requirements. Conflicts
between reliability and regular product feature development must be prioritized
and escalated accordingly.

Plan and manage reliability holistically, across all your functions and teams.
Consider setting up a Cloud Centre of Excellence (CCoE) that includes a
reliability pillar. For more information, see
[Optimize your organization's cloud journey with a Cloud Center of Excellence](https://cloud.google.com/blog/topics/training-certifications/optimize-your-organizations-cloud-journey-with-a-cloud-center-of-excellence).

## Focus areas for reliability

The activities that you perform to design, deploy, and manage a reliable system
can be categorized in the following focus areas. Each of the reliability
principles and recommendations in this pillar is relevant to one of these focus
areas.

- **Scoping**: To understand your system, conduct a detailed analysis of its architecture. You need to understand the components, how they work and interact, how data and actions flow through the system, and what could go wrong. Identify potential failures, bottlenecks, and risks, which helps you to take actions to mitigate those issues.
- **Observation**: To help prevent system failures, implement comprehensive and continuous observation and monitoring. Through this observation, you can understand trends and identify potential problems proactively.
- **Response**: To reduce the impact of failures, respond appropriately and recover efficiently. Automated responses can also help reduce the impact of failures. Even with planning and controls, failures can still occur.
- **Learning**: To help prevent failures from recurring, learn from each experience, and take appropriate actions.

## Core principles

The recommendations in the reliability pillar of the Well-Architected Framework are
mapped to the following core principles:

- [Define reliability based on user-experience goals](https://docs.cloud.google.com/architecture/framework/reliability/define-reliability-based-on-user-experience-goals)
- [Set realistic targets for reliability](https://docs.cloud.google.com/architecture/framework/reliability/set-targets)
- [Build highly available systems through resource redundancy](https://docs.cloud.google.com/architecture/framework/reliability/build-highly-available-systems)
- [Take advantage of horizontal scalability](https://docs.cloud.google.com/architecture/framework/reliability/horizontal-scalability)
- [Detect potential failures by using observability](https://docs.cloud.google.com/architecture/framework/reliability/observability)
- [Design for graceful degradation](https://docs.cloud.google.com/architecture/framework/reliability/graceful-degradation)
- [Perform testing for recovery from failures](https://docs.cloud.google.com/architecture/framework/reliability/perform-testing-for-recovery-from-failures)
- [Perform testing for recovery from data loss](https://docs.cloud.google.com/architecture/framework/reliability/perform-testing-for-recovery-from-data-loss)
- [Conduct thorough postmortems](https://docs.cloud.google.com/architecture/framework/reliability/conduct-postmortems)

> [!NOTE]
> **Note:** To learn about the building blocks of infrastructure reliability in Google Cloud, see [Google Cloud infrastructure reliability guide](https://docs.cloud.google.com/architecture/infra-reliability-guide).

## Contributors

Authors:

- [Laura Hyatt](https://www.linkedin.com/in/laura-hyatt) \| Customer Engineer, FSI
- [Jose Andrade](https://www.linkedin.com/in/jmandrade) \| Customer Engineer, SRE Specialist
- [Gino Pelliccia](https://www.linkedin.com/in/gino-pelliccia-13637025) \| Principal Architect

<br />

Other contributors:

- [Andrés-Leonardo Martínez-Ortiz](https://www.linkedin.com/in/almo) \| Technical Program Manager
- [Brian Kudzia](https://www.linkedin.com/in/brian-kudzia-3061558) \| Enterprise Infrastructure Customer Engineer
- [Daniel Lees](https://www.linkedin.com/in/daniellees) \| Cloud Security Architect
- [Filipe Gracio, PhD](https://www.linkedin.com/in/filipegracio) \| Customer Engineer, AI/ML Specialist
- [Gary Harmson](https://www.linkedin.com/in/garyharmson) \| Principal Architect
- [Kumar Dhanagopal](https://www.linkedin.com/in/kumardhanagopal) \| Cross-Product Solution Developer
- [Marwan Al Shawi](https://www.linkedin.com/in/marwanalshawi) \| Partner Customer Engineer
- [Nicolas Pintaux](https://www.linkedin.com/in/nicolaspintaux) \| Customer Engineer, Application Modernization Specialist
- [Radhika Kanakam](https://www.linkedin.com/in/radhika-kanakam-18ab876) \| Program Lead, Google Cloud Well-Architected Framework
- [Ryan Cox](https://www.linkedin.com/in/ryanlcox) \| Principal Architect
- [Samantha He](https://www.linkedin.com/in/samantha-he-05a98173) \| Technical Writer
- [Wade Holmes](https://www.linkedin.com/in/wholmes) \| Global Solutions Director
- [Zach Seils](https://www.linkedin.com/in/zachseils) \| Networking Specialist

<br />

<br />

<br />


# Define reliability based on user-experience goals

This principle in the reliability pillar of the
[Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework)
helps you to assess your users' experience, and then map the findings to
reliability goals and metrics.

This principle is relevant to the *scoping*
[focus area](https://docs.cloud.google.com/architecture/framework/reliability#focus-areas)
of reliability.

## Principle overview

Observability tools provide large amounts of data, but not all of the data
directly relates to the impacts on the users. For example, you might observe
high CPU usage, slow server operations, or even crashed tasks. However, if these
issues don't affect the user experience, then they don't constitute an outage.

To measure the user experience, you need to distinguish between internal system
behavior and user-facing problems. Focus on metrics like the success ratio of
user requests. Don't rely solely on server-centric metrics, like CPU usage,
which can lead to misleading conclusions about your service's reliability. True
reliability means that users can consistently and effectively use your
application or service.

## Recommendations

To help you measure user experience effectively, consider the recommendations
in the following sections.

### Measure user experience

To truly understand your service's reliability, prioritize metrics that reflect
your users' actual experience. For example, measure the users' query success
ratio, application latency, and error rates.

Ideally, collect this data directly from the user's device or browser. If this
direct data collection isn't feasible, shift your measurement point
progressively further away from the user in the system. For example, you can use
the load balancer or frontend service as the measurement point. This approach
helps you identify and address issues before those issues can significantly
impact your users.

### Analyze user journeys

To understand how users interact with your system, you can use tracing tools
like
[Cloud Trace](https://docs.cloud.google.com/trace/docs/overview).
By following a user's journey through your application, you can find bottlenecks
and latency issues that might degrade the user's experience. Cloud Trace
captures detailed performance data for each *hop* in your service architecture.
This data helps you identify and address performance issues more efficiently,
which can lead to a more reliable and satisfying user experience.

<br />

<br />


# Set realistic targets for reliability

This principle in the reliability pillar of the
[Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework)
helps you define reliability goals that are technically feasible for your
workloads in Google Cloud.

This principle is relevant to the *scoping*
[focus area](https://docs.cloud.google.com/architecture/framework/reliability#focus-areas)
of reliability.

## Principle overview

Design your systems to be just reliable enough for user happiness. It might
seem counterintuitive, but a goal of 100% reliability is often not the most
effective strategy. Higher reliability might result in a significantly higher
cost, both in terms of financial investment and potential limitations on
innovation. If users are already happy with the current level of service, then
efforts to further increase happiness might yield a low return on investment.
Instead, you can better spend resources elsewhere.

You need to determine the level of reliability at which your users are happy,
and determine the point where the cost of incremental improvements begin to
outweigh the benefits. When you determine this level of *sufficient
reliability*, you can allocate resources strategically and focus on features and
improvements that deliver greater value to your users.

## Recommendations

To set realistic reliability targets, consider the recommendations in the
following subsections.

### Accept some failure and prioritize components

Aim for high availability such as 99.99% uptime, but don't set a target of 100%
uptime. Acknowledge that some failures are inevitable.

The gap between 100% uptime and a 99.99% target is the allowance for failure.
This gap is often called the *error budget*. The error budget can help you take
risks and innovate, which is fundamental to any business to stay competitive.

Prioritize the reliability of the most critical components in the system.
Accept that less critical components can have a higher tolerance for failure.

### Balance reliability and cost

To determine the optimal reliability level for your system, conduct thorough
cost-benefit analyses.

Consider factors like system requirements, the consequences of failures, and
your organization's risk tolerance for the specific application. Remember to
consider your
[disaster recovery metrics](https://docs.cloud.google.com/architecture/dr-scenarios-planning-guide#basics_of_dr_planning),
such as the recovery time objective (RTO) and recovery point objective (RPO).
Decide what level of reliability is acceptable within the budget and other
constraints.

Look for ways to improve efficiency and reduce costs without compromising
essential reliability features.

<br />

<br />


# Build highly available systems through resource redundancy

This principle in the reliability pillar of the
[Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework)
provides recommendations to plan, build, and manage resource redundancy, which
can help you to avoid failures.

This principle is relevant to the *scoping*
[focus area](https://docs.cloud.google.com/architecture/framework/reliability#focus-areas)
of reliability.

## Principle overview

After you
[decide the level of reliability](https://docs.cloud.google.com/architecture/framework/reliability/set-targets)
that you need, you must design your systems to avoid any
[single points of failure](https://docs.cloud.google.com/architecture/infra-reliability-guide/design#avoid_single_points_of_failure).
Every critical component in the system must be replicated across multiple
machines, zones, and
[regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones).
For example, a critical database can't be located in only one region, and a
metadata server can't be deployed in only one single zone or region. In those
examples, if the sole zone or region has an outage, the system has a global
outage.

## Recommendations

To build redundant systems, consider the recommendations in the following
subsections.

### Identify failure domains and replicate services

Map out your system's
[failure domains](https://docs.cloud.google.com/architecture/infra-reliability-guide/building-blocks),
from individual VMs to regions, and design for redundancy across the failure
domains.

To ensure high availability, distribute and replicate your services and
applications across multiple zones and regions. Configure the system for
automatic failover to make sure that the services and applications continue to
be available in the event of zone or region outages.

For examples of multi-zone and multi-region architectures, see
[Design reliable infrastructure for your workloads in Google Cloud](https://docs.cloud.google.com/architecture/infra-reliability-guide/design#deployment_architectures).

### Detect and address issues promptly

Continuously track the status of your failure domains to detect and address
issues promptly.

You can monitor the current status of Google Cloud services in all regions
by using the
[Google Cloud Service Health dashboard](https://status.cloud.google.com/).
You can also view incidents relevant to your project by using
[Personalized Service Health](https://cloud.google.com/service-health).
You can use load balancers to detect resource health and automatically route
traffic to healthy backends. For more information, see
[Health checks overview](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts).

### Test failover scenarios

Like a fire drill, regularly simulate failures to validate the effectiveness of
your replication and failover strategies.

For more information, see
[Simulate a zone outage for a regional MIG](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-simulate-zonal-outage)
and
[Simulate a zone failure in GKE regional clusters](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/simulate-zone-failure).

<br />

<br />


# Take advantage of horizontal scalability

This principle in the reliability pillar of the
[Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework)
provides recommendations to help you use horizontal scalability. By using
horizontal scalability, you can help ensure that your workloads in
Google Cloud can scale efficiently and maintain performance.

This principle is relevant to the *scoping*
[focus area](https://docs.cloud.google.com/architecture/framework/reliability#focus-areas)
of reliability.

## Principle overview

Re-architect your system to a horizontal architecture. To accommodate growth in
traffic or data, you can add more resources. You can also remove resources when
they're not in use.

To understand the value of horizontal scaling, consider the limitations of
vertical scaling.

A common scenario for vertical scaling is to use a MySQL database as the
primary database with critical data. As database usage increases, more RAM and
CPU is required. Eventually, the database reaches the memory limit on the host
machine, and needs to be upgraded. This process might need to be repeated
several times. The problem is that there are hard limits on how much a database
can grow. VM sizes are not unlimited. The database can reach a point when it's
no longer possible to add more resources.

Even if resources were unlimited, a large VM can become a single point of
failure. Any problem with the primary database VM can cause error responses or
cause a system-wide outage that affects all users. Avoid single points of
failure, as described in
[Build highly available systems through resource redundancy](https://docs.cloud.google.com/architecture/framework/reliability/build-highly-available-systems).

Besides these scaling limits, vertical scaling tends to be more expensive. The
cost can increase exponentially as machines with greater amounts of compute
power and memory are acquired.

Horizontal scaling, by contrast, can cost less. The potential for horizontal
scaling is virtually unlimited in a system that's designed to scale.

## Recommendations

To transition from a single VM architecture to a horizontal multiple-machine
architecture, you need to plan carefully and use the right tools. To help you
achieve horizontal scaling, consider the recommendations in the following
subsections.

### Use managed services

Managed services remove the need to manually manage horizontal scaling. For
example, with Compute Engine managed instance groups (MIGs), you can add or
remove VMs to scale your application horizontally. For containerized
applications, Cloud Run is a serverless platform that can automatically
scale your stateless containers based on incoming traffic.

### Promote modular design

Modular components and clear interfaces help you scale individual components as
needed, instead of scaling the entire application. For more information, see
[Promote modular design](https://docs.cloud.google.com/architecture/framework/performance-optimization/promote-modular-design)
in the performance optimization pillar.

### Implement a stateless design

Design applications to be stateless, meaning no locally stored data. This lets
you add or remove instances without worrying about data consistency.

<br />


# Detect potential failures by using observability

This principle in the reliability pillar of the
[Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework)
provides recommendations to help you proactively identify areas where errors and
failures might occur.

This principle is relevant to the *observation*
[focus area](https://docs.cloud.google.com/architecture/framework/reliability#focus-areas)
of reliability.

## Principle overview

To maintain and improve the reliability of your workloads in
Google Cloud, you need to implement effective observability by using
metrics, logs, and traces.

- Metrics are numerical measurements of activities that you want to track for your application at specific time intervals. For example, you might want to track technical metrics like request rate and error rate, which can be used as service-level indicators (SLIs). You might also need to track application-specific business metrics like orders placed and payments received.
- Logs are time-stamped records of discrete events that occur within an application or system. The event could be a failure, an error, or a change in state. Logs might include metrics, and you can also use logs for SLIs.
- A trace represents the journey of a single user or transaction through a number of separate applications or the components of an application. For example, these components could be microservices. Traces help you to track what components were used in the journeys, where bottlenecks exist, and how long the journeys took.

Metrics, logs, and traces help you monitor your system continuously.
Comprehensive monitoring helps you find out where and why errors occurred. You
can also detect potential failures before errors occur.

## Recommendations

To detect potential failures efficiently, consider the recommendations in the
following subsections.

### Gain comprehensive insights

To track key metrics like response times and error rates, use
[Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)
and
[Cloud Logging](https://docs.cloud.google.com/logging/docs/overview).
These tools also help you to ensure that the metrics consistently meet the needs
of your workload.

To make data-driven decisions, analyze default service metrics to understand
component dependencies and their impact on overall workload performance.

To customize your monitoring strategy, create and publish your own metrics by
using the Google Cloud SDK.

### Perform proactive troubleshooting

Implement robust error handling and enable logging across all of the components
of your workloads in Google Cloud. Activate logs like
[Cloud Storage access logs](https://docs.cloud.google.com/storage/docs/access-logs)
and
[VPC Flow Logs](https://docs.cloud.google.com/vpc/docs/flow-logs).

When you configure logging, consider the associated
[costs](https://cloud.google.com/stackdriver/pricing#logging-costs).
To control logging costs, you can configure
[exclusion filters](https://docs.cloud.google.com/logging/docs/routing/overview#exclusions)
on the log sinks to exclude certain logs from being stored.

### Optimize resource utilization

Monitor CPU consumption, network I/O metrics, and disk I/O metrics to detect
under-provisioned and over-provisioned resources in services like
GKE, Compute Engine, and Managed Service for Apache Spark. For a
complete list of supported services, see
[Cloud Monitoring overview](https://docs.cloud.google.com/monitoring/docs/monitoring-overview).

### Prioritize alerts

For alerts, focus on critical metrics, set appropriate thresholds to minimize
alert fatigue, and ensure timely responses to significant issues. This targeted
approach lets you proactively maintain workload reliability. For more
information, see
[Alerting overview](https://docs.cloud.google.com/monitoring/alerts).

<br />

<br />


# Design for graceful degradation

This principle in the reliability pillar of the
[Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework)
provides recommendations to help you to design your Google Cloud workloads
to fail gracefully.

This principle is relevant to the *response*
[focus area](https://docs.cloud.google.com/architecture/framework/reliability#focus-areas)
of reliability.

## Principle overview

Graceful degradation is a design approach where a system that experiences a
high load continues to function, possibly with reduced performance or accuracy.
Graceful degradation ensures continued availability of the system and prevents
complete failure, even if the system's work isn't optimal. When the load returns
to a manageable level, the system resumes full functionality.

For example, during periods of high load, Google Search prioritizes results
from higher-ranked web pages, potentially sacrificing some accuracy. When the
load decreases, Google Search recomputes the search results.

## Recommendations

To design your systems for graceful degradation, consider the recommendations
in the following subsections.

### Implement throttling

Ensure that your replicas can independently handle overloads and can throttle
incoming requests during high-traffic scenarios. This approach helps you to
prevent cascading failures that are caused by shifts in excess traffic between
zones.

Use tools like
[Apigee](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)
to control the rate of API requests during high-traffic times. You can configure
policy rules to reflect how you want to scale back requests.

### Drop excess requests early

Configure your systems to drop excess requests at the frontend layer to protect
backend components. Dropping some requests prevents global failures and enables
the system to recover more gracefully.With this approach, some users might
experience errors. However, you can minimize the impact of outages, in contrast
to an approach like *circuit-breaking* , where *all* traffic is dropped during an
overload.

### Handle partial errors and retries

Build your applications to handle partial errors and retries seamlessly. This
design helps to ensure that as much traffic as possible is served during
high-load scenarios.

### Test overload scenarios

To validate that the throttle and request-drop mechanisms work effectively,
regularly simulate overload conditions in your system. Testing helps ensure that
your system is prepared for real-world traffic surges.

### Monitor traffic spikes

Use analytics and monitoring tools to predict and respond to traffic surges
before they escalate into overloads. Early detection and response can help
maintain service availability during high-demand periods.

<br />

<br />


# Perform testing for recovery from failures

This principle in the reliability pillar of the
[Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework)
provides recommendations to help you design and run tests for recovery in the
event of failures.

This principle is relevant to the *learning*
[focus area](https://docs.cloud.google.com/architecture/framework/reliability#focus-areas)
of reliability.

## Principle overview

To be sure that your system can recover from failures, you must periodically
run tests that include regional failovers, release rollbacks, and data
restoration from backups.

This testing helps you to practice responses to events that pose major risks to
reliability, such as the outage of an entire
[region](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones).
This testing also helps you verify that your system behaves as intended during a
disruption.

In the unlikely event of an entire region going down, you need to fail over all
traffic to another region. During normal operation of your workload, when data
is modified, it needs to be synchronized from the primary region to the failover
region. You need to verify that the replicated data is always very recent, so
that users don't experience data loss or session breakage. The load balancing
system must also be able to shift traffic to the failover region at any time
without service interruptions. To minimize downtime after a regional outage,
operations engineers also need to be able to manually and efficiently shift user
traffic away from a region, in as less time as possible. This operation is
sometimes called *draining a region*, which means you stop the inbound traffic
to the region and move all the traffic elsewhere.

## Recommendations

When you design and run tests for failure recovery, consider the
recommendations in the following subsections.

### Define the testing objectives and scope

Clearly define what you want to achieve from the testing. For example, your
objectives can include the following:

- Validate the recovery time objective (RTO) and the recovery point objective (RPO). For details, see [Basics of DR planning](https://docs.cloud.google.com/architecture/dr-scenarios-planning-guide#basics_of_dr_planning).
- Assess system resilience and fault tolerance under various failure scenarios.
- Test the effectiveness of automated failover mechanisms.

Decide which components, services, or regions are in the testing scope. The
scope can include specific application tiers like the frontend, backend, and
database, or it can include specific Google Cloud resources like
Cloud SQL instances or GKE clusters. The scope must also specify any
external dependencies, such as third-party APIs or cloud interconnections.

### Prepare the environment for testing

Choose an appropriate environment, preferably a staging or sandbox environment
that replicates your production setup. If you conduct the test in production,
ensure that you have safety measures ready, like automated monitoring and manual
rollback procedures.

Create a backup plan. Take snapshots or backups of critical databases and
services to prevent data loss during the test. Ensure that your team is prepared
to do manual interventions if the automated failover mechanisms fail.

To prevent test disruptions, ensure that your IAM roles,
policies, and failover configurations are correctly set up. Verify that the
necessary permissions are in place for the test tools and scripts.

Inform stakeholders, including operations, DevOps, and application owners,
about the test schedule, scope, and potential impact. Provide stakeholders with
an estimated timeline and the expected behaviors during the test.

### Simulate failure scenarios

Plan and execute failures by using tools like
[Chaos Monkey](https://netflix.github.io/chaosmonkey/).
You can use custom scripts to simulate failures of critical services such as a
shutdown of a primary node in a multi-zone GKE cluster or a disabled
Cloud SQL instance. You can also use scripts to simulate a region-wide
network outage by using firewall rules or API restrictions based on your scope
of test. Gradually escalate the failure scenarios to observe system behavior
under various conditions.

Introduce load testing alongside failure scenarios to replicate real-world
usage during outages. Test cascading failure impacts, such as how frontend
systems behave when backend services are unavailable.

To validate configuration changes and to assess the system's resilience against
human errors, test scenarios that involve misconfigurations. For example, run
tests with incorrect DNS failover settings or incorrect IAM
permissions.

### Monitor system behavior

Monitor how load balancers, health checks, and other mechanisms reroute
traffic. Use Google Cloud tools like Cloud Monitoring and
Cloud Logging to capture metrics and events during the test.

Observe changes in latency, error rates, and throughput during and after the
failure simulation, and monitor the overall performance impact. Identify any
degradation or inconsistencies in the user experience.

Ensure that logs are generated and alerts are triggered for key events, such as
service outages or failovers. Use this data to verify the effectiveness of your
alerting and incident response systems.

### Verify recovery against your RTO and RPO

Measure how long it takes for the system to resume normal operations after a
failure, and then compare this data with the defined RTO and document any
gaps.

Ensure that data integrity and availability align with the RPO. To test
database consistency, compare snapshots or backups of the database before and
after a failure.

Evaluate service restoration and confirm that all services are restored to a
functional state with minimal user disruption.

### Document and analyze results

Document each test step, failure scenario, and corresponding system behavior.
Include timestamps, logs, and metrics for detailed analyses.

Highlight bottlenecks, single points of failure, or unexpected behaviors
observed during the test. To help prioritize fixes, categorize issues by
severity and impact.

Suggest improvements to the system architecture, failover mechanisms, or
monitoring setups. Based on test findings, update any relevant failover policies
and playbooks. Present a postmortem report to stakeholders. The report should
summarize the outcomes, lessons learned, and next steps. For more information,
see
[Conduct thorough postmortems](https://docs.cloud.google.com/architecture/framework/reliability/conduct-postmortems).

### Iterate and improve

To validate ongoing reliability and resilience, plan periodic testing (for
example, quarterly).

Run tests under different scenarios, including infrastructure changes, software
updates, and increased traffic loads.

Automate failover tests by using CI/CD pipelines to integrate reliability
testing into your development lifecycle.

During the postmortem, use feedback from stakeholders and end users to improve
the test process and system resilience.

<br />


# Perform testing for recovery from data loss

This principle in the reliability pillar of the
[Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework)
provides recommendations to help you design and run tests for recovery from data
loss.

This principle is relevant to the *learning*
[focus area](https://docs.cloud.google.com/architecture/framework/reliability#focus-areas)
of reliability.

## Principle overview

To ensure that your system can recover from situations where data is lost or
corrupted, you need to run tests for those scenarios. Instances of data loss
might be caused by a software bug or some type of natural disaster. After such
events, you need to restore data from backups and bring all of the services back
up again by using the freshly restored data.

We recommend that you use three criteria to judge the success or failure of this
type of recovery test: data integrity, recovery time objective (RTO), and
recovery point objective (RPO). For details about the RTO and RPO metrics, see
[Basics of DR planning](https://docs.cloud.google.com/architecture/dr-scenarios-planning-guide#basics_of_dr_planning).

The goal of data restoration testing is to periodically verify that your
organization can continue to meet business continuity requirements. Besides
measuring RTO and RPO, a data restoration test must include testing of the
entire application stack and all the critical infrastructure services with the
restored data. This is necessary to confirm that the entire deployed application
works correctly in the test environment.

## Recommendations

When you design and run tests for recovering from data loss, consider the
recommendations in the following subsections.

### Verify backup consistency and test restoration processes

You need to verify that your backups contain consistent and usable snapshots of
data that you can restore to immediately bring applications back into service.
To validate data integrity, set up automated consistency checks to run after
each backup.

To test backups, restore them in a non-production environment. To ensure your
backups can be restored efficiently and that the restored data meets application
requirements, regularly simulate data recovery scenarios. Document the steps for
data restoration, and train your teams to execute the steps effectively during a
failure.

### Schedule regular and frequent backups

To minimize data loss during restoration and to meet RPO targets, it's
essential to have regularly scheduled backups. Establish a backup frequency that
aligns with your RPO. For example, if your RPO is 15 minutes, schedule backups
to run at least every 15 minutes. Optimize the backup intervals to reduce the
risk of data loss.

Use Google Cloud tools like Cloud Storage, Cloud SQL
automated backups, or Spanner backups to schedule and manage backups.
For critical applications, use near-continuous backup solutions like
[point-in-time recovery (PITR) for Cloud SQL](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/pitr)
or incremental backups for large datasets.

### Define and monitor RPO

Set a clear RPO based on your business needs, and monitor adherence to the RPO.
If backup intervals exceed the defined RPO, use Cloud Monitoring to set up
alerts.

### Monitor backup health

Use
[Google Cloud Backup and DR service](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)
or similar tools to track the health of your backups and confirm that they are
stored in secure and reliable locations. Ensure that the backups are replicated
across multiple
[regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones)
for added resilience.

### Plan for scenarios beyond backup

Combine backups with disaster recovery strategies like active-active failover
setups or cross-region replication for improved recovery time in extreme cases.
For more information, see
[Disaster recovery planning guide](https://docs.cloud.google.com/architecture/dr-scenarios-planning-guide).

<br />

<br />


# Conduct thorough postmortems

This principle in the reliability pillar of the
[Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework)
provides recommendations to help you conduct effective postmortems after
failures and incidents.

This principle is relevant to the *learning*
[focus area](https://docs.cloud.google.com/architecture/framework/reliability#focus-areas)
of reliability.

## Principle overview

A postmortem is a written record of an incident, its impact, the actions taken
to mitigate or resolve the incident, the root causes, and the follow-up actions
to prevent the incident from recurring. The goal of a postmortem is to learn
from mistakes and not assign blame.

The following diagram shows the workflow of a postmortem:

![The workflow of a postmortem.](https://docs.cloud.google.com/static/architecture/framework/images/postmortem-workflow.svg)

The workflow of a postmortem includes the following steps:

- Create postmortem
- Capture the facts
- Identify and analyze the root causes
- Plan for the future
- Execute the plan

Conduct postmortem analyses after major events and non-major events like the
following:

- User-visible downtimes or degradations beyond a certain threshold.
- Data losses of any kind.
- Interventions from on-call engineers, such as a release rollback or rerouting of traffic.
- Resolution times above a defined threshold.
- Monitoring failures, which usually imply manual incident discovery.

## Recommendations

Define postmortem criteria before an incident occurs so that everyone knows
when a post mortem is necessary.

To conduct effective postmortems, consider the recommendations in the following
subsections.

### Conduct blameless postmortems

Effective postmortems focus on processes, tools, and technologies, and don't
place blame on individuals or teams. The purpose of a postmortem analysis is to
improve your technology and future, not to find who is guilty. Everyone makes
mistakes. The goal should be to analyze the mistakes and learn from them.

The following examples show the difference between feedback that assigns blame
and blameless feedback:

- **Feedback that assigns blame**: "We need to rewrite the entire complicated backend system! It's been breaking weekly for the last three quarters and I'm sure we're all tired of fixing things piecemeal. Seriously, if I get paged one more time I'll rewrite it myself..."
- **Blameless feedback**: "An action item to rewrite the entire backend system might actually prevent these pages from continuing to happen. The maintenance manual for this version is quite long and really difficult to be fully trained up on. I'm sure our future on-call engineers will thank us!"

### Make the postmortem report readable by all the intended audiences

For each piece of information that you plan to include in the report, assess
whether that information is important and necessary to help the audience
understand what happened. You can move supplementary data and explanations to an
appendix of the report. Reviewers who need more information can request it.

### Avoid complex or over-engineered solutions

Before you start to explore solutions for a problem, evaluate the importance of
the problem and the likelihood of a recurrence. Adding complexity to the system
to solve problems that are unlikely to occur again can lead to increased
instability.

### Share the postmortem as widely as possible

To ensure that issues don't remain unresolved, publish the outcome of the
postmortem to a wide audience and get support from management. The value of a
postmortem is proportional to the learning that occurs after the postmortem.
When more people learn from incidents, the likelihood of similar failures
recurring is reduced.

<br />


# Well-Architected Framework: Cost optimization pillar

The cost optimization pillar in the
[Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework)
describes principles and recommendations to optimize the cost of your workloads
in Google Cloud.

The intended audience includes the following:

- CTOs, CIOs, CFOs, and other executives who are responsible for strategic cost management.
- Architects, developers, administrators, and operators who make decisions that affect cost at all the stages of an organization's cloud journey.

The cost models for on-premises and cloud workloads differ significantly.
On-premises IT costs include capital expenditure (CapEx) and operational
expenditure (OpEx). On-premises hardware and software assets are acquired and
the acquisition costs are
[depreciated](https://en.wikipedia.org/wiki/Depreciation)
over the operating life of the assets. In the cloud, the costs for most cloud
resources are treated as OpEx, where costs are incurred when the cloud resources
are consumed. This fundamental difference underscores the importance of the
following core principles of cost optimization.

> [!NOTE]
> **Note:** You might be able to classify the cost of some Google Cloud services (like Compute Engine sole-tenant nodes) as capital expenditure. For more information, see [Sole-tenancy accounting FAQ](https://docs.cloud.google.com/compute/docs/nodes/sole-tenancy-accounting-faq).


For cost optimization principles and recommendations that are specific to AI and ML workloads, see
[AI and ML perspective: Cost optimization](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/cost-optimization)
in the Well-Architected Framework.

## Core principles

The recommendations in the cost optimization pillar of the Well-Architected Framework
are mapped to the following core principles:

- [**Align cloud spending with business
  value**](https://docs.cloud.google.com/architecture/framework/cost-optimization/align-cloud-spending-business-value): Ensure that your cloud resources deliver measurable business value by aligning IT spending with business objectives.
- [**Foster a culture of cost
  awareness**](https://docs.cloud.google.com/architecture/framework/cost-optimization/foster-culture-cost-awareness): Ensure that people across your organization consider the cost impact of their decisions and activities, and ensure that they have access to the cost information required to make informed decisions.
- [**Optimize resource
  usage**](https://docs.cloud.google.com/architecture/framework/cost-optimization/optimize-resource-usage): Provision only the resources that you need, and pay only for the resources that you consume.
- [**Optimize
  continuously**](https://docs.cloud.google.com/architecture/framework/cost-optimization/optimize-continuously): Continuously monitor your cloud resource usage and costs, and proactively make adjustments as needed to optimize your spending. This approach involves identifying and addressing potential cost inefficiencies before they become significant problems.

These principles are closely aligned with the core tenets of
[cloud FinOps](https://cloud.google.com/learn/what-is-finops).
FinOps is relevant to any organization, regardless of its size or maturity in
the cloud. By adopting these principles and following the related
recommendations, you can control and optimize costs throughout your journey in
the cloud.

## Contributors

Author: [Nicolas Pintaux](https://www.linkedin.com/in/nicolaspintaux) \| Customer Engineer, Application Modernization Specialist

Other contributors:

- [Anuradha Bajpai](https://www.linkedin.com/in/anuradhabajpai) \| Solutions Architect
- [Daniel Lees](https://www.linkedin.com/in/daniellees) \| Cloud Security Architect
- [Eric Lam](https://www.linkedin.com/in/ericlam) \| Head of Google Cloud FinOps
- [Fernando Rubbo](https://www.linkedin.com/in/fernandorubbo) \| Cloud Solutions Architect
- [Filipe Gracio, PhD](https://www.linkedin.com/in/filipegracio) \| Customer Engineer, AI/ML Specialist
- [Gary Harmson](https://www.linkedin.com/in/garyharmson) \| Principal Architect
- [Jose Andrade](https://www.linkedin.com/in/jmandrade) \| Customer Engineer, SRE Specialist
- [Kent Hua](https://www.linkedin.com/in/kenthua) \| Solutions Manager
- [Kumar Dhanagopal](https://www.linkedin.com/in/kumardhanagopal) \| Cross-Product Solution Developer
- [Marwan Al Shawi](https://www.linkedin.com/in/marwanalshawi) \| Partner Customer Engineer
- [Radhika Kanakam](https://www.linkedin.com/in/radhika-kanakam-18ab876) \| Program Lead, Google Cloud Well-Architected Framework
- [Samantha He](https://www.linkedin.com/in/samantha-he-05a98173) \| Technical Writer
- [Steve McGhee](https://www.linkedin.com/in/stevemcghee) \| Reliability Advocate
- [Sergei Lilichenko](https://www.linkedin.com/in/sergei-lilichenko) \| Solutions Architect
- [Wade Holmes](https://www.linkedin.com/in/wholmes) \| Global Solutions Director
- [Zach Seils](https://www.linkedin.com/in/zachseils) \| Networking Specialist

<br />

<br />

<br />


# Align cloud spending with business value

This principle in the cost optimization pillar of the [Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework)
provides recommendations to align your use of Google Cloud resources with
your organization's business goals.

## Principle overview

To effectively manage cloud costs, you need to maximize the business value that
the cloud resources provide and minimize the [total cost of ownership (TCO)](https://www.finops.org/assets/terminology/#total-cost-of-ownership).
When you evaluate the resource options for your cloud
workloads, consider not only the cost of provisioning and using the resources,
but also the cost of managing them. For example, virtual machines (VMs) on
[Compute Engine](https://cloud.google.com/products/compute) might be a cost-effective option for hosting applications.
However, when you consider the overhead to maintain, patch, and scale the VMs,
the TCO can increase. On the other hand, serverless services like
[Cloud Run](https://docs.cloud.google.com/run/docs) can offer greater
business value. The lower operational overhead lets your team focus on core
activities and helps to increase agility.

To ensure that your cloud resources deliver optimal value, evaluate the following
factors:

- **Provisioning and usage costs**: The expenses incurred when you purchase, provision, or consume resources.
- **Management costs**: The recurring expenses for operating and maintaining resources, including tasks like patching, monitoring and scaling.
- **Indirect costs**: The costs that you might incur to manage issues like downtime, data loss, or security breaches.
- **Business impact**: The potential benefits from the resources, like increased revenue, improved customer satisfaction, and faster time to market.

By aligning cloud spending with business value, you get the following benefits:

- **Value-driven decisions**: Your teams are encouraged to prioritize solutions that deliver the greatest business value and to consider both short-term and long-term cost implications.
- **Informed resource choice**: Your teams have the information and knowledge that they need to assess the business value and TCO of various deployment options, so they choose resources that are cost-effective.
- **Cross-team alignment**: Cross-functional collaboration between business, finance, and technical teams ensures that cloud decisions are aligned with the overall objectives of the organization.

## Recommendations

To align cloud spending with business objectives, consider the following recommendations.

### Prioritize managed services and serverless products

Whenever possible, choose managed services and [serverless products](https://docs.cloud.google.com/serverless)
to reduce operational overhead and maintenance costs. This choice lets your teams
concentrate on their core business activities. They can accelerate the delivery
of new features and functionalities, and help drive innovation and value.

The following are examples of how you can implement this recommendation:

- To run PostgreSQL, MySQL, or Microsoft SQL Server server databases, use [Cloud SQL](https://docs.cloud.google.com/sql) instead of deploying those databases on VMs.
- To run and manage Kubernetes clusters, use [Google Kubernetes Engine (GKE) Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) instead of deploying containers on VMs.
- For your Apache Hadoop or Apache Spark processing needs, use [Managed Service for Apache Spark](https://docs.cloud.google.com/dataproc) and [Managed Service for Apache Spark Serverless](https://docs.cloud.google.com/dataproc-serverless/docs). Per-second billing can help to achieve significantly [lower TCO](https://cloud.google.com/resources/analyzing-economic-benefits-of-dataproc-whitepaper) when compared to on-premises data lakes.

### Balance cost efficiency with business agility

Controlling costs and optimizing resource utilization are important goals.
However, you must balance these goals with the need for flexible infrastructure
that lets you innovate rapidly, respond quickly to changes, and deliver value
faster. The following are examples of how you can achieve this balance:

- Adopt [DORA metrics](https://dora.dev) for software delivery performance. Metrics like change failure rate (CFR), time to detect (TTD), and time to restore (TTR) can help to identify and fix bottlenecks in your development and deployment processes. By reducing downtime and accelerating delivery, you can achieve both operational efficiency and business agility.
- Follow [Site Reliability Engineering (SRE)](https://sre.google) practices to improve operational reliability. SRE's focus on automation, observability, and incident response can lead to reduced downtime, lower recovery time, and higher customer satisfaction. By minimizing downtime and improving operational reliability, you can prevent revenue loss and avoid the need to overprovision resources as a safety net to handle outages.

### Enable self-service optimization

Encourage a culture of experimentation and exploration by providing your teams
with self-service cost optimization tools, observability tools, and resource
management platforms. Enable them to provision, manage, and optimize their cloud
resources autonomously. This approach helps to foster a sense of ownership,
accelerate innovation, and ensure that teams can respond quickly to changing needs
while being mindful of cost efficiency.

### Adopt and implement FinOps

Adopt FinOps to establish a collaborative environment where everyone is empowered
to make informed decisions that balance cost and value. FinOps fosters financial
accountability and promotes effective cost optimization in the cloud.

### Promote a value-driven and TCO-aware mindset

Encourage your team members to adopt a holistic attitude toward cloud spending,
with an emphasis on TCO and not just upfront costs. Use techniques like [value stream mapping](https://en.wikipedia.org/wiki/Value-stream_mapping)
to visualize and analyze the flow of value through your software delivery process
and to identify areas for improvement. Implement [unit costing](https://info.sada.com/whitepaper/next-frontier-cloud-finops)
for your applications and services to gain a granular understanding of cost
drivers and discover opportunities for cost optimization. For more information,
see [Maximize business value with cloud FinOps](https://cloud.google.com/resources/cloud-finops-whitepaper).

<br />


# Foster a culture of cost awareness

This principle in the cost optimization pillar of the [Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework)
provides recommendations to promote cost awareness across your organization and
ensure that team members have the cost information that they need to make
informed decisions.

Conventionally, the responsibility for cost management might be centralized to a
few select stakeholders and primarily focused on initial project architecture
decisions. However, team members across all cloud user roles (analyst, architect,
developer, or administrator) can help to reduce the cost of your resources in
Google Cloud. By sharing cost data appropriately, you can empower team
members to make cost-effective decisions throughout their development and
deployment processes.

## Principle overview

Stakeholders across various roles -- product owners, developers, deployment
engineers, administrators, and financial analysts -- need visibility into relevant
cost data and its relationship to business value. When provisioning and managing
cloud resources, they need the following data:

- **Projected resource costs**: Cost estimates at the time of design and deployment.
- **Real-time resource usage costs**: Up-to-date cost data that can be used for ongoing monitoring and budget validation.
- **Costs mapped to business metrics**: Insights into how cloud spending affects key performance indicators (KPIs), to enable teams to identify cost-effective strategies.

Every individual might not need access to raw cost data. However, promoting cost
awareness across all roles is crucial because individual decisions can affect
costs.

By promoting cost visibility and ensuring clear ownership of cost management
practices, you ensure that everyone is aware of the financial implications of
their choices and everyone actively contributes to the organization's cost
optimization goals. Whether through a centralized FinOps team or a distributed
model, establishing accountability is crucial for effective cost optimization
efforts.

## Recommendations

To promote cost awareness and ensure that your team members have the cost
information that they need to make informed decisions, consider the following
recommendations.

### Provide organization-wide cost visibility

To achieve organization-wide cost visibility, the teams that are responsible for
cost management can take the following actions:

- **Standardize cost calculation and budgeting**: Use a consistent method to determine the full costs of cloud resources, after factoring in discounts and shared costs. Establish clear and standardized budgeting processes that align with your organization's goals and enable proactive cost management.
- **Use standardized cost management and visibility tools** : Use appropriate tools that provide real-time insights into cloud spending and generate regular (for example, weekly) cost progression snapshots. These tools enable proactive budgeting, forecasting, and identification of optimization opportunities. The tools could be cloud provider tools (like the [Google Cloud Billing dashboard](https://docs.cloud.google.com/billing/docs/how-to/reports)), third-party solutions, or open-source solutions like the [Cost Attribution solution](https://github.com/google/cost-attribution-solution).
- **Implement a cost allocation system**: Allocate a portion of the overall cloud budget to each team or project. Such an allocation gives the teams a sense of ownership over cloud spending and encourages them to make cost-effective decisions within their allocated budget.
- **Promote transparency**: Encourage teams to discuss cost implications during the design and decision-making processes. Create a safe and supportive environment for sharing ideas and concerns related to cost optimization. Some organizations use positive reinforcement mechanisms like leaderboards or recognition programs. If your organization has restrictions on sharing raw cost data due to business concerns, explore alternative approaches for sharing cost information and insights. For example, consider sharing aggregated metrics (like the total cost for an environment or feature) or relative metrics (like the average cost per transaction or user).

### Understand how cloud resources are billed

Pricing for Google Cloud resources might vary across
[regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones).
Some resources are billed monthly at a fixed price, and others might be billed
based on usage.
To understand how Google Cloud resources are billed, use the
[Google Cloud pricing calculator](https://cloud.google.com/products/calculator)
and product-specific pricing information (for example, [Google Kubernetes Engine (GKE) pricing](https://cloud.google.com/kubernetes-engine/pricing)).

### Understand resource-based cost optimization options

For each type of cloud resource that you plan to use, explore strategies to
optimize utilization and efficiency. The strategies include rightsizing,
autoscaling, and adopting serverless technologies where appropriate. The following
are examples of cost optimization options for a few Google Cloud products:

- Cloud Run lets you configure [always-allocated CPUs](https://docs.cloud.google.com/run/docs/configuring/cpu-allocation) to handle predictable traffic loads at a fraction of the price of the default allocation method (that is, CPUs allocated only during request processing).
- You can purchase [BigQuery slot commitments](https://docs.cloud.google.com/bigquery/docs/reservations-commitments) to save money on data analysis.
- [GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cost-optimization-metrics) provides detailed metrics to help you understand cost optimization options.
- Understand how [network pricing](https://cloud.google.com/vpc/network-pricing) can affect the cost of data transfers and how you can optimize costs for specific networking services. For example, you can reduce the data transfer costs for external Application Load Balancers by using Cloud CDN or Google Cloud Armor. For more information, see [Ways to lower external Application Load Balancer costs](https://docs.cloud.google.com/vpc/network-pricing#ways-to-lower-external-application-load-balancer-costs).

### Understand discount-based cost optimization options

Familiarize yourself with the discount programs that Google Cloud offers,
such as the following examples:

- [**Committed use discounts (CUDs)**](https://docs.cloud.google.com/docs/cuds): CUDs are suitable for resources that have predictable and steady usage. CUDs let you get significant reductions in price in exchange for committing to specific resource usage over a period (typically one to three years). You can also use [CUD auto-renewal](https://docs.cloud.google.com/compute/docs/instances/renew-commitments-automatically) to avoid having to manually repurchase commitments when they expire.
- [**Sustained use discounts**](https://docs.cloud.google.com/compute/docs/sustained-use-discounts): For certain Google Cloud products like Compute Engine and GKE, you can get automatic discount credits after continuous resource usage beyond specific duration thresholds.
- [**Spot VMs**](https://cloud.google.com/solutions/spot-vms): For fault-tolerant and flexible workloads, Spot VMs can help to reduce your Compute Engine costs. The cost of Spot VMs is significantly lower than regular VMs. However, Compute Engine might preemptively stop or delete Spot VMs to reclaim capacity. Spot VMs are suitable for batch jobs that can tolerate preemption and don't have high availability requirements.
- **Discounts for specific product options** : Some managed services like BigQuery offer [discounts](https://docs.cloud.google.com/bigquery/docs/reservations-intro) when you purchase dedicated or autoscaling query processing capacity.

Evaluate and choose the discounts options that align with your workload
characteristics and usage patterns.

### Incorporate cost estimates into architecture blueprints

Encourage teams to develop architecture blueprints that include cost estimates
for different deployment options and configurations. This practice empowers teams
to compare costs proactively and make informed decisions that align with both
technical and financial objectives.

### Use a consistent and standard set of labels for all your resources

You can use [labels](https://docs.cloud.google.com/resource-manager/docs/best-practices-labels)
to track costs and to identify and classify resources. Specifically, you can use
labels to allocate costs to different projects, departments, or cost centers.
Defining a
[formal labeling policy](https://docs.cloud.google.com/resource-manager/docs/best-practices-labels#example_labels_table)
that aligns with the needs of the main stakeholders in your organization helps
to make costs visible more widely. You can also use labels to filter resource
cost and usage data based on target audience.

Use automation tools like Terraform to enforce labeling on every resource that
is created. To enhance cost visibility and attribution further, you can use the
tools provided by the open-source [cost attribution solution](https://github.com/google/cost-attribution-solution).

### Share cost reports with team members

By sharing cost reports with your team members, you empower them to take
ownership of their cloud spending. This practice enables cost-effective decision
making, continuous cost optimization, and systematic improvements to your cost
allocation model.

Cost reports can be of several types, including the following:

- **Periodic cost reports**: Regular reports inform teams about their current cloud spending. Conventionally, these reports might be spreadsheet exports. More effective methods include automated emails and specialized dashboards. To ensure that cost reports provide relevant and actionable information without overwhelming recipients with unnecessary detail, the reports must be tailored to the target audiences. Setting up tailored reports is a foundational step toward more real-time and interactive cost visibility and management.
- **Automated notifications**: You can configure cost reports to proactively notify relevant stakeholders (for example, through email or chat) about cost anomalies, budget thresholds, or opportunities for cost optimization. By providing timely information directly to those who can act on it, automated alerts encourage prompt action and foster a proactive approach to cost optimization.
- **Google Cloud dashboards** : You can use the [built-in billing dashboards](https://docs.cloud.google.com/billing/docs/how-to/reports) in Google Cloud to get insights into cost breakdowns and to identify opportunities for cost optimization. Google Cloud also provides [FinOps hub](https://docs.cloud.google.com/billing/docs/how-to/finops-hub) to help you monitor savings and get recommendations for cost optimization. An AI engine powers the FinOps hub to recommend cost optimization opportunities for all the resources that are currently deployed. To control access to these recommendations, you can implement role-based access control (RBAC).
- **Custom dashboards** : You can create custom dashboards by exporting cost data to an analytics database, like [BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery). Use a visualization tool like [Data Studio](https://docs.cloud.google.com/looker-studio) to connect to the analytics database to build interactive reports and enable fine-grained access control through role-based permissions.
- **Multicloud cost reports**: For multicloud deployments, you need a unified view of costs across all the cloud providers to ensure comprehensive analysis, budgeting, and optimization. Use tools like BigQuery to centralize and analyze cost data from multiple cloud providers, and use Data Studio to build team-specific interactive reports.

<br />


# Optimize resource usage

This principle in the cost optimization pillar of the [Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework) provides recommendations to help you plan and provision resources to match the requirements
and consumption patterns of your cloud workloads.

## Principle overview

To optimize the cost of your cloud resources, you need to thoroughly understand
your workloads resource requirements and load patterns. This understanding is
the basis for a well defined cost model that lets you forecast the total cost of
ownership (TCO) and identify cost drivers throughout your cloud adoption journey.
By proactively analyzing and forecasting cloud spending, you can make informed
choices about resource provisioning, utilization, and cost optimization. This
approach lets you control cloud spending, avoid overprovisioning, and ensure that
cloud resources are aligned with the dynamic needs of your workloads and
environments.

## Recommendations

To effectively optimize cloud resource usage, consider the following recommendations.

### Choose environment-specific resources

Each deployment environment has different requirements for availability,
reliability and scalability. For example, developers might prefer an environment
that lets them rapidly deploy and run applications for short durations, but might
not need high availability. On the other hand, a production environment typically
needs high availability. To maximize the utilization of your resources, define
environment-specific requirements based on your business needs. The following
table lists examples of environment-specific requirements.

> [!NOTE]
> **Note:** The requirements that are listed in this table are not exhaustive or prescriptive. They're meant to serve as examples to help you understand how requirements can vary based on the environment type.

|---|---|
| **Environment** | **Requirements** |
| Production | - High availability - Predictable performance - Operational stability - Security with robust resources |
| Development and testing | - Cost efficiency - Flexible infrastructure with [burstable capacity](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices/cloud-bursting-pattern) - Ephemeral infrastructure when data persistence is not necessary |
| Other environments (like staging and QA) | - Tailored resource allocation based on environment-specific requirements |

### Choose workload-specific resources

Each of your cloud workloads might have different requirements for availability,
scalability, security, and performance. To optimize costs, you need to align
resource choices with the specific requirements of each workload. For example,
a stateless application might not require the same level of availability or
reliability as a stateful backend. The following table lists more examples of
workload-specific requirements.

> [!NOTE]
> **Note:** The requirements that are listed in this table are not exhaustive or prescriptive. They're meant to serve as examples to help you understand how requirements can vary based on the workload type.

|---|---|---|
| **Workload type** | **Workload requirements** | **Resource options** |
| Mission-critical | Continuous availability, robust security, and high performance | Premium resources and managed services like [Spanner](https://docs.cloud.google.com/spanner) for high availability and global consistency of data. |
| Non-critical | Cost-efficient and autoscaling infrastructure | Resources with basic features and ephemeral resources like [Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot). |
| Event-driven | Dynamic scaling based on the current demand for capacity and performance | Serverless services like [Cloud Run](https://docs.cloud.google.com/run) and [Cloud Run functions](https://cloud.google.com/blog/products/serverless/google-cloud-functions-is-now-cloud-run-functions?e=48754805). |
| Experimental workloads | Low cost and flexible environment for rapid development, iteration, testing, and innovation | Resources with basic features, ephemeral resources like [Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot), and sandbox environments with defined spending limits. |

A benefit of the cloud is the opportunity to take advantage of the most
appropriate computing power for a given workload. Some workloads are developed
to take advantage of processor instruction sets, and others might not be designed
in this way. Benchmark and profile your workloads accordingly. Categorize your
workloads and make workload-specific resource choices (for example, choose
appropriate [machine families](https://docs.cloud.google.com/compute/docs/machine-resource#recommendations_for_machine_types)
for Compute Engine VMs). This practice helps
to optimize costs, enable innovation, and maintain the level of availability and
performance that your workloads need.

The following are examples of how you can implement this recommendation:

- For mission-critical workloads that serve globally distributed users, consider using [Spanner](https://docs.cloud.google.com/spanner). Spanner removes the need for complex database deployments by ensuring reliability and consistency of data in all [regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones).
- For workloads with fluctuating load levels, use autoscaling to ensure that you don't incur costs when the load is low and yet maintain sufficient capacity to meet the current load. You can configure autoscaling for many Google Cloud services, including [Compute Engine VMs](https://docs.cloud.google.com/compute/docs/autoscaler), [Google Kubernetes Engine (GKE) clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler), and [Cloud Run](https://docs.cloud.google.com/run/docs/about-instance-autoscaling). When you set up autoscaling, you can configure maximum scaling limits to ensure that costs remain within specified budgets.

### Select regions based on cost requirements

For your cloud workloads, carefully evaluate the available Google Cloud
regions and choose regions that align with your cost objectives. The region with
lowest cost might not offer optimal latency or it might not meet your
sustainability requirements. Make informed decisions about where to deploy your
workloads to achieve the desired balance. You can use the [Google Cloud Region Picker](https://cloud.withgoogle.com/region-picker/)
to understand the trade-offs between cost, sustainability, latency, and other
factors.

### Use built-in cost optimization options

Google Cloud products provide built-in features to help you optimize
resource usage and control costs. The following table lists examples of cost
optimization features that you can use in some Google Cloud products:

|---|---|
| **Product** | **Cost optimization feature** |
| Compute Engine | - Automatically add or remove VMs based on the current load by using [autoscaling](https://docs.cloud.google.com/compute/docs/autoscaler). - Avoid overprovisioning by creating and using [custom machine types](https://docs.cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type) that match your workload's requirements. - For non-critical or fault-tolerant workloads, reduce costs by using [Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot). - In development environments, reduce costs by [limiting the run time](https://docs.cloud.google.com/compute/docs/instances/limit-vm-runtime) of VMs or by [suspending](https://docs.cloud.google.com/compute/docs/instances/suspend-resume-instance) or [stopping](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance) VMs when you don't need them. |
| GKE | - Automatically adjust the size of GKE clusters based on the current load by using [cluster autoscaler](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler). - Automatically create and manage node pools based on workload requirements and ensure optimal resource utilization by using [node auto-provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning). |
| Cloud Storage | - Automatically transition data to lower-cost storage classes based on the age of data or based on access patterns by using [Object Lifecycle Management](https://docs.cloud.google.com/storage/docs/lifecycle). - Dynamically move data to the most cost-effective storage class based on usage patterns by using [Autoclass](https://docs.cloud.google.com/storage/docs/autoclass). |
| BigQuery | - Reduce query processing costs for steady-state workloads by using [capacity-based pricing.](https://cloud.google.com/bigquery/pricing#capacity_compute_analysis_pricing) - Optimize query performance and costs by using partitioning and clustering techniques. |
| Google Cloud VMware Engine | - Reduce VMware costs by using [cost-optimization strategies](https://cloud.google.com/blog/topics/cost-management/cost-optimization-of-google-cloud-vmware-engine-deployments?e=48754805) like CUDs, optimizing storage consumption, and rightsizing ESXi clusters. |

### Optimize resource sharing

To maximize the utilization of cloud resources, you can deploy multiple
applications or services on the same infrastructure, while still meeting the
security and other requirements of the applications. For example, in development
and testing environments, you can use the same cloud infrastructure to test all
the components of an application. For the production environment, you can deploy
each component on a separate set of resources to limit the extent of impact in
case of incidents.

The following are examples of how you can implement this recommendation:

- Use a single [Cloud SQL](https://docs.cloud.google.com/sql) instance for multiple non-production environments.
- Enable multiple development teams to share a GKE cluster by using the [fleet team management](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/team-management) feature in GKE with appropriate access controls.
- Use [GKE Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) to take advantage of cost-optimization techniques like bin packing and autoscaling that GKE implements by default.
- For AI and ML workloads, save GPU costs by using [GPU-sharing strategies](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/timesharing-gpus#what-is-gpu-sharing) like multi-instance GPUs, time-sharing GPUs, and NVIDIA MPS.

### Develop and maintain reference architectures

Create and maintain a repository of reference architectures that are tailored to
meet the requirements of different deployment environments and workload types.
To streamline the design and implementation process for individual projects, the
blueprints can be centrally managed by a team like a [Cloud Center of Excellence](https://cloud.google.com/resources/cloud-teams) (CCoE). Project teams
can choose suitable blueprints based on clearly defined criteria, to ensure
architectural consistency and adoption of best practices. For requirements that
are unique to a project, the project team and the central architecture team should
collaborate to design new reference architectures. You can share the reference
architectures across the organization to foster knowledge sharing and expand the
repository of available solutions. This approach ensures consistency, accelerates
development, simplifies decision-making, and promotes efficient resource
utilization.

Review the [reference architectures](https://docs.cloud.google.com/architecture/all-reference-architectures) provided by Google for various use cases and
technologies. These reference architectures incorporate best practices for
resource selection, sizing, configuration, and deployment. By using these
reference architectures, you can accelerate your development process and achieve
cost savings from the start.

### Enforce cost discipline by using organization policies

Consider using [organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview)
to limit the available Google Cloud locations and products that team
members can use. These policies help to ensure that teams adhere to cost-effective
solutions and provision resources in locations that are aligned with your cost
optimization goals.

### Estimate realistic budgets and set financial boundaries

Develop detailed budgets for each project, workload, and deployment environment.
Make sure that the budgets cover all aspects of cloud operations, including
infrastructure costs, software licenses, personnel, and anticipated growth. To
prevent overspending and ensure alignment with your financial goals, establish
clear spending limits or thresholds for projects, services, or specific resources.
Monitor cloud spending regularly against these limits. You can use [proactive quota alerts](https://docs.cloud.google.com/docs/quotas/set-up-quota-alerts)
to identify potential cost overruns early and take timely corrective action.

In addition to setting budgets, you can use [quotas](https://docs.cloud.google.com/docs/quotas/view-manage) and limits to help enforce cost discipline and
prevent unexpected spikes in spending. You can exercise granular control over
resource consumption by setting quotas at various levels, including projects,
services, and even specific resource types.

The following are examples of how you can implement this recommendation:

- **Project-level quotas**: Set spending limits or resource quotas at the project level to establish overall financial boundaries and control resource consumption across all the services within the project.
- **Service-specific quotas**: Configure quotas for specific Google Cloud services like Compute Engine or BigQuery to limit the number of instances, CPUs, or storage capacity that can be provisioned.
- **Resource type-specific quotas**: Apply quotas to individual resource types like Compute Engine VMs, Cloud Storage buckets, Cloud Run instances, or GKE nodes to restrict their usage and prevent unexpected cost overruns.
- **Quota alerts**: Get notifications when your quota usage (at the project level) reaches a percentage of the maximum value.

By using quotas and limits in conjunction with budgeting and monitoring, you can
create a proactive and multi-layered approach to cost control. This approach
helps to ensure that your cloud spending remains within defined boundaries and
aligns with your business objectives. Remember, these cost controls are not
permanent or rigid. To ensure that the cost controls remain aligned with current
industry standards and reflect your evolving business needs, you must review the
controls regularly and adjust them to include new technologies and best practices.

<br />

<br />


# Optimize continuously

This principle in the cost optimization pillar of the [Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework)
provides recommendations to help you optimize the cost of your cloud deployments
based on constantly changing and evolving business goals.

As your business grows and evolves, your cloud workloads need to adapt to changes
in resource requirements and usage patterns. To derive maximum value from your
cloud spending, you must maintain cost-efficiency while continuing to support
business objectives. This requires a proactive and adaptive approach that focuses
on continuous improvement and optimization.

## Principle overview

To optimize cost continuously, you must proactively monitor and analyze your
cloud environment and make suitable adjustments to meet current requirements.
Focus your monitoring efforts on key performance indicators (KPIs) that directly
affect your end users' experience, align with your business goals, and provide
insights for continuous improvement. This approach lets you identify and address
inefficiencies, adapt to changing needs, and continuously align cloud spending
with strategic business goals. To balance comprehensive observability with cost
effectiveness, understand the costs and benefits of monitoring resource usage
and use appropriate process-improvement and optimization strategies.

## Recommendations

To effectively monitor your Google Cloud environment and optimize cost
continuously, consider the following recommendations.

### Focus on business-relevant metrics

Effective monitoring starts with identifying the metrics that are most important
for your business and customers. These metrics include the following:

- **User experience metrics**: Latency, error rates, throughput, and customer satisfaction metrics are useful for understanding your end users' experience when using your applications.
- **Business outcome metrics**: Revenue, customer growth, and engagement can be correlated with resource usage to identify opportunities for cost optimization.
- **[DevOps Research \& Assessment (DORA)](https://dora.dev) metrics**: Metrics like deployment frequency, lead time for changes, change failure rate, and time to restore provide insights into the efficiency and reliability of your software delivery process. By improving these metrics, you can increase productivity, reduce downtime, and optimize cost.
- **[Site Reliability Engineering (SRE)](https://sre.google) metrics**: Error budgets help teams to quantify and manage the acceptable level of service disruption. By establishing clear expectations for reliability, error budgets empower teams to innovate and deploy changes more confidently, knowing their safety margin. This proactive approach promotes a balance between innovation and stability, helping prevent excessive operational costs associated with major outages or prolonged downtime.

### Use observability for resource optimization

The following are recommendations to use observability to identify resource
bottlenecks and underutilized resources in your cloud deployments:

- **Monitor resource utilization** : Use resource utilization metrics to identify Google Cloud resources that are underutilized. For example, use metrics like CPU and memory utilization to identify [idle VM resources](https://docs.cloud.google.com/monitoring/agent/process-metrics#view_performance_metrics_for_top_resource-consuming_vms). For Google Kubernetes Engine (GKE), you can view a detailed [breakdown of costs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cost-allocations) and [cost-related optimization metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cost-optimization-metrics). For Google Cloud VMware Engine, [review resource utilization](https://cloud.google.com/blog/topics/cost-management/cost-optimization-of-google-cloud-vmware-engine-deployments) to optimize CUDs, storage consumption, and ESXi right-sizing.
- **Use cloud recommendations** : [Active Assist](https://docs.cloud.google.com/solutions/active-assist) is a portfolio of intelligent tools that help you optimize your cloud operations. These tools provide actionable recommendations to reduce costs, increase performance, improve security and even make sustainability-focused decisions. For example, [VM rightsizing insights](https://docs.cloud.google.com/compute/docs/instance-groups/apply-machine-type-recommendations-managed-instance-groups) can help to optimize resource allocation and avoid unnecessary spending.
- **Correlate resource utilization with performance**: Analyze the relationship between resource utilization and application performance to determine whether you can downgrade to less expensive resources without affecting the user experience.

### Balance troubleshooting needs with cost

Detailed observability data can help with diagnosing and troubleshooting issues.
However, storing excessive amounts of observability data or exporting unnecessary
data to external monitoring tools can lead to unnecessary costs. For efficient
troubleshooting, consider the following recommendations:

- **Collect sufficient data for troubleshooting**: Ensure that your monitoring solution captures enough data to efficiently diagnose and resolve issues when they arise. This data might include logs, traces, and metrics at various levels of granularity.
- **Use sampling and aggregation**: Balance the need for detailed data with cost considerations by using sampling and aggregation techniques. This approach lets you collect representative data without incurring excessive storage costs.
- **Understand the pricing models of your monitoring tools and services**: Evaluate different monitoring solutions and choose options that align with your project's specific needs, budget, and usage patterns. Consider factors like data volume, retention requirements, and the required features when making your selection.
- **Regularly review your monitoring configuration**: Avoid collecting excessive data by removing unnecessary metrics or logs.

### Tailor data collection to roles and set role-specific retention policies

Consider the specific data needs of different roles. For example, developers
might primarily need access to traces and application-level logs, whereas IT
administrators might focus on system logs and infrastructure metrics. By tailoring
data collection, you can reduce unnecessary storage costs and avoid overwhelming
users with irrelevant information.

Additionally, you can define retention policies based on the needs of each role
and any regulatory requirements. For example, developers might need access to
detailed logs for a shorter period, while financial analysts might require
longer-term data.

### Consider regulatory and compliance requirements

In certain industries, regulatory requirements mandate data retention. To avoid
legal and financial risks, you need to ensure that your monitoring and data
retention practices help you adhere to relevant regulations. At the same time,
you need to maintain cost efficiency. Consider the following recommendations:

- Determine the specific data retention requirements for your industry or region, and ensure that your monitoring strategy meets the requirements of those requirements.
- Implement appropriate data archival and retrieval mechanisms to meet audit and compliance needs while minimizing storage costs.

### Implement smart alerting

Alerting helps to detect and resolve issues in a timely manner. However, a
balance is necessary between an approach that keeps you informed, and one that
overwhelms you with notifications. By designing intelligent alerting systems,
you can prioritize critical issues that have higher business impact. Consider
the following recommendations:

- **Prioritize issues that affect customers**: Design alerts that trigger rapidly for issues that directly affect the customer experience, like website outages, slow response times, or transaction failures.
- **Tune for temporary problems**: Use appropriate thresholds and delay mechanisms to avoid unnecessary alerts for temporary problems or self-healing system issues that don't affect customers.
- **Customize alert severity**: Ensure that the most urgent issues receive immediate attention by differentiating between critical and noncritical alerts.
- **Use notification channels wisely**: Choose appropriate channels for alert notifications (email, SMS, or paging) based on the severity and urgency of the alerts.

<br />


# Well-Architected Framework: Performance optimization pillar

This pillar in the
[Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework)
provides recommendations to optimize the performance of workloads in
Google Cloud.

This document is intended for architects, developers, and administrators who
plan, design, deploy, and manage workloads in Google Cloud.

The recommendations in this pillar can help your organization to operate
efficiently, improve customer satisfaction, increase revenue, and reduce cost.
For example, when the backend processing time of an application decreases, users
experience faster response times, which can lead to higher user retention and
more revenue.

The performance optimization process can involve a trade-off between
performance and cost. However, optimizing performance can sometimes help you
reduce costs. ​​For example, when the load increases, autoscaling can help to
provide predictable performance by ensuring that the system resources aren't
overloaded. Autoscaling also helps you to reduce costs by removing unused
resources during periods of low load.

Performance optimization is a continuous process, not a one-time activity. The
following diagram shows the stages in the performance optimization process:

![Performance optimization process](https://docs.cloud.google.com/static/architecture/framework/images/perf-optimization-process.svg)

The performance optimization process is an ongoing cycle that includes the
following stages:

1. **Define requirements**: Define granular performance requirements for each layer of the application stack before you design and develop your applications. To plan resource allocation, consider the key workload characteristics and performance expectations.
2. **Design and deploy**: Use elastic and scalable design patterns that can help you meet your performance requirements.
3. **Monitor and analyze**: Monitor performance continually by using logs, tracing, metrics, and alerts.
4. **Optimize**: Consider potential redesigns as your applications evolve.
   Rightsize cloud resources and use new features to meet changing performance
   requirements.

   As shown in the preceding diagram, continue the cycle of monitoring,
   re-assessing requirements, and adjusting the cloud resources.


For performance optimization principles and recommendations that are specific to AI and ML workloads, see
[AI and ML perspective: Performance optimization](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/performance-optimization)
in the Well-Architected Framework.

## Core principles

The recommendations in the performance optimization pillar of the Well-Architected Framework
are mapped to the following core principles:

- [Plan resource allocation](https://docs.cloud.google.com/architecture/framework/performance-optimization/plan-resource-allocation)
- [Take advantage of elasticity](https://docs.cloud.google.com/architecture/framework/performance-optimization/elasticity)
- [Promote modular design](https://docs.cloud.google.com/architecture/framework/performance-optimization/promote-modular-design)
- [Continuously monitor and improve performance](https://docs.cloud.google.com/architecture/framework/performance-optimization/continuously-monitor-and-improve-performance)

## Contributors

Authors:

- [Daniel Lees](https://www.linkedin.com/in/daniellees) \| Cloud Security Architect
- [Gary Harmson](https://www.linkedin.com/in/garyharmson) \| Principal Architect
- [Luis Urena](https://www.linkedin.com/in/urena-luis) \| Developer Relations Engineer
- [Zach Seils](https://www.linkedin.com/in/zachseils) \| Networking Specialist

<br />

Other contributors:

- [Filipe Gracio, PhD](https://www.linkedin.com/in/filipegracio) \| Customer Engineer, AI/ML Specialist
- [Jose Andrade](https://www.linkedin.com/in/jmandrade) \| Customer Engineer, SRE Specialist
- [Kumar Dhanagopal](https://www.linkedin.com/in/kumardhanagopal) \| Cross-Product Solution Developer
- [Marwan Al Shawi](https://www.linkedin.com/in/marwanalshawi) \| Partner Customer Engineer
- [Nicolas Pintaux](https://www.linkedin.com/in/nicolaspintaux) \| Customer Engineer, Application Modernization Specialist
- [Ryan Cox](https://www.linkedin.com/in/ryanlcox) \| Principal Architect
- [Radhika Kanakam](https://www.linkedin.com/in/radhika-kanakam-18ab876) \| Program Lead, Google Cloud Well-Architected Framework
- [Samantha He](https://www.linkedin.com/in/samantha-he-05a98173) \| Technical Writer
- [Wade Holmes](https://www.linkedin.com/in/wholmes) \| Global Solutions Director

<br />

<br />

<br />


# Plan resource allocation

This principle in the performance optimization pillar of the
[Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework)
provides recommendations to help you plan resources for your workloads in
Google Cloud. It emphasizes the importance of defining granular
requirements before you design and develop applications for cloud deployment or
migration.

## Principle overview

To meet your business requirements, it's important that you define the performance
requirements for your applications, before design and development. Define these
requirements as granularly as possible for the application as a whole and for
each layer of the application stack. For example, in the storage layer, you
must consider the throughput and I/O operations per second (IOPS) that the
applications need.

From the beginning, plan application designs with performance and scalability in
mind. Consider factors such as the number of users, data volume, and potential
growth over time.

Performance requirements for each workload vary and depend on the type of
workload. Each workload can contain a mix of component systems and services that
have unique sets of performance characteristics. For example, a system that's
responsible for periodic batch processing of large datasets has different
performance demands than an interactive virtual desktop solution.
Your optimization strategies must address the specific needs of each workload.

Select services and features that align with the performance goals of each
workload. For performance optimization, there's no one-size-fits-all solution. When you
optimize each workload, the entire system can achieve optimal performance and
efficiency.

Consider the following workload characteristics that can influence your
performance requirements:

- **Deployment archetype** : The [deployment archetype](https://docs.cloud.google.com/architecture/deployment-archetypes) that you select for an application can influence your choice of products and features, which then determine the performance that you can expect from your application.
- **Resource placement** : When you select a Google Cloud [region](https://docs.cloud.google.com/docs/geography-and-regions) for your application resources, we recommend that you prioritize low latency for end users, adhere to data-locality regulations, and ensure the availability of required Google Cloud products and services.
- **Network connectivity**: Choose networking services that optimize data access and content delivery. Take advantage of Google Cloud's global network, high-speed backbones, interconnect locations, and caching services.
- **Application hosting options**: When you select a hosting platform, you must evaluate the performance advantages and disadvantages of each option. For example, consider bare metal, virtual machines, containers, and serverless platforms.
- **Storage strategy** : Choose an [optimal storage strategy](https://docs.cloud.google.com/architecture/storage-advisor) that's based on your performance requirements.
- **Resource configurations**: The machine type, IOPS, and throughput can have a significant impact on performance. Additionally, early in the design phase, you must consider appropriate security capabilities and their impact on resources. When you plan security features, be prepared to accommodate the necessary performance trade-offs to avoid any unforeseen effects.

## Recommendations

To ensure optimal resource allocation, consider the recommendations in the
following sections.

### Configure and manage quotas

Ensure that your application uses only the necessary resources, such as memory,
storage, and processing power. Over-allocation can lead to unnecessary expenses,
while under-allocation might result in performance degradation.

To accommodate elastic scaling and to ensure that adequate resources are
available, regularly monitor the capacity of your quotas. Additionally, track
quota usage to identify potential scaling constraints or over-allocation issues,
and then make informed decisions about resource allocation.

### Educate and promote awareness

Inform your users about the performance requirements and provide
[educational resources](https://www.cloudskillsboost.google/course_templates/734)
about effective performance management techniques.

To evaluate progress and to identify areas for improvement, regularly document the
target performance and the actual performance. Load test your application to find
potential breakpoints and to understand how you can scale the application.

### Monitor performance metrics

Use
[Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)
to analyze trends in performance metrics, to analyze the effects of experiments,
to define alerts for critical metrics, and to perform retrospective analyses.

[Active Assist](https://docs.cloud.google.com/recommender/docs/whatis-activeassist)
is a set of tools that can provide insights and recommendations to help optimize
resource utilization. These recommendations can help you to adjust resource
allocation and improve performance.

<br />


# Take advantage of elasticity

This principle in the performance optimization pillar of the
[Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework)
provides recommendations to help you incorporate elasticity, which is the ability
to adjust resources dynamically based on changes in workload requirements.

Elasticity allows different components of
a system to scale independently. This targeted scaling can help improve performance and
cost efficiency by allocating resources precisely where they're needed, without
over provisioning or under provisioning your resources.

## Principle overview

The performance requirements of a system directly influence when and how the
system scales vertically or scales horizontally. You need to evaluate the system's
capacity and determine the load that the system is expected to handle at baseline.
Then, you need to determine how you want the system to respond to increases and decreases
in the load.

When the load increases, the system must scale out horizontally, scale up
vertically, or both. For horizontal scaling, add replica nodes to ensure that
the system has sufficient overall capacity to fulfill the increased demand. For
vertical scaling, replace the application's existing components with components
that contain more capacity, more memory, and more storage.

When the load decreases, the system must scale down (horizontally, vertically,
or both).

Define the *circumstances* in which the system scales up or scales down. Plan to
manually scale up systems for known periods of high traffic. Use tools like
autoscaling, which responds to increases or decreases in the load.

## Recommendations

To take advantage of elasticity, consider the recommendations in the following
sections.

### Plan for peak load periods

You need to plan an efficient scaling path for known events, such as expected
periods of increased customer demand.

Consider scaling up your system ahead of known periods of high traffic. For
example, if you're a retail organization, you expect demand to increase during
seasonal sales. We recommend that you manually scale up or scale out your systems before
those sales to ensure that your system can immediately handle the increased load
or immediately adjust existing limits. Otherwise, the system might take several minutes to
add resources in response to real-time changes. Your application's capacity
might not increase quickly enough and cause some users to experience delays.

For unknown or unexpected events, such as a sudden surge in demand or traffic,
you can use autoscaling features to trigger elastic scaling that's based on
metrics. These metrics can include CPU utilization, load balancer serving
capacity, latency, and even custom metrics that you define in
[Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview).

For example, consider an application that runs on a
[Compute Engine](https://docs.cloud.google.com/compute/docs/overview)
managed instance group (MIG). This application has a requirement that each instance performs
optimally until the average CPU utilization reaches 75%. In this example, you
might define an
[autoscaling policy](https://docs.cloud.google.com/compute/docs/autoscaler#autoscaling_policy)
that creates more instances when the CPU utilization reaches the threshold.
These newly-created instances help absorb the load, which helps ensure that the average
CPU utilization remains at an optimal rate until the maximum number of instances
that you've configured for the MIG is reached. When the demand decreases, the
autoscaling policy removes the instances that are no longer needed.

Plan
[resource slot reservations in BigQuery](https://docs.cloud.google.com/bigquery/docs/reservations-intro#reservations)
or adjust the limits for autoscaling configurations in Spanner by using the
[managed autoscaler](https://docs.cloud.google.com/spanner/docs/managed-autoscaler).

### Use predictive scaling

If your system components include Compute Engine, you must evaluate whether
[predictive autoscaling](https://docs.cloud.google.com/compute/docs/autoscaler#predictive_mode)
is suitable for your workload. Predictive autoscaling forecasts the future load
based on your metrics' historical trends---for example, CPU utilization.
Forecasts are recomputed every few minutes, so the autoscaler rapidly adapts its
forecast to very recent changes in load. Without predictive autoscaling, an
autoscaler can only scale a group reactively, based on observed real-time changes
in load. Predictive autoscaling works with both real-time data and
historical data to respond to both the current and the forecasted load.

### Implement serverless architectures

Consider implementing a serverless architecture with serverless services that
are inherently elastic, such as the following:

- [Cloud Run](https://docs.cloud.google.com/run/docs)
- [Cloud Run functions](https://docs.cloud.google.com/functions/docs)
- [BigQuery](https://docs.cloud.google.com/bigquery/docs)
- [Spanner](https://docs.cloud.google.com/spanner/docs)
- [Eventarc](https://docs.cloud.google.com/eventarc/docs)
- [Workflows](https://docs.cloud.google.com/workflows/docs)
- [Pub/Sub](https://docs.cloud.google.com/pubsub/docs)

Unlike autoscaling in other services that require fine-tuning rules (for
example, Compute Engine), serverless autoscaling is instant and can
scale down to zero resources.

### Use Autopilot mode for Kubernetes

For complex applications that require greater control over Kubernetes, consider
[Autopilot mode in Google Kubernetes Engine (GKE)](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview).
Autopilot mode provides automation and scalability by default.
GKE automatically scales nodes and resources based on
traffic. GKE manages nodes, creates new nodes for your applications, and
configures automatic upgrades and repairs.

<br />


# Promote modular design

This principle in the performance optimization pillar of the
[Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework)
provides recommendations to help you promote a modular design.
Modular components and clear interfaces can enable flexible scaling,
independent updates, and future component separation.

## Principle overview

Understand the dependencies between the application components and the system
components to design a scalable system.

Modular design enables flexibility and resilience, regardless of whether a
monolithic or microservices architecture was initially deployed. By decomposing
the system into well-defined, independent modules with clear interfaces, you can
scale individual components to meet specific demands.

Targeted scaling can help optimize resource utilization and reduce costs in the
following ways:

- Provisions only the necessary resources to each component, and allocates fewer resources to less-demanding components.
- Adds more resources during high-traffic periods to maintain the user experience.
- Removes under-utilized resources without compromising performance.

Modularity also enhances maintainability. Smaller, self-contained units are
easier to understand, debug, and update, which can lead to faster development
cycles and reduced risk.

While modularity offers significant advantages, you must evaluate the potential
performance trade-offs. The increased communication between modules can
introduce latency and overhead. Strive for a balance between modularity and
performance. A highly modular design might not be universally suitable. When
performance is critical, a more tightly coupled approach might be appropriate.
System design is an
[iterative process](https://docs.cloud.google.com/architecture/framework/performance-optimization),
in which you continuously review and refine your modular design.

## Recommendations

To promote modular designs, consider the recommendations in the following
sections.

### Design for loose coupling

Design a
[loosely coupled architecture](https://docs.cloud.google.com/architecture/microservices-architecture-refactoring-monoliths).
Independent components with minimal dependencies can help you build
[scalable and resilient applications](https://docs.cloud.google.com/architecture/scalable-and-resilient-apps).
As you plan the boundaries for your services, you must consider the availability
and scalability requirements. For example, if one component has requirements that
are different from your other components, you can design the component as a standalone
service. Implement a plan for graceful failures for less-important subprocesses
or services that don't impact the response time of the primary services.

### Design for concurrency and parallelism

Design your application to support multiple tasks concurrently, like processing
multiple user requests or running background jobs while users interact with your
system. Break large tasks into smaller chunks that can be processed at the same
time by multiple service instances. Task concurrency lets you use features like
autoscaling to increase the resource allocation in products like the following:

- [Compute Engine](https://docs.cloud.google.com/compute/docs/autoscaler)
- [GKE](https://docs.cloud.google.com/spanner/docs/autoscaling-overview)
- [BigQuery](https://docs.cloud.google.com/bigquery/docs/slots-autoscaling-intro)
- [Spanner](https://docs.cloud.google.com/spanner/docs/autoscaling-overview)

### Balance modularity for flexible resource allocation

Where possible, ensure that each component uses only the necessary resources
(like memory, storage, and processing power) for specific operations. Resource
over-allocation can result in unnecessary costs, while resource under-allocation can
compromise performance.

### Use well-defined interfaces

Ensure modular components communicate effectively through clear, standardized
interfaces (like APIs and message queues) to reduce overhead from translation
layers or from extraneous traffic.

### Use stateless models

A stateless model can help ensure that you can handle each request or interaction with
the service independently from previous requests. This model facilitates
scalability and recoverability, because you can grow, shrink, or restart the
service without losing the data necessary for in-progress requests or
processes.

### Choose complementary technologies

Choose technologies that complement the modular design. Evaluate programming
languages, frameworks, and databases for their modularity support.

For more information, see the following resources:

- [Re-architecting to cloud native](https://cloud.google.com/resources/rearchitecting-to-cloud-native)
- [Introduction to microservices](https://docs.cloud.google.com/architecture/microservices-architecture-introduction)

<br />


# Continuously monitor and improve performance

This principle in the performance optimization pillar of the
[Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework)
provides recommendations to help you continuously monitor and improve performance.

After you deploy applications, continuously monitor their performance by using
logs, tracing, metrics, and alerts. As your applications grow and evolve, you
can use the trends in these data points to re-assess your performance
requirements. You might eventually need to redesign parts of your applications
to maintain or improve their performance.

## Principle overview

The process of continuous performance improvement requires robust monitoring
tools and strategies. Cloud observability tools can help you to collect key
performance indicators (KPIs) such as latency, throughput, error rates, and
resource utilization. Cloud environments offer a variety of methods to conduct
granular performance assessments across the application, the network, and the
end-user experience.

Improving performance is an ongoing effort that requires a multi-faceted
approach. The following key mechanisms and processes can help you to boost
performance:

- To provide clear direction and help track progress, define performance objectives that align with your business goals. Set SMART goals: specific, measurable, achievable, relevant, and time-bound.
- To measure performance and identify areas for improvement, gather KPI metrics.
- To continuously monitor your systems for issues, use visualized workflows in monitoring tools. Use architecture process mapping techniques to identify redundancies and inefficiencies.
- To create a culture of ongoing improvement, provide training and programs that support your employees' growth.
- To encourage proactive and continuous improvement, incentivize your employees and customers to provide ongoing feedback about your application's performance.

## Recommendations

To promote modular designs, consider the recommendations in the following
sections.

### Define clear performance goals and metrics

Define clear performance objectives that align with your business goals. This
requires a deep understanding of your application's architecture and the
performance requirements of each application component.

As a priority, optimize the most critical components that directly influence your
core business functions and user experience. To help ensure that these components
continue to run efficiently and meet your business needs, set specific and
measurable performance targets. These targets can include response times, error
rates, and resource utilization thresholds.

This proactive approach can help you to identify and address potential bottlenecks,
optimize resource allocation, and ultimately deliver a seamless and
high-performing experience for your users.

### Monitor performance

Continuously monitor your cloud systems for performance issues and set up
alerts for any potential problems. Monitoring and alerts can help you to catch
and fix issues before they affect users. Application profiling can help to
identify bottlenecks and can help to optimize resource use.

You can use tools that facilitate effective troubleshooting and network
optimization. Use [Google Cloud Observability](https://docs.cloud.google.com/stackdriver/docs) to identify areas that have
high CPU consumption, memory consumption, or network consumption. These
capabilities can help developers improve efficiency,
reduce costs, and enhance the user experience.
[Network Intelligence Center](https://docs.cloud.google.com/network-intelligence-center/docs/overview) shows
visualizations of the topology of your network infrastructure, and can help you
to identify high-latency paths.

### Incentivize continuous improvement

Create a culture of ongoing improvement that can benefit both the application and
the user experience.

Provide your employees with training and development opportunities that enhance
their skills and knowledge in performance techniques across cloud services.
Establish a community of practice (CoP) and offer mentorship and coaching
programs to support employee growth.

To prevent *reactive* performance management and encourage proactive performance
management, encourage ongoing feedback from your employees, your customers, and
your stakeholders. You can consider gamifying the process by tracking KPIs on
performance and presenting those metrics to teams on a frequent basis in the
form of a league table.

To understand your performance and user happiness over time, we recommend that
you measure user feedback quantitatively and qualitatively. The
[HEART](https://dl.acm.org/doi/10.1145/1753326.1753687)
framework can help you capture user feedback across five categories:

- Happiness
- Engagement
- Adoption
- Retention
- Task success

By using such a framework, you can incentivize engineers with data-driven
feedback, user-centered metrics, actionable insights, and a clear understanding
of goals.

<br />


# Well-Architected Framework: Sustainability pillar

The sustainability pillar in the
[Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework)
provides recommendations to design, build, and manage workloads in Google Cloud
that are energy-efficient and carbon-aware.

The target audience for this document includes decision-makers, architects,
administrators, developers, and operators who design, build, deploy, and
maintain workloads in Google Cloud.

Architectural and operational decisions have a significant impact on the energy
usage, water impact, and carbon footprint that's driven by your workloads in the
cloud. Every workload, whether it's a small website or a large-scale ML model,
consumes energy and contributes to carbon emissions and water resource
intensity. When you integrate sustainability into your cloud architecture and
design process, you build systems that are efficient, cost-effective, *and*
environmentally sustainable. A sustainable architecture is resilient and
optimized, which creates a positive feedback loop of higher efficiency, lower
cost, and lower environmental impact.

## Sustainable by design: Holistic business outcomes

Sustainability isn't a trade-off against other core business objectives;
sustainability practices help to accelerate your other business objectives.
Architecture choices that prioritize low-carbon resources and operations help
you build systems that are also faster, cheaper, and more secure. Such systems
are considered to be *sustainable by design*, where optimizing for
sustainability leads to overall positive outcomes for performance, cost,
security, resilience, and user experience.

### Performance optimization

Systems that are
[optimized for performance](https://docs.cloud.google.com/architecture/framework/performance-optimization)
inherently use fewer resources. An efficient application that completes a task
faster requires compute resources for a shorter duration. Therefore, the
underlying hardware consumes less kilowatt-hours (kWh) of energy. Optimized
performance also leads to lower latency and better user experience. Time and
energy aren't wasted by resources waiting on inefficient processes. When you
use specialized hardware (for example, GPUs and TPUs), adopt efficient
algorithms, and maximize parallel processing, you improve performance *and*
reduce the carbon footprint of your cloud workload.

### Cost optimization

Cloud operational expenditure depends on resource usage. Due to this direct
correlation, when you continuously
[optimize cost](https://docs.cloud.google.com/architecture/framework/cost-optimization),
you also reduce energy consumption and carbon emissions. When you right-size
VMs, implement aggressive autoscaling, archive old data, and eliminate idle
resources, you reduce resource usage and cloud costs. You also reduce the carbon
footprint of your systems, because the data centers consume less energy to run
your workloads.

### Security and resilience

[Security](https://docs.cloud.google.com/architecture/framework/security)
and
[reliability](https://docs.cloud.google.com/architecture/framework/reliability)
are prerequisites for a sustainable cloud environment. A compromised system---for
example, a system that's affected by a denial of service (DoS) attack or an
unauthorized data breach---can dramatically increase resource consumption. These
incidents can trigger massive spikes in traffic, create runaway compute cycles
for mitigation, and necessitate lengthy, high-energy operations for forensic
analysis, cleanup, and data restoration. Strong security measures can help to
prevent unnecessary spikes in resource usage, so that your operations remain
stable, predictable, and energy-efficient.

### User experience

Systems that prioritize efficiency, performance, accessibility, and minimal use
of data can help to reduce energy usage by end users. An application that loads
a smaller model or processes less data to deliver results faster helps to reduce
the energy that's consumed by network devices and end-user devices. This
reduction in energy usage particularly benefits users who have limited bandwidth
or who use older devices. Further, sustainable architecture helps to minimize
planetary harm and demonstrates your commitment to socially responsible
technology.

## Sustainability value of migrating to the cloud

Migrating on-premises workloads to the cloud can help to reduce your
organization's environmental footprint. The transition to cloud infrastructure
can reduce energy usage and associated emissions by
[1.4 to 2 times](https://research.google/blog/good-news-about-the-carbon-footprint-of-machine-learning-training/)
when compared to typical on-premises deployments. Cloud data centers are modern,
custom-designed facilities that are built for high
[power usage effectiveness (PUE)](https://en.wikipedia.org/wiki/Power_usage_effectiveness).
Older on-premises data centers often lack the scale that's necessary to justify
investments in advanced cooling and power distribution systems.

## Shared responsibility and shared fate

[Shared responsibilities and shared fate on Google Cloud](https://docs.cloud.google.com/architecture/framework/security/shared-responsibility-shared-fate)
describes how security for cloud workloads is a shared responsibility between
Google and you, the customer. This shared responsibility model also applies to
sustainability.

Google is responsible for the sustainability *of* Google Cloud, which
means the energy efficiency and water stewardship of our data centers,
infrastructure, and core services. We invest continuously in renewable energy,
climate-conscious cooling, and hardware optimization. For more information about
Google's sustainability strategy and progress, see
[Google Sustainability 2025 Environmental Report](https://sustainability.google/google-2025-environmental-report/).

You, the customer, are responsible for sustainability
*in* the cloud, which means optimizing your workloads to be energy efficient.
For example, you can right-size resources, use serverless services that scale to
zero, and manage data lifecycles effectively.

We also advocate a shared fate model: sustainability isn't just a division of
tasks but a collaborative partnership between you and Google to reduce the
environmental footprint for the entire ecosystem.

## Use AI for business impact

The sustainability pillar of the Well-Architected Framework (this document) includes
guidance to help you design sustainable AI systems. However, a comprehensive
sustainability strategy extends beyond the environmental impact of AI workloads.
The strategy should include ways to use AI to optimize operations and create new
business value.

AI serves as a catalyst for sustainability by transforming vast datasets into
actionable insights. It enables organizations to transition from reactive
compliance to proactive optimization, such as in the following areas:

- **Operational efficiency**: Streamline operations through improved inventory management, supply chain optimization, and intelligent energy management.
- **Transparency and risk**: Use data for granular supply chain transparency, regulatory compliance, and climate risk modeling.
- **Value and growth** : Develop new revenue streams in sustainable finance and [recommerce](https://en.wikipedia.org/wiki/Recommerce).

Google offers the following products and features to help you derive insights
from data and build capabilities for a sustainable future:

- [Google Earth AI](https://ai.google/earth-ai/): Uses planetary-scale geospatial data to analyze environmental changes and monitor supply chain impacts.
- [WeatherNext](https://deepmind.google/science/weathernext/): Provides advanced weather forecasting and climate risk analytics to help you build resilience against climate volatility.
- [Geospatial insights with Google Earth](https://mapsplatform.google.com/solutions/visualize-data/): Uses geospatial data to add rich contextual data to locations, which enables smarter site selection, resource planning, and operations.
- [Google Maps routes optimization](https://mapsplatform.google.com/maps-products/#routes-section): Optimizes logistics and delivery routes to increase efficiency and reduce fuel consumption and transportation emissions.

## Collaborations with partners and customers

Google Cloud and
[TELUS](https://www.telus.com)
have partnered to advance cloud sustainability by migrating workloads to
Google's carbon-neutral infrastructure and leveraging data analytics to optimize
operations. This collaboration provides social and environmental benefits
through initiatives like smart-city technology, which uses real-time data to
reduce traffic congestion and carbon emissions across municipalities in Canada.
For more information about this collaboration, see
[Google Cloud and TELUS collaborate for sustainability](https://cloud.google.com/blog/topics/sustainability/google-cloud-and-telus-collaborate-for-sustainability).

## Core principles

The recommendations in the sustainability pillar of the Well-Architected Framework are mapped to the following core principles:

- [Use regions that consume low-carbon energy](https://docs.cloud.google.com/architecture/framework/sustainability/low-carbon-regions)
- [Optimize AI and ML workloads for energy efficiency](https://docs.cloud.google.com/architecture/framework/sustainability/ai-ml-energy-efficiency)
- [Optimize resource usage for sustainability](https://docs.cloud.google.com/architecture/framework/sustainability/optimize-resource-usage)
- [Develop energy-efficient software](https://docs.cloud.google.com/architecture/framework/sustainability/energy-efficient-software)
- [Optimize data and storage for sustainability](https://docs.cloud.google.com/architecture/framework/sustainability/optimize-storage)
- [Continuously measure and improve sustainability](https://docs.cloud.google.com/architecture/framework/sustainability/continuously-measure-improve)
- [Promote a culture of sustainability](https://docs.cloud.google.com/architecture/framework/sustainability/culture)
- [Align sustainability practices with industry guidelines](https://docs.cloud.google.com/architecture/framework/sustainability/industry-guidelines)

## Contributors

Author: [Brett Tackaberry](https://www.linkedin.com/in/tackaberry) \| Principal Architect

Other contributors:

- [Alex Stepney](https://www.linkedin.com/in/alexstepney/) \| Lead Principal Architect
- [Daniel Lees](https://www.linkedin.com/in/daniellees) \| Cloud Security Architect
- [Denise Pearl](https://www.linkedin.com/in/denise-pearl) \| Global Marketing Lead, Sustainability
- [Kumar Dhanagopal](https://www.linkedin.com/in/kumardhanagopal) \| Cross-Product Solution Developer
- [Laura Hyatt](https://www.linkedin.com/in/laura-hyatt) \| Customer Engineer, FSI
- [Nicolas Pintaux](https://www.linkedin.com/in/nicolaspintaux) \| Customer Engineer, Application Modernization Specialist
- [Radhika Kanakam](https://www.linkedin.com/in/radhika-kanakam-18ab876) \| Program Lead, Google Cloud Well-Architected Framework

<br />

<br />

<br />


# Use regions that consume low-carbon energy

This principle in the sustainability pillar of the
[Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework/sustainability)
provides recommendations to help you select low-carbon regions for your
workloads in Google Cloud.

## Principle overview

When you plan to deploy a workload in Google Cloud, an important
architectural decision is the choice of Google Cloud region for the
workload. This decision affects the carbon footprint of your workload. To
minimize the carbon footprint, your region-selection strategy must include the
following elements:

- **Data-driven selection** : To identify and prioritize regions, consider the ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg) [Low CO~2~](https://cloud.google.com/sustainability/region-carbon#region-picker) indicator and the [carbon-free energy (CFE)](https://cloud.google.com/sustainability/region-carbon) metric.
- **Policy-based governance** : Restrict resource creation to environmentally optimal locations by using the [resource locations](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations) constraint in Organization Policy Service.
- **Operational flexibility** : Use techniques like time-shifting and carbon-aware scheduling to run batch workloads during hours when the carbon intensity of the [electrical grid](https://en.wikipedia.org/wiki/Electrical_grid) is the lowest.

The electricity that's used to power your application and workloads in the cloud
is an important factor that affects your choice of Google Cloud regions.
In addition, consider the following factors:

- **Data residency and sovereignty** : The location where you need to store your data is a foundational factor that dictates your choice of Google Cloud region. This choice affects compliance with local [data residency](https://docs.cloud.google.com/assured-workloads/docs/data-residency) requirements.
- **Latency for end users**: The geographical distance between your end users and the regions where you deploy applications affects user experience and application performance.
- **Cost**: The pricing for Google Cloud resources can be different across regions.

The
[Google Cloud Region Picker](https://cloud.withgoogle.com/region-picker/)
tool helps you select optimal Google Cloud regions based on your
requirements for carbon footprint, cost, and latency. You can also use
[Cloud Location Finder](https://docs.cloud.google.com/location-finder/docs/overview)
to find cloud locations in Google Cloud and other providers based
on your requirements for proximity, carbon-free energy (CFE) usage, and other
parameters.

## Recommendations

To deploy your cloud workloads in low-carbon regions, consider the
recommendations in the following sections. These recommendations are based on
the guidance in
[Carbon-free energy for Google Cloud regions](https://cloud.google.com/sustainability/region-carbon).

### Understand the carbon intensity of cloud regions

Google Cloud data centers in a region use energy from the electrical grid
where the region is located. Google measures the carbon impact of a region by
using the CFE metric, which is calculated every hour. CFE indicates the
percentage of carbon-free energy out of the total energy that's consumed during
an hour. The CFE metric depends on two factors:

- The type of power-generation plants that supply the grid during a given period.
- [Google-attributed](https://sustainability.google/progress/projects/ppa/) clean energy that's supplied to the grid during that time.

For information about the aggregated average hourly CFE% for each
Google Cloud region, see
[Carbon-free energy for Google Cloud regions](https://cloud.google.com/sustainability/region-carbon).
You can also get this data in a machine-readable format from the
[Carbon free energy for Google Cloud regions](https://github.com/GoogleCloudPlatform/region-carbon-info)
repository in GitHub and a
[BigQuery public dataset](https://console.cloud.google.com/marketplace/product/bigquery-public-datasets/regional-cfe).

### Incorporate CFE in your location-selection strategy

Consider the following recommendations:

- Select the cleanest region for your applications. If you plan to run an application for a long period, run it in the region that has the highest CFE%. For batch workloads, you have greater flexibility in choosing a region because you can predict when the workload must run.
- Select low-carbon regions. Certain pages in the Google Cloud website and location selectors in the Google Cloud console show the ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg) [Low CO~2~](https://cloud.google.com/sustainability/region-carbon#region-picker) indicator for regions that have the lowest carbon impact.
- Restrict the creation of resources to specific low-carbon Google Cloud regions by using the [resource locations](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations) Organization Policy constraint. For example, to allow the creation of resources in only US-based low-carbon regions, create a constraint that specifies the `in:us-low-carbon-locations` value group.

When you select locations for your Google Cloud resources, also consider
[best practices for region selection](https://cloud.google.com/solutions/best-practices-compute-engine-region-selection),
including factors like data residency requirements, latency to end users,
redundancy of the application, availability of services, and pricing.

### Use time-of-day scheduling

The carbon intensity of an electrical grid can vary significantly throughout the
day. The variation depends on the mix of energy sources that supply the grid. You
can schedule workloads, particularly those that are flexible or non-urgent, to
run when the grid is supplied by a higher proportion of CFE.

For example, many grids have higher CFE percentages during off-peak hours or
when renewable sources like solar and wind supply more power to the grid. By
scheduling compute-intensive tasks such as model training and large-scale batch
inference during higher-CFE hours, you can significantly reduce the associated
carbon emissions without affecting performance or cost. This approach is known
as *time-shifting*, where you use the dynamic nature of a grid's carbon
intensity to optimize your workloads for sustainability.

<br />

<br />


# Optimize AI and ML workloads for energy efficiency

This principle in the sustainability pillar of the
[Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework/sustainability)
provides recommendations for optimizing AI and ML workloads to reduce their
energy usage and carbon footprint.

## Principle overview

To optimize AI and ML workloads for sustainability, you need to adopt a holistic
approach to designing, deploying, and operating the workloads. Select
appropriate models and specialized hardware like Tensor Processing Units (TPUs),
run the workloads in low-carbon regions, optimize to reduce resource usage, and
apply operational best practices.

Architectural and operational practices that optimize the cost and performance
of AI and ML workloads inherently lead to reduced energy consumption and lower
carbon footprint. The
[AI and ML perspective](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml)
in the Well-Architected Framework describes principles and recommendations to design,
build, and manage AI and ML workloads that meet your operational, security,
reliability, cost, and performance goals. In addition, the
[Cloud Architecture Center](https://docs.cloud.google.com/architecture/ai-ml)
provides detailed reference architectures and design guides for AI and ML
workloads in Google Cloud.

## Recommendations

To optimize AI and ML workloads for energy efficiency, consider the
recommendations in the following sections.

### Architect for energy efficiency by using TPUs

AI and ML workloads can be compute-intensive. The energy consumption by AI and
ML workloads is a key consideration for sustainability.
[TPUs](https://docs.cloud.google.com/tpu)
let you significantly improve the energy efficiency and sustainability of your
AI and ML workloads.

TPUs are custom-designed accelerators that are purpose-built for AI and ML
workloads. The specialized architecture of TPUs make them highly effective for
large-scale matrix multiplication, which is the foundation of deep learning.
TPUs can perform complex tasks at scale with greater efficiency than
general-purpose processors like CPUs or GPUs.

TPUs provide the following direct benefits for sustainability:

- **Lower energy consumption** : TPUs are engineered for optimal energy efficiency. They deliver higher computations per watt of energy consumed. Their specialized architecture significantly reduces the power demands of large-scale training and inference tasks, which leads to reduced operational costs *and* lower energy consumption.
- **Faster training and inference**: The exceptional performance of TPUs lets you train complex AI models in hours rather than days. This significant reduction in the total compute time contributes directly to a smaller environmental footprint.
- **Reduced cooling needs**: TPUs incorporate advanced liquid cooling, which provides efficient thermal management and significantly reduces the energy that's used for cooling the data center.
- **Optimization of the AI lifecycle**: By integrating hardware and software, TPUs provide an optimized solution across the entire AI lifecycle, from data processing to model serving.

### Follow the 4Ms best practices for resource selection

Google recommends a set of best practices to reduce energy usage and carbon
emissions significantly for AI and ML workloads. We call these best practices
[*4Ms*](https://cloud.google.com/transform/betting-on-efficient-ai-the-4-ms):

- **Model** : Select efficient ML model architectures. For example, [sparse models](https://ai.googleblog.com/2021/03/constructing-transformers-for-longer.html) improve ML quality and reduce computation by 3-10 times when compared to dense models.
- **Machine**: Choose processors and systems that are optimized for ML training. These processors improve performance and energy efficiency by 2-5 times when compared to general-purpose processors.
- **Mechanization** : Deploy your compute-intensive workloads in the cloud. Your workloads use less energy and cause lower emissions by 1.4 to 2 times when compared to on-premises deployments. Cloud data centers use newer, custom-designed warehouses that are built for energy efficiency and have a high [power usage effectiveness (PUE)](https://en.wikipedia.org/wiki/Power_usage_effectiveness) ratio. On-premises data centers are often older and smaller, therefore investments in energy-efficient cooling and power distribution systems might not be economical.
- **Map** : Select Google Cloud locations that use the cleanest energy. This approach helps to reduce the gross carbon footprint of your workloads by 5-10 times. For more information, see [Carbon-free energy for Google Cloud regions](https://cloud.google.com/sustainability/region-carbon).

For more information about the 4Ms best practices and efficiency metrics, see the
following research papers:

- [The carbon footprint of machine learning training will plateau, then shrink](https://www.techrxiv.org/doi/full/10.36227/techrxiv.19139645.v1)
- [The data denter as a computer: An introduction to the design of warehouse-scale machines, second edition](https://research.google/pubs/the-datacenter-as-a-computer-an-introduction-to-the-design-of-warehouse-scale-machines-second-edition/)

### Optimize AI models and algorithms for training and inference

The architecture of an AI model and the algorithms that are used for training
and inference have a significant impact on energy consumption. Consider the
following recommendations.

#### Select efficient AI models

Choose smaller, more efficient AI models that meet your performance
requirements. Don't select the largest available model as a default choice. For
example, a smaller, distilled model version like
[DistilBERT](https://huggingface.co/papers/1910.01108)
can deliver similar performance with significantly less computational overhead
and faster inference than a larger model like BERT.

#### Use domain-specific, hyper-efficient solutions

Choose specialized ML solutions that provide better performance and require
significantly less compute power than a large foundation model. These
specialized solutions are often pre-trained and hyper-optimized. They can
provide significant reductions in energy consumption and research effort for
both training and inference workloads. The following are examples of
domain-specific specialized solutions:

- [Earth AI](https://ai.google/earth-ai/) is an energy-efficient solution that synthesizes large amounts of global geospatial data to provide timely, accurate, and actionable insights.
- [WeatherNext](https://deepmind.google/science/weathernext/) produces faster, more efficient, and highly accurate global weather forecasts when compared to conventional physics-based methods.

#### Apply appropriate model compression techniques

The following are examples of techniques that you can use for model compression:

- **Pruning**: Remove unnecessary parameters from a neural network. These are parameters that don't contribute significantly to a model's performance. This technique reduces the size of the model and the computational resources that are required for inference.
- **Quantization**: Reduce the precision of model parameters. For example, reduce the precision from 32-bit floating-point to 8-bit integers. This technique can help to significantly decrease the memory footprint and power consumption without a noticeable reduction in accuracy.
- **Knowledge distillation** : Train a smaller *student* model to mimic the behavior of a larger, more complex *teacher* model. The student model can achieve a high level of performance with fewer parameters and by using less energy.

#### Use specialized hardware

As mentioned in
[Follow the 4Ms best practices for resource selection](https://docs.cloud.google.com/architecture/framework/printable#resource-selection-best-practices), choose processors
and systems that are optimized for ML training. These processors improve
performance and energy efficiency by 2-5 times when compared to general-purpose
processors.

#### Use parameter-efficient fine-tuning

Instead of adjusting all of a model's billions of parameters (full
fine-tuning), use parameter-efficient fine-tuning (PEFT) methods like low-rank
adaptation (LoRA). With this technique, you freeze the original model's weights
and train only a small number of new, lightweight layers. This approach helps to
reduce cost and energy consumption.

### Follow best practices for AI and ML operations

Operational practices significantly affect the sustainability of your AI and ML
workloads. Consider the following recommendations.

#### Optimize model training processes

Use the following techniques to optimize your model training processes:

- **Early stopping**: Monitor the training process and stop it when you don't observe further improvement in model performance against the validation set. This technique helps you prevent unnecessary computations and energy use.
- **Efficient data loading**: Use efficient data pipelines to ensure that the GPUs and TPUs are always utilized and don't wait for data. This technique helps to maximize resource utilization and reduce wasted energy.
- **Optimized hyperparameter tuning**: To find optimal hyperparameters more efficiently, use techniques like Bayesian optimization or reinforcement learning. Avoid exhaustive grid searches, which can be resource-intensive operations.

#### Improve inference efficiency

To improve the efficiency of AI inference tasks, use the following techniques:

- **Batching**: Group multiple inference requests in batches and take advantage of parallel processing on GPUs and TPUs. This technique helps to reduce the energy cost per prediction.
- **Advanced caching**: Implement a multi-layered caching strategy, which includes key-value (KV) caching for autoregressive generation and semantic-prompt caching for application responses. This technique helps to bypass redundant model computations and can yield significant reductions in energy usage and carbon emissions.

#### Measure and monitor

Monitor and measure the following parameters:

- **Usage and cost**: Use appropriate tools to track the token usage, energy consumption, and carbon footprint of your AI workloads. This data helps you identify opportunities for optimization and report progress toward sustainability goals.
- **Performance** : Continuously monitor model performance in production. Identify issues like data drift, which can indicate that the model needs to be fine-tuned again. If you need to re-train the model, you can use the original fine-tuned model as a starting point and save significant time, money, and energy on updates.
  - To track performance metrics, use [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview).
  - To correlate model changes with improvements in performance metrics, use [event annotations](https://docs.cloud.google.com/monitoring/dashboards/show-events).

For more information about operationalizing continuous improvement, see
[Continuously measure and improve sustainability](https://docs.cloud.google.com/architecture/framework/sustainability/continuously-measure-improve).

#### Implement carbon-aware scheduling

Architect your ML pipeline jobs to run in regions with the cleanest energy mix.
Use the Carbon Footprint report to identify the least
carbon-intensive regions. Schedule resource-intensive tasks as batch jobs during
periods when the local electrical grid has a higher percentage of carbon-free
energy (CFE).

#### Optimize data pipelines

ML operations and fine-tuning require a clean, high-quality dataset. Before
you start ML jobs, use managed data processing services to prepare the data
efficiently. For example, use
[Dataflow](https://docs.cloud.google.com/dataflow/docs/overview)
for streaming and batch processing and use
[Managed Service for Apache Spark](https://docs.cloud.google.com/dataproc/docs/concepts/overview)
for managed Spark and Hadoop pipelines. An optimized data pipeline helps to
ensure that your fine-tuning workload doesn't wait for data, so you can
maximize resource utilization and help reduce wasted energy.

#### Embrace MLOps

To automate and manage the entire ML lifecycle, implement
[ML Operations (MLOps) practices](https://docs.cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning). These practices help
to ensure that models are continuously monitored, validated, and redeployed
efficiently, which helps to prevent unnecessary training or resource allocation.

#### Use managed services

Instead of managing your own infrastructure, use managed cloud services like
[Vertex AI](https://docs.cloud.google.com/vertex-ai).
The cloud platform handles the underlying resource management, which lets you
focus on the fine-tuning process. Use services that include built-in tools for
hyperparameter tuning, model monitoring, and resource management.

## What's next

- [How much energy does Google's AI use? We did the math](https://cloud.google.com/blog/products/infrastructure/measuring-the-environmental-impact-of-ai-inference/)
- [Ironwood: The first Google TPU for the age of inference](https://blog.google/products/google-cloud/ironwood-tpu-age-of-inference/)
- [Google Sustainability 2025 Environmental Report](https://sustainability.google/google-2025-environmental-report/)
- [More Efficient In-Context Learning with GLaM](https://research.google/blog/more-efficient-in-context-learning-with-glam/)
- [Context caching overview](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/context-cache/context-cache-overview)

<br />

<br />


# Optimize resource usage for sustainability

This principle in the sustainability pillar of the
[Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework/sustainability)
provides recommendations to help you optimize resource usage by your workloads
in Google Cloud.

## Principle overview

Optimizing resource usage is crucial for enhancing the sustainability of your
cloud environment. Every resource that's provisioned---from compute cycles to data
storage---directly affects energy usage, water intensity, and carbon emissions. To
reduce the environmental footprint of your workloads, you need to make informed
choices when you provision, manage, and use cloud resources.

## Recommendations

To optimize resource usage, consider the recommendations in the following
sections.

### Implement automated and dynamic scaling

Automated and dynamic scaling ensures that resource usage is optimal, which
helps to prevent energy waste from idle or over-provisioned infrastructure. The
reduction in wasted energy translates to lower costs and lower carbon emissions.

Use the following techniques to implement automated and dynamic scalability.

#### Use horizontal scaling

Horizontal scaling is the preferred scaling technique for most cloud-first
applications. Instead of increasing the size of each instance, known as
*vertical scaling* , you add instances to distribute the load. For example, you
can use
[managed instance groups (MIGs)](https://docs.cloud.google.com/compute/docs/autoscaler)
to automatically scale out a group of Compute Engine VMs. Horizontally scaled
infrastructure is more resilient because the failure of an instance doesn't
affect the availability of the application. Horizontal scaling is also a
resource-efficient technique for applications that have variable load levels.

#### Configure appropriate scaling policies

Configure autoscaling settings based on the requirements of your workloads.
Define custom metrics and thresholds that are specific to application behavior.
Instead of relying solely on CPU utilization, consider metrics like queue depth
for asynchronous tasks, request latency, and custom application metrics. To
prevent frequent, unnecessary scaling or *flapping* , define clear scaling
policies. For example, for workloads that you deploy in
Google Kubernetes Engine (GKE), configure an appropriate
[cluster autoscaling policy](https://cloud.google.com/blog/products/containers-kubernetes/gke-features-to-optimize-resource-allocation).

#### Combine reactive and proactive scaling

With reactive scaling, the system scales in response to real-time load changes.
This technique is suitable for applications that have unpredictable spikes in
load.

Proactive scaling is suitable for workloads with predictable patterns, such as
fixed daily business hours and weekly reports generation. For such workloads,
use scheduled autoscaling to pre-provision resources so that they can handle an
anticipated load level. This technique prevents a scramble for resources and
ensures smoother user experience with higher efficiency. This technique also
helps you plan proactively for known spikes in load such as major sales events
and focused marketing efforts.

Google Cloud managed services and features like GKE
Autopilot, Cloud Run, and MIGs automatically manage proactive
scaling by learning from your workload patterns. By default, when a
Cloud Run service doesn't receive any traffic, it scales to zero
instances.

#### Design stateless applications

For an application to scale horizontally, its components should be stateless.
This means that a specific user's session or data isn't tied to a single compute
instance. When you store session state outside the compute instance, such as in
Memorystore for Redis, any compute instance can handle requests from any
user. This design approach enables horizontal scaling that's seamless and
efficient.

### Use scheduling and batches

Batch processing is ideal for large-scale, non-urgent workloads. Batch jobs can
help to optimize your workloads for energy efficiency and cost.

Use the following techniques to implement scheduling and batch jobs.

#### Schedule for low carbon intensity

Schedule your batch jobs to run in low-carbon regions and during periods when
the local electrical grid has a high percentage of clean energy. To identify
the least carbon-intensive times of day for a region, use the
[Carbon Footprint report](https://docs.cloud.google.com/carbon-footprint/docs/view-carbon-data).

#### Use Spot VMs for noncritical workloads

[Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot)
let you take advantage of unused Compute Engine capacity at a steep discount.
Spot VMs can be preempted, but they provide a cost-effective way
to process large datasets without the need for dedicated, always-on resources.
Spot VMs are ideal for non-critical, fault-tolerant batch jobs.

#### Consolidate and parallelize jobs

To reduce the overhead for starting up and shutting down individual jobs, group
similar jobs into a single large batch. Run these high-volume workloads on
services like
[Batch](https://docs.cloud.google.com/batch/docs/get-started).
The service automatically provisions and manages the necessary infrastructure,
which helps to ensures optimal resource utilization.

#### Use managed services

Managed services like Batch and
[Dataflow](https://docs.cloud.google.com/dataflow/docs/overview)
automatically handle resource provisioning, scheduling, and monitoring. The
cloud platform handles resource optimization. You can focus on the application
logic. For example,
[Dataflow automatically scales the number of workers](https://docs.cloud.google.com/dataflow/docs/horizontal-autoscaling)
based on the data volume in the pipeline, so you don't pay for idle resources.

### Match VM machine families to workload requirements

The machine types that you can use for your Compute Engine VMs are
grouped into
[machine families](https://docs.cloud.google.com/compute/docs/machine-resource),
which are optimized for different workloads. Choose appropriate machine families
based on the requirements of your workloads.

| Machine family | Recommended for workload types | Sustainability guidance |
|---|---|---|
| **General-purpose instances (E2, N2, N4, Tau T2A/T2D)**: These instances provide a balanced ratio of CPU to memory. | Web servers, microservices, small to medium databases, and development environments. | The E2 series is highly cost-efficient and energy-efficient due to its dynamic allocation of resources. The Tau T2A series uses Arm-based processors, which are often more energy-efficient per unit of performance for large-scale workloads. |
| **Compute-optimized instances (C2, C3)**: These instances provide a high vCPU-to-memory ratio and high performance per core. | High performance computing (HPC), batch processing, gaming servers, and CPU-based data analytics. | A C-series instance lets you complete CPU-intensive tasks faster, which reduces the total compute time and energy consumption of the job. |
| **Memory-optimized instances (M3, M2)**: These instances are designed for workloads that require a large amount of memory. | Large in-memory databases and data warehouses, such as SAP HANA or in-memory analytics. | Memory-optimized instances enable the consolidation of memory-heavy workloads on fewer physical nodes. This consolidation reduces the total energy that's required when compared to using multiple smaller instances. High-performance memory reduces data-access latency, which can reduce the total time that the CPU spends in an active state. |
| **Storage-optimized instances (Z3):**These instances provide high-throughput, low-latency local SSD storage. | Data warehousing, log analytics, and SQL, NoSQL, and vector databases. | Storage-optimized instances process massive datasets locally, which helps to eliminate the energy that's used for cross-location network data egress. When you use local storage for high-IOPS tasks, you avoid over-provisioning multiple standard instances. |
| **Accelerator-optimized instances (A3, A2, G2)**: These instances are built for GPU and TPU-accelerated workloads, such as AI, ML, and HPC. | ML model training and inference, and scientific simulations. | [TPUs](https://docs.cloud.google.com/tpu) are engineered for optimal energy efficiency. They deliver higher computations per watt. A GPU-accelerated instance like the A3 series with NVIDIA H100 GPUs can be significantly more energy-efficient for training large models than a CPU-only alternative. Although a GPU-accelerated instance has higher nominal power usage, the task is completed much faster. |

### Upgrade to the latest machine types

Use of the latest machine types might help to improve sustainability. When
machine types are updated, they're often designed to be more energy-efficient
and to provide higher performance per watt. VMs that use the latest machine
types might complete the same amount of work with lower power consumption.

CPUs, GPUs, and TPUs often benefit from technical advancements in chip
architecture, such as the following:

- **Specialized cores**: Advancements in processors often include specialized cores or instructions for common workloads. For example, CPUs might have dedicated cores for vector operations or integrated AI accelerators. When these tasks are offloaded from the main CPU, the tasks are completed more efficiently and they consume less energy.
- **Improved power management**: Advancements in chip architectures often include more sophisticated power management features, such as dynamic adjustment of voltage and frequency based on the workload. These power-management features enable the chips to run at peak efficiency and enter low-power states when they are idle, which minimizes energy consumption.

The technical improvements in chip architecture provide the following direct
benefits for sustainability and cost:

- **Higher performance per watt** : This is a key metric for sustainability. For example, the [C4 VMs demonstrate 40% higher price-performance](https://cloud.google.com/blog/products/compute/c4-machine-series-is-now-ga) when compared to C3 VMs for the same energy consumption. The [C4A processor provides 60% higher energy-efficiency](https://cloud.google.com/blog/products/compute/try-c4a-the-first-google-axion-processor?e=48754805) over comparable x86 processors. These performance capabilities let you complete tasks faster or use fewer instances for the same load.
- **Lower total energy consumption**: With improved processors, compute resources are used for a shorter duration for a given task, which reduces the overall energy usage and carbon footprint. The carbon impact is particularly high for short-lived, compute-intensive workloads like batch jobs and ML model training.
- **Optimal resource utilization**: The latest machine types are often better suited for modern software and are more compatible with advanced features of cloud platforms. These machine types typically enable better resource utilization, which reduces the need for over-provisioning and helps to ensure that every watt of power is used productively.

### Deploy containerized applications

You can use container-based, fully-managed services such as GKE
and Cloud Run as a part of your strategy for sustainable cloud
computing. These services help to optimize resource utilization and automate
resource management.

#### Leverage the scale-to-zero capability of Cloud Run

Cloud Run provides a managed serverless environment that
automatically scales instances to zero when there is no incoming traffic for a
service or when a job is completed. Autoscaling helps to eliminate energy
consumption by idle infrastructure. Resources are powered only when they
actively process requests. This strategy is highly effective for intermittent
or event-driven workloads. For AI workloads, you can use
[GPUs with Cloud Run](https://docs.cloud.google.com/run/docs/configuring/services/gpu),
which lets you consume and pay for GPUs only when they are used.

#### Automate resource optimization using GKE

GKE is a container orchestration platform, which ensures that
applications use only the resources that they need. To help you
automate resource optimization, GKE provides the following
techniques:

- **[Bin packing](https://kubernetes.io/docs/concepts/scheduling-eviction/resource-bin-packing/)**: GKE Autopilot intelligently packs multiple containers on the available nodes. Bin packing maximizes the utilization of each node and reduces the number of idle or underutilized nodes, which helps to reduce energy consumption.
- **[Horizontal Pod autoscaling (HPA)](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/horizontalpodautoscaler)**: With HPA, the number of container replicas (Pods) is adjusted automatically based on predefined metrics like CPU usage or custom application-specific metrics. For example, if your application experiences a spike in traffic, GKE adds Pods to meet the demand. When the traffic subsides, GKE reduces the number of Pods. This dynamic scaling prevents over-provisioning of resources, so you don't pay for or power up unnecessary compute capacity.
- **[Vertical Pod autoscaling (VPA)](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/verticalpodautoscaler)**: You can configure GKE to automatically adjust the CPU and memory allocations and limits for individual containers. This configuration ensures that a container isn't allocated more resources than it needs, which helps to prevent resource over-provisioning.
- **[GKE multidimensional Pod autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multidimensional-pod-autoscaling)**: For complex workloads, you can configure HPA and VPA simultaneously to optimize both the number of Pods and the size of each Pod. This technique helps to ensure the smallest possible energy footprint for the required performance.
- **[Topology-Aware Scheduling (TAS)](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/schedule-gke-workloads-tas)**: TAS enhances the network efficiency for AI and ML workloads in GKE by placing Pods based on the physical structure of the data center infrastructure. TAS strategically colocates workloads to minimize network hops. This colocation helps to reduce communication latency and energy consumption. By optimizing the physical alignment of nodes and specialized hardware, TAS accelerates task completion and maximizes the energy efficiency of large-scale AI and ML workloads.

### Configure carbon-aware scheduling

At Google, we continually shift our workloads to
[locations](https://blog.google/outreach-initiatives/sustainability/carbon-aware-computing-location/)
and
[times](https://blog.google/inside-google/infrastructure/data-centers-work-harder-sun-shines-wind-blows/)
that provide the cleanest electricity. We also repurpose, or
[harvest](https://cloud.google.com/blog/topics/sustainability/hardware-harvesting-at-google-reducing-waste-and-emissions),
older equipment for alternative use cases. You can use this carbon-aware
scheduling strategy to ensure that your containerized workloads use clean
energy.

To implement carbon-aware scheduling, you need information about the energy mix
that powers data centers in a region in real time. You can get this information
in a machine-readable format from the
[Carbon free energy for Google Cloud regions](https://github.com/GoogleCloudPlatform/region-carbon-info)
repository in GitHub or from a
[BigQuery public dataset](https://console.cloud.google.com/marketplace/product/bigquery-public-datasets/regional-cfe).
The hourly grid mix and carbon intensity data that's used to calculate the
Google annual carbon dataset is sourced from
[Electricity Maps](https://app.electricitymaps.com/).

To implement carbon-aware scheduling, we recommend the following techniques:

- **Geographical shifting**: Schedule your workloads to run in regions that use a higher proportion of renewable energy sources. This approach lets you use cleaner electrical grids.
- **Temporal shifting**: For non-critical, flexible workloads like batch processing, configure the workloads to run during off-peak hours or when renewable energy is most abundant. This approach is known as temporal shifting and helps reduce the overall carbon footprint by taking advantage of cleaner energy sources when they are available.

### Architect energy-efficient disaster recovery

Preparing for disaster recovery (DR) often involves pre-provisioning redundant
resources in a secondary region. However, idle or under-utilized resources can
cause significant energy waste. Choose DR strategies that maximize resource
utilization and minimize the carbon impact without compromising your recovery
time objectives (RTO).

#### Optimize for cold start efficiency

Use the following approaches to minimize or eliminate active resources in your
secondary (DR) region:

- **Prioritize [cold DR](https://en.wikipedia.org/wiki/Backup_site#Cold_site)**: Keep resources in the DR region turned off or in a scaled-to-zero state. This approach helps to eliminate the carbon footprint of idle compute resources.
- **Take advantage of serverless failover**: Use managed serverless services like Cloud Run for DR endpoints. Cloud Run scales to zero when it isn't in use, so you can maintain a DR topology that consumes no energy until traffic is diverted to the DR region.
- **Automate recovery with infrastructure-as-code (IaC)**: Instead of keeping resources in the DR site running (warm), use an IaC tool like Terraform to rapidly provision environments only when needed.

#### Balance redundancy and utilization

Resource redundancy is a primary driver of energy waste. To reduce redundancy,
use the following approaches:

- **Prefer active-active over active-passive**: In an active-passive setup, the resources in the passive site are idle, which results in wasted energy. An active-active architecture that's optimally sized ensures that all of the provisioned resources across both regions actively serve traffic. This approach helps you maximize the energy efficiency of your infrastructure.
- **Right-size redundancy**: Replicate data and services across regions only when the replication is necessary to meet high-availability or DR requirements. Every additional replica increases the energy cost of persistent storage and network egress.

<br />

<br />


# Develop energy-efficient software

This principle in the sustainability pillar of the
[Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework/sustainability)
provides recommendations to write software that minimizes energy consumption and
server load.

## Principle overview

When you follow best practices to build your cloud applications, you optimize
the energy that's utilized by the cloud infrastructure resources: AI, compute,
storage, and network. You also help to reduce the water requirements of the data
centers and the energy that end-user devices consume when they access your
applications.

To build energy-efficient software, you need to integrate sustainability
considerations throughout the software lifecycle, from design and development to
deployment, maintenance, and archival. For detailed guidance about using AI to
build software that minimizes the environmental impact of cloud workloads, see
the Google Cloud ebook,
[Build Software Sustainably](https://cloud.google.com/resources/content/build-software-sustainably).

## Recommendations

The recommendations in this section are grouped into the following focus areas:

- [Minimize computational work](https://docs.cloud.google.com/architecture/framework/printable#minimal-computations): Favor lean, focused code that eliminates redundant logic and avoids unnecessary computations or feature bloat.
- [Use efficient algorithms and data structures](https://docs.cloud.google.com/architecture/framework/printable#efficient-algorithms): Choose time-efficient and memory-efficient algorithms that reduce CPU load and minimize memory usage.
- [Optimize compute and data operations](https://docs.cloud.google.com/architecture/framework/printable#optimized-operations): Develop with the goal of efficiently using all of the available resources, including CPU, memory, disk I/O, and network. For example, when you replace busy loops with event-driven logic, you avoid unnecessary polling.
- [Implement frontend optimization](https://docs.cloud.google.com/architecture/framework/printable#optimized-frontend): To reduce the power that's consumed by end-user devices, use strategies like minimization, compression, and [lazy-loading](https://en.wikipedia.org/wiki/Lazy_loading) for images and assets.

### Minimize computational work

To write energy-efficient software, you need to minimize the total amount of
computational work that your application performs. Every unnecessary
instruction, redundant loop, and extra feature consumes energy, time, and
resources. Use the following recommendations to build software that performs
minimal computations.

#### Write lean, focused code

To write minimal code that's essential to achieve the required outcomes, use the
following approaches:

- **Eliminate redundant logic and feature bloat**: Write code that performs only the essential functions. Avoid features that increase the computational overhead and complexity but don't provide measurable value to your users.
- **Refactor**: To improve energy efficiency over time, regularly audit your applications to identify unused features. Take action to remove or refactor such features as appropriate.
- **Avoid unnecessary operations** : Don't compute a value or run an action until the result is needed. Use techniques like [lazy evaluation](https://en.wikipedia.org/wiki/Lazy_evaluation), which delay computations until a dependent component in the application needs the output.
- **Prioritize code readability and reusability** : Write code that's readable and reusable. This approach minimizes duplication and follows the [don't repeat yourself (DRY) principle](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself), which can help to reduce carbon emissions from software development and maintenance.

#### Use backend caching

Backend caching ensures that an application does not perform the same work
repeatedly. A high cache-hit ratio leads to an almost linear reduction in energy
consumption per request. To implement backend caching, use the following
techniques:

- **Cache frequent data** : Store frequently accessed data in a temporary, high-performance storage location. For example, use an in-memory caching service like [Memorystore](https://docs.cloud.google.com/memorystore/docs). When an application retrieves data from a cache, the volume of database queries and disk I/O operations is reduced. Consequently, the load on the databases and servers in the backend decreases.
- **Cache API responses**: To avoid redundant and costly network calls, cache the results of frequent API requests.
- **Prioritize in-memory caching**: To eliminate slow disk I/O operations and complex database queries, store data in high-speed memory (RAM).
- **Select appropriate [cache-write strategies](https://en.wikipedia.org/wiki/Cache_(computing)#Write_policies)** :
  - The write-through strategy ensures that data is written synchronously to the cache *and* the persistent store. This strategy increases the likelihood of cache hits, so the persistent store gets fewer energy-intensive read requests.
  - The write-back (write-behind) strategy enhances the performance of write-heavy applications. Data is written to the cache first, and the database is updated asynchronously later. This strategy reduces the immediate write load on slower databases.
- **Use smart eviction policies**: Keep the cache lean and efficient. To remove stale or low-utility data and to maximize the space that's available for frequently requested data, use policies like time to live (TTL), least recently used (LRU), and least frequently used (LFU).

### Use efficient algorithms and data structures

The algorithms and data structures that you choose determine the raw
computational complexity of your software. When you select appropriate
algorithms and data structures, you minimize the number of CPU cycles and memory
operations that are required to complete a task. Fewer CPU cycles and memory
operations lead to lower energy consumption.

#### Choose algorithms for optimal time complexity

Prioritize algorithms that achieve the required result in the least amount of
time. This approach helps to reduce the duration of resource usage. To select
algorithms that optimize resource usage, use the following approaches:

- **Focus on reducing complexity** : To evaluate complexity, look beyond runtime metrics and consider the theoretical complexity of the algorithm. For example, when compared to [bubble sorting](https://en.wikipedia.org/wiki/Bubble_sort), [merge sorting](https://en.wikipedia.org/wiki/Merge_sort) significantly reduces the computational load and energy consumption for large datasets.
- **Avoid redundant work**: Use built-in, optimized functions in your chosen programming language or framework. These functions are often implemented in a lower-level and more energy-efficient language like C or C++, so they are better optimized for the underlying hardware compared to custom-coded functions.

#### Select data structures for efficiency

The data structures that you choose determine the speed at which data can be
retrieved, inserted, or processed. This speed affects CPU and memory usage. To
select efficient data structures, use the following approaches:

- **Optimize for search and retrieval**: For common operations like checking whether an item exists or retrieving a specific value, prefer data structures that are optimized for speed. For example, hash maps or hash sets enable near-constant time lookups, which is a more energy-efficient approach than linearly searching through an array.
- **Minimize memory footprint**: Efficient data structures help to reduce the overall memory footprint of an application. Reduced memory access and management leads to lower power consumption. In addition, a leaner memory profile enables processes to run more efficiently, which lets you postpone resource upgrades.
- **Use specialized structures** : Use data structures that are purpose-built for a given problem. For example, use a [trie](https://en.wikipedia.org/wiki/Trie) data structure for rapid string-prefix searching, and use a priority queue when you need to access only the highest or lowest value efficiently.

### Optimize compute and data operations

When you develop software, focus on efficient and proportional resource usage
across the entire technology stack. Treat CPU, memory, disk, and network as
limited and shared resources. Recognize that efficient usage of resources leads
to tangible reductions in costs and energy consumption.

#### Optimize CPU utilization and idle time

To minimize the time that the CPU spends in an active, energy-consuming state
without performing meaningful work, use the following approaches:

- **Prefer event-driven logic over polling**: Replace resource-intensive busy loops or constant checking (polling) with event-driven logic. An event-driven architecture ensures that the components of an application operate only when they're triggered by relevant events. This approach enables on-demand processing, which eliminates the need for resource-intensive polling.
- **Prevent constant high frequency**: Write code that doesn't force the CPU to constantly operate at its highest frequency. To minimize energy consumption, systems that are idle should be able to enter low-power states or sleep modes.
- **Use asynchronous processing**: To prevent threads from being locked during idle wait times, use asynchronous processing. This approach frees resources and leads to higher overall resource utilization.

#### Manage memory and disk I/O efficiently

Inefficient memory and disk usage leads to unnecessary processing and increased
power consumption. To manage memory and I/O efficiently, use the following
techniques:

- **Strict memory management**: Take action to proactively release unused memory resources. Avoid holding large objects in memory for longer periods than necessary. This approach prevents performance bottlenecks and reduces the power that's consumed for memory access.
- **Optimize disk I/O**: Reduce the frequency of your application's read and write interactions with persistent storage resources. For example, use an intermediary memory buffer to store data. Write the data to persistent storage at fixed intervals or when the buffer reaches a certain size.
- **Batch operations**: Consolidate frequent, small disk operations into fewer, larger batch operations. A batch operation consumes less energy than many individual, small transactions.
- **Use compression** : Reduce the amount of data that's written to or read from disks by applying suitable data-compression techniques. For example, to compress data that you store in Cloud Storage, you can use [decompressive transcoding](https://docs.cloud.google.com/storage/docs/transcoding).

#### Minimize network traffic

Network resources consume significant energy during data transfer operations.
To optimize network communication, use the following techniques:

- **Minimize payload size**: Design your APIs and applications to transfer only the data that's needed for a request. Avoid fetching or returning large JSON or XML structures in cases where only a few fields are required. Ensure that the data structures that are returned are concise.
- **Reduce round-trips**: To reduce the number of network round-trips that are required to complete a user action, use smarter protocols. For example, prefer HTTP/3 over HTTP/1.1, choose GraphQL over REST, use binary protocols, and consolidate API calls. When you reduce the volume of network calls, you reduce the energy consumption for both your servers and for end-user devices.

### Implement frontend optimization

Frontend optimization minimizes the data that your end users must download and
process, which helps to reduce the load on the resources of end-user devices.

#### Minimize code and assets

When end users need to download and process smaller and more efficiently
structured resources, their devices consume less power. To minimize the download
volume and processing load on end-user devices, use the following techniques:

- **Minimization and compression**: For JavaScript, CSS, and HTML files, remove unnecessary characters like whitespaces and comments by using appropriate minimization tools. Ensure that files like images are compressed and optimized. You can automate the minimization and compression of web assets by using a CI/CD pipeline.
- **Lazy loading**: Load images, videos, and non-critical assets only when they are actually needed, such as when these elements scroll into the viewport of a web page. This approach reduces the volume of initial data transfer and the processing load on end-user devices.
- **Smaller JavaScript bundles** : Eliminate unused code from your JavaScript bundles by using modern module bundlers and techniques like [tree shaking](https://webpack.js.org/guides/tree-shaking/). This approach results in smaller files that load faster and use fewer server resources.
- **Browser caching**: Use HTTP caching headers to instruct the user's browser to store static assets locally. Browser caching helps to prevent repeated downloads and unnecessary network traffic on subsequent visits.

#### Prioritize lightweight user experience (UX)

The design of your user interface can have a significant impact on the
computational complexity for rendering frontend content. To build frontend
interfaces that provide a lightweight UX, use the following techniques:

- **Efficient rendering** : Avoid resource-intensive, frequent [Document Object Model (DOM)](https://en.wikipedia.org/wiki/Document_Object_Model) manipulation. Write code that minimizes the rendering complexity and eliminates unnecessary re-rendering.
- **Lightweight design patterns** : Where appropriate, prefer static sites or [progressive web apps (PWAs)](https://en.wikipedia.org/wiki/Progressive_web_app). Such sites and apps load faster and require fewer server resources.
- **Accessibility and performance** : Responsive, fast-loading sites are often more sustainable and accessible. An optimized, clutter-free design reduces the resources that are consumed when content is rendered. Websites that are optimized for performance and speed can help to drive higher revenue. According to a research study by Deloitte and Google, [Milliseconds Make Millions](https://www.thinkwithgoogle.com/_qs/documents/9757/Milliseconds_Make_Millions_report_hQYAbZJ.pdf#page=5), a 0.1-second (100ms) improvement in site speed leads to an 8.4% increase in conversions for retail sites and a 9.2% increase in the average order value.

<br />

<br />


# Optimize data and storage for sustainability

This principle in the sustainability pillar of the
[Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework/sustainability)
provides recommendations to help you optimize the energy efficiency and carbon
footprint for your storage resources in Google Cloud.

## Principle overview

Stored data isn't a passive resource. Energy is consumed and carbon emissions
occur throughout the lifecycle of data. Every gigabyte of stored data requires
physical infrastructure that's continuously powered, cooled, and managed. To
achieve sustainable cloud architecture, treat data as a valuable but
environmentally costly asset and prioritize proactive data governance.

Your decisions about data retention, quality, and location can help you achieve
substantial reductions in cloud costs and energy consumption. Minimize the data
that you store, optimize where and how data you store data, and implement
automated deletion and archival strategies. When you reduce data clutter, you
improve system performance and fundamentally reduce the long-term environmental
footprint of your data.

## Recommendations

To optimize your data lifecycle and storage resources for sustainability,
consider the recommendations in the following sections.

### Prioritize high-value data

Stored data that's unused, duplicated, or obsolete continues to consume energy
to power the underlying infrastructure. To reduce the storage-related carbon
footprint, use the following techniques.

#### Identify and eliminate duplication

Establish policies to prevent the needless replication of datasets across
multiple Google Cloud projects or services. Use central data repositories
like
[BigQuery datasets](https://docs.cloud.google.com/bigquery/docs/datasets-intro)
or
[Cloud Storage buckets](https://docs.cloud.google.com/storage/docs/buckets)
as single sources of truth and grant appropriate access to these repositories.

#### Remove shadow data and dark data

*Dark data* is data for which the utility or owner is unknown. *Shadow data*
means unauthorized copies of data. Scan your storage systems and find dark data
and shadow data by using a data discovery and cataloging solution like
[Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/introduction).
Regularly audit these findings and implement a process for archival or deletion
of dark and shadow data as appropriate.

#### Minimize the data volume for AI workloads

Store only the features and processed data that are required for model training
and serving. Where possible, use techniques like data sampling, aggregation, and
synthetic data generation to achieve model performance without relying on
massive raw datasets.

#### Integrate data quality checks

Implement automatic data validation and data cleaning pipelines by using
services like
[Managed Service for Apache Spark](https://docs.cloud.google.com/dataproc/docs/concepts/overview),
[Dataflow](https://docs.cloud.google.com/dataflow/docs/overview),
or Knowledge Catalog at the point of data ingestion.
Low-quality data causes wasted storage space. It also leads to unnecessary
energy consumption when the data is used later for analytics or AI training.

#### Review the value density of data

Periodically review high-volume datasets like logs and IoT streams. Determine
whether any data can be summarized, aggregated, or down-sampled to maintain the
required information density and reduce the physical storage volume.

#### Critically evaluate the need for backups

Assess the need for backups of data that you can regenerate with minimal effort.
Examples of such data include intermediate ETL results, ephemeral caches, and
training data that's derived from a stable, permanent source. Retain backups for
only the data that is unique or expensive to recreate.

### Optimize storage lifecycle management

Automate the storage lifecycle so that when the utility of data declines, the
data is moved to an energy-efficient storage class or retired, as appropriate.
Use the following techniques.

#### Select an appropriate Cloud Storage class

Automate the transition of data in Cloud Storage to lower-carbon storage
classes based on access frequency by using
[Object Lifecycle Management](https://docs.cloud.google.com/storage/docs/lifecycle).

- Use Standard storage for only actively used datasets, such as current production models.
- Transition data such as older AI training datasets or less-frequently accessed backups to Nearline or Coldline storage.
- For long-term retention, use Archive storage, which is optimized for energy efficiency at scale.

#### Implement aggressive data lifecycle policies

Define clear, automated time to live (TTL) policies for non-essential data,
such as log files, temporary model artifacts, and outdated intermediate results.
Use lifecycle rules to automatically delete such data after a defined period.

#### Mandate resource tagging

Mandate the use of consistent resource tags and labels for all of your
Cloud Storage buckets, BigQuery datasets, and persistent
disks. Create tags that indicate the data owner, purpose of the data, and the
retention period. Use Organization Policy Service constraints to ensure that required tags,
such as retention period, are applied to resources. Tags let you automate
lifecycle management, create granular FinOps reports, and produce carbon
emissions reports.

#### Right-size and deprovision compute storage

Regularly audit persistent disks that are attached to Compute Engine instances
and ensure that the disks aren't over-provisioned. Use snapshots only when they
are necessary for backup. Delete old, unused snapshots. For databases, use data
retention policies to reduce the size of the underlying persistent disks.

#### Optimize the storage format

For storage that serves analytics workloads, prefer compressed, columnar formats
like Parquet or optimized Avro over row-based formats like JSON or CSV. Columnar
storage significantly reduces physical disk-space requirements and improves the
read efficiency. This optimization helps to reduce energy consumption for the
associated compute and I/O operations.

### Optimize regionality and data movement

The physical location and movement of your data affect the consumption of
network resources and the energy required for storage. Optimize data regionality
by using the following techniques.

#### Select low-carbon storage regions

Depending on your compliance requirements, store data in Google Cloud regions
that use a higher percentage of carbon-free energy (CFE) or that have lower grid
carbon intensity. Restrict the creation of storage buckets in high-carbon
regions by using the
[resource locations](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations)
Organization Policy constraint. For information about CFE and carbon-intensity
data for Google Cloud regions, see
[Carbon-free energy for Google Cloud regions](https://cloud.google.com/sustainability/region-carbon).

#### Minimize replication

Replicate data across regions only to meet mandatory disaster recovery (DR) or
high-availability (HA) requirements. Cross-region and multi-region replication
operations significantly increase the energy cost and carbon footprint of your
data.

#### Optimize data processing locations

To reduce energy consumption for network data transfer, deploy
compute-intensive workloads like AI training and BigQuery
processing in the same region as the data source.

#### Optimize data movement for your partners and customers

To move large volumes of data across cloud services, locations, and providers,
encourage your partners and customers to use
[Storage Transfer Service](https://docs.cloud.google.com/storage-transfer/docs/overview)
or data-sharing APIs. Avoid mass data dumps. For public datasets, use
[Requester Pays](https://docs.cloud.google.com/storage/docs/requester-pays)
buckets to shift the data transfer and processing costs and the environmental
impact to end users.

<br />

<br />


# Continuously measure and improve sustainability

This principle in the sustainability pillar of the
[Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework/sustainability)
provides recommendations to help you measure and continuously improve the
sustainability of your workloads in Google Cloud.

## Principle overview

To ensure that your cloud workloads remain sustainable, you need accurate and
transparent metrics. Verifiable metrics let you translate sustainability goals
to actions. Every resource that you create in the cloud has an associated carbon
footprint. To build and maintain sustainable cloud architectures, you must
integrate the measurement of carbon data into your operational feedback loop.

The recommendations in this section provide a framework for using
[Carbon Footprint](https://cloud.google.com/carbon-footprint)
to quantify carbon emissions, identify carbon hotspots, implement targeted
workload optimizations, and verify the outcomes of the optimization efforts.
This framework lets you efficiently align your cost optimization goals with
verifiable carbon reduction targets.

### Carbon Footprint reporting methodology

Carbon Footprint provides a transparent, auditable, and
globally-aligned report of your cloud-related emissions. The report adheres to
international standards, primarily the
[Greenhouse Gas (GHG) Protocol](https://ghgprotocol.org/standards)
for carbon reporting and accounting. The Carbon Footprint report
uses location-based and market-based accounting methods. Location-based
accounting is based on the local grid's emissions factor. Market-based
accounting considers Google's purchases of carbon-free energy (CFE). This dual
approach helps you understand both the physical-grid impact and the
carbon benefit of your workloads in Google Cloud.

For more information about how the Carbon Footprint report is
prepared, including the data sources used, Scope-3 inclusions, and the
customer allocation model, see
[Carbon Footprint reporting methodology](https://docs.cloud.google.com/carbon-footprint/docs/methodology).

## Recommendations

To use carbon measurement for continuous improvement, consider the
recommendations in the following sections. The recommendations are structured as
phases of maturity for implementing sustainable-by-design cloud operations:

- [Phase 1: Establish a baseline](https://docs.cloud.google.com/architecture/framework/printable#establish-baseline)
- [Phase 2: Identify hotspots](https://docs.cloud.google.com/architecture/framework/printable#identify-hotspots)
- [Phase 3: Implement targeted optimization](https://docs.cloud.google.com/architecture/framework/printable#optimize)
- [Phase 4: Institutionalize sustainability practices and reporting](https://docs.cloud.google.com/architecture/framework/printable#institutionalize)

### Phase 1: Establish a baseline

In this phase, you set up the necessary tools and ensure that data is
accessible and correctly integrated.

1. **Grant permissions** : Grant permissions to teams like FinOps, SecOps and platform engineering so that they can access the Carbon Footprint dashboard in the Google Cloud console. Grant the [Carbon Footprint Viewer role](https://docs.cloud.google.com/carbon-footprint/docs/iam#standard-roles) (`roles/billing.carbonViewer`) in Identity and Access Management (IAM) for the appropriate billing account.
2. **Automate data export** : Configure automated [export of Carbon Footprint data](https://docs.cloud.google.com/carbon-footprint/docs/export) to BigQuery. The exported data lets you perform deep analysis, correlate carbon data with cost and usage data, and produce custom reports.
3. **Define carbon-related key performance indicators (KPIs)** : Establish metrics that connect carbon emissions to business value. For example, carbon intensity is a metric for the number of kilograms of [CO~2~ equivalent](https://en.wikipedia.org/wiki/Global_warming_potential) per customer, transaction, or revenue unit.

### Phase 2: Identify carbon hotspots

Identify the areas that have the largest environmental impact by analyzing the
granular data in the Carbon Footprint report. Use the following
techniques for this analysis:

- **Prioritize by scope**: To quickly identify the largest gross carbon emitters, analyze the data in the dashboard by project, region, and service.
- **Use dual-accounting**: When you evaluate the carbon impact in a region, consider both location-based emissions (the environmental impact of the local electrical grid) and market-based emissions (the benefit of Google's CFE investments).
- **Correlate with cost** : Join the carbon data in BigQuery with your billing data and assess the impact of optimization actions on sustainability *and* cost. High cost can often be correlated with high carbon emissions.
- **Annotate data to measure return on effort (ROE)**: Annotate the carbon data in BigQuery with specific events, like right-sizing a resource or decommissioning a large service. The annotations let you attribute reductions in carbon emission and cost to specific optimization initiatives, so that you can measure and demonstrate the outcome of each initiative.

### Phase 3: Implement targeted optimization

This is the execution phase for implementing sustainable-by-design cloud
operations. Use the following strategies to optimize specific resources that you
identify as significant drivers of cost and carbon emissions:

- **Decommission unattended projects** : Regularly check the [unattended project recommender](https://docs.cloud.google.com/recommender/docs/unattended-project-recommender) that's integrated with the Carbon Footprint data. To achieve immediate, verified reductions in carbon emissions and cost, automate the review and eventual removal of unused projects.
- **Right-size resources** : Match the provisioned resource capacity to actual utilization by using Active Assist right-sizing [recommenders](https://docs.cloud.google.com/recommender/docs/recommenders) like [machine type recommendations for Compute Engine VMs](https://docs.cloud.google.com/compute/docs/instances/apply-machine-type-recommendations-for-instances). For compute-intensive tasks and AI workloads, use the most efficient machine types and AI models.
- **Adopt carbon-aware scheduling** : For batch workloads that aren't time-critical, integrate regional CFE data into the scheduling logic. Where feasible, limit the creation of new resources to low-carbon regions by using the [resource locations](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations) constraint in Organization Policy Service.
- **Reduce data sprawl**: Implement data governance policies to ensure that infrequently accessed data is transitioned to an appropriate cold storage class (Nearline, Coldline, or Archive) or is permanently deleted. This strategy helps to reduce the energy cost of your storage resources.
- **Refine application code**: Fix code-level inefficiencies that cause excessive resource usage or unnecessary computation.

For more information, see the following:

- [Use regions that consume low-carbon energy](https://docs.cloud.google.com/architecture/framework/sustainability/low-carbon-regions)
- [Optimize AI and ML workloads](https://docs.cloud.google.com/architecture/framework/sustainability/ai-ml-energy-efficiency)
- [Optimize resource usage](https://docs.cloud.google.com/architecture/framework/sustainability/optimize-resource-usage)
- [Develop energy-efficient software](https://docs.cloud.google.com/architecture/framework/sustainability/energy-efficient-software)
- [Optimize data and storage for sustainability](https://docs.cloud.google.com/architecture/framework/sustainability/optimize-storage)

### Phase 4: Institutionalize your sustainability practices and reporting

In this phase, you embed carbon measurement into your governance framework. This
approach helps to ensure that your organization has the capabilities and
controls that are necessary for continuous sustainability improvements and
verifiable reporting.

- **Implement *GreenOps* governance** : Establish a formal [GreenOps](https://en.wikipedia.org/wiki/Green_computing#Cloud_computing) function or working group to integrate Carbon Footprint data with Cloud Billing data. This function must define accountability for carbon reduction targets across projects, align cost optimization with sustainability goals, and implement reporting to track carbon efficiency against spending.
- **Use Carbon Footprint data for reporting and compliance**: Use the verified, auditable Carbon Footprint data in BigQuery to create formal environmental, social, and governance (ESG) disclosures. This approach lets you meet stakeholder demands for transparency and helps to ensure compliance with mandatory and voluntary regulations.
- **Invest in training and awareness** : Implement mandatory sustainability training for relevant technical and non-technical teams. Your teams need to know how to access and interpret the Carbon Footprint data and how to apply optimization recommendations in their daily workflows and design choices. For more information, see [Provide role-based sustainability training](https://docs.cloud.google.com/architecture/framework/sustainability/culture#provide_role-based_sustainability_training).
- **Define carbon requirements**: Incorporate carbon emission metrics as non-functional requirements (NFR) in your application's acceptance criteria for new deployments. This practice helps to ensure that architects and developers prioritize low-carbon design options from the start of the application development lifecycle.
- **Automate GreenOps**: Automate the implementation of Active Assist recommendations by using scripts, templates, and infrastructure-as-code (IaC) pipelines. This practice ensures that teams apply recommendations consistently and rapidly across the organization.

<br />

<br />


# Promote a culture of sustainability

This principle in the sustainability pillar of the
[Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework/sustainability)
provides recommendations to help you build a culture where teams across your
organization are aware of and proficient in sustainability practices.

## Principle overview

To apply sustainability practices, you need more than tools and techniques. You
need a cultural shift that's driven by education and accountability. Your teams
need to be aware of sustainability concerns and they must have practical
proficiency in sustainability practices.

- *Awareness of sustainability* is the contextual knowledge that every architectural and operational decision has tangible effects on sustainability. Teams must recognize that the cloud isn't an abstract collection of virtual resources, but it's driven by physical resources that consume energy and produce carbon emissions.
- *Proficiency in sustainability practices* includes knowledge to interpret carbon emissions data, experience with implementing cloud sustainability governance, and technical skills to refactor code for energy efficiency.

To align sustainability practices with organizational goals, your teams need to
understand how energy usage by cloud infrastructure and software contributes to
the organization's carbon footprint. Well-planned training helps to ensure that
all of your stakeholders---from developers and architects to finance professionals
and operations engineers---understand the sustainability context of their daily
work. This shared understanding empowers teams to move beyond passive compliance
to active optimization, which makes your cloud workloads sustainable-by-design.
Sustainability becomes a core non-functional requirement (NFR) like other
requirements for security, cost, performance, and reliability.

## Recommendations

To build awareness of sustainability concerns and proficiency in sustainability
practices, consider the recommendations in the following sections.

### Provide business context and alignment with organizational goals

Sustainability isn't just a technical exercise; it requires a cultural shift
that aligns individual actions with the environmental mission of your
organization. When teams understand the *why* behind sustainability initiatives,
they are more likely to adopt the initiatives as core principles rather than as
optional tasks.

#### Connect to the big picture

Help your teams understand how individual architectural choices---such as
selecting a low-carbon region or optimizing a data pipeline---contribute to the
organization's overall sustainability commitments. Explicitly communicate how
these choices affect the local community and the industry. Transform abstract
carbon metrics into tangible indicators of progress toward corporate social
responsibility (CSR) goals.

For example, a message like the following informs teams about the positive
outcome and executive recognition of a decision to migrate a workload to a
low-carbon region and to use a power-efficient machine type. The message
references the
[CO~2~ equivalent](https://en.wikipedia.org/wiki/Global_warming_potential),
which helps your team contextualize the impact of carbon reduction measures.
> *"By migrating our data analytics engine to the us-central1
> ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg) [Low CO~2~](https://cloud.google.com/sustainability/region-carbon#region-picker) region and
> upgrading our clusters to C4A Axion-based instances, we fundamentally
> changed our carbon profile. This shift resulted in a 75% reduction in the carbon
> intensity of our data analytics engine, which translates to a reduction of 12
> metric tons of CO~2~ equivalent this quarter. This migration had a
> significant impact on our business goals and was included in the Q4 newsletter
> to our board."*

#### Communicate financial and sustainability goals

Transparency is critical for aligning sustainability practices with goals. To
the extent feasible, widely share sustainability goals and progress across the
organization. Highlight sustainability progress in the annual financial
statements. Such communication ensures that technical teams view their work as a
vital part of the organization's public-facing commitments and financial health.

#### Embrace a shared fate mindset

Educate teams about the collaborative nature of cloud sustainability. Google is
responsible for the sustainability *of* the cloud, which includes the efficiency
of the infrastructure and data centers. You (the customer) are responsible for
sustainability of your resources and workloads *in* the cloud. When you frame
this collaboration as a partnership of shared fate, you reinforce the
understanding that your organization and Google work together to achieve optimal
environmental outcomes.

### Provide role-based sustainability training

To ensure that sustainability is a practical skill rather than a theoretical
concept, tailor the sustainability training to specific job roles. The
sustainability tools and techniques that a data scientist can use are very
different from those available to a FinOps analyst, as described in the
following table:

| Role | Training focus |
|---|---|
| Data scientists and ML engineers | **Carbon-intensity of compute** : Demonstrate the differences between running AI training jobs on [legacy systems](https://en.wikipedia.org/wiki/Legacy_system) versus purpose-built AI accelerators. Highlight how a model with fewer parameters can produce the required accuracy with significantly lower energy consumption. |
| Developers | **Code efficiency and resource consumption**: Illustrate how high-latency code or inefficient loops translate directly to extended CPU runtime and increased energy consumption. Emphasize the importance of lightweight containers and the need to optimize application performance to reduce the environmental footprint of software. |
| Architects | **Sustainable by design** : Focus on region selection and workload placement. Show how choosing a ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg) [Low CO~2~](https://cloud.google.com/sustainability/region-carbon#region-picker) region with a high percentage of renewable energy (like `northamerica-northeast1`) fundamentally changes the carbon profile of your entire application stack before you write a single line of code. |
| Platform engineers and operations engineers | **Maximizing utilization**: Emphasize the environmental cost of idle resources and over-provisioning. Present scenarios for automated scaling and right-sizing to ensure that cloud resources are used efficiently. Explain how to create and track sustainability-related metrics like utilization and how to translate metrics like compute time into equivalent metrics of carbon emissions. |
| FinOps | **Unit economics of carbon**: Focus on the relationship between financial spend and environmental impact. Demonstrate how GreenOps practices let an organization track carbon per transaction, which helps to make sustainability a key performance indicator (KPI) that's as critical as conventional KPIs like cost and utilization. |
| Product managers | **Sustainability as a feature**: Demonstrate how to integrate carbon-reduction goals into product roadmaps. Show how simplified user journeys can help to reduce the energy consumption by both cloud resources and end-user devices. |
| Business leaders | **Strategic alignment and reporting**: Focus on how cloud sustainability affects environmental, social, and governance (ESG) scores and public reputation. Illustrate how sustainability choices help to reduce regulatory risk and fulfill commitments to the community and industry. |

### Advocate for sustainability and recognize success

To sustain long-term progress, you need to move beyond internal technical fixes
and begin influencing your partners and the industry.

#### Empower managers to advocate for sustainability

Provide managers the data and permissions that they need to prioritize
environmental impact similar to other business metrics like speed-to-market and
cost. When managers have this data, they begin to view sustainability as a
quality and efficiency standard rather than as a nice-to-have capability that
slows production. They actively advocate for new cloud provider features---such as
more granular carbon data and newer, greener processors in specific regions.

#### Align with industry standards and frameworks

To ensure that your sustainability efforts are credible and measurable, align
internal practices with recognized global and regional standards. For more
information, see
[Align sustainability practices with industry guidelines](https://docs.cloud.google.com/architecture/framework/sustainability/industry-guidelines).

### Incentivize sustainability efforts

To ensure that sustainability becomes an enduring part of the engineering
culture, teams must realize the value of prioritizing sustainability. Transition
from high-level goals to specific, measurable KPIs that reward improvement and
efficiency.

#### Define carbon KPIs and NFRs

Treat sustainability as a core technical requirement. When you define carbon
KPIs, such as grams of CO~2~ equivalent per million requests or
carbon-intensity per AI training run, you make the impact on sustainability
visible and actionable. For example, integrate sustainability into the NFRs for
every new project. In other words, just as a system must meet a specific latency
or availability target, the system must also stay within a defined carbon
emissions budget.

#### Measure return on effort

Help your teams identify high-impact, low-effort sustainability wins---such as
shifting a batch job to a different region---versus a complex code refactoring
exercise that might provide minimal gains. Provide visibility into the return on
effort (ROE). When a team chooses a more efficient processor family, they must
know exactly how much carbon emission they avoided relative to the time and
effort that's required to migrate to the new processor.

#### Recognize and celebrate carbon reduction

Sustainability impact is often hidden in the background of infrastructure. To
build the momentum for sustainability progress, make successes visible to the
entire organization. For example, use annotations in monitoring dashboards to
mark when a team deployed a specific sustainability optimization. This
visibility lets teams point to data in the dashboard and claim recognition for
their successes.

<br />

<br />


# Align sustainability practices with industry guidelines

This principle in the sustainability pillar of the
[Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework/sustainability)
provides an overview of industry guidelines and frameworks with which you should
align your sustainability efforts.

## Principle overview

To ensure that your sustainability initiatives are built upon a foundation of
globally recognized methods for measurement, reporting, and verification, we
recommend that you align your initiatives with the following industry
guidelines:

- [W3C Web Sustainability Guidelines](https://docs.cloud.google.com/architecture/framework/printable#ws-guidelines)
- [Green Software Foundation](https://docs.cloud.google.com/architecture/framework/printable#gsg-guidelines)
- [Greenhouse Gas Protocol](https://docs.cloud.google.com/architecture/framework/printable#ghg-protocol)

When you align your sustainability initiatives with these shared external
guidelines, your initiatives get the credibility and auditability that
investors, regulatory bodies, and other external stakeholders demand. You also
foster accountability across engineering teams, embed sustainability within
employee training, and successfully integrate cloud operations into
enterprise-wide commitments for environmental, social, and governance
(ESG) reporting.

## W3C Web Sustainability Guidelines

[W3C Web Sustainability Guidelines (WSG)](https://www.w3.org/TR/web-sustainability-guidelines/)
is an emerging framework of best practices developed by a W3C working group to
address the environmental impact of digital products and services. The
guidelines cover the entire lifecycle of a digital solution including business
and product strategy, user experience (UX) design, web development, hosting,
infrastructure, and systems. The core goal of WSG is to enable developers and
architects to build websites and web applications that are more energy-efficient
and that reduce network traffic, client-side processing, and server-side
resource consumption. These guidelines serve a critical reference point for
aligning application-level sustainability with cloud-level architectural
decisions.

## Green Software Foundation

The
[Green Software Foundation (GSF)](https://greensoftware.foundation/)
focuses on building an industry ecosystem around sustainable software. Its
mission is to drive the creation of software that's designed, built, and
operated to minimize the carbon footprint. The GSF developed the Software Carbon
Intensity (SCI) specification, which provides a common standard for measuring
the rate of carbon emissions of any piece of software. Alignment with the GSF
helps developers connect an application's efficiency directly to the carbon
impact of the cloud environment.

## Greenhouse Gas Protocol

The
[Greenhouse Gas (GHG) Protocol](https://ghgprotocol.org/)
is a widely used set of standards for measuring, managing, and publicly
reporting greenhouse gas emissions. The protocol was developed through a
partnership between the World Resources Institute (WRI) and the World Business
Council for Sustainable Development (WBCSD). The GHG protocol provides the
essential framework for corporate climate accounting. The
Carbon Footprint report provides data for
[emission scopes](https://docs.cloud.google.com/carbon-footprint/docs/methodology#boundaries)
that are relevant to cloud usage. For more information, see
[Carbon Footprint reporting methodology](https://docs.cloud.google.com/carbon-footprint/docs/methodology).

Adherence to the GHG Protocol helps to ensure that your sustainability
initiatives have credibility and that external parties can audit your carbon
emissions data. You also help prevent the perception of
[greenwashing](https://en.wikipedia.org/wiki/Greenwashing)
and satisfy the due-diligence requirements of your investors, regulators, and
external stakeholders. Verified and audited data helps your organization prove
accountability and build trust in public-facing sustainability commitments.

<br />